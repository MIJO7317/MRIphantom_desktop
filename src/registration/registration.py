import os
import ants
import nibabel as nib
import numpy as np

from PySide6.QtWidgets import (
    QVBoxLayout,
    QApplication,
    QMainWindow,
)
from PySide6 import QtWidgets
from UI.registration_screen import Ui_ManualRegistrationWindow
from src.visualization.overlay_viewer import VTKOverlayViewer


def rigid_reg(fixed: str, moving: str, save_path: str):
    ants_fixed = ants.image_read(fixed)
    ants_moving = ants.image_read(moving)

    res = ants.registration(
        fixed=ants_fixed, moving=ants_moving, type_of_transform="Rigid"
    )

    transform = ants.read_transform(res["fwdtransforms"][0])

    ants_warped = ants.apply_ants_transform(
        transform, ants_moving, data_type="image", reference=ants_fixed
    )

    print('registration finished')

    nib.save(ants_warped, os.path.join(save_path, 'MRI_warped.nii.gz'))
    nib.save(ants_fixed, os.path.join(save_path, 'CT_fixed.nii.gz'))

    print('images saved')

    return ants_warped


def apply_manual_shift(fixed: str, moving: str, save_path: str, x: float, y: float, z: float, xy: float, xz: float,
                       yz: float):
    """
    Apply a manual shift to an image with translation and rotation.

    Args:
        fixed: str, path to the fixed image file.
        moving: str, path to the moving image file.
        save_path: str, directory path where the shifted image will be saved.
        x: float, translation along the X-axis.
        y: float, translation along the Y-axis.
        z: float, translation along the Z-axis.
        xy: float, rotation around the XY plane in degrees.
        xz: float, rotation around the XZ plane in degrees.
        yz: float, rotation around the YZ plane in degrees.

    Returns:
        ants.ANTsImage: the shifted image.
    """

    ants_moving = ants.image_read(moving)
    ants_fixed = ants.image_read(fixed)

    # Convert rotation angles from degrees to radians
    xy_rad = np.deg2rad(xy)
    xz_rad = np.deg2rad(xz)
    yz_rad = np.deg2rad(yz)

    # Create rotation matrices
    R_xz = np.array([
        [1, 0, 0],
        [0, np.cos(xz_rad), -np.sin(xz_rad)],
        [0, np.sin(xz_rad), np.cos(xz_rad)]
    ])

    R_yz = np.array([
        [np.cos(yz_rad), 0, np.sin(yz_rad)],
        [0, 1, 0],
        [-np.sin(yz_rad), 0, np.cos(yz_rad)]
    ])

    R_xy = np.array([
        [np.cos(xy_rad), -np.sin(xy_rad), 0],
        [np.sin(xy_rad), np.cos(xy_rad), 0],
        [0, 0, 1]
    ])

    # Combined rotation matrix (R = R_xy * R_yz * R_xz)
    R_combined = R_xy @ R_yz @ R_xz

    # Create the affine transformation matrix
    matrix = np.eye(4)
    matrix[:3, :3] = R_combined
    matrix[:3, 3] = [x, y, z]

    affine_transform = ants.create_ants_transform(
        transform_type="AffineTransform",
        matrix=matrix[:3, :3],
        offset=matrix[:3, 3]
    )

    shifted_image = ants.apply_ants_transform(
        transform=affine_transform,
        data=ants_moving,
        reference=ants_fixed,
        data_type="image"
    )

    nib.save(shifted_image, os.path.join(save_path, 'MRI_warped_fixed.nii.gz'))

    return shifted_image


class ManualRegistrationWindow(QMainWindow):
    """
    Manual Registration widget
    """

    def __init__(self, fixed_file, moving_file, save_path, title="Модуль ручного совмещения - MRI QA Solution"):
        super().__init__()

        self.ui = Ui_ManualRegistrationWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(title)

        # connect actions to navigation buttons
        self.ui.saveButton.clicked.connect(self.save_images)
        self.moving_autoreg_file = moving_file
        self.fixed_autoreg_file = fixed_file
        self.save_path = save_path

        self.ui.x_slider.valueChanged.connect(self.update_position)
        self.ui.y_slider.valueChanged.connect(self.update_position)
        self.ui.z_slider.valueChanged.connect(self.update_position)
        self.ui.xy_slider.valueChanged.connect(self.update_rotation)
        self.ui.xz_slider.valueChanged.connect(self.update_rotation)
        self.ui.yz_slider.valueChanged.connect(self.update_rotation)

        self.setup_sliders()

        self.overlay_viewer = VTKOverlayViewer(self.fixed_autoreg_file, self.moving_autoreg_file, False, self)
        if self.ui.image_widget.layout():
            QtWidgets.QWidget().setLayout(self.ui.image_widget.layout())
        self.viewer_layout = QVBoxLayout(self.ui.image_widget)
        self.viewer_layout.addWidget(self.overlay_viewer)
        self.ui.image_widget.setLayout(self.viewer_layout)

    def setup_sliders(self):
        self.ui.x_slider.setRange(-10, 10)
        self.ui.y_slider.setRange(-10, 10)
        self.ui.z_slider.setRange(-20, 20)
        self.ui.xy_slider.setRange(-90, 90)
        self.ui.xz_slider.setRange(-90, 90)
        self.ui.yz_slider.setRange(-90, 90)

    def update_position(self):
        x = self.ui.x_slider.value()
        y = self.ui.y_slider.value()
        z = self.ui.z_slider.value()
        self.overlay_viewer.update_position(x, y, z)

    def update_rotation(self):
        xy = self.ui.xy_slider.value()
        xz = self.ui.xz_slider.value()
        yz = self.ui.yz_slider.value()
        self.overlay_viewer.update_rotation(xy, xz, yz)

    def save_images(self):
        print('x = ', self.ui.x_slider.value())
        print('y = ', self.ui.y_slider.value())
        print('z = ', self.ui.z_slider.value())
        print('xy = ', self.ui.xy_slider.value())
        print('xz = ', self.ui.xz_slider.value())
        print('yz = ', self.ui.yz_slider.value())
        # совместить изображения с указанными значениями слайдеров
        # сохранить изображения
        params = [
            self.ui.x_slider.value(),
            self.ui.y_slider.value(),
            -self.ui.z_slider.value(),
            self.ui.xy_slider.value(),
            self.ui.xz_slider.value(),
            self.ui.yz_slider.value()
        ]
        apply_manual_shift(self.fixed_autoreg_file, self.moving_autoreg_file, self.save_path, *params)
        self.close()




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    fixed_file = "C:\\dev\\git\\MRIphantom_desktop\\studies\\test\\CT_fixed.nii.gz"
    moving_file = "C:\\dev\\git\\MRIphantom_desktop\\studies\\test\\MRI_warped.nii.gz"
    window = ManualRegistrationWindow(fixed_file, moving_file, 'C:\\dev\\git\\MRIphantom_desktop\\studies\\test')
    window.show()
    sys.exit(app.exec())
