# Hello. Welcome to the One-at-a-time fleet share percentage sensitivity analysis study. 
To run the simulation, type this into the command line: 

`dakota -i fleet-share.in -o fleet-share.out`

This will generate 5 sqlite output files in the 
`../../../cyclus-files/oat/fleet-share/` directory. 
They contain the results for EG01-30 transition scenario with varying MOX PWR fleet share
percentage 0,5,10,15,20 %. 
To analyze the results for environmental impact, resource utilization, and goodness of transition 
evaluation metrics from these sqlite files, use the `fleet-share.ipynb` jupyter notebook. 

To analyze the results for the proliferation risk evaluation metric from these sqlite files, 
use the `fleet-share-pu.ipynb` jupyter notebook. 
However, before being able to run the jupyter notebook, you need to run this is the command line:

`dakota -i fleet-share-exp.in -o fleet-share-exp.out`

This will generate 5 sqlite output files in the 
`../../../cyclus-files/oat/fleet-share/` directory. 
The distinction between these output files and the non-exp ones is that these cyclus input 
files include an `<explicit_inventory>True</explicit_inventory>` that turns on 
explicit inventory tracking. This is required to use the isotopic capabilities in cymetric. 
These simulations take significantly longer to run. 
