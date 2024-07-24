import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QMainWindow, QFrame
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkRenderingContextOpenGL2 import *
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkDICOMImageReader
from vtkmodules.vtkInteractionImage import vtkImageViewer, vtkImageViewer2
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkActor2D,
    vtkRenderWindowInteractor,
    vtkTextMapper,
    vtkTextProperty
)

# Helper class to format slice status message
class StatusMessage:
    @staticmethod
    def format(slice: int, max_slice: int):
        return f'Slice Number {slice + 1}/{max_slice + 1}'

# Define own interaction style
class MyVtkInteractorStyleImage(vtkInteractorStyleImage):
    def __init__(self, parent=None):
        super().__init__()
        self.AddObserver('KeyPressEvent', self.key_press_event)
        self.AddObserver('MouseWheelForwardEvent', self.mouse_wheel_forward_event)
        self.AddObserver('MouseWheelBackwardEvent', self.mouse_wheel_backward_event)
        self.image_viewer = None
        self.status_mapper = None
        self.slice = 0
        self.min_slice = 0
        self.max_slice = 0

    def set_image_viewer(self, image_viewer):
        self.image_viewer = image_viewer
        self.min_slice = image_viewer.GetSliceMin()
        self.max_slice = image_viewer.GetSliceMax()
        self.slice = self.min_slice
        print(f'Slicer: Min = {self.min_slice}, Max= {self.max_slice}')

    def set_status_mapper(self, status_mapper):
        self.status_mapper = status_mapper

    def move_slice_forward(self):
        if self.slice < self.max_slice:
            self.slice += 1
            print(f'MoveSliceForward::Slice = {self.slice}')
            self.image_viewer.SetSlice(self.slice)
            msg = StatusMessage.format(self.slice, self.max_slice)
            self.status_mapper.SetInput(msg)
            self.image_viewer.Render()

    def move_slice_backward(self):
        if self.slice > self.min_slice:
            self.slice -= 1
            print(f'MoveSliceBackward::Slice = {self.slice}')
            self.image_viewer.SetSlice(self.slice)
            msg = StatusMessage.format(self.slice, self.max_slice)
            self.status_mapper.SetInput(msg)
            self.image_viewer.Render()

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

class DICOMViewer(QWidget):
    def __init__(self, dicom_dir):
        super().__init__()

        # self.layout = QVBoxLayout(self)

        self.colors = vtkNamedColors()
        self.reader = vtkDICOMImageReader()
        self.reader.SetDirectoryName(dicom_dir)
        self.reader.Update()

        self.vtk_widget = QVTKRenderWindowInteractor(self)
        # self.layout.addWidget(self.vtk_widget)
        # self.layout.addWidget(QLabel('Виджет добавлен'))

        self.image_viewer = vtkImageViewer2()
        self.image_viewer.SetInputConnection(self.reader.GetOutputPort())

        self.slice_text_prop = vtkTextProperty()
        self.slice_text_prop.SetFontFamilyToCourier()
        self.slice_text_prop.SetFontSize(32)
        self.slice_text_prop.SetVerticalJustificationToBottom()
        self.slice_text_prop.SetJustificationToLeft()

        self.slice_text_mapper = vtkTextMapper()
        msg = StatusMessage.format(self.image_viewer.GetSliceMin(), self.image_viewer.GetSliceMax())
        self.slice_text_mapper.SetInput(msg)
        self.slice_text_mapper.SetTextProperty(self.slice_text_prop)

        self.slice_text_actor = vtkActor2D()
        self.slice_text_actor.SetMapper(self.slice_text_mapper)
        self.slice_text_actor.SetPosition(15, 10)

        self.usage_text_prop = vtkTextProperty()
        self.usage_text_prop.SetFontFamilyToCourier()
        self.usage_text_prop.SetFontSize(30)
        self.usage_text_prop.SetVerticalJustificationToTop()
        self.usage_text_prop.SetJustificationToLeft()

        self.usage_text_mapper = vtkTextMapper()
        self.usage_text_mapper.SetInput(
            'Slice with mouse wheel\n  or Up/Down-Key\n- Zoom with pressed right\n '
            ' mouse button while dragging'
        )
        self.usage_text_mapper.SetTextProperty(self.usage_text_prop)

        self.usage_text_actor = vtkActor2D()
        self.usage_text_actor.SetMapper(self.usage_text_mapper)
        self.usage_text_actor.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
        self.usage_text_actor.GetPositionCoordinate().SetValue(0.05, 0.95)

        self.render_window_interactor = self.vtk_widget.GetRenderWindow().GetInteractor()
        self.my_interactor_style = MyVtkInteractorStyleImage()

        self.my_interactor_style.set_image_viewer(self.image_viewer)
        self.my_interactor_style.set_status_mapper(self.slice_text_mapper)

        self.image_viewer.SetupInteractor(self.render_window_interactor)
        self.render_window_interactor.SetInteractorStyle(self.my_interactor_style)
        self.render_window_interactor.Initialize()

        self.image_viewer.GetRenderer().AddActor2D(self.slice_text_actor)
        self.image_viewer.GetRenderer().AddActor2D(self.usage_text_actor)

        self.image_viewer.Render()
        self.image_viewer.GetRenderer().ResetCamera()
        self.image_viewer.GetRenderer().SetBackground(self.colors.GetColor3d('SlateGray'))
        self.image_viewer.GetRenderWindow().SetSize(800, 800)
        self.image_viewer.GetRenderWindow().SetWindowName('ReadDICOMSeries')
        self.image_viewer.Render()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dicom_directory = '/Users/bzavolovich/Developer/MRIphantom_desktop/images/DICOM_MR_contour'  # Replace with your DICOM directory path
    viewer = DICOMViewer(dicom_directory)
    viewer.show()
    sys.exit(app.exec_())
