"""
Module: histogram
Module for histogram visualization
"""
from PySide6.QtWidgets import QWidget, QGridLayout

from PySide6.QtWebEngineWidgets import QWebEngineView
import plotly.express as px


class Histogram(QWidget):
    """
    Histogram widget
    """
    def __init__(self, input_data, title="Гистограмма отклонений"):
        super().__init__()
        self.data = input_data
        self.setWindowTitle(title)
        self.browser = QWebEngineView(self)
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.browser)
        self.resize(1200, 800)
        self.init_histogram()

    def init_histogram(self):
        """
        Initialize the histogram
        """
        fig = px.histogram(self.data, histnorm="probability density")
        self.browser.setHtml(fig.to_html(include_plotlyjs="cdn"))
