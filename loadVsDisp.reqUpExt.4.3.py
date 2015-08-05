print '+++requestUpdateExtent'
info = inputs[0].GetInformation()
# Ask for the next timestep.
print '~~~~timeIdx', self.timeIdx, 'self.timeSteps[self.timeIdx]', self.timeSteps[self.timeIdx]
info.Set(vtk.vtkStreamingDemandDrivenPipeline.UPDATE_TIME_STEP(),
   self.timeSteps[self.timeIdx])
print '---requestUpdateExtent'
