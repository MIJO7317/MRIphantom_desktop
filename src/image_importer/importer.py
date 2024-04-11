"""
Module: importer
Module for importing MRI and CT images
"""

from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QTableWidget,
    QGridLayout,
    QHeaderView,
    QPushButton,
    QApplication,
)

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
        window_widget.setWindowTitle(title)

        # add filetypes to combobox
        self.ui.dataComboBox.addItem("DICOM")

        # connect actions to navigation buttons
        self.ui.forwardButton.clicked.connect(window_widget.switch_to_select_screen)
        self.ui.cancelButton.clicked.connect(window_widget.cancel_event)


class ImporterSelectScreen(QWidget):
    def __init__(self, window_widget):
        super().__init__()

        self.ui = Ui_ImporterSelectScreen()
        self.ui.setupUi(self)

        # connect actions to navigation buttons
        self.ui.backButton.clicked.connect(window_widget.switch_to_main_screen)
        self.ui.forwardButton.clicked.connect(window_widget.switch_to_summary_screen)
        self.ui.cancelButton.clicked.connect(window_widget.cancel_event)


class ImporterSummaryScreen(QWidget):
    def __init__(self, window_widget):
        super().__init__()
        self.ui = Ui_ImporterSummaryScreen()
        self.ui.setupUi(self)

        # connect actions to navigation buttons
        self.ui.backButton.clicked.connect(window_widget.switch_to_select_screen)
        self.ui.importButton.clicked.connect(window_widget.finish_importing)
        self.ui.cancelButton.clicked.connect(window_widget.cancel_event)


class ImporterWindow(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.importer_main = ImporterMainScreen(self)
        self.addWidget(self.importer_main)

        self.importer_select = ImporterSelectScreen(self)
        self.addWidget(self.importer_select)

        self.importer_summary = ImporterSummaryScreen(self)
        self.addWidget(self.importer_summary)

        self.setCurrentWidget(self.importer_main)

    def switch_to_main_screen(self):
        self.setCurrentWidget(self.importer_main)
        self.setWindowTitle("Импорт изображений - MRI QA Solution")

    def switch_to_select_screen(self):
        self.setCurrentWidget(widget.importer_select)
        self.setWindowTitle("Выбрать серию - MRI QA Solution")

    def switch_to_summary_screen(self):
        self.setCurrentWidget(widget.importer_summary)
        self.setWindowTitle("Подтвердить импорт - MRI QA Solution")

    def finish_importing(self):
        self.close()

    def cancel_event(self):
        self.close()


import sys

app = QApplication(sys.argv)
widget = ImporterWindow()
widget.show()
app.exec()
