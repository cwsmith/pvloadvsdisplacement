# pvloadvsdisplacement
Python code for a Paraview programmable filter that hopes to support plotting the maximum load vs the maximum displacement over a set of user selected elements.

# How to use
* Open a pvtu file
* select some elements via 'select elements through'
* Filters->Alphabetical->Extract Selection 
* Click apply
* Filters->Alphabetical->Programmable Filter
* Paste loadVsDisp.4.3.py into the 'Script' text box
* Paste loadVsDisp.reqInfo.4.3.py into the 'RequestInformation Script' text box
* Paste loadVsDisp.reqUpExt.4.3.py into the 'RequestUpdateExtent Script' text box
