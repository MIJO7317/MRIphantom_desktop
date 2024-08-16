"""
Module: scatter2d
Module for 2D scatter viewer
"""
from PySide6.QtWidgets import QWidget, QSlider, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt

import numpy as np
import plotly.graph_objects as go
import pandas as pd

class Scatter2D(QWidget):
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
        
        # Set size policy to keep the aspect ratio
        self.browser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.slider = QSlider(Qt.Horizontal)
        self.min_value_slider = 0
        self.max_value_slider = 59
        self.slider.setMinimum(self.min_value_slider)
        self.slider.setMaximum(
            self.max_value_slider
        )  # Set the maximum value as per your requirement
        self.slider.valueChanged.connect(self.update_scatter_plot)
        
        self.label = QLabel('1', self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter |
                                Qt.AlignmentFlag.AlignVCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(self.browser)
        h_layout = QHBoxLayout(self)
        h_layout.addWidget(self.slider)
        h_layout.addSpacing(15)
        h_layout.addWidget(self.label)
        layout.addLayout(h_layout)
        self.resize(850, 850)
        self.init_scatter2d()

    def init_scatter2d(self, z_value=0):
        """
        Initialize 2D scatter viewer
        """
        
        self.fig = go.Figure()
        
        df_ct = pd.DataFrame(self.data_ct, columns=["x", "y", "z"])
        df_mri = pd.DataFrame(self.data_mri, columns=["x", "y", "z"])

        # Filter data based on the z-axis value
        ct_points = df_ct[df_ct["z"] == z_value][["x", "y"]].values
        mr_points = df_mri[df_mri["z"] == z_value][["x", "y"]].values

        # Add CT points
        scatter_ct = go.Scatter(
            x=ct_points[:, 0],
            y=ct_points[:, 1],
            mode='markers',
            marker=dict(
                size=10,
                color='blue',
                symbol='circle'
            ),
            name='КТ'
        )
        self.fig.add_trace(scatter_ct)

        # Add MRI points
        scatter_mri = go.Scatter(
            x=mr_points[:, 0],
            y=mr_points[:, 1],
            mode='markers',
            marker=dict(
                size=10,
                color='red',
                symbol='circle'
            ),
            name='МРТ'
        )
        self.fig.add_trace(scatter_mri)

        # Customize the layout
        self.fig.update_layout(
            title='Сравнение точек КТ и МРТ',
            title_font=dict(size=20, family='Times New Roman'),
            font=dict(family='Times New Roman'),
            plot_bgcolor='rgba(255,255,255,1)',
            xaxis=dict(
                visible=True,
                showgrid=True,
                gridcolor='gray',
                gridwidth=1,
                zeroline=True,
                zerolinecolor='gray',
                zerolinewidth=2,
                title='X Координата'
            ),
            yaxis=dict(
                visible=True,
                showgrid=True,
                gridcolor='gray',
                gridwidth=1,
                zeroline=True,
                zerolinecolor='gray',
                zerolinewidth=2,
                scaleanchor='x',
                scaleratio=1,
                title='Y Координата'
            ),
            margin=dict(t=50, b=50, l=50, r=50),
            legend=dict(
                x=0,
                y=1,
                bgcolor='rgba(255,255,255,0.5)',
                bordercolor='rgba(0,0,0,0.5)'
            )
        )

        self.browser.setHtml(self.fig.to_html(include_plotlyjs="cdn"))

    def update_scatter_plot(self, value):
        # Update scatter plot when slider value changes
        z_value = value  # Adjust this according to your data range
        self.label.setText(str(value+1))
        self.init_scatter2d(z_value)
