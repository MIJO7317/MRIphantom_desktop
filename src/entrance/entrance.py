import os
import sys
import inspect
import json
import numpy as np
import nibabel as nib
from datetime import datetime
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QFileDialog, QLabel
from PySide6.QtCore import (
    Slot,
    QEvent,
    Qt,
    Signal,
    QRunnable,
    QThreadPool,
    QObject,
    QEventLoop,
)
from PySide6 import QtCore

from src.visualization.scatter3d import Scatter3D
from src.visualization.scatter2d import Scatter2D
from src.visualization.plots import Plots
from src.visualization.table import Table
from src.visualization.sequence_viewer import VTKSliceViewer

from UI.main_window_v2 import Ui_MainWindow

from src.spinner.spinner import Spinner
from src.segmentation.process import (
    get_coords
)
from src.segmentation.process_v2 import segmentation, count_difference_2
from src.registration.registration import ManualRegistrationWindow, rigid_reg, match_voxel_sizes

from src.image_importer.importer import ImporterWindow

workdir = os.path.realpath(
    os.path.abspath(
        os.path.join(
            os.path.split(inspect.getfile(inspect.currentframe()))[0], "../../"
        )
    )
)


class Worker(QRunnable):
    """
    Worker class for executing a function in a separate thread.

    This class inherits from QRunnable and provides a framework for executing a function
    in a separate thread.

    Attributes:
    - signaller: An instance of Signaller class for emitting signals.
    - fn: The function to be executed in the separate thread.

    Methods:
    - __init__: Initializes the Worker object.
    - run: Runs the function in a separate thread.
    """

    def __init__(self, fn=None):
        super().__init__()
        self.signaller = Signaller()
        self.fn = fn

    def run(self):
        """
        Runs the function in a separate thread.
        """
        self.signaller.started.emit()
        self.fn()
        self.signaller.finished.emit()


class Signaller(QObject):
    """
    Class for defining signals used for communication between threads.

    This class inherits from QObject and defines signals for various events
    used for communication between threads.

    Signals:
    - value_updated: Signal emitted when a value is updated, with an integer argument.
    - interrupt: Signal emitted to indicate interruption, with a boolean argument.
    - started: Signal emitted when a task is started.
    - finished: Signal emitted when a task is finished.
    """

    value_updated = Signal(int)
    interrupt = Signal(bool)
    started = Signal()
    finished = Signal()


class EntranceWindow(QMainWindow):
    send_shift = Signal()

    def __init__(self):
        super().__init__()

        self.coords_mri = None
        self.coords_ct = None
        self.slice_differences = None
        self.differences = None
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

        self.filename_ct = None
        self.filename_mri = None
        self.write_path = None
        self.output_dirname = None
        self.output_path = None
        self.format = None

        self.initUi()

    def initUi(self):
        self.context = {}

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.ui.moving_viewer = None
        self.ui.fixed_viewer = None

        self.ui.body_stackedWidget.setCurrentWidget(self.ui.body_stackedWidgetPageMain)
        self.ui.mainPageButton.setCheckable(True)
        self.ui.mainPageButton.setChecked(True)
        self.ui.mainPageButton.clicked.connect(self.main_page_button_pressed)
        self.ui.statsPageButton.setCheckable(True)
        self.ui.statsPageButton.setChecked(False)
        self.ui.statsPageButton.clicked.connect(self.stats_page_button_pressed)
        self.ui.scatter3dButton.setCheckable(True)
        self.ui.scatter3dButton.setChecked(False)
        self.ui.scatter3dButton.clicked.connect(self.scatter3d_page_button_pressed)
        self.ui.scatter2dButton.setCheckable(True)
        self.ui.scatter2dButton.setChecked(False)
        self.ui.scatter2dButton.clicked.connect(self.scatter2d_page_button_pressed)

        self.ui.ctPageButton.setCheckable(True)
        self.ui.ctPageButton.setChecked(True)
        self.ui.ctPageButton.clicked.connect(self.ct_page_button_pressed)
        self.ui.geometryPageButton.setChecked(True)
        self.ui.geometryPageButton.setChecked(False)
        self.ui.geometryPageButton.clicked.connect(self.geometry_page_button_pressed)
        self.ui.fixed_stackedWidget.setCurrentIndex(0)

        self.ui.titleEdit.setPlaceholderText("Название теста")

        self.ui.fixedimgEdit.setPlaceholderText("Выберите папку с КТ")
        self.ui.movingimgEdit.setPlaceholderText("Выберите папку с МРТ")
        self.ui.fixedimgEdit.mousePressEvent = (
            lambda event: self.openFixedImageDirectoryDialog()
        )
        self.ui.movingimgEdit.mousePressEvent = (
            lambda event: self.openMovingImageDirectoryDialog()
        )

        self.fixed_image_path = None
        self.moving_image_path = None
        self.ct_img = None
        self.mri_img = None

        # geometric model selector
        self.ui.phantomTypeCombo.addItem("Elekta (Axial Grid)")

        # registration buttons (automatic and manual)
        self.ui.autoregistrationButton.setCheckable(True)
        self.ui.autoregistrationButton.toggled.connect(self.autoregister_button_pressed)
        self.ui.manualregistrationButton.setCheckable(True)
        self.ui.manualregistrationButton.toggled.connect(self.manual_registration_button_pressed)
        self.registration_thread_pool = QThreadPool()

        # analyze button
        self.ui.analyzeButton.setCheckable(True)
        self.ui.analyzeButton.toggled.connect(self.analyzeImages)
        self.analyze_thread_pool = QThreadPool()

        # statusbar
        self.ui.statusLabel.setText("Готов к работе")

        # loading spinner
        self.spinner = Spinner()
        self.thread_pool = QThreadPool()

    def openFixedImageDirectoryDialog(self):
        """
        Opens a file dialog window to select a fixed image (CT) directory.

        This method displays a file dialog window
        to allow the user to select a CT image directory.
        The selected directory path is then displayed in a QLineEdit widget
        and saved to the instance variable self.fixed_image_path.

        Parameters:
        - self: The instance of the class.

        Returns:
        None
        """
        self.study_name = self.ui.titleEdit.text()
        write_path = os.path.realpath(
            os.path.join(workdir, f"studies/{self.study_name}")
        )
        self.write_path = write_path
        os.makedirs(write_path, exist_ok=True)
        fixed_image_importer = ImporterWindow('fixed', write_path)
        fixed_image_importer.setAttribute(Qt.WA_DeleteOnClose)
        fixed_image_importer.show()

        loop = QEventLoop()
        fixed_image_importer.destroyed.connect(loop.quit)
        loop.exec()

        dicom_dir = fixed_image_importer.directory_path
        saved_nifti_filepath = os.path.join(write_path, "image_fixed.nii")

        if saved_nifti_filepath:
            self.ui.fixedimgEdit.setText(saved_nifti_filepath)
            self.fixed_image_path = saved_nifti_filepath

        self.fixed_image_viewer = VTKSliceViewer(dicom_dir)
        self.fixed_viewer_layout = QVBoxLayout(self.ui.fixed_frame)
        self.fixed_viewer_layout.addWidget(QLabel('КТ'))
        self.fixed_viewer_layout.addWidget(self.fixed_image_viewer)

    def openMovingImageDirectoryDialog(self):
        """
        Opens a file dialog window to select
        a moving image (MRI) directory.

        This method displays a file dialog window
        to allow the user to select an MRI image directory.
        The selected directory path is then displayed in a QLineEdit widget
        and saved to the instance variable self.moving_image_path.

        Parameters:
        - self: The instance of the class.

        Returns:
        None
        """
        self.study_name = self.ui.titleEdit.text()
        write_path = os.path.realpath(
            os.path.join(workdir, f"studies/{self.study_name}")
        )
        self.write_path = write_path
        os.makedirs(write_path, exist_ok=True)
        moving_image_importer = ImporterWindow('moving', write_path)
        moving_image_importer.setAttribute(Qt.WA_DeleteOnClose)
        moving_image_importer.show()

        loop = QEventLoop()
        moving_image_importer.destroyed.connect(loop.quit)
        loop.exec()

        dicom_dir = moving_image_importer.directory_path
        saved_nifti_filepath = os.path.join(write_path, "image_moving.nii")
        if saved_nifti_filepath:
            self.ui.movingimgEdit.setText(saved_nifti_filepath)
            self.moving_image_path = saved_nifti_filepath
        self.moving_image_viewer = VTKSliceViewer(dicom_dir)
        self.moving_viewer_layout = QVBoxLayout(self.ui.moving_frame)
        self.moving_viewer_layout.addWidget(QLabel('МРТ'))
        self.moving_viewer_layout.addWidget(self.moving_image_viewer)

    def autoregister_button_pressed(self):
        self.ui.statusLabel.setText("Выполняется автоматическое совмещение МРТ и КТ...")
        QApplication.processEvents()  # Force update the UI

        worker_autoregistration = Worker(self.autoregistration())
        self.registration_thread_pool.start(worker_autoregistration)
        worker_autoregistration.signaller.finished.connect(self.finish_registration())

    def autoregistration(self):
        rigid_reg(self.fixed_image_path, self.moving_image_path, self.write_path)
        self.ui.statusLabel.setText("Открыто окно ручной корректировки совмещения...")
        QApplication.processEvents()  # Force update the UI

    def manual_registration_button_pressed(self):
        print('start reslicing')
        match_voxel_sizes(
            os.path.join(self.write_path, 'image_fixed.nii'),
            os.path.join(self.write_path, 'image_moving.nii'),
            self.write_path
        )
        print('finish reslicing')
        self.ui.statusLabel.setText("Открыт интерфейс ручного совмещения...")
        QApplication.processEvents()  # Force update the UI

        worker_manualregistration = Worker(self.manual_registration())
        self.registration_thread_pool.start(worker_manualregistration)
        worker_manualregistration.signaller.finished.connect(self.finish_registration())

    def manual_registration(self):
        print('open window')
        manual_window = ManualRegistrationWindow(
            os.path.join(self.write_path, 'image_fixed.nii'),
            os.path.join(self.write_path, 'image_moving.nii'),
            self.write_path
        )
        manual_window.setAttribute(Qt.WA_DeleteOnClose)
        manual_window.show()

        loop = QEventLoop()
        manual_window.destroyed.connect(loop.quit)
        loop.exec()


    def finish_registration(self):
        self.ui.statusLabel.setText("Совмещение МРТ и КТ завершено")

        self.moving_viewer_layout.removeWidget(self.moving_image_viewer)
        self.moving_image_viewer.deleteLater()
        moving_path = os.path.join(self.write_path, 'image_moving.nii')
        self.moving_image_viewer = VTKSliceViewer(moving_path, is_dicom=False)
        self.moving_viewer_layout.addWidget(self.moving_image_viewer)

        self.fixed_viewer_layout.removeWidget(self.fixed_image_viewer)
        self.fixed_image_viewer.deleteLater()
        fixed_path = os.path.join(self.write_path, 'image_fixed.nii')
        self.fixed_image_viewer = VTKSliceViewer(fixed_path, is_dicom=False)
        self.fixed_viewer_layout.addWidget(self.fixed_image_viewer)

    @Slot()
    def analyze(self):
        """
        Analyzes the images to detect markers and perform marker analysis.

        This method performs the following steps:
        1. Generates slices of original images using slice_img_generator.
        2. Performs threshold segmentation on the generated slices using perform_thresholding.
        3. Detects markers in the thresholded images and saves them as .pickle files.
        4. Performs marker analysis to calculate differences between markers.
        5. Retrieves coordinates of markers from the saved .pickle files.

        Parameters:
        - self: The instance of the class.

        Returns:
        None
        """

        if self.ui.geometryPageButton.isChecked() is False:
            self.moving_image_path = os.path.join(self.write_path, "image_moving.nii")
            self.fixed_image_path = os.path.join(self.write_path, "image_fixed.nii")

            self.ui.statusLabel.setText("Выполняется сегментация изображений...")
            img_mri = nib.load(self.moving_image_path)
            img_mri_data = img_mri.get_fdata()
            img_mri = img_mri_data[:, :, :].copy()
            img_mri = img_mri + np.abs(np.min(img_mri))
            img_mri *= 255.0 / (np.max(img_mri) + 1e-5)
            img_mri = img_mri.astype(np.uint8)

            img_ct = nib.load(self.fixed_image_path)
            img_ct_data = img_ct.get_fdata()
            img_ct = img_ct_data[:, :, :].copy()
            img_ct = img_ct + np.abs(np.min(img_ct))
            img_ct *= 255.0 / (np.max(img_ct) + 1e-5)
            img_ct = img_ct.astype(np.uint8)

            ct_pickle_path = os.path.join(self.write_path, "markers_CT.pickle")
            mri_pickle_path = os.path.join(self.write_path, "markers_MRI.pickle")
            all_mri_points, all_ct_points = segmentation(
                img_mri[:, :, 45:105],
                img_ct[:, :, 45:105],
                mri_pickle_path,
                ct_pickle_path
            )

            _, self.differences, self.slice_differences = count_difference_2(
                ct_pickle_path, mri_pickle_path, self.write_path
            )

            self.coords_ct = get_coords(
                os.path.join(self.write_path, "markers_CT.pickle")
            )
            self.coords_mri = get_coords(
                os.path.join(self.write_path, "markers_MRI.pickle")
            )
            self.ui.statusLabel.setText("Расчет выполнен")

        else:
            self.ui.statusLabel.setText("Геометрическая модель не загружена")

    @Slot()
    def finishAnalysis(self):
        """
        Finishes the analysis process and displays various visualization outputs.
        Parameters:
        - self: The instance of the class.
        Returns:
        None
        """
        self.spinner.close()
        stats_path = os.path.join(
            workdir, "studies", self.study_name, "difference_stats.json"
        )
        with open(stats_path, "r") as fp:
            data = json.load(fp)
        self.params_table = Table(
            data,
            headers=["Параметр", "Значение"],
            title="Итоговая статистика по фантому",
        )
        # Update UI elements
        self.ui.label.setText('Статистика отклонений')

        # Remove existing layout and widget from stats_frame if they exist
        if hasattr(self, 'stats_table_layout'):
            # Remove all widgets from the layout
            while self.stats_table_layout.count():
                child = self.stats_table_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            # Delete the layout itself
            self.stats_table_layout.deleteLater()

        # Create and add the new layout and widget
        self.stats_table_layout = QVBoxLayout(self.ui.stats_frame)
        self.stats_table_layout.addWidget(self.params_table)

        self.ui.label_2.setText('3D просмотр')

        # Remove existing layout and widget from scatter3d_frame if they exist
        if hasattr(self, 'scatter3d_layout'):
            while self.scatter3d_layout.count():
                child = self.scatter3d_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.scatter3d_layout.deleteLater()

        # Create and add the new layout and widget
        self.scatter3d = Scatter3D(self.coords_ct, self.coords_mri)
        self.scatter3d_layout = QVBoxLayout(self.ui.scatter3d_frame)
        self.scatter3d_layout.addWidget(self.scatter3d)

        self.ui.label_3.setText('2D просмотр')

        # Remove existing layout and widget from scatter2d_frame if they exist
        if hasattr(self, 'scatter2d_layout'):
            while self.scatter2d_layout.count():
                child = self.scatter2d_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.scatter2d_layout.deleteLater()

        # Create and add the new layout and widget
        self.scatter2d = Scatter2D(self.coords_ct, self.coords_mri)
        self.scatter2d_layout = QVBoxLayout(self.ui.scatter2d_frame)
        self.scatter2d_layout.addWidget(self.scatter2d)

        # Remove existing layout and widget from plots_frame if they exist
        if hasattr(self, 'plots_layout'):
            while self.plots_layout.count():
                child = self.plots_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.plots_layout.deleteLater()

        # Create and add the new layout and widget
        self.plots = Plots(self.slice_differences)
        self.plots_layout = QVBoxLayout(self.ui.plots_frame)
        self.plots_layout.addWidget(self.plots)

    @Slot()
    def analyzeImages(self):
        self.study_name = self.ui.titleEdit.text()
        (self.output_dirname, self.filename_ct, self.filename_mri) = (
            self.createFilename(self.study_name)
        )
        output_dirname = os.path.join(workdir, "studies", self.output_dirname)
        self.output_path = os.path.realpath(output_dirname).replace("\\", "/")
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        write_path = os.path.realpath(
            os.path.join(workdir, f"studies/{self.output_dirname}")
        )
        write_path = write_path.replace("\\", "/")
        self.write_path = write_path

        self.context = {
            "workdir": workdir,
            "title": self.ui.titleEdit.text(),
            "fixedimgpath": self.ui.fixedimgEdit.text(),
            "movingimgpath": self.ui.movingimgEdit.text(),
        }

        self.spinner.show()

        worker_to_nifti = Worker(self.analyze)
        self.analyze_thread_pool.start(worker_to_nifti)
        worker_to_nifti.signaller.finished.connect(self.finishAnalysis)

        # self.ui.titleEdit.setText("")
        # self.ui.fixedimgEdit.setText("")
        # self.ui.movingimgEdit.setText("")

    def createFilename(self, title):
        """
        Creates filenames for CT and MRI images based on a given title.

        This method generates filenames for CT and MRI images
        using the provided title and the current date.
        It appends 'CT_' or 'MRI_' prefixes to the title
        for CT and MRI images, respectively.
        The filenames are formatted as "{prefix}-{date}{extension}".

        Parameters:
        - self: The instance of the class.
        - title: A string representing the title to be included in the filename.

        Returns:
        A tuple containing the prefix, filename for CT, and filename for MRI.
        """
        prefix = f'{title if title else ""}'
        prefix_ct = f'CT_{title if title else ""}'
        prefix_mri = f'MRI_{title if title else ""}'
        extension = ""
        file_name_format = "{:s}-{:%d-%m-%Y}{:s}"
        date = datetime.now()
        return (
            prefix,
            file_name_format.format(prefix_ct, date, extension),
            file_name_format.format(prefix_mri, date, extension),
        )

    @Slot()
    def openStudy(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        study_path = QFileDialog.getExistingDirectory(
            self, "Выбрать исследование", f"{workdir}/studies", options=options
        )
        study_title = study_path.split("/")[-1]

        ct_file = [
            f
            for f in os.listdir(study_path)
            if os.path.isfile(os.path.join(study_path, f))
            and f.startswith("CT")
            and f.endswith(".nii")
        ]
        mri_file = [
            f
            for f in os.listdir(study_path)
            if os.path.isfile(os.path.join(study_path, f))
            and f.startswith("MRI")
            and f.endswith(".nii")
        ]

        self.context.update(
            {
                "study_path": study_path,
                "study_title": study_title,
                "CT_filename": ct_file[0],
                "MRI_filename": mri_file[0],
            }
        )

    def eventFilter(self, source, event):
        """
        Filters mouse button press events for a specified source widget.

        This method filters mouse button press events for the specified source widget.
        If the event type is MouseButtonPress and the length of the text in the source widget is 2,
        the cursor is moved to the beginning of the text.

        Parameters:
        - self: The instance of the class.
        - source: The widget to which the event filter is applied.
        - event: The event object.

        Returns:
        True if the event is handled, False otherwise.
        """
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if len(source.text()) == 2:
                source.home(False)
                return True
        return super(EntranceWindow, self).eventFilter(source, event)

    def event(self, event):
        """
        Handles key press events for the widget.

        This method processes key press events for the widget. If the event type is KeyPress,
        it checks for certain key combinations and triggers appropriate actions:
        - Enter, Return, or Down arrow key: Moves focus to the next child widget.
        - Up arrow key: Moves focus to the previous child widget.

        Parameters:
        - self: The instance of the class.
        - event: The event object containing information about the key press event.

        Returns:
        The result of the event handling.
        """
        if event.type() == QEvent.KeyPress and event.key() in (
            Qt.Key_Enter,
            Qt.Key_Return,
            Qt.Key_Down,
        ):
            self.focusNextPrevChild(True)
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Up:
            self.focusPreviousChild()

        return super().event(event)

    def main_page_button_pressed(self):
        self.ui.statsPageButton.setChecked(False)
        self.ui.scatter3dButton.setChecked(False)
        self.ui.scatter2dButton.setChecked(False)
        self.ui.body_stackedWidget.setCurrentWidget(self.ui.body_stackedWidgetPageMain)

        self.moving_viewer_layout.removeWidget(self.moving_image_viewer)
        self.moving_image_viewer.deleteLater()
        moving_path = os.path.join(self.write_path, 'image_moving.nii')
        self.moving_image_viewer = VTKSliceViewer(moving_path, is_dicom=False)
        self.moving_viewer_layout.addWidget(self.moving_image_viewer)

        self.fixed_viewer_layout.removeWidget(self.fixed_image_viewer)
        self.fixed_image_viewer.deleteLater()
        fixed_path = os.path.join(self.write_path, 'image_fixed.nii')
        self.fixed_image_viewer = VTKSliceViewer(fixed_path, is_dicom=False)
        self.fixed_viewer_layout.addWidget(self.fixed_image_viewer)


    def stats_page_button_pressed(self):
        self.ui.mainPageButton.setChecked(False)
        self.ui.scatter3dButton.setChecked(False)
        self.ui.scatter2dButton.setChecked(False)
        self.ui.body_stackedWidget.setCurrentWidget(self.ui.body_stackedWidgetPageStats)

    def scatter3d_page_button_pressed(self):
        self.ui.mainPageButton.setChecked(False)
        self.ui.statsPageButton.setChecked(False)
        self.ui.scatter2dButton.setChecked(False)
        self.ui.body_stackedWidget.setCurrentWidget(self.ui.body_stackedWidgetPage3d)

    def scatter2d_page_button_pressed(self):
        self.ui.mainPageButton.setChecked(False)
        self.ui.statsPageButton.setChecked(False)
        self.ui.scatter3dButton.setChecked(False)
        self.ui.body_stackedWidget.setCurrentWidget(self.ui.body_stackedWidgetPage2d)

    def ct_page_button_pressed(self):
        self.ui.geometryPageButton.setChecked(False)
        self.ui.fixed_stackedWidget.setCurrentWidget(self.ui.ct_page)

    def geometry_page_button_pressed(self):
        self.ui.ctPageButton.setChecked(False)
        self.ui.fixed_stackedWidget.setCurrentWidget(self.ui.geometry_page)

    def shutdown(self):
        # Stop ongoing processes
        if hasattr(self, 'analyze_thread_pool'):
            self.analyze_thread_pool.clear()

        # Close and release resources for visualization objects
        for attr in ['scatter3d', 'scatter2d', 'plots', 'params_table']:
            if hasattr(self, attr):
                obj = getattr(self, attr)
                if obj is not None:
                    obj.close()
                    setattr(self, attr, None)

        # Close the spinner
        if hasattr(self, 'spinner'):
            self.spinner.close()

        if hasattr(self, 'thread_pool'):
            self.thread_pool.waitForDone()

        if hasattr(self, 'fixed_image_viewer'):
            self.fixed_image_viewer.close()
            self.fixed_image_viewer.deleteLater()
            self.fixed_image_viewer = None

        if hasattr(self, 'fixed_viewer_layout'):
            while self.fixed_viewer_layout.count():
                item = self.fixed_viewer_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            self.ui.fixed_frame.setLayout(None)
            self.fixed_viewer_layout.deleteLater()
            self.fixed_viewer_layout = None

        if hasattr(self, 'moving_image_viewer'):
            self.moving_image_viewer.close()
            self.moving_image_viewer.deleteLater()
            self.moving_image_viewer = None

        if hasattr(self, 'moving_viewer_layout'):
            while self.moving_viewer_layout.count():
                item = self.moving_viewer_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            self.ui.moving_frame.setLayout(None)
            self.moving_viewer_layout.deleteLater()
            self.moving_viewer_layout = None

        # Clear data
        self.coords_ct = None
        self.coords_mri = None
        self.differences = None
        self.slice_differences = None

        # Clear file paths
        self.write_path = None
        self.output_path = None
        self.filename_ct = None
        self.filename_mri = None

        # Clear other attributes
        self.study_name = None
        self.context = None

        # Clear UI fields
        self.ui.titleEdit.setText("")
        self.ui.fixedimgEdit.setText("")
        self.ui.movingimgEdit.setText("")

    def closeEvent(self, event):
        self.shutdown()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    entrance = EntranceWindow()
    entrance.show()
    sys.exit(app.exec())
