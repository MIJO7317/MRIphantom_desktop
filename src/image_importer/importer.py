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


def switch_to_select_screen():
    widget.setCurrentWidget(widget.importer_select)
    print("Перешел в Select Screen")


class ImporterMainScreen(QWidget):
    """
    Main Importer widget
    """

    def __init__(self):
        super().__init__()

        # Add table
        self.layout = QGridLayout(self)
        self.table = QTableWidget()
        self.table.setColumnCount(2)

        # Adjust table to window size
        h = self.table.horizontalHeader()
        h.setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        # Add export option
        p = QPushButton("Далее (в Select Screen)")
        p.clicked.connect(switch_to_select_screen)
        self.layout.addWidget(p)
        self.resize(800, 600)


def switch_to_summary_screen():
    widget.setCurrentWidget(widget.importer_summary)
    print("Перешел в Summary Screen")


class ImporterSelectScreen(QWidget):
    def __init__(self, title="Выбрать серию - MRI QA Solution"):
        super().__init__()

        self.setWindowTitle(title)

        # Add table
        self.layout = QGridLayout(self)
        self.table = QTableWidget()
        self.table.setColumnCount(2)

        # Adjust table to window size
        h = self.table.horizontalHeader()
        h.setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        # Add export option
        p = QPushButton("Далее (в Summary Screen)")
        p.clicked.connect(switch_to_summary_screen())
        self.layout.addWidget(p)
        self.resize(700, 400)


def finish_importing():
    print("success!!!")


class ImporterSummaryScreen(QWidget):
    def __init__(self, title="Выбрать серию - MRI QA Solution"):
        super().__init__()

        self.setWindowTitle(title)

        # Add table
        self.layout = QGridLayout(self)
        self.table = QTableWidget()
        self.table.setColumnCount(2)

        # Adjust table to window size
        h = self.table.horizontalHeader()
        h.setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        # Add export option
        p = QPushButton("Завершить импорт")
        p.clicked.connect(finish_importing())
        self.layout.addWidget(p)
        self.resize(700, 400)


class ImporterWindow(QStackedWidget):
    def __init__(self, title="Имортировать изображение - MRI QA Solution"):
        super().__init__()

        self.setWindowTitle(title)

        self.importer_main = ImporterMainScreen()
        self.addWidget(self.importer_main)

        self.importer_select = ImporterSelectScreen()
        self.addWidget(self.importer_select)

        self.importer_summary = ImporterSummaryScreen()
        self.addWidget(self.importer_summary)

        self.setCurrentWidget(self.importer_main)
        self.resize(800, 600)


import sys

app = QApplication(sys.argv)
widget = ImporterWindow()
widget.show()
app.exec()
