import numpy as np
import paraview.vtk.numpy_interface.algorithms as alg 
from vtk.numpy_interface import dataset_adapter as dsa

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

info = inputs[0].GetInformation()
t=info.Get(vtk.vtkDataObject.DATA_TIME_STEP())

##Update the pipeline to time t
## causes recursion - 
##   the updatepipeline call runs the filter and that in
##   turn runs the updatepipeline call again....
#src = paraview.simple.GetActiveSource()
#print dir(src)
#src.UpdatePipeline(time=t)

max_stress = maxStress(inputs[0])
print 'max_stress', max_stress

d = inputs[0].PointData["Solution"]
max_disp = alg.max_per_block(alg.mag(d)).Arrays[0]

arr = np.zeros(3)
arr[0] = info.Get(vtk.vtkDataObject.DATA_TIME_STEP())
arr[1] = max_disp
arr[2] = max_stress
print arr
output.RowData.append(arr,'loadVsDisp_1')

# Extract the value for the current time step.
print 'timeIdx', self.timeIdx, 'numSteps', self.numSteps
if self.timeIdx < self.numSteps-1:
  # If we are not done, ask the pipeline to re-execute us.
  self.timeIdx += 1
  print 'if --- timeIdx', self.timeIdx, 'numSteps', self.numSteps
  request.Set(vtk.vtkStreamingDemandDrivenPipeline.CONTINUE_EXECUTING(), 1)
else:
  # We are done. Populate the output.
  #output.RowData.append(self.arr, 'foo')
  print 'else --- timeIdx', self.timeIdx, 'numSteps', self.numSteps
  # Stop execution
  request.Remove(vtk.vtkStreamingDemandDrivenPipeline.CONTINUE_EXECUTING())
