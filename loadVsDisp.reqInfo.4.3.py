import numpy as np
print '\n\n\n\n'
print '+++requestInfo'
self.timeIdx = int(0)
self.numSteps = 4
self.stepSize = 0.25
self.timeSteps = np.zeros(self.numSteps)
for i in range(0,self.numSteps):
  self.timeSteps[i] = i*self.stepSize
print self.timeSteps
print '---requestInfo'
