import os
import subprocess
import json
from pathlib import Path
from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QGridLayout,
    QHeaderView,
    QPushButton,
    QFileDialog,
    QApplication,
    QMessageBox,
)
from PySide6.QtCore import Qt
from pydicom import dcmread
from src.preprocess.unpack import unpack_dicoms

from UI.import_main_screen import Ui_ImporterMainScreen
from UI.import_select_screen import Ui_ImporterSelectScreen
from UI.import_summary_screen import Ui_ImporterSummaryScreen


class ImporterMainScreen(QWidget):
    """
    Main Importer widget
    """

    def __init__(self, window_widget, title="Импорт изображений - MRI QA Solution"):
        super().__init__()
        self.ui = Ui_ImporterMainScreen()
        self.ui.setupUi(self)
        self.window_widget = window_widget
        window_widget.setWindowTitle(title)

        # add filetypes to combobox
        self.ui.dataComboBox.addItem("DICOM")

        # connect actions to navigation buttons
        self.ui.browseButton.clicked.connect(self.browse_file)
        self.ui.forwardButton.clicked.connect(self.forward)
        self.ui.cancelButton.clicked.connect(window_widget.cancel_event)
        self.directory_path = None

    def browse_file(self):
        directory_dialog = QFileDialog()
        self.directory_path = directory_dialog.getExistingDirectory(self, "Выберите папку с DICOM-файлами", "")

        if self.directory_path:
            self.window_widget.directory_path = self.directory_path
            self.ui.filepathLineEdit.setText(self.directory_path)

    def forward(self):
        if not self.directory_path:
            QMessageBox.warning(self, "Папка не выбрана", "Пожалуйста, выберите папку с DICOM-файлами.")
        else:
            self.window_widget.directory_path = self.directory_path
            self.window_widget.switch_to_select_screen()


class ImporterSelectScreen(QWidget):
    def __init__(self, window_widget):
        super().__init__()
        self.ui = Ui_ImporterSelectScreen()
        self.ui.setupUi(self)
        self.window_widget = window_widget

        # connect actions to navigation buttons
        self.ui.backButton.clicked.connect(window_widget.switch_to_main_screen)
        self.ui.forwardButton.clicked.connect(self.forward)
        self.ui.cancelButton.clicked.connect(window_widget.cancel_event)

        # Connect table item click to a handler
        self.ui.tableWidget.itemClicked.connect(self.select_series)

        self.series_dict = {}

    def forward(self):
        if not hasattr(self, 'selected_series_id'):
            QMessageBox.warning(self, "Последовательность не выбрана", "Пожалуйста, выберите последовательность.")
        else:
            self.window_widget.series_id = self.selected_series_id
            self.window_widget.series_files = self.series_dict[self.selected_series_id]
            self.window_widget.switch_to_summary_screen()

    def update_sequences(self):
        if not self.window_widget.directory_path:
            return

        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID последовательности", "Описание"])

        self.series_dict = {}
        dicom_files = [f for f in os.listdir(self.window_widget.directory_path) if f.endswith('.dcm')]

        for dicom_file in dicom_files:
            dicom_path = os.path.join(self.window_widget.directory_path, dicom_file)
            ds = dcmread(dicom_path)
            series_id = ds.SeriesInstanceUID
            series_description = ds.SeriesDescription if 'SeriesDescription' in ds else "N/A"

            if series_id not in self.series_dict:
                self.series_dict[series_id] = []

            self.series_dict[series_id].append(dicom_path)

        for series_id, files in self.series_dict.items():
            series_description = dcmread(files[0]).SeriesDescription if 'SeriesDescription' in dcmread(files[0]) else "N/A"
            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)
            self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(series_id))
            self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(series_description))

    def select_series(self, item):
        row = item.row()
        self.selected_series_id = self.ui.tableWidget.item(row, 0).text()


class ImporterSummaryScreen(QWidget):
    def __init__(self, window_widget, image_type, target_dir):
        super().__init__()
        self.ui = Ui_ImporterSummaryScreen()
        self.ui.setupUi(self)
        self.window_widget = window_widget
        self.target_dir = target_dir
        self.image_type = image_type

        # connect actions to navigation buttons
        self.ui.backButton.clicked.connect(window_widget.switch_to_select_screen)
        self.ui.importButton.clicked.connect(self.import_series)
        self.ui.cancelButton.clicked.connect(window_widget.cancel_event)

    def update_summary(self):
        if not self.window_widget.series_id:
            return

        self.ui.summaryTableWidget.clear()
        self.ui.summaryTableWidget.setRowCount(0)
        self.ui.summaryTableWidget.setColumnCount(2)
        self.ui.summaryTableWidget.setHorizontalHeaderLabels(["Параметр", "Значение"])

        # Use the first file from the selected series to show the summary
        ds = dcmread(self.window_widget.series_files[0])

        def add_row(label, value):
            row_position = self.ui.summaryTableWidget.rowCount()
            self.ui.summaryTableWidget.insertRow(row_position)
            self.ui.summaryTableWidget.setItem(row_position, 0, QTableWidgetItem(label))
            self.ui.summaryTableWidget.setItem(row_position, 1, QTableWidgetItem(value))

        # Add relevant information to the table
        metadata = {}
        metadata["Размерность"] = f"{ds.Rows} x {ds.Columns}"
        metadata["Размер вокселя"] = str(ds.PixelSpacing) if 'PixelSpacing' in ds else "N/A"
        metadata["Толщина среза"] = str(ds.SliceThickness) if 'SliceThickness' in ds else "N/A"
        metadata["Начало координат"] = str(ds.ImagePositionPatient) if 'ImagePositionPatient' in ds else "N/A"
        metadata["Ориентация"] = str(ds.ImageOrientationPatient) if 'ImageOrientationPatient' in ds else "N/A"
        metadata["Размер файла"] = f"{(os.path.getsize(self.window_widget.series_files[0])) / (1024 * 1024):.2f} MB"
        metadata["Модальность"] = ds.Modality
        metadata["SOP Class UID"] = ds.SOPClassUID
        metadata["Дата исследования"] = ds.StudyDate

        # Add the metadata to the table widget
        for key, value in metadata.items():
            add_row(key, value)

        # Determine the filename for the JSON file based on the modality
        if ds.Modality == "MR":
            json_filename = "mri_data.json"
        elif ds.Modality == "CT":
            json_filename = "ct_data.json"
        else:
            json_filename = f"{ds.Modality.lower()}_data.json"

        # Save metadata to the JSON file
        with open(os.path.join(self.target_dir, json_filename), 'w', encoding='utf-8') as json_file:
            json.dump({'voxel_size': float(ds.PixelSpacing[0]), 'slice_thickness': float(ds.SliceThickness)}, json_file, ensure_ascii=False, indent=4)

    def import_series(self):
        if not self.window_widget.series_files:
            return

        source_folder = Path(self.window_widget.directory_path)
        if self.image_type == 'fixed':
            output_name = "image_fixed"
        else:
            output_name = "image_moving"

        try:
            unpack_dicoms(source_folder, self.target_dir, name=output_name)
            output_nifti = os.path.join(self.target_dir, f"{output_name}.nii")
            QMessageBox.information(self, "Изображение успешно импортировано", f"NIfTI файл создан по пути {output_nifti}")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Import Failed", str(e))

        self.window_widget.finish_importing()




class ImporterWindow(QStackedWidget):
    def __init__(self, image_type, target_dir):
        super().__init__()

        self.importer_main = ImporterMainScreen(self)
        self.addWidget(self.importer_main)

        self.importer_select = ImporterSelectScreen(self)
        self.addWidget(self.importer_select)

        self.importer_summary = ImporterSummaryScreen(window_widget=self, image_type=image_type, target_dir=target_dir)
        self.addWidget(self.importer_summary)

        self.setCurrentWidget(self.importer_main)
        self.directory_path = None
        self.series_id = None
        self.series_files = []

    def switch_to_main_screen(self):
        self.setCurrentWidget(self.importer_main)
        self.setWindowTitle("Импорт изображений - MRI QA Solution")

    def switch_to_select_screen(self):
        self.importer_select.update_sequences()
        self.setCurrentWidget(self.importer_select)
        self.setWindowTitle("Выбрать последовательность - MRI QA Solution")

    def switch_to_summary_screen(self):
        self.importer_summary.update_summary()
        self.setCurrentWidget(self.importer_summary)
        self.setWindowTitle("Подтвердить импорт - MRI QA Solution")

    def finish_importing(self):
        self.close()

    def cancel_event(self):
        self.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ImporterWindow()
    window.show()
    sys.exit(app.exec())
