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

vtk.vtkObject.GlobalWarningDisplayOff()

class MyVtkInteractorStyleImage(vtkInteractorStyleImage):
    def __init__(self, slice_type, parent=None):
        super().__init__()
        self.AddObserver('KeyPressEvent', self.key_press_event)
        self.AddObserver('MouseWheelForwardEvent', self.mouse_wheel_forward_event)
        self.AddObserver('MouseWheelBackwardEvent', self.mouse_wheel_backward_event)
        self.AddObserver('MouseMoveEvent', self.mouse_move_event)

        self.image_viewer = None
        self.status_mapper = None
        self.coord_mapper = None
        self.slice_type = slice_type  # Set the slice type
        self.slice = 0
        self.min_slice = 0
        self.max_slice = 0
        self.voxel_size = (1.0, 1.0, 1.0)  # Default voxel size
        self.origin = (0.0, 0.0, 0.0)  # Default origin

    def set_image_viewer(self, image_viewer):
        self.image_viewer = image_viewer

        # Determine slice min and max based on the slice type
        if self.slice_type == 'axial':
            self.min_slice = 0
            self.max_slice = image_viewer.GetInput().GetDimensions()[2] - 1
        elif self.slice_type == 'sagittal':
            self.min_slice = 0
            self.max_slice = image_viewer.GetInput().GetDimensions()[0] - 1
        elif self.slice_type == 'coronal':
            self.min_slice = 0
            self.max_slice = image_viewer.GetInput().GetDimensions()[1] - 1

        # Set initial slice to the middle of the range
        self.slice = (self.min_slice + self.max_slice) // 2
        self.image_viewer.SetSlice(self.slice)

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
            x_coord, y_coord, z_coord = world_pos
            # Calculate coordinate based on slice type
            if self.slice_type == 'axial':
                z_coord = self.origin[2] + self.slice * self.voxel_size[2]
            elif self.slice_type == 'sagittal':
                x_coord = self.origin[0] + self.slice * self.voxel_size[0]
            elif self.slice_type == 'coronal':
                y_coord = self.origin[1] + self.slice * self.voxel_size[1]

            coord_msg = f'X: {x_coord:.2f} mm, Y: {y_coord:.2f} mm, Z: {z_coord:.2f} mm'
            self.coord_mapper.SetInput(coord_msg)
            self.image_viewer.Render()
        super().OnMouseMove()

    def update_status(self):
        self.image_viewer.SetSlice(self.slice)
        # Update z_position based on slice type
        if self.slice_type == 'axial':
            z_position = self.origin[2] + self.slice * self.voxel_size[2]
        elif self.slice_type == 'sagittal':
            z_position = self.origin[0] + self.slice * self.voxel_size[0]
        elif self.slice_type == 'coronal':
            z_position = self.origin[1] + self.slice * self.voxel_size[1]

        msg = StatusMessage.format(self.slice, self.max_slice, z_position)
        self.status_mapper.SetInput(msg)
        self.image_viewer.Render()

    def cleanup(self):
        if self.image_viewer:
            self.image_viewer.GetRenderWindow().Finalize()
            self.image_viewer.GetRenderer().RemoveAllViewProps()
            self.image_viewer.GetInput().ReleaseData()

        if self.GetInteractor():
            self.GetInteractor().RemoveAllObservers()
            self.GetInteractor().TerminateApp()

        self.image_viewer = None
        self.status_mapper = None
        self.coord_mapper = None



class StatusMessage:
    @staticmethod
    def format(slice: int, max_slice: int, z_position: float):
        return f'Slice number {slice + 1}/{max_slice + 1} ({z_position:.2f} mm)'


class VTKOverlayViewer(QtWidgets.QWidget):
    def __init__(self, filepath_fixed, filepath_moving, is_dicom=False, parent=None):
        super().__init__(parent)

        self.x = 0
        self.y = 0
        self.z = 0

        self.layout = QtWidgets.QGridLayout(self)

        # Create VTK renderers for the 3 views: Axial, Sagittal, and Coronal
        self.axial_viewer = self.create_viewer('axial', filepath_fixed, filepath_moving, is_dicom)
        self.sagittal_viewer = self.create_viewer('sagittal', filepath_fixed, filepath_moving, is_dicom)
        self.coronal_viewer = self.create_viewer('coronal', filepath_fixed, filepath_moving, is_dicom)

        # Add VTK widgets to the layout in a 2x2 grid
        self.layout.addWidget(self.axial_viewer[0], 0, 0)
        self.layout.addWidget(self.sagittal_viewer[0], 0, 1)
        self.layout.addWidget(self.coronal_viewer[0], 1, 0)

        self.axial_viewer[1].SetSliceOrientationToXY()  # Axial view
        self.sagittal_viewer[1].SetSliceOrientationToYZ()  # Sagittal view
        self.coronal_viewer[1].SetSliceOrientationToXZ()  # Coronal view

        # Set the initial slice for all viewers to the middle slice
        self.axial_viewer[1].SetSlice((self.axial_viewer[1].GetSliceMin() + self.axial_viewer[1].GetSliceMax()) // 2)
        self.sagittal_viewer[1].SetSlice(
            (self.sagittal_viewer[1].GetSliceMin() + self.sagittal_viewer[1].GetSliceMax()) // 2)
        self.coronal_viewer[1].SetSlice(
            (self.coronal_viewer[1].GetSliceMin() + self.coronal_viewer[1].GetSliceMax()) // 2)

        # Synchronize slices across views
        self.axial_viewer[1].AddObserver("SliceChangedEvent", self.sync_views)
        self.sagittal_viewer[1].AddObserver("SliceChangedEvent", self.sync_views)
        self.coronal_viewer[1].AddObserver("SliceChangedEvent", self.sync_views)

    def create_viewer(self, slice_type, filepath_fixed, filepath_moving, is_dicom):
        vtk_widget = QVTKRenderWindowInteractor(self)

        ren = vtk.vtkRenderer()
        vtk_widget.GetRenderWindow().AddRenderer(ren)
        iren = vtk_widget.GetRenderWindow().GetInteractor()

        if is_dicom:
            reader_fixed = vtk.vtkDICOMImageReader()
            reader_fixed.SetDirectoryName(filepath_fixed)
        else:
            reader_fixed = vtk.vtkNIFTIImageReader()
            reader_fixed.SetFileName(filepath_fixed)

            reader_moving = vtk.vtkNIFTIImageReader()
            reader_moving.SetFileName(filepath_moving)

        reader_fixed.Update()
        if not is_dicom:
            reader_moving.Update()

        red_color_map = self.create_color_map((1, 0, 0))  # Red for fixed image
        green_color_map = self.create_color_map((0, 1, 0))  # Green for moving image

        color_fixed = vtk.vtkImageMapToColors()
        color_fixed.SetInputConnection(reader_fixed.GetOutputPort())
        color_fixed.SetLookupTable(red_color_map)

        if not is_dicom:
            color_moving = vtk.vtkImageMapToColors()
            color_moving.SetInputConnection(reader_moving.GetOutputPort())
            color_moving.SetLookupTable(green_color_map)

            blend = vtk.vtkImageBlend()
            blend.AddInputConnection(color_fixed.GetOutputPort())
            blend.AddInputConnection(color_moving.GetOutputPort())
            blend.SetOpacity(0, 0.5)  # Opacity for the fixed image
            blend.SetOpacity(1, 0.5)  # Opacity for the moving image
            blend.Update()
        else:
            blend = vtk.vtkImageBlend()
            blend.AddInputConnection(color_fixed.GetOutputPort())
            blend.SetOpacity(0, 0.5)  # Opacity for the fixed image
            blend.Update()

        image_viewer = vtkImageViewer2()
        image_viewer.SetRenderWindow(vtk_widget.GetRenderWindow())
        image_viewer.SetInputConnection(blend.GetOutputPort())
        image_viewer.SetSlice((image_viewer.GetSliceMin() + image_viewer.GetSliceMax()) // 2)

        if is_dicom:
            patient_name = reader_fixed.GetPatientName() if reader_fixed.GetPatientName() else "Unknown"
            study_uid = reader_fixed.GetStudyUID() if reader_fixed.GetStudyUID() else "Unknown"
            dimensions = reader_fixed.GetOutput().GetDimensions()
            voxel_size = reader_fixed.GetOutput().GetSpacing()
            origin = reader_fixed.GetOutput().GetOrigin()
            additional_info = (
                f'Patient: {patient_name}\n'
                f'UID: {study_uid}\n'
                f'Dim: {dimensions}\n'
                f'Voxel size: {voxel_size}\n'
                f'Origin: {origin}'
            )
        else:
            dimensions = reader_fixed.GetOutput().GetDimensions()
            voxel_size = reader_fixed.GetOutput().GetSpacing()
            origin = reader_fixed.GetOutput().GetOrigin()
            additional_info = (
                f'Dim: {dimensions}\n'
                f'Voxel size: {voxel_size}\n'
                f'Origin: {origin}'
            )

        slice_text_prop = vtkTextProperty()
        slice_text_prop.SetFontFamilyToCourier()
        slice_text_prop.SetFontSize(12)
        slice_text_prop.SetVerticalJustificationToBottom()
        slice_text_prop.SetJustificationToLeft()

        slice_text_mapper = vtkTextMapper()
        msg = StatusMessage.format(image_viewer.GetSliceMin(), image_viewer.GetSliceMax(), origin[2])
        slice_text_mapper.SetInput(msg)
        slice_text_mapper.SetTextProperty(slice_text_prop)

        slice_text_actor = vtkActor2D()
        slice_text_actor.SetMapper(slice_text_mapper)
        slice_text_actor.SetPosition(15, 10)

        usage_text_prop = vtkTextProperty()
        usage_text_prop.SetFontFamilyToCourier()
        usage_text_prop.SetFontSize(14)
        usage_text_prop.SetVerticalJustificationToTop()
        usage_text_prop.SetJustificationToLeft()

        usage_text_mapper = vtkTextMapper()
        usage_text_mapper.SetInput(
            'MRI - green\n CT - red\n'
            + additional_info
        )
        usage_text_mapper.SetTextProperty(usage_text_prop)

        usage_text_actor = vtkActor2D()
        usage_text_actor.SetMapper(usage_text_mapper)
        usage_text_actor.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
        usage_text_actor.GetPositionCoordinate().SetValue(0.05, 0.95)

        coord_text_prop = vtkTextProperty()
        coord_text_prop.SetFontFamilyToCourier()
        coord_text_prop.SetFontSize(12)
        coord_text_prop.SetVerticalJustificationToTop()
        coord_text_prop.SetJustificationToLeft()

        coord_text_mapper = vtkTextMapper()
        coord_text_mapper.SetInput('X: 0.00 mm, Y: 0.00 mm, Z: 0.00 mm')
        coord_text_mapper.SetTextProperty(coord_text_prop)

        coord_text_actor = vtkActor2D()
        coord_text_actor.SetMapper(coord_text_mapper)
        coord_text_actor.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
        coord_text_actor.GetPositionCoordinate().SetValue(0.05, 0.3)

        render_window_interactor = vtk_widget.GetRenderWindow().GetInteractor()
        my_interactor_style = MyVtkInteractorStyleImage(slice_type)

        my_interactor_style.set_image_viewer(image_viewer)
        my_interactor_style.set_status_mapper(slice_text_mapper)
        my_interactor_style.set_coord_mapper(coord_text_mapper)
        my_interactor_style.set_voxel_size(voxel_size)
        my_interactor_style.set_origin(origin)

        image_viewer.SetupInteractor(render_window_interactor)
        render_window_interactor.SetInteractorStyle(my_interactor_style)
        render_window_interactor.Initialize()

        image_viewer.Render()
        image_viewer.GetRenderer().ResetCamera()
        image_viewer.GetRenderWindow().SetSize(400, 400)
        image_viewer.GetRenderWindow().SetWindowName('ReadDICOMSeries' if is_dicom else 'ReadNIFTIFile')

        image_viewer.GetRenderer().AddActor2D(slice_text_actor)
        image_viewer.GetRenderer().AddActor2D(usage_text_actor)
        image_viewer.GetRenderer().AddActor2D(coord_text_actor)
        image_viewer.Render()

        image_data = reader_fixed.GetOutput()
        extent = image_data.GetExtent()

        iren.Initialize()

        return vtk_widget, image_viewer, reader_fixed, reader_moving

    def sync_views(self, obj, event):
        # Get the slice index based on the orientation of the triggering viewer
        if obj == self.axial_viewer[1]:
            current_slice = self.axial_viewer[1].GetSlice()
            # Synchronize the corresponding dimensions for sagittal and coronal
            self.sagittal_viewer[1].SetSlice(current_slice)
            self.coronal_viewer[1].SetSlice(current_slice)
        elif obj == self.sagittal_viewer[1]:
            current_slice = self.sagittal_viewer[1].GetSlice()
            # Synchronize the corresponding dimensions for axial and coronal
            self.axial_viewer[1].SetSlice(current_slice)
            self.coronal_viewer[1].SetSlice(current_slice)
        elif obj == self.coronal_viewer[1]:
            current_slice = self.coronal_viewer[1].GetSlice()
            # Synchronize the corresponding dimensions for axial and sagittal
            self.axial_viewer[1].SetSlice(current_slice)
            self.sagittal_viewer[1].SetSlice(current_slice)

        # Render all viewers after updating slices
        self.axial_viewer[1].Render()
        self.sagittal_viewer[1].Render()
        self.coronal_viewer[1].Render()

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

        # Iterate over each view: axial, sagittal, and coronal
        for viewer, orientation in [(self.axial_viewer, 'XY'),
                                    (self.sagittal_viewer, 'YZ'),
                                    (self.coronal_viewer, 'XZ')]:
            # Retrieve the appropriate readers for each view
            if orientation == 'XY':
                reader_fixed, reader_moving = self.axial_viewer[2], self.axial_viewer[3]
            elif orientation == 'YZ':
                reader_fixed, reader_moving = self.sagittal_viewer[2], self.sagittal_viewer[3]
            elif orientation == 'XZ':
                reader_fixed, reader_moving = self.coronal_viewer[2], self.coronal_viewer[3]

            # Reslice transform filter
            transform_filter = vtk.vtkImageReslice()
            transform_filter.SetInputConnection(reader_moving.GetOutputPort())
            transform_filter.SetResliceTransform(transform)

            # Set the reslice axes based on the orientation
            if orientation == 'XY':
                transform_filter.SetResliceAxesDirectionCosines(1, 0, 0, 0, 1, 0, 0, 0, 1)
            elif orientation == 'YZ':
                transform_filter.SetResliceAxesDirectionCosines(1, 0, 0, 0, 1, 0, 0, 0, 1)
            elif orientation == 'XZ':
                transform_filter.SetResliceAxesDirectionCosines(1, 0, 0, 0, 1, 0, 0, 0, 1)

            transform_filter.SetOutputSpacing(reader_moving.GetOutput().GetSpacing())
            transform_filter.SetOutputOrigin(reader_moving.GetOutput().GetOrigin())
            transform_filter.SetInterpolationModeToLinear()
            transform_filter.Update()

            # Color mapping
            red_color_map = self.create_color_map((1, 0, 0))  # Red for fixed image
            green_color_map = self.create_color_map((0, 1, 0))  # Green for moving image

            color_fixed = vtk.vtkImageMapToColors()
            color_fixed.SetInputConnection(reader_fixed.GetOutputPort())
            color_fixed.SetLookupTable(red_color_map)

            color_moving = vtk.vtkImageMapToColors()
            color_moving.SetInputConnection(transform_filter.GetOutputPort())
            color_moving.SetLookupTable(green_color_map)

            # Blend the images
            blend = vtk.vtkImageBlend()
            blend.AddInputConnection(color_fixed.GetOutputPort())
            blend.AddInputConnection(color_moving.GetOutputPort())
            blend.SetOpacity(0, 0.5)  # Opacity for the fixed image
            blend.SetOpacity(1, 0.5)  # Opacity for the moving image
            blend.Update()

            # Set the blended image as input for the viewer and render
            viewer[1].SetInputConnection(blend.GetOutputPort())
            viewer[1].Render()

    def cleanup(self):
        # Properly shut down the interactor
        self.axial_viewer[0].GetRenderWindow().GetInteractor().TerminateApp()
        self.sagittal_viewer[0].GetRenderWindow().GetInteractor().TerminateApp()
        self.coronal_viewer[0].GetRenderWindow().GetInteractor().TerminateApp()

        # Ensure the interactor is removed and widgets are cleaned up
        self.axial_viewer[0].GetRenderWindow().Finalize()
        self.sagittal_viewer[0].GetRenderWindow().Finalize()
        self.coronal_viewer[0].GetRenderWindow().Finalize()

        self.axial_viewer[0].SetRenderWindow(None)
        self.sagittal_viewer[0].SetRenderWindow(None)
        self.coronal_viewer[0].SetRenderWindow(None)

        self.axial_viewer[0].GetRenderWindow().GetInteractor().SetRenderWindow(None)
        self.sagittal_viewer[0].GetRenderWindow().GetInteractor().SetRenderWindow(None)
        self.coronal_viewer[0].GetRenderWindow().GetInteractor().SetRenderWindow(None)

        self.axial_viewer = None
        self.sagittal_viewer = None
        self.coronal_viewer = None

        self.layout = None

    def closeEvent(self, event):
        # Cleanup the central widget before closing the main window
        if self.central_widget:
            self.central_widget.cleanup()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, fixed_file, moving_file, is_dicom=False, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Overlay Viewer")
        self.resize(800, 800)

        self.central_widget = VTKOverlayViewer(fixed_file, moving_file, is_dicom, self)
        self.setCentralWidget(self.central_widget)

    def closeEvent(self, event):
        # Cleanup before closing the application
        self.central_widget.cleanup()
        super().closeEvent(event)


if __name__ == "__main__":
    moving_file = "C:\\dev\\git\\MRIphantom_desktop\\studies\\10\\image_fixed.nii"
    fixed_file = "C:\\dev\\git\\MRIphantom_desktop\\studies\\10\\image_moving.nii"

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(fixed_file, moving_file, False)
    window.show()
    sys.exit(app.exec())