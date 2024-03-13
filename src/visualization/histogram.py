from PySide6.QtWidgets import QWidget, QTableWidget, QGridLayout, \
    QTableWidgetItem, QHeaderView, QFileDialog, QMessageBox, \
    QPushButton

from PySide6.QtWebEngineWidgets import *

import plotly.express as px

import pandas as pd

class Histogram(QWidget):
    def __init__(self, d, title="Гистограмма отклонений"):

        super().__init__()

        self.d = d
        self.setWindowTitle(title)

        self.browser = QWebEngineView(self)

        # Add table
        self.l = QGridLayout(self)
        self.l.addWidget(self.browser)

        self.resize(1200,800)

        self.init_histogram()

    def init_histogram(self):

        fig = px.histogram(self.d, histnorm='probability density')

        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    T = Histogram()
    T.show()

    app.exec_()