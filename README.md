# pvloadvsdisplacement 
Python code for a Paraview programmable filter that
supports plotting the maximum load vs the maximum displacement over time for a
set of user selected elements. The values being computed are specific to a
solid mechanics analysis run in [Albany](https://github.com/gahansen/Albany), but the process and code can be
extended to support other inputs.

Tested in Paraview 4.3.1 on GNU/Linux.

![plot](plot.png)

# Load the plugin (first use only)
* Tools->Manage Plugins
* Click 'Load New ...'
* Select 'loadVsDisp.xml'

# Create a load vs displacement plot
* Open a pvd file
* select some elements via 'select elements through'
* Filters->Alphabetical->Extract Selection 
* Click apply
* Filters->Alphabetical->Load Vs Displacement
* Set 'displacementFieldName' to the name of the VTU field containing the displacement field - typically 'Solution' or 'disp'
* Set 'numStressFields' equal to the number of VTU stress fields 
* Set 'stressFieldName' to the base name of the VTU stress field - typically 'Cauchy_Stress_' or 'Stress_'
* Set 'Field Association' to 'Row Data'
* Click apply
* Click the row in the spreadsheet window - it should become shaded
* Filters->Alphabetical->Plot Selection Over Time
* Click apply
* Under 'X Axis Parameters' set 'X Array Name' to 'max_disp'
* Under 'Series Parameters' select only the 'max_stress' box
* The plot title and axis labels can be set as needed via the other filter properties 

# Helpful documentation

[VTK C++](http://www.vtk.org/doc/nightly/html/classvtkTable.html)

[Python and C++ Examples](http://www.vtk.org/doc/nightly/html/c2_vtk_e_8.html)

[Easy Customization of the ParaView Python Programmable Filter Property Panel](http://www.kitware.com/blog/home/post/534)
(the <code>python_filter_generator.py</code> script is from this blog post)
