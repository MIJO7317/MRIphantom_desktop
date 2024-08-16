"""
Module: scatter2d
Module for 2D scatter viewer
"""
from PySide6.QtWidgets import QWidget, QSlider, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt

# import plotly.express as px
import plotly.graph_objects as go
from scipy.spatial import cKDTree
import numpy as np
import pandas as pd


class Scatter2DDev(QWidget):
    """
    2D scatter deviations view widget
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
        self.slider.valueChanged.connect(self.update_scatter_dev_plot)
        
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
        self.init_scatter2d_dev()

    def init_scatter2d_dev(self, z_value = 0, max_deviation = 3, grid_step = 30):
        """
        Initialize 2D scatter deviations viewer
        """
        
        self.fig = go.Figure()
        
        df_ct = pd.DataFrame(self.data_ct, columns=["x", "y", "z"])
        df_mri = pd.DataFrame(self.data_mri, columns=["x", "y", "z"])

        # Filter data based on the z-axis value
        ct_points = df_ct[df_ct["z"] == z_value][["x", "y"]].values
        mr_points = df_mri[df_mri["z"] == z_value][["x", "y"]].values

        # Build KD-tree for nearest neighbor search
        tree = cKDTree(mr_points)
        distances, indices = tree.query(ct_points)

        # Reorder CT points to match nearest MR points
        mr_points = mr_points[indices]
        deviations = np.linalg.norm(mr_points - ct_points, axis=1)
        
        # Create masks for points within and beyond max_deviation
        within_max = deviations <= grid_step/2
        beyond_max = ~within_max
        
        # Prepare color and text data
        colors = np.where(within_max, deviations, grid_step/2)
        text = [f'{d:.2f}' if d <= grid_step/2 else 'NaN' for d in deviations]
        
        # Add scatter plot for points within max_deviation
        scatter_within = go.Scatter(
            x=ct_points[within_max, 0],
            y=ct_points[within_max, 1],
            mode='markers+text',
            marker=dict(
                size=40,
                color=colors[within_max],
                colorscale='YlOrRd',
                colorbar=dict(
                    title='Отклонение', 
                    titleside='right',
                    tickfont=dict(size=14),
                    title_font=dict(size=16)
                ),
                cmin=0,
                cmax=max_deviation
            ),
            text=[t for t, w in zip(text, within_max) if w],
            textposition='middle center',
            textfont=dict(size=14, color='black'),
            hoverinfo='none',
            showlegend=False
        )
        self.fig.add_trace(scatter_within)

        # Add scatter plot for points beyond max_deviation
        scatter_beyond = go.Scatter(
            x=ct_points[beyond_max, 0],
            y=ct_points[beyond_max, 1],
            mode='markers+text',
            marker=dict(
                size=40,
                color='gray',
            ),
            text=[t for t, b in zip(text, beyond_max) if b],
            textposition='middle center',
            textfont=dict(size=14, color='black'),
            hoverinfo='none',
            showlegend=False
        )
        self.fig.add_trace(scatter_beyond)

        # Customize the layout
        self.fig.update_layout(
            title='Отклонения МРТ от КТ',
            title_font=dict(size=20, family='Times New Roman'),
            font=dict(family='Times New Roman'),
            plot_bgcolor='rgba(255,255,255,1)',
            xaxis=dict(
                showline=False,  # Hide axis line
                showgrid=False,  # Hide grid lines
                showticklabels=False,  # Hide axis ticks and labels
                zeroline=False  # Hide the zero line
            ),
            yaxis=dict(
                showline=False,  # Hide axis line
                showgrid=False,  # Hide grid lines
                showticklabels=False,  # Hide axis ticks and labels
                zeroline=False  # Hide the zero line
            ),
            margin=dict(t=50, b=0, l=0, r=0)
        )

        self.browser.setHtml(self.fig.to_html(include_plotlyjs="cdn"))

    def update_scatter_dev_plot(self, value):
        # Update scatter plot when slider value changes
        z_value = value  # Adjust this according to your data range
        self.label.setText(str(value+1))
        self.init_scatter2d_dev(z_value)
