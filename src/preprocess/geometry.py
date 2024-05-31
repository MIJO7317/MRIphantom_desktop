import vtk
import numpy as np
import matplotlib.pyplot as plt


vtk_file = 'C:\\dev\\git\\MRIphantom_desktop\\assets\\geometry\\base_01.vtk'
grid_size = (512, 512, 179)

reader = vtk.vtkPolyDataReader()
reader.SetFileName(vtk_file)
reader.Update()

polydata = reader.GetOutput()

points_array = np.empty((0, 3), dtype=np.float64)

for i in range(polydata.GetNumberOfCells()):
    pts = polydata.GetCell(i).GetPoints()
    np_pts = np.array([pts.GetPoint(i) for i in range(pts.GetNumberOfPoints())])
    points_array = np.append(points_array, np_pts, axis=0)

print(points_array.shape)
