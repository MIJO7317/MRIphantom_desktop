import sys
import vtk
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import os
import pydicom

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("MRI DICOM Slices Viewer")

        # Set up the central widget with a vertical layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create and set up the VTK renderer
        self.vtk_widget = QVTKRenderWindowInteractor(self.central_widget)
        self.layout.addWidget(self.vtk_widget)

        self.iren = self.vtk_widget.GetRenderWindow().GetInteractor()

        # Initialize the VTK scene
        self.renderer = vtk.vtkRenderer()
        self.vtk_widget.GetRenderWindow().AddRenderer(self.renderer)

        # Load and visualize the DICOM series
        self.load_dicom_series('/Users/bzavolovich/Developer/MRIphantom_desktop/images/DICOM_CT_contour')

        # Start the VTK interaction
        self.iren.Initialize()

    def load_dicom_series(self, folder_path):
        # Read DICOM series using VTK
        reader = vtk.vtkDICOMImageReader()
        reader.SetDirectoryName(folder_path)
        reader.Update()

        # Extract image data
        image_data = reader.GetOutput()

        # Set up a plane widget for each orientation (axial, coronal, sagittal)
        self.setup_plane_widget(image_data, orientation='axial')
        self.setup_plane_widget(image_data, orientation='coronal')
        self.setup_plane_widget(image_data, orientation='sagittal')

        # Reset the camera to view the whole scene
        self.renderer.ResetCamera()

    def setup_plane_widget(self, image_data, orientation='axial'):
        # Create a plane widget
        plane_widget = vtk.vtkImagePlaneWidget()
        plane_widget.SetInteractor(self.iren)
        plane_widget.SetInputData(image_data)

        # Configure the plane orientation
        if orientation == 'axial':
            plane_widget.SetPlaneOrientationToZAxes()
        elif orientation == 'coronal':
            plane_widget.SetPlaneOrientationToYAxes()
        elif orientation == 'sagittal':
            plane_widget.SetPlaneOrientationToXAxes()

        # Enable the plane widget interaction
        plane_widget.On()

        # Set lookup table for better visualization
        lookup_table = vtk.vtkLookupTable()
        lookup_table.SetRange(image_data.GetScalarRange())
        lookup_table.SetValueRange(0.0, 1.0)
        lookup_table.SetSaturationRange(0.0, 0.0)
        lookup_table.SetRampToLinear()
        lookup_table.Build()

        # Apply the lookup table
        plane_widget.GetColorMap().SetLookupTable(lookup_table)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
