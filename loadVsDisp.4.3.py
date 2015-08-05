import numpy as np
import paraview.vtk.numpy_interface.algorithms as alg 
from vtk import vtkFloatArray

def maxStress(inp):
  base = 'Cauchy_Stress_'
  max_stress = 0
  for i in range(1,6):
    name = base + str(i)
    s = inp.CellData[name]
    ms = alg.max(alg.eigenvalue(s))
    if ms > max_stress:
      max_stress = ms
  return max_stress

def addColumn(table,name,v):
  c = vtkFloatArray()
  c.SetName(name)
  c.InsertNextValue(v)
  table.AddColumn(c)

info = inputs[0].GetInformation()
t=info.Get(vtk.vtkDataObject.DATA_TIME_STEP())
print 'time', t

max_stress = maxStress(inputs[0])
print 'max_stress', max_stress

d = inputs[0].PointData["Solution"]
max_disp = alg.max_per_block(alg.mag(d)).Arrays[0]
print 'max_disp', max_disp

addColumn(output,'time',t)
addColumn(output,'XArrayName',max_disp)
addColumn(output,'max_stress',max_stress)
