"""
Module: report
Module for report widget
"""
from PySide6.QtWidgets import QWidget, QGridLayout, QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
import sys
from table import Table
import plotly.express as px
import pandas as pd


class Report(QWidget):
    """
    Report widget
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Report')
        self.browser = QWebEngineView(self)
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.browser)
        self.resize(1200, 800)
        self.init_report()

    def init_report(self):
        self.browser.setHtml('hello world')


if __name__ == '__main__':
    app = QApplication()
    report = Report()
    report.show()
    sys.exit(app.exec())
