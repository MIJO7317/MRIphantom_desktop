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
    slice_img_generator,
    perform_thresholding,
    isolate_markers,
    get_coords,
    count_difference,
    count_difference_geometry,
)
from src.segmentation.process_v2 import segmentation, count_difference_2
from src.registration.registration import ManualRegistrationWindow, rigid_reg

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
        self.is_interpolated = False
        self.is_geometric = False

        self.initUi()

    def initUi(self):
        self.context = {}

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.ui.moving_viewer = None
        self.ui.fixed_viewer = None

        self.ui.titleEdit.setPlaceholderText("Название теста")
        self.ui.descriptionEdit.setPlaceholderText("Описание")

        self.ui.fixedimgEdit.setPlaceholderText("Выберите папку с КТ (Fixed)")
        self.ui.movingimgEdit.setPlaceholderText("Выберите папку с МРТ (Moving)")
        self.ui.fixedimgEdit.mousePressEvent = (
            lambda event: self.openFixedImageDirectoryDialog()
        )
        self.ui.movingimgEdit.mousePressEvent = (
            lambda event: self.openMovingImageDirectoryDialog()
        )
        self.ui.interpolateButton.stateChanged.connect(
            self.interpolationButtonStateChanged
        )
        self.ui.geometryButton.stateChanged.connect(self.geometryButtonStateChanged)

        self.fixed_image_path = None
        self.moving_image_path = None
        self.ct_img = None
        self.mri_img = None

        self.ui.phantomTypeCombo.addItem("Elekta (Axial Grid)")

        self.ui.analyzeButton.setCheckable(True)
        self.ui.analyzeButton.toggled.connect(self.analyzeImages)
        self.analyze_thread_pool = QThreadPool()

        self.ui.registrationButton.setCheckable(True)
        self.ui.registrationButton.toggled.connect(self.register_button_pressed)
        self.registration_thread_pool = QThreadPool()

        self.ui.statusLabel.setText("Готов к работе")

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
        fixedImageImporter = ImporterWindow('fixed', write_path)
        fixedImageImporter.setAttribute(Qt.WA_DeleteOnClose)
        fixedImageImporter.show()

        loop = QEventLoop()
        fixedImageImporter.destroyed.connect(loop.quit)
        loop.exec()

        dicom_dir = fixedImageImporter.directory_path
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
        movingImageImporter = ImporterWindow('moving', write_path)
        movingImageImporter.setAttribute(Qt.WA_DeleteOnClose)
        movingImageImporter.show()

        loop = QEventLoop()
        movingImageImporter.destroyed.connect(loop.quit)
        loop.exec()

        dicom_dir = movingImageImporter.directory_path
        saved_nifti_filepath = os.path.join(write_path, "image_moving.nii")

        if saved_nifti_filepath:
            self.ui.movingimgEdit.setText(saved_nifti_filepath)
            self.moving_image_path = saved_nifti_filepath

        self.moving_image_viewer = VTKSliceViewer(dicom_dir)
        self.moving_viewer_layout = QVBoxLayout(self.ui.moving_frame)
        self.moving_viewer_layout.addWidget(QLabel('МРТ'))
        self.moving_viewer_layout.addWidget(self.moving_image_viewer)

    def register_button_pressed(self):
        self.ui.statusLabel.setText("Выполняется совмещение МРТ и КТ...")
        QApplication.processEvents()  # Force update the UI

        worker_register = Worker(self.registerImages())
        self.registration_thread_pool.start(worker_register)
        worker_register.signaller.finished.connect(self.finishRegistration())

    def registerImages(self):
        rigid_reg(self.fixed_image_path, self.moving_image_path, self.write_path)
        self.ui.statusLabel.setText("Открыто окно ручной корректировки совмещения...")
        QApplication.processEvents()  # Force update the UI

    def finishRegistration(self):
        self.ui.statusLabel.setText("Совмещение МРТ и КТ завершено")

        manual_window = ManualRegistrationWindow(
            os.path.join(self.write_path, 'CT_fixed.nii'),
            os.path.join(self.write_path, 'MRI_warped.nii'),
            self.write_path
        )
        manual_window.setAttribute(Qt.WA_DeleteOnClose)
        manual_window.show()

        loop = QEventLoop()
        manual_window.destroyed.connect(loop.quit)
        loop.exec()

        # обновить МРТ
        self.moving_viewer_layout.removeWidget(self.moving_image_viewer)
        self.moving_image_viewer.deleteLater()

        moving_path = os.path.join(self.write_path, 'MRI_warped_fixed.nii')
        self.moving_image_viewer = VTKSliceViewer(moving_path, is_dicom=False)
        self.moving_viewer_layout.addWidget(self.moving_image_viewer)

        # обновить КТ
        self.fixed_viewer_layout.removeWidget(self.fixed_image_viewer)
        self.fixed_image_viewer.deleteLater()

        fixed_path = os.path.join(self.write_path, 'CT_fixed.nii')
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

        if self.is_geometric is False:
            self.moving_image_path = os.path.join(self.write_path, "MRI_warped_fixed.nii")
            self.fixed_image_path = os.path.join(self.write_path, "CT_fixed.nii")

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

            # self.ui.statusLabel.setText("Выполняется распаковка КТ изображений")
            # # create generators for original images
            # ct_slice_gen = slice_img_generator(
            #     self.fixed_image_path, self.is_interpolated
            # )
            # self.ui.statusLabel.setText("Выполняется распаковка МРТ изображений")
            # mri_slice_gen = slice_img_generator(
            #     self.moving_image_path, self.is_interpolated
            # )
            #
            # # threshold segmentation
            # self.ui.statusLabel.setText("Выполняется сегментация КТ изображений")
            # ct_thresh_gen = perform_thresholding(
            #     ct_slice_gen, False, self.is_interpolated
            # )
            # self.ui.statusLabel.setText("Выполняется сегментация МРТ изображений")
            # mri_thresh_gen = perform_thresholding(
            #     mri_slice_gen, True, self.is_interpolated
            # )
            #
            # ct_pickle_path = os.path.join(self.write_path, "markers_CT.pickle")
            # mri_pickle_path = os.path.join(self.write_path, "markers_MRI.pickle")
            # # detect markers and save as .pickle
            # self.ui.statusLabel.setText("Выполняется детекция маркеров на КТ")
            # isolate_markers(ct_thresh_gen, ct_pickle_path, self.is_interpolated)
            # self.ui.statusLabel.setText("Выполняется детекция маркеров на МРТ")
            # isolate_markers(mri_thresh_gen, mri_pickle_path, self.is_interpolated)
            # # perform marker analysis
            # self.ui.statusLabel.setText("Выполняется расчет отклонений")
            # _, self.differences, self.slice_differences = count_difference(
            #     ct_pickle_path, mri_pickle_path, self.write_path
            # )
            #
            # self.coords_ct = get_coords(
            #     os.path.join(self.write_path, "markers_CT.pickle")
            # )
            # self.coords_mri = get_coords(
            #     os.path.join(self.write_path, "markers_MRI.pickle")
            # )

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
            self.ui.statusLabel.setText("Выполняется распаковка и предобработка МРТ")
            self.moving_image_path = os.path.join(self.write_path, "MRI_warped_fixed.nii")
            self.fixed_image_path = os.path.join(self.write_path, "CT_fixed.nii")

            # create generators for original images
            ct_slice_gen = slice_img_generator(
                self.fixed_image_path, self.is_interpolated
            )
            mri_slice_gen = slice_img_generator(
                self.moving_image_path, self.is_interpolated
            )

            # threshold segmentation
            self.ui.statusLabel.setText("Выполняется сегментация МРТ")
            ct_thresh_gen = perform_thresholding(
                ct_slice_gen, False, self.is_interpolated
            )
            mri_thresh_gen = perform_thresholding(
                mri_slice_gen, True, self.is_interpolated
            )

            ct_pickle_path = os.path.join(self.write_path, "markers_CT.pickle")
            mri_pickle_path = os.path.join(self.write_path, "markers_MRI.pickle")
            # detect markers and save as .pickle
            self.ui.statusLabel.setText("Выполняется детекция маркеров на МРТ")
            isolate_markers(ct_thresh_gen, ct_pickle_path, self.is_interpolated)
            isolate_markers(mri_thresh_gen, mri_pickle_path, self.is_interpolated)
            # perform marker analysis
            self.ui.statusLabel.setText("Выполняется расчет отклонений")
            _, self.differences, self.slice_differences = count_difference_geometry(
                ct_pickle_path, mri_pickle_path, self.write_path
            )

            self.coords_ct = get_coords(
                os.path.join(self.write_path, "markers_CT.pickle")
            )
            self.coords_mri = get_coords(
                os.path.join(self.write_path, "markers_MRI.pickle")
            )
            self.ui.statusLabel.setText("Расчет выполнен")


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
        self.params_table.show()
        self.scatter3d = Scatter3D(self.coords_ct, self.coords_mri)
        self.scatter3d.show()
        self.scatter2d = Scatter2D(self.coords_ct, self.coords_mri)
        self.scatter2d.show()
        self.plots = Plots(self.slice_differences)
        self.plots.show()

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
            "description": self.ui.descriptionEdit.text(),
            "fixedimgpath": self.ui.fixedimgEdit.text(),
            "movingimgpath": self.ui.movingimgEdit.text(),
        }

        self.spinner.show()

        worker_to_nifti = Worker(self.analyze)
        self.analyze_thread_pool.start(worker_to_nifti)
        worker_to_nifti.signaller.finished.connect(self.finishAnalysis)

        # self.ui.descriptionEdit.setText("")
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

    # TODO simplify
    def interpolationButtonStateChanged(self):
        if self.is_interpolated:
            self.is_interpolated = False
        else:
            self.is_interpolated = True

    # TODO simplify
    def geometryButtonStateChanged(self):
        if self.is_geometric:
            self.is_geometric = False
        else:
            self.is_geometric = True

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
        self.ui.descriptionEdit.setText("")
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
