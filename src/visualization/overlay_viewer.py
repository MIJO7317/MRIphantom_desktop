import sys
import vtk
from PySide6 import QtWidgets
import vtkmodules.qt
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkInteractionImage import vtkImageViewer2
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkRenderingCore import (
    vtkActor2D,
    vtkTextMapper,
    vtkTextProperty
)

class MyVtkInteractorStyleImage(vtkInteractorStyleImage):
    def __init__(self, parent=None):
        super().__init__()
        self.AddObserver('KeyPressEvent', self.key_press_event)
        self.AddObserver('MouseWheelForwardEvent', self.mouse_wheel_forward_event)
        self.AddObserver('MouseWheelBackwardEvent', self.mouse_wheel_backward_event)
        self.AddObserver('MouseMoveEvent', self.mouse_move_event)
        self.image_viewer = None
        self.status_mapper = None
        self.coord_mapper = None
        self.slice = 0
        self.min_slice = 0
        self.max_slice = 0
        self.voxel_size = (1.0, 1.0, 1.0)  # Default voxel size
        self.origin = (0.0, 0.0, 0.0)  # Default origin

    def set_image_viewer(self, image_viewer):
        self.image_viewer = image_viewer
        self.min_slice = image_viewer.GetSliceMin()
        self.max_slice = image_viewer.GetSliceMax()
        self.slice = self.min_slice

    def set_status_mapper(self, status_mapper):
        self.status_mapper = status_mapper

    def set_coord_mapper(self, coord_mapper):
        self.coord_mapper = coord_mapper

    def set_voxel_size(self, voxel_size):
        self.voxel_size = voxel_size

    def set_origin(self, origin):
        self.origin = origin

    def move_slice_forward(self):
        if self.slice < self.max_slice:
            self.slice += 1
            self.update_status()

    def move_slice_backward(self):
        if self.slice > self.min_slice:
            self.slice -= 1
            self.update_status()

    def key_press_event(self, obj, event):
        key = self.GetInteractor().GetKeySym()
        if key == 'Up':
            self.move_slice_forward()
        elif key == 'Down':
            self.move_slice_backward()

    def mouse_wheel_forward_event(self, obj, event):
        self.move_slice_forward()

    def mouse_wheel_backward_event(self, obj, event):
        self.move_slice_backward()

    def mouse_move_event(self, obj, event):
        pos = self.GetInteractor().GetEventPosition()
        picker = vtk.vtkPropPicker()
        picker.Pick(pos[0], pos[1], 0, self.image_viewer.GetRenderer())
        world_pos = picker.GetPickPosition()
        if world_pos:
            x_coord = world_pos[0]
            y_coord = world_pos[1]
            z_coord = self.origin[2] + self.slice * self.voxel_size[2]
            coord_msg = f'X: {x_coord:.2f} mm, Y: {y_coord:.2f} mm, Z: {z_coord:.2f} mm'
            self.coord_mapper.SetInput(coord_msg)
            self.image_viewer.Render()
        super().OnMouseMove()

    def update_status(self):
        self.image_viewer.SetSlice(self.slice)
        z_position = self.origin[2] + self.slice * self.voxel_size[2]
        msg = StatusMessage.format(self.slice, self.max_slice, z_position)
        self.status_mapper.SetInput(msg)
        self.image_viewer.Render()

class StatusMessage:
    @staticmethod
    def format(slice: int, max_slice: int, z_position: float):
        return f'Slice Number {slice + 1}/{max_slice + 1} (Z: {z_position:.2f} mm)'

class VTKOverlayViewer(QtWidgets.QWidget):
    def __init__(self, filepath_fixed, filepath_moving, is_dicom=False, parent=None):
        super().__init__(parent)

        self.x = 0
        self.y = 0
        self.z = 0

        self.layout = QtWidgets.QVBoxLayout(self)
        self.vtk_widget = QVTKRenderWindowInteractor(self)
        self.layout.addWidget(self.vtk_widget)

        self.ren = vtk.vtkRenderer()
        self.vtk_widget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtk_widget.GetRenderWindow().GetInteractor()

        if is_dicom:
            self.reader_fixed = vtk.vtkDICOMImageReader()
            self.reader_fixed.SetDirectoryName(filepath_fixed)
        else:
            self.reader_fixed = vtk.vtkNIFTIImageReader()
            self.reader_fixed.SetFileName(filepath_fixed)

            self.reader_moving = vtk.vtkNIFTIImageReader()
            self.reader_moving.SetFileName(filepath_moving)

        self.reader_fixed.Update()
        if not is_dicom:
            self.reader_moving.Update()

        red_color_map = self.create_color_map((1, 0, 0))  # Red for fixed image
        green_color_map = self.create_color_map((0, 0, 1))  # Blue for moving image

        color_fixed = vtk.vtkImageMapToColors()
        color_fixed.SetInputConnection(self.reader_fixed.GetOutputPort())
        color_fixed.SetLookupTable(red_color_map)

        if not is_dicom:
            color_moving = vtk.vtkImageMapToColors()
            color_moving.SetInputConnection(self.reader_moving.GetOutputPort())
            color_moving.SetLookupTable(green_color_map)

            self.blend = vtk.vtkImageBlend()
            self.blend.AddInputConnection(color_fixed.GetOutputPort())
            self.blend.AddInputConnection(color_moving.GetOutputPort())
            self.blend.SetOpacity(0, 0.5)  # Opacity for the fixed image
            self.blend.SetOpacity(1, 0.5)  # Opacity for the moving image
            self.blend.Update()
        else:
            self.blend = vtk.vtkImageBlend()
            self.blend.AddInputConnection(color_fixed.GetOutputPort())
            self.blend.SetOpacity(0, 0.5)  # Opacity for the fixed image
            self.blend.Update()

        self.image_viewer = vtkImageViewer2()
        self.image_viewer.SetRenderWindow(self.vtk_widget.GetRenderWindow())
        self.image_viewer.SetInputConnection(self.blend.GetOutputPort())

        if is_dicom:
            patient_name = self.reader_fixed.GetPatientName() if self.reader_fixed.GetPatientName() else "Unknown"
            study_uid = self.reader_fixed.GetStudyUID() if self.reader_fixed.GetStudyUID() else "Unknown"
            dimensions = self.reader_fixed.GetOutput().GetDimensions()
            voxel_size = self.reader_fixed.GetOutput().GetSpacing()
            origin = self.reader_fixed.GetOutput().GetOrigin()
            additional_info = f'Patient: {patient_name}\nStudy UID: {study_uid}\nDimensions: {dimensions}\nVoxel Size: {voxel_size}\nOrigin: {origin}'
        else:
            dimensions = self.reader_fixed.GetOutput().GetDimensions()
            voxel_size = self.reader_fixed.GetOutput().GetSpacing()
            origin = self.reader_fixed.GetOutput().GetOrigin()
            additional_info = f'Dimensions: {dimensions}\nVoxel Size: {voxel_size}\nOrigin: {origin}'

        self.slice_text_prop = vtkTextProperty()
        self.slice_text_prop.SetFontFamilyToCourier()
        self.slice_text_prop.SetFontSize(12)
        self.slice_text_prop.SetVerticalJustificationToBottom()
        self.slice_text_prop.SetJustificationToLeft()

        self.slice_text_mapper = vtkTextMapper()
        msg = StatusMessage.format(self.image_viewer.GetSliceMin(), self.image_viewer.GetSliceMax(), origin[2])
        self.slice_text_mapper.SetInput(msg)
        self.slice_text_mapper.SetTextProperty(self.slice_text_prop)

        self.slice_text_actor = vtkActor2D()
        self.slice_text_actor.SetMapper(self.slice_text_mapper)
        self.slice_text_actor.SetPosition(15, 10)

        self.usage_text_prop = vtkTextProperty()
        self.usage_text_prop.SetFontFamilyToCourier()
        self.usage_text_prop.SetFontSize(14)
        self.usage_text_prop.SetVerticalJustificationToTop()
        self.usage_text_prop.SetJustificationToLeft()

        self.usage_text_mapper = vtkTextMapper()
        self.usage_text_mapper.SetInput(
            'Slice with mouse wheel\n or Up/Down-Key\n- Zoom with pressed right\n '
            ' mouse button while dragging\n\n' + additional_info
        )
        self.usage_text_mapper.SetTextProperty(self.usage_text_prop)

        self.usage_text_actor = vtkActor2D()
        self.usage_text_actor.SetMapper(self.usage_text_mapper)
        self.usage_text_actor.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
        self.usage_text_actor.GetPositionCoordinate().SetValue(0.05, 0.95)

        self.coord_text_prop = vtkTextProperty()
        self.coord_text_prop.SetFontFamilyToCourier()
        self.coord_text_prop.SetFontSize(12)
        self.coord_text_prop.SetVerticalJustificationToTop()
        self.coord_text_prop.SetJustificationToLeft()

        self.coord_text_mapper = vtkTextMapper()
        self.coord_text_mapper.SetInput('X: 0.00 mm, Y: 0.00 mm, Z: 0.00 mm')
        self.coord_text_mapper.SetTextProperty(self.coord_text_prop)

        self.coord_text_actor = vtkActor2D()
        self.coord_text_actor.SetMapper(self.coord_text_mapper)
        self.coord_text_actor.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
        self.coord_text_actor.GetPositionCoordinate().SetValue(0.05, 0.3)

        self.render_window_interactor = self.vtk_widget.GetRenderWindow().GetInteractor()
        self.my_interactor_style = MyVtkInteractorStyleImage()

        self.my_interactor_style.set_image_viewer(self.image_viewer)
        self.my_interactor_style.set_status_mapper(self.slice_text_mapper)
        self.my_interactor_style.set_coord_mapper(self.coord_text_mapper)
        self.my_interactor_style.set_voxel_size(voxel_size)
        self.my_interactor_style.set_origin(origin)

        self.image_viewer.SetupInteractor(self.render_window_interactor)
        self.render_window_interactor.SetInteractorStyle(self.my_interactor_style)
        self.render_window_interactor.Initialize()

        self.image_viewer.Render()
        self.image_viewer.GetRenderer().ResetCamera()
        self.image_viewer.GetRenderWindow().SetSize(400, 400)
        self.image_viewer.GetRenderWindow().SetWindowName('ReadDICOMSeries' if is_dicom else 'ReadNIFTIFile')

        self.image_viewer.GetRenderer().AddActor2D(self.slice_text_actor)
        self.image_viewer.GetRenderer().AddActor2D(self.usage_text_actor)
        self.image_viewer.GetRenderer().AddActor2D(self.coord_text_actor)
        self.image_viewer.Render()

        self.image_data = self.reader_fixed.GetOutput()
        self.extent = self.image_data.GetExtent()

        self.iren.Initialize()


    def create_color_map(self, color):
        color_transfer = vtk.vtkColorTransferFunction()
        color_transfer.AddRGBPoint(0, 0, 0, 0)
        color_transfer.AddRGBPoint(255, *color)
        return color_transfer

    def update_parameters(self, x=None, y=None, z=None, rot_x=None, rot_y=None, rot_z=None):
        # Update position parameters
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z

        # Update rotation parameters
        if rot_x is not None:
            self.rotation_x = rot_x
        if rot_y is not None:
            self.rotation_y = rot_y
        if rot_z is not None:
            self.rotation_z = rot_z

        # Update the view
        self.update_view()

    def update_view(self):
        transform = vtk.vtkTransform()
        transform.Translate(self.x, self.y, self.z)
        transform.RotateX(self.rotation_x)
        transform.RotateY(self.rotation_y)
        transform.RotateZ(self.rotation_z)

        transform_filter = vtk.vtkImageReslice()
        transform_filter.SetInputConnection(self.reader_moving.GetOutputPort())
        transform_filter.SetResliceTransform(transform)
        transform_filter.SetResliceAxesDirectionCosines(
            1, 0, 0, 0, 1, 0, 0, 0, 1
        )
        transform_filter.SetOutputSpacing(self.reader_moving.GetOutput().GetSpacing())
        transform_filter.SetOutputOrigin(self.reader_moving.GetOutput().GetOrigin())
        transform_filter.SetInterpolationModeToLinear()
        transform_filter.Update()

        red_color_map = self.create_color_map((1, 0, 0))  # Red for fixed image
        green_color_map = self.create_color_map((0, 0, 1))  # Blue for moving image

        color_fixed = vtk.vtkImageMapToColors()
        color_fixed.SetInputConnection(self.reader_fixed.GetOutputPort())
        color_fixed.SetLookupTable(red_color_map)

        color_moving = vtk.vtkImageMapToColors()
        color_moving.SetInputConnection(transform_filter.GetOutputPort())
        color_moving.SetLookupTable(green_color_map)

        self.blend.RemoveAllInputs()
        self.blend.AddInputConnection(color_fixed.GetOutputPort())
        self.blend.AddInputConnection(color_moving.GetOutputPort())
        self.blend.SetOpacity(0, 0.5)  # Set opacity for the fixed image
        self.blend.SetOpacity(1, 0.5)  # Set opacity for the moving image
        self.blend.Update()

        self.image_viewer.Render()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, fixed_file, moving_file, is_dicom=False, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Overlay Viewer")
        self.resize(800, 800)

        self.central_widget = VTKOverlayViewer(fixed_file, moving_file, is_dicom, self)
        self.setCentralWidget(self.central_widget)

if __name__ == "__main__":
    moving_file = "C:\\dev\\git\\MRIphantom_desktop\\studies\\danke\\MRI_warped_fixed.nii.gz"
    fixed_file = "C:\\dev\\git\\MRIphantom_desktop\\studies\\danke\\CT_fixed.nii.gz"

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(fixed_file, moving_file, False)
    window.show()
    sys.exit(app.exec())
