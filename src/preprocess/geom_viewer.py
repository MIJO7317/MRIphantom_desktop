import vtk

reader = vtk.vtkUnstructuredGridReader()
reader.SetFileName("C:\\dev\\git\\MRIphantom_desktop\\assets\\geometry\\base_01.vtk")
reader.Update()

mapper = vtk.vtkDataSetMapper()
mapper.SetInputData(reader.GetOutput())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(1, 1, 1)  # Set background to white

render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

interactor.Initialize()
render_window.Render()
interactor.Start()
