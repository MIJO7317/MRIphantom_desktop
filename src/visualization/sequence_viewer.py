import sys
import vtk
import os
from PySide6 import QtCore, QtWidgets
import vtkmodules.qt
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkInteractionImage import vtkImageViewer2
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkRenderingCore import (
    vtkActor2D,
    vtkRenderWindowInteractor,
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
        # print(f'Slicer: Min = {self.min_slice}, Max= {self.max_slice}')

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
            # print(f'MoveSliceForward::Slice = {self.slice}')
            self.update_status()

    def move_slice_backward(self):
        if self.slice > self.min_slice:
            self.slice -= 1
            # print(f'MoveSliceBackward::Slice = {self.slice}')
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
        super().OnMouseMove()  # Call parent class method

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

class VTKSliceViewer(QtWidgets.QWidget):
    def __init__(self, file_path, is_dicom=True, parent=None):
        super().__init__(parent)

        # Set up the layout
        self.layout = QtWidgets.QVBoxLayout(self)
        self.vtk_widget = QVTKRenderWindowInteractor(self)
        self.layout.addWidget(self.vtk_widget)
        self.colors = vtkNamedColors()

        # Set up the VTK renderer and interactor
        self.ren = vtk.vtkRenderer()
        self.vtk_widget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtk_widget.GetRenderWindow().GetInteractor()

        # Determine if file_path is a directory or a file
        if is_dicom:
            # Load and display the DICOM series
            self.reader = vtk.vtkDICOMImageReader()
            self.reader.SetDirectoryName(file_path)
        else:
            # Load and display the NIFTI file
            self.reader = vtk.vtkNIFTIImageReader()
            self.reader.SetFileName(file_path)

        self.reader.Update()

        self.image_viewer = vtkImageViewer2()
        self.image_viewer.SetRenderWindow(self.vtk_widget.GetRenderWindow())
        self.image_viewer.SetInputConnection(self.reader.GetOutputPort())

        # Get additional information from DICOM or NIFTI file
        if is_dicom:
            patient_name = self.reader.GetPatientName() if self.reader.GetPatientName() else "Unknown"
            study_uid = self.reader.GetStudyUID() if self.reader.GetStudyUID() else "Unknown"
            dimensions = self.reader.GetOutput().GetDimensions()
            voxel_size = self.reader.GetOutput().GetSpacing()
            origin = self.reader.GetOutput().GetOrigin()
            additional_info = f'Patient: {patient_name}\nStudy UID: {study_uid}\nDimensions: {dimensions}\nVoxel Size: {voxel_size}\nOrigin: {origin}'
        else:
            dimensions = self.reader.GetOutput().GetDimensions()
            voxel_size = self.reader.GetOutput().GetSpacing()
            origin = self.reader.GetOutput().GetOrigin()
            additional_info = f'Dimensions: {dimensions}\nVoxel Size: {voxel_size}\nOrigin: {origin}'

        # Slice text properties
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

        # Usage text properties
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

        # Cursor coordinates text properties
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

        # Add text actors to the renderer
        self.image_viewer.GetRenderer().AddActor2D(self.slice_text_actor)
        self.image_viewer.GetRenderer().AddActor2D(self.usage_text_actor)
        self.image_viewer.GetRenderer().AddActor2D(self.coord_text_actor)

        self.image_viewer.Render()

        # Get the image data
        self.image_data = self.reader.GetOutput()
        self.extent = self.image_data.GetExtent()

        # Initialize VTK
        self.iren.Initialize()

    def close(self):
        if self.vtk_widget:
            self.vtk_widget.GetRenderWindow().Finalize()
            self.vtk_widget.TerminateApp()
            self.vtk_widget.close()
        super().close()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, file_path, is_dicom=True, parent=None):
        super().__init__(parent)
        self.setWindowTitle("DICOM/NIFTI Viewer")
        self.resize(800, 800)

        # Set up the central widget with VTK content
        self.central_widget = VTKSliceViewer(file_path, is_dicom, self)
        self.setCentralWidget(self.central_widget)

if __name__ == "__main__":
    file_path = "C:\\dev\\git\\MRIphantom_desktop\\studies\\1registration\\MRI_warped.nii.gz"
    is_dicom = True if os.path.isdir(file_path) else False

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(file_path, is_dicom)
    window.show()
    sys.exit(app.exec())
