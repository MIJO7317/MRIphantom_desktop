from PySide6.QtWidgets import QWidget, QSlider, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt

import plotly.express as px
import pandas as pd
import numpy as np
import nibabel as nib
from PIL import Image
import io
import base64

class Scatter2D(QWidget):
    """
    2D scatter view widget
    """
    def __init__(self, data_ct, data_mri, mri_nifti_path, ct_nifti_path, title="2D просмотр отклонений"):
        super().__init__()

        self.fig = None
        self.data_ct = data_ct
        self.data_mri = data_mri
        self.show_mri = True
        self.show_ct = True

        # Load the NIfTI files
        self.mri_img = nib.load(mri_nifti_path)
        self.mri_data = self.mri_img.get_fdata()

        self.ct_img = nib.load(ct_nifti_path)
        self.ct_data = self.ct_img.get_fdata()

        self.setWindowTitle(title)

        self.browser = QWebEngineView(self)

        self.slider = QSlider(Qt.Horizontal)
        self.min_value_slider = 41
        self.max_value_slider = 107
        self.slider.setMinimum(self.min_value_slider)
        self.slider.setMaximum(self.max_value_slider)
        self.slider.valueChanged.connect(self.update_scatter_plot)

        self.mri_button = QPushButton("Toggle MRI", self)
        self.mri_button.setCheckable(True)
        self.mri_button.setChecked(True)
        self.mri_button.clicked.connect(self.toggle_mri)

        self.ct_button = QPushButton("Toggle CT", self)
        self.ct_button.setCheckable(True)
        self.ct_button.setChecked(True)
        self.ct_button.clicked.connect(self.toggle_ct)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.mri_button)
        button_layout.addWidget(self.ct_button)

        layout = QVBoxLayout(self)
        layout.addWidget(self.browser)
        layout.addWidget(self.slider)
        layout.addLayout(button_layout)
        self.resize(850, 850)
        self.init_scatter2d()

    def init_scatter2d(self, z_value=0):
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

        # Create scatter plot
        fig = px.scatter(df_filtered, x="x", y="y", color="modality")
        fig.update_traces(marker_size=5)

        # Add MRI image layer if enabled
        if self.show_mri and self.min_value_slider <= z_value < self.max_value_slider:
            mri_slice = np.flipud(self.mri_data[:, :, z_value])
            mri_slice_normalized = (mri_slice - np.min(mri_slice)) / (np.max(mri_slice) - np.min(mri_slice)) * 255
            mri_image = Image.fromarray(mri_slice_normalized.astype(np.uint8))

            with io.BytesIO() as output:
                mri_image.save(output, format="PNG")
                png_data = output.getvalue()

            png_base64 = base64.b64encode(png_data).decode('utf-8')

            fig.add_layout_image(
                dict(
                    source=f'data:image/png;base64,{png_base64}',
                    xref="x",
                    yref="y",
                    x=0,
                    y=mri_slice.shape[0],
                    sizex=mri_slice.shape[1],
                    sizey=mri_slice.shape[0],
                    sizing="contain",
                    opacity=1,
                    layer="below"
                )
            )

        # Add CT image layer if enabled
        if self.show_ct and self.min_value_slider <= z_value < self.max_value_slider:
            ct_slice = np.flipud(self.ct_data[:, :, z_value])
            ct_slice_normalized = (ct_slice - np.min(ct_slice)) / (np.max(ct_slice) - np.min(ct_slice)) * 255
            ct_image = Image.fromarray(ct_slice_normalized.astype(np.uint8))

            with io.BytesIO() as output:
                ct_image.save(output, format="PNG")
                png_data = output.getvalue()

            png_base64 = base64.b64encode(png_data).decode('utf-8')

            fig.add_layout_image(
                dict(
                    source=f'data:image/png;base64,{png_base64}',
                    xref="x",
                    yref="y",
                    x=0,
                    y=ct_slice.shape[0],
                    sizex=ct_slice.shape[1],
                    sizey=ct_slice.shape[0],
                    sizing="contain",
                    opacity=0.5,
                    layer="below"
                )
            )

        fig.update_layout(xaxis=dict(scaleanchor="y", scaleratio=1))

        self.browser.setHtml(fig.to_html(include_plotlyjs="cdn"))

    def update_scatter_plot(self, value):
        z_value = value
        self.init_scatter2d(z_value)

    def toggle_mri(self):
        self.show_mri = not self.show_mri
        self.update_scatter_plot(self.slider.value())

    def toggle_ct(self):
        self.show_ct = not self.show_ct
        self.update_scatter_plot(self.slider.value())

# Пример использования:
# data_ct и data_mri - это ваши данные, содержащие координаты x, y, z
# mri_nifti_path и ct_nifti_path - пути к вашим NIfTI-файлам

# data_ct = ...
# data_mri = ...
# mri_nifti_path = 'path/to/your/mri_file.nii'
# ct_nifti_path = 'path/to/your/ct_file.nii'

# Пример создания виджета
# widget = Scatter2D(data_ct, data_mri, mri_nifti_path, ct_nifti_path)
# widget.show()
