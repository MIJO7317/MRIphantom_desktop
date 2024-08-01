import vtk
import os


class MRISliceViewer:
    def __init__(self, dicom_dir):
        self.dicom_dir = dicom_dir

        self.reader = vtk.vtkDICOMImageReader()
        self.reader.SetDirectoryName(dicom_dir)

        if not os.listdir(dicom_dir):
            raise ValueError("Directory is empty or does not contain DICOM files.")

        self.reader.Update()
        self.image_data = self.reader.GetOutput()
        self.extent = self.image_data.GetExtent()

        self.current_slice = self.extent[4]
        self.min_slice = self.extent[4]
        self.max_slice = self.extent[5]

        self.setup_rendering()

    def setup_rendering(self):
        self.renderer = vtk.vtkRenderer()
        self.render_window = vtk.vtkRenderWindow()
        self.render_window.AddRenderer(self.renderer)
        self.interactor = vtk.vtkRenderWindowInteractor()
        self.interactor.SetRenderWindow(self.render_window)

        self.image_mapper = vtk.vtkImageMapper()
        self.image_mapper.SetInputData(self.image_data)
        self.image_mapper.SetColorWindow(255)
        self.image_mapper.SetColorLevel(127.5)
        self.image_mapper.SetZSlice(self.current_slice)

        self.image_actor = vtk.vtkActor2D()
        self.image_actor.SetMapper(self.image_mapper)

        self.renderer.AddActor2D(self.image_actor)
        self.renderer.SetBackground(0.1, 0.1, 0.1)

        self.interactor.AddObserver('KeyPressEvent', self.keypress)
        self.render_window.Render()
        self.interactor.Start()

    def keypress(self, obj, event):
        key = obj.GetKeySym()
        if key == "Up":
            self.next_slice()
        elif key == "Down":
            self.previous_slice()

    def next_slice(self):
        if self.current_slice < self.max_slice:
            self.current_slice += 1
            self.update_slice()

    def previous_slice(self):
        if self.current_slice > self.min_slice:
            self.current_slice -= 1
            self.update_slice()

    def update_slice(self):
        self.image_mapper.SetZSlice(self.current_slice)
        self.render_window.Render()


if __name__ == "__main__":
    dicom_dir = 'C:\dev\git\MRIphantom_desktop\images\DICOM_CT_contour'

    # Validate the directory
    if not os.path.isdir(dicom_dir):
        raise ValueError("The specified directory does not exist or is not a directory.")

    viewer = MRISliceViewer(dicom_dir)
