from PySide6.QtWidgets import QWidget, QSlider, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt, QUrl

import plotly.express as px
import numpy as np
import nibabel as nib

class Viewer(QWidget):
    def __init__(self, path_ct, path_mri):
        super().__init__()

        self.setWindowTitle("Просмотр изображений")

        self.path_ct = path_ct
        self.path_mri = path_mri

        self.browser = QWebEngineView(self)

        image_ct = nib.load(path_ct)
        image_mri = nib.load(path_mri)

        self.data_ct = image_ct.get_fdata()
        self.data_mri = image_mri.get_fdata()

        print('min ct: ', np.min(self.data_ct))
        print('max ct: ', np.max(self.data_ct))

        print('min mri: ', np.min(self.data_mri))
        print('max mri: ', np.max(self.data_mri))

        self.image_shape = self.data_ct.shape

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(self.image_shape[2])  # Set the maximum value as per your requirement
        self.slider.valueChanged.connect(self.update_viewer)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.browser)
        self.layout.addWidget(self.slider)

        self.resize(850, 800)
        self.init_viewer()

    def init_viewer(self, z_value=60):
        image = px.imshow(self.data_ct[:,:,50])
        image.show()
        # self.browser.setHtml(image.to_html(full_html=False))

    def update_viewer(self, value):
        z_value = value
        self.init_viewer(z_value)

if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    T = Viewer('/Users/bzavolovich/Developer/MRIphantom_interface/input_CT.nii.gz', '/Users/bzavolovich/Developer/MRIphantom_interface/input_MRI_resliced.nii.gz')
    T.show()

    app.exec()
