Name = 'Load Vs Displacement'
Label = 'Load Vs Displacement'
Help = 'Plot the maximum load vs the maximum displacement for a selected set of elements'

NumberOfInputs = 1
InputDataType = 'vtkUnstructuredGrid'
OutputDataType = 'vtkTable' # omit this line to use 'same as input'
ExtraXml = ''

Properties = dict(
  numStressFields = 0,
  stressFieldName = 'Cauchy_Stress_',
  displacementFieldName = 'Solution'
)

def RequestData():
  import numpy as np
  import paraview.vtk.numpy_interface.algorithms as alg 
  from vtk import vtkFloatArray

  def maxStress(inp):
    max_stress = 0
    for i in range(1,numStressFields+1):
      name = stressFieldName + str(i)
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

  max_stress = maxStress(inputs[0])
  d = inputs[0].PointData[displacementFieldName]
  max_disp = alg.max_per_block(alg.mag(d)).Arrays[0]
  
  addColumn(output,'max_disp',max_disp)
  addColumn(output,'max_stress',max_stress)
