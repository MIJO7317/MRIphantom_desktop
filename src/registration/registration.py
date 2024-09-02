import os
import ants
import nibabel as nib
import numpy as np

from PySide6.QtWidgets import (
    QVBoxLayout,
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QPushButton
)
from PySide6 import QtWidgets
from UI.registration_screen import Ui_ManualRegistrationWindow
from src.visualization.overlay_viewer import VTKOverlayViewer


def rigid_reg(fixed: str, moving: str, save_path: str):
    ants_fixed = ants.image_read(fixed)
    ants_moving = ants.image_read(moving)
    
    # Сохранение начальной трансформации во временный файл
    initial_transform_file = os.path.join(save_path, 'initial_transform.mat')
    if not os.path.exists(initial_transform_file):
        # Тождественное преобразование
        euler_transform = ants.create_ants_transform(
            transform_type="Euler3DTransform",
            translation = (0, 0, 0)
        )
        ants.write_transform(euler_transform, initial_transform_file)
    
    res = ants.registration(
        fixed=ants_fixed, moving=ants_moving, type_of_transform="Rigid", initial_transform=[initial_transform_file], random_seed = 0
    )
    transform = ants.read_transform(res["fwdtransforms"][0])
    ants_warped = ants.apply_ants_transform(
        transform, ants_moving, data_type="image", reference=ants_fixed
    )
    nib.save(ants_warped, os.path.join(save_path, 'image_moving.nii'))
    nib.save(ants_fixed, os.path.join(save_path, 'image_fixed.nii'))
    return ants_warped


def match_voxel_sizes(fixed: str, moving: str, save_path: str):
    # Load fixed and moving images using ANTs
    ants_fixed = ants.image_read(fixed)
    ants_moving = ants.image_read(moving)

    # Resample the moving image to match the fixed image's voxel size
    resampled_moving = ants.resample_image_to_target(ants_moving, ants_fixed)

    # Save the resampled moving image and the fixed image
    nib.save(resampled_moving, os.path.join(save_path, 'image_moving.nii'))
    nib.save(ants_fixed, os.path.join(save_path, 'image_fixed.nii'))

    return resampled_moving


def calculate_image_center(image):
    """
    Calculate the center of an image taking into account its spacing and origin.

    Parameters:
    - image: ANTsImage object.

    Returns:
    - center_x, center_y, center_z: Coordinates of the image center in world space.
    """
    spacing = image.spacing
    origin = image.origin
    extent = image.shape

    # Center coordinates in world space
    center_x = origin[0] + (extent[0] - 1) / 2.0 * spacing[0]
    center_y = origin[1] + (extent[1] - 1) / 2.0 * spacing[1]
    center_z = origin[2] + (extent[2] - 1) / 2.0 * spacing[2]

    return center_x, center_y, center_z

def apply_manual_shift(fixed: str, moving: str, save_path: str, x: float, y: float, z: float, z_rot: float, y_rot: float, x_rot: float):
    ants_moving = ants.image_read(moving)
    ants_fixed = ants.image_read(fixed)

    # Calculate the center of the moving image
    center_x, center_y, center_z = calculate_image_center(ants_moving)

    # Convert rotation angles from degrees to radians
    z_rad = np.deg2rad(z_rot)
    y_rad = np.deg2rad(y_rot)
    x_rad = np.deg2rad(x_rot)

    # Create rotation matrices
    mat_z = np.array([
        [np.cos(z_rad), -np.sin(z_rad), 0],
        [np.sin(z_rad), np.cos(z_rad), 0],
        [0, 0, 1]
    ])

    mat_x = np.array([
        [1, 0, 0],
        [0, np.cos(x_rad), -np.sin(x_rad)],
        [0, np.sin(x_rad), np.cos(x_rad)]
    ])

    mat_y = np.array([
        [np.cos(y_rad), 0, np.sin(y_rad)],
        [0, 1, 0],
        [-np.sin(y_rad), 0, np.cos(y_rad)]
    ])

    # Combined rotation matrix (R = mat_z * mat_x * mat_y)
    R_combined = mat_z @ mat_x @ mat_y

    # Create the affine transformation matrix
    matrix = np.eye(4)

    # Translation part (translation to center, rotation, then translation back)
    translate_to_center = np.array([
        [1, 0, 0, center_x],
        [0, 1, 0, center_y],
        [0, 0, 1, center_z],
        [0, 0, 0, 1]
    ])

    translate_back = np.array([
        [1, 0, 0, -center_x],
        [0, 1, 0, -center_y],
        [0, 0, 1, -center_z],
        [0, 0, 0, 1]
    ])

    # Combine the transformations
    matrix = translate_to_center @ matrix
    matrix[:3, :3] = R_combined
    matrix = translate_back @ matrix

    # Final translation
    matrix[:3, 3] += [x, y, z]

    # Create the affine transformation
    affine_transform = ants.create_ants_transform(
        transform_type="AffineTransform",
        matrix=matrix[:3, :3],
        offset=matrix[:3, 3]
    )

    initial_transform_file = os.path.join(save_path, 'initial_transform.mat')
    ants.write_transform(affine_transform, initial_transform_file)

    shifted_image = ants.apply_ants_transform(
        transform=affine_transform,
        data=ants_moving,
        reference=ants_fixed,
        data_type="image"
    )

    nib.save(shifted_image, os.path.join(save_path, 'image_moving.nii'))

    return shifted_image


def flip_image(ants_image, axis):
    """
    Flip the image along the specified axis.

    Args:
        ants_image: ANTsImage object to be flipped.
        axis: str, the axis to flip ('x', 'y', 'z').

    Returns:
        ants.ANTsImage: the flipped image.
    """
    data = ants_image.numpy()

    if axis == 'x':
        flipped_data = np.flip(data, axis=0)
    elif axis == 'y':
        flipped_data = np.flip(data, axis=1)
    elif axis == 'z':
        flipped_data = np.flip(data, axis=2)
    else:
        raise ValueError(f"Invalid axis: {axis}. Must be 'x', 'y', or 'z'.")

    flipped_image = ants.from_numpy(flipped_data, origin=ants_image.origin, spacing=ants_image.spacing, direction=ants_image.direction)
    return flipped_image


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

        self.timer_id = -1

        self.ui.x_slider.valueChanged.connect(self.value_changed)
        self.ui.y_slider.valueChanged.connect(self.value_changed)
        self.ui.z_slider.valueChanged.connect(self.value_changed)
        self.ui.z_rotation_slider.valueChanged.connect(self.value_changed)
        self.ui.y_rotation_slider.valueChanged.connect(self.value_changed)
        self.ui.x_rotation_slider.valueChanged.connect(self.value_changed)

        self.ui.flip_x_button.clicked.connect(lambda: self.flip_image('x'))
        self.ui.flip_y_button.clicked.connect(lambda: self.flip_image('y'))
        self.ui.flip_z_button.clicked.connect(lambda: self.flip_image('z'))

        self.setup_sliders()

        self.overlay_viewer = VTKOverlayViewer(self.fixed_autoreg_file, self.moving_autoreg_file, False, self)
        if self.ui.image_widget.layout():
            QtWidgets.QWidget().setLayout(self.ui.image_widget.layout())
        self.viewer_layout = QVBoxLayout(self.ui.image_widget)
        self.viewer_layout.addWidget(self.overlay_viewer)
        self.ui.image_widget.setLayout(self.viewer_layout)

    def setup_sliders(self):
        self.ui.x_slider.setRange(-100, 100)
        self.ui.y_slider.setRange(-100, 100)
        self.ui.z_slider.setRange(-100, 100)
        self.ui.z_rotation_slider.setRange(-180, 180)
        self.ui.y_rotation_slider.setRange(-180, 180)
        self.ui.x_rotation_slider.setRange(-180, 180)

    def flip_image(self, axis):
        ants_moving = ants.image_read(self.moving_autoreg_file)
        flipped_image = flip_image(ants_moving, axis)
        flipped_image_path = os.path.join(self.save_path, 'image_moving_flipped.nii')
        ants.image_write(flipped_image, flipped_image_path)
        self.moving_autoreg_file = flipped_image_path

        self.viewer_layout.removeWidget(self.overlay_viewer)
        self.overlay_viewer.deleteLater()
        self.overlay_viewer = VTKOverlayViewer(self.fixed_autoreg_file, self.moving_autoreg_file, False, self)
        self.viewer_layout.addWidget(self.overlay_viewer)

    def timerEvent(self, event):
        self.killTimer(self.timer_id)
        self.timer_id = -1
        self.update_parameters()

    def value_changed(self):
        if self.timer_id != -1:
            self.killTimer(self.timer_id)

        self.timer_id = self.startTimer(1500)

    def update_parameters(self):
        x = self.ui.x_slider.value()
        y = self.ui.y_slider.value()
        z = self.ui.z_slider.value()
        z_rot = self.ui.z_rotation_slider.value()
        y_rot = self.ui.y_rotation_slider.value()
        x_rot = self.ui.x_rotation_slider.value()
        self.overlay_viewer.update_parameters(x, y, z, x_rot, y_rot, z_rot)

        # apply_manual_shift(self.fixed_autoreg_file, self.moving_autoreg_file, self.save_path, x, y, z, xy, xz, yz)
        # self.viewer_layout.removeWidget(self.overlay_viewer)
        # self.overlay_viewer.deleteLater()
        # self.overlay_viewer = VTKOverlayViewer(self.fixed_autoreg_file, self.moving_autoreg_file,
        #                                        False, self)
        # self.viewer_layout.addWidget(self.overlay_viewer)

    def save_images(self):
        params = [
            -self.ui.x_slider.value(),
            self.ui.y_slider.value(),
            self.ui.z_slider.value(),
            self.ui.z_rotation_slider.value(),
            self.ui.y_rotation_slider.value(),
            self.ui.x_rotation_slider.value()
        ]
        apply_manual_shift(self.fixed_autoreg_file, self.moving_autoreg_file, self.save_path, *params)
        self.close()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    fixed_file = "C:\\dev\\git\\MRIphantom_desktop\\studies\\12341\\image_fixed.nii"
    moving_file = "C:\\dev\\git\\MRIphantom_desktop\\studies\\12341\\image_moving.nii"
    window = ManualRegistrationWindow(fixed_file, moving_file, 'C:\\dev\\git\\MRIphantom_desktop\\studies\\12341')
    window.show()
    sys.exit(app.exec())
