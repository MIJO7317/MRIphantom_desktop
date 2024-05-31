#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.7.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'C:/Users/Mike/Downloads/_phantome_')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Cylinder_1 = geompy.MakeCylinderRH(1, 118)
Multi_Translation_1 = geompy.MakeMultiTranslation2D(Cylinder_1, OX, 20, 11, OY, 20, 11)
Vertex_1 = geompy.MakeVertex(100, 100, 0)
Cylinder_2 = geompy.MakeCylinder(Vertex_1, OZ, 105, 300)
Cylinder_3 = geompy.MakeCylinder(Vertex_1, OZ, 5, 300)
Cut_1 = geompy.MakeCutList(Cylinder_2, [Cylinder_3], True)
Common_1 = geompy.MakeCommonList([Multi_Translation_1, Cut_1], True)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Cylinder_1, 'Cylinder_1' )
geompy.addToStudy( Multi_Translation_1, 'Multi-Translation_1' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Cylinder_2, 'Cylinder_2' )
geompy.addToStudy( Cylinder_3, 'Cylinder_3' )
geompy.addToStudy( Cut_1, 'Cut_1' )
geompy.addToStudy( Common_1, 'Common_1' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
