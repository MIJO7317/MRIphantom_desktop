import os
import sys
import inspect
import json
import nibabel as nib
from datetime import datetime
from PySide6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QFileDialog)
from PySide6.QtCore import Slot, QEvent, Qt, Signal, QRunnable, QThreadPool, QObject
from PySide6 import QtCore

# TODO join visualizations into separate class
from src.visualization.scatter3d import Scatter3D
from src.visualization.scatter2d import Scatter2D
from src.visualization.histogram import Histogram
from src.visualization.plots import Plots
from src.visualization.table import Table

from UI.main_window import Ui_MainWindow
from src.spinner.spinner import Spinner
from src.segmentation.process import (slice_img_generator, perform_thresholding,
                                      isolate_markers, get_coords,
                                      count_difference)

workdir = os.path.realpath(os.path.abspath(os.path.join(
    os.path.split(inspect.getfile(inspect.currentframe()))[0], "../../")))


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


class EntranceWindow(QMainWindow):
    send_shift = Signal()

    def __init__(self):
        super().__init__()

        self.study_name = None
        self.plots = None
        self.histogram = None
        self.scatter2d = None
        self.scatter3d = None
        self.params_table = None
        self.thread_pool = None
        self.spinner = None
        self.registration_thread_pool = None
        self.analyze_thread_pool = None
        self.mri_img = None
        self.ct_img = None
        self.moving_image_path = None
        self.fixed_image_path = None
        self.vbox = None
        self.context = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.filename_CT = None
        self.filename_MRI = None
        self.write_path = None
        self.output_dirname = None
        self.output_path = None
        self.format = None
        self.is_interpolated = False
        self.is_geometric = False

        self.initUi()

    def initUi(self):
        self.context = {}

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.ui.titleEdit.setPlaceholderText("Название теста")
        self.ui.descriptionEdit.setPlaceholderText("Описание")

        self.ui.fixedimgEdit.setPlaceholderText("Укажите путь папки с КТ (Fixed)")
        self.ui.movingimgEdit.setPlaceholderText("Укажите путь папки с МРТ (Moving)")
        self.ui.fixedimgEdit.mousePressEvent = lambda event: self.openFixedImageDirectoryDialog()
        self.ui.movingimgEdit.mousePressEvent = lambda event: self.openMovingImageDirectoryDialog()
        self.ui.interpolateButton.stateChanged.connect(self.interpolationButtonStateChanged)
        self.ui.geometryButton.stateChanged.connect(self.geometryButtonStateChanged)

        self.fixed_image_path = None
        self.moving_image_path = None
        self.ct_img = None
        self.mri_img = None

        self.ui.phantomTypeCombo.addItem("Elekta MR phantom (Axial Grid)")

        self.ui.analyzeButton.setCheckable(True)
        self.ui.analyzeButton.toggled.connect(self.analyzeImages)
        self.analyze_thread_pool = QThreadPool()
        self.registration_thread_pool = QThreadPool()

        self.spinner = Spinner()
        self.thread_pool = QThreadPool()

    def openFixedImageDirectoryDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        directory = QFileDialog.getOpenFileName(self, "Выбрать изображение КТ (Fixed)", "",
                                                options=options)
        if directory:
            self.ui.fixedimgEdit.setText(directory[0])
            self.fixed_image_path = directory[0]

    def openMovingImageDirectoryDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        directory = QFileDialog.getOpenFileName(self, "Выбрать изображение МРТ (Moving)", "", options=options)
        if directory[0]:
            self.ui.movingimgEdit.setText(directory[0])  # Display the directory path in the QLineEdit
            self.moving_image_path = directory[0]  # Save the directory path to self.movingimagepath

    @Slot()
    def analyze(self):
        print(self.is_interpolated)
        # create generators for original images
        ct_slice_gen = slice_img_generator(self.fixed_image_path, interpolation=self.is_interpolated)
        mri_slice_gen = slice_img_generator(self.moving_image_path, interpolation=self.is_interpolated)

        # threshold segmentation
        ct_thresh_gen = perform_thresholding(ct_slice_gen, is_mri=False, interpolation=self.is_interpolated)
        mri_thresh_gen = perform_thresholding(mri_slice_gen, is_mri=True, interpolation=self.is_interpolated)

        isolate_markers(ct_thresh_gen, os.path.join(self.write_path, 'markers_CT.pickle'), interpolation=self.is_interpolated)
        isolate_markers(mri_thresh_gen, os.path.join(self.write_path, 'markers_MRI.pickle'), interpolation=self.is_interpolated)

        params, self.differences, self.slice_differences = count_difference(os.path.join(self.write_path, 'markers_CT.pickle'),
                                                                            os.path.join(self.write_path, 'markers_MRI.pickle'),
                                                                            self.write_path)

        self.coords_ct = get_coords(os.path.join(self.write_path, 'markers_CT.pickle'))
        self.coords_mri = get_coords(os.path.join(self.write_path, 'markers_MRI.pickle'))

    @Slot()
    def finishAnalyze(self):
        self.spinner.close()
        with open(os.path.join(workdir, 'studies', self.study_name, 'difference_stats.json'), 'r') as fp:
            data = json.load(fp)
        self.params_table = Table(data, headers=['Parameter', 'Value'], title='Elekta phantom stats')
        self.params_table.show()
        self.scatter3d = Scatter3D(self.coords_ct, self.coords_mri)
        self.scatter3d.show()
        self.scatter2d = Scatter2D(self.coords_ct, self.coords_mri)
        self.scatter2d.show()
        self.histogram = Histogram(self.differences)
        self.histogram.show()
        self.plots = Plots(self.slice_differences)
        self.plots.show()

    @Slot()
    def analyzeImages(self):
        self.study_name = self.ui.titleEdit.text()
        print(f"start analyzing study '{self.study_name}'...")
        print('workdir: ', workdir)
        self.output_dirname, self.filename_CT, self.filename_MRI = self.createFilename(self.study_name)
        self.output_path = os.path.realpath(os.path.join(workdir, 'studies', self.output_dirname)).replace("\\", "/")
        if not os.path.exists(self.output_path):
            print('creating directory: ', self.output_path)
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

        worker_to_nifti = Worker(self.analyze)
        self.analyze_thread_pool.start(worker_to_nifti)
        worker_to_nifti.signaller.finished.connect(self.finishAnalyze)

        self.ui.descriptionEdit.setText("")
        self.ui.titleEdit.setText("")
        self.ui.fixedimgEdit.setText("")
        self.ui.movingimgEdit.setText("")

    def createFilename(self, title):
        prefix = f'{title if title else ""}'
        prefix_ct = f'CT_{title if title else ""}'
        prefix_mri = f'MRI_{title if title else ""}'
        extension = ''
        file_name_format = "{:s}-{:%d-%m-%Y}{:s}"
        date = datetime.now()
        return prefix, file_name_format.format(prefix_ct, date, extension), file_name_format.format(prefix_mri, date,
                                                                                                    extension)

    @Slot()
    def openStudy(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        study_path = QFileDialog.getExistingDirectory(self, "Выбрать исследование", f"{workdir}/studies",
                                                      options=options)
        study_title = study_path.split("/")[-1]

        ct_file = [f for f in os.listdir(study_path)
                   if os.path.isfile(os.path.join(study_path, f)) and f.startswith('CT') and f.endswith('.nii.gz')]
        mri_file = [f for f in os.listdir(study_path)
                    if os.path.isfile(os.path.join(study_path, f)) and f.startswith('MRI') and f.endswith('.nii.gz')]

        # Load NIfTI images using nibabel
        ct_img = nib.load(os.path.join(study_path, ct_file[0]))
        mri_img = nib.load(os.path.join(study_path, mri_file[0]))

        self.context.update({
            "study_path": study_path,
            "study_title": study_title,
            "CT_filename": ct_file[0],
            "MRI_filename": mri_file[0]
        })

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

    # TODO simplify
    def interpolationButtonStateChanged(self):
        if self.is_interpolated:
            self.is_interpolated = False
        else:
            self.is_interpolated = True
        print("Interpolation button state changed: ", self.is_interpolated)

    # TODO simplify
    def geometryButtonStateChanged(self):
        if self.is_geometric:
            self.is_geometric = False
        else:
            self.is_geometric = True
        print("Geometry button state changed: ", self.is_geometric)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    entrance = EntranceWindow()
    entrance.show()
    sys.exit(app.exec())
