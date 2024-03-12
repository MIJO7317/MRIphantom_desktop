from PySide6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QFileDialog)
from PySide6.QtCore import Slot, QEvent, Qt, Signal, QRunnable, QThreadPool, QObject
from PySide6 import QtCore
from PySide6.QtPdf import QPdfDocument
import sys
import inspect

from gui.scatter3d import Scatter3D
from gui.scatter2d import Scatter2D
from gui.histogram import Histogram
from gui.plots import Plots

from datetime import datetime
from UI.main_window import Ui_MainWindow
from src.spinner.spinner import Spinner

from src.preprocess.unpack import unpack_nii_stack
import nibabel as nib

from src.segmentation.process import *

cmd_main = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(
    inspect.currentframe()))[0], "../../../")))

if cmd_main not in sys.path:
    sys.path.insert(0, cmd_main)

workdir = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(
    inspect.currentframe()))[0], "../../../")))


class Worker(QRunnable):
    def __init__(self, fn):
        super().__init__()
        self.signaller = Signaller()
        self.fn = fn

    def run(self):
        self.signaller.started.emit()
        self.fn()
        self.signaller.finished.emit()


class Signaller(QObject):
    value_updated = Signal(int)
    interrupt = Signal(bool)
    started = Signal()
    finished = Signal()


def auto_capital(line_edit_object):
    edit = line_edit_object
    text = edit.text()
    edit.setText(text.title())


class EntranceWindow(QMainWindow):
    send_shift = Signal()

    def __init__(self):
        super().__init__()

        self.threadPool = None
        self.spinner = None
        self.registrationThreadPool = None
        self.analyzeThreadPool = None
        self.mri_img = None
        self.ct_img = None
        self.moving_image_path = None
        self.fixed_image_path = None
        self.vbox = None
        self.context = None
        self.pdf = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.filenameCT = None
        self.filenameMRI = None
        self.write_path = None
        self.output_dirname = None
        self.output_path = None
        self.format = None

        self.initUi()

    def initUi(self):
        self.pdf = QPdfDocument(self)

        self.context = {}

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.ui.titleEdit.setPlaceholderText("Название теста")
        self.ui.titleEdit.textChanged.connect(lambda: auto_capital(self.ui.titleEdit))

        self.ui.descriptionEdit.setPlaceholderText("Описание")
        self.ui.descriptionEdit.textChanged.connect(lambda: auto_capital(self.ui.descriptionEdit))

        self.ui.fixedimgEdit.setPlaceholderText("Укажите путь папки с КТ (Fixed)")
        self.ui.movingimgEdit.setPlaceholderText("Укажите путь папки с МРТ (Moving)")
        self.ui.fixedimgEdit.mousePressEvent = lambda event: self.open_fixed_image_directory_dialog()
        self.ui.movingimgEdit.mousePressEvent = lambda event: self.open_moving_image_directory_dialog()

        self.fixed_image_path = None
        self.moving_image_path = None
        self.ct_img = None
        self.mri_img = None

        self.ui.phantomTypeCombo.addItem("Elekta MR phantom (Axial Grid)")

        self.ui.analyzeButton.setCheckable(True)
        self.ui.analyzeButton.toggled.connect(self.analyze_images)
        self.analyzeThreadPool = QThreadPool()
        self.registrationThreadPool = QThreadPool()

        self.ui.openStudyButton.clicked.connect(self.open_study)

        self.ui.openPdfButton.clicked.connect(self.open_pdf)

        self.spinner = Spinner()
        self.threadPool = QThreadPool()

    def open_fixed_image_directory_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        directory = QFileDialog.getOpenFileName(self, "Выбрать изображение КТ (Fixed)", "", options=options)
        if directory:
            self.ui.fixedimgEdit.setText(directory[0])  # Display the directory path in the QLineEdit
            self.fixed_image_path = directory[0]  # Save the directory path to self.fixedimagepath

    def open_moving_image_directory_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        directory = QFileDialog.getOpenFileName(self, "Выбрать изображение МРТ (Moving)", "", options=options)
        if directory[0]:
            self.ui.movingimgEdit.setText(directory[0])  # Display the directory path in the QLineEdit
            self.moving_image_path = directory[0]  # Save the directory path to self.movingimagepath

    @Slot()
    def to_nifti(self):
        unpack_nii_stack(self.fixed_image_path, os.path.join(self.write_path, 'CT_png'))
        unpack_nii_stack(self.moving_image_path, os.path.join(self.write_path, 'MRI_warped_png'))
        self.ui.nameVideoLabel.setText(f'Файлы .nii распакованы')

        # сделать сегментацию по трешхолду -> обрезка всего лишнего вне круга
        perform_thresholding(os.path.join(self.write_path, 'CT_png'), os.path.join(self.write_path, 'CT_png_results'))
        self.ui.nameVideoLabel.setText(f'Завершена сегментация КТ')

        perform_thresholding(os.path.join(self.write_path, 'MRI_warped_png'),
                             os.path.join(self.write_path, 'MRI_png_results'), is_mri=True)
        self.ui.nameVideoLabel.setText(f'Завершена сегментация МРТ')

        # find_differences(os.path.join(self.write_path, 'CT_png_results'), os.path.join(self.write_path, 'MRI_png_results'), os.path.join(self.write_path, 'difference_img'))
        isolate_markers(os.path.join(self.write_path, 'CT_png_results'), os.path.join(self.write_path, 'markers_CT'))
        self.ui.nameVideoLabel.setText(f'Завершена детекция маркеров на КТ')

        isolate_markers(os.path.join(self.write_path, 'MRI_png_results'), os.path.join(self.write_path, 'markers_MRI'))
        self.ui.nameVideoLabel.setText(f'Завершена детекция маркеров на МРТ')

        self.ui.nameVideoLabel.setText(f'Выполняю расчет отклонений...')
        params, self.differences, self.slice_differences = count_difference(os.path.join(self.write_path, 'markers_CT'),
                                                                            os.path.join(self.write_path,
                                                                                         'markers_MRI'),
                                                                            self.write_path)
        self.ui.nameVideoLabel.setText(f'Расчет отклонений завершен. Вывод результатов')

        self.coords_ct = get_coords_ct(os.path.join(self.write_path, 'markers_CT'))
        self.coords_mri = get_coords_mri(os.path.join(self.write_path, 'markers_MRI'))

    @Slot()
    def finish_to_nifti(self):
        self.spinner.close()

        with open('Users/bzavolovich/Developer/MRIphantom_interface/studies/29January/difference_stats.json',
                  'r') as fp:
            data = json.load(fp)

        self.t = Table(data, headers=['Parameter', 'Value'], title='Elekta phantom stats')
        self.t.show()

        self.scatter3d = Scatter3D(self.coords_ct, self.coords_mri)
        self.scatter3d.show()

        self.scatter2d = Scatter2D(self.coords_ct, self.coords_mri)
        self.scatter2d.show()

        self.histogram = Histogram(self.differences)
        self.histogram.show()

        self.plots = Plots(self.slice_differences)
        self.plots.show()

    @Slot()
    def analyze_images(self):

        self.output_dirname, self.filenameCT, self.filenameMRI = self.create_file_name(self.ui.titleEdit.text())
        self.output_path = os.path.realpath(os.path.join(workdir, 'studies', self.output_dirname)).replace("\\", "/")
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        write_path = os.path.realpath(os.path.join(workdir, f'studies/{self.output_dirname}'))
        write_path = write_path.replace("\\", "/")
        self.write_path = write_path

        self.context = {
            "workdir": workdir,
            "title": self.ui.titleEdit.text(),
            "description": self.ui.descriptionEdit.text(),
            "fixedimgpath": self.ui.fixedimgEdit.text(),
            "movingimgpath": self.ui.movingimgEdit.text(),
        }

        self.spinner.show()

        worker_to_nifti = Worker(self.to_nifti)
        self.analyzeThreadPool.start(worker_to_nifti)
        worker_to_nifti.signaller.finished.connect(self.finish_to_nifti)

        self.ui.descriptionEdit.setText("")
        self.ui.titleEdit.setText("")
        self.ui.fixedimgEdit.setText("")
        self.ui.movingimgEdit.setText("")

    def create_file_name(self, title):
        prefix = f'{title if title else ""}'
        prefixCT = f'CT_{title if title else ""}'
        prefixMRI = f'MRI_{title if title else ""}'
        extension = ''
        file_name_format = "{:s}-{:%d-%m-%Y}{:s}"
        date = datetime.now()
        return prefix, file_name_format.format(prefixCT, date, extension), file_name_format.format(prefixMRI, date,
                                                                                                   extension)

    @Slot()
    def open_study(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        study_path = QFileDialog.getExistingDirectory(self, "Выбрать исследование", f"{workdir}/studies",
                                                      options=options)
        study_title = study_path.split("/")[-1]

        CT_file = [f for f in os.listdir(study_path)
                   if os.path.isfile(os.path.join(study_path, f)) and f.startswith('CT') and f.endswith('.nii.gz')]
        MRI_file = [f for f in os.listdir(study_path)
                    if os.path.isfile(os.path.join(study_path, f)) and f.startswith('MRI') and f.endswith('.nii.gz')]

        # Load NIfTI images using nibabel
        ct_img = nib.load(os.path.join(study_path, CT_file[0]))
        mri_img = nib.load(os.path.join(study_path, MRI_file[0]))

        self.context.update({
            "study_path": study_path,
            "study_title": study_title,
            "CT_filename": CT_file[0],
            "MRI_filename": MRI_file[0]
        })

    @Slot()
    def open_pdf(self):
        pdf_url, _ = QFileDialog.getOpenFileName(self, "Открыть отчет", f"{workdir}/pdfs")
        self.pdf.load(pdf_url)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if len(source.text()) == 2:
                source.home(False)
                return True
        return super(EntranceWindow, self).eventFilter(source, event)

    def event(self, event):
        if event.type() == QEvent.KeyPress and event.key() in (
                Qt.Key_Enter,
                Qt.Key_Return,
                Qt.Key_Down
        ):
            self.focusNextPrevChild(True)
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Up:
            self.focusPreviousChild()

        return super().event(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    entrance = EntranceWindow()
    entrance.show()
    sys.exit(app.exec())
