"""
Module: scatter2d
Module for 2D scatter viewer
"""
from PySide6.QtWidgets import QWidget, QSlider, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt

import plotly.express as px
import pandas as pd


class MarkerViewer(QWidget):
    """
    2D scatter view widget
    """
    def __init__(self, data_ct, data_mri, title="2D просмотр отклонений"):
        super().__init__()

        self.fig = None
        self.data_ct = data_ct
        self.data_mri = data_mri

        self.setWindowTitle(title)
        self.browser = QWebEngineView(self)

        self.slider = QSlider(Qt.Horizontal)
        self.min_value_slider = 0
        self.max_value_slider = 60
        self.slider.setMinimum(self.min_value_slider)
        self.slider.setMaximum(
            self.max_value_slider
        )  # Set the maximum value as per your requirement
        self.slider.valueChanged.connect(self.update_scatter_plot)

        layout = QVBoxLayout(self)
        layout.addWidget(self.browser)
        layout.addWidget(self.slider)
        self.resize(850, 850)
        self.init_scatter2d()

    def init_scatter2d(self, z_value=50):
        """
        Initialize 2D scatter viewer
        """
        df_ct = pd.DataFrame(self.data_ct, columns=["x", "y", "z"])
        df_ct["modality"] = "CT"

        df_mri = pd.DataFrame(self.data_mri, columns=["x", "y", "z"])
        df_mri["modality"] = "MRI"

        df = pd.concat([df_ct, df_mri])

        # Filter data based on the z-axis value
        df_filtered = df[df["z"] == z_value]

        self.fig = px.scatter(df_filtered, x="x", y="y", color="modality")
        self.fig.update_traces(marker_size=5)

        self.browser.setHtml(self.fig.to_html(include_plotlyjs="cdn"))

    def update_scatter_plot(self, value):
        # Update scatter plot when slider value changes
        z_value = value  # Adjust this according to your data range

        self.init_scatter2d(z_value)
