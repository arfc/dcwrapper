# Hello. Welcome to the One-at-a-time Cooling time sensitivity analysis study. 
To run the simulation, type this into the command line: 

`dakota -i cooling-time.in -o cooling-time.out`

This will generate 5 sqlite output files in the 
`../../../cyclus-files/oat/cooling-time/` directory. 
They contain the results for EG01-30 transition scenario with varying cooling time of 0,2,4,6,8 years. 
To analyze the results for environmental impact, resource utilization, and goodness of transition 
evaluation metrics from these sqlite files, use the `cooling-time.ipynb` jupyter notebook. 

To analyze the results for the proliferation risk evaluation metric from these sqlite files, 
use the `cooling-time-pu.ipynb` jupyter notebook. 
However, before being able to run the jupyter notebook, you need to run this is the command line:

`dakota -i cooling-time-exp.in -o cooling-time-exp.out`

This will generate 5 sqlite output files in the 
`../../../cyclus-files/oat/cooling-time/` directory. 
The distinction between these output files and the non-exp ones is that these cyclus input 
files include an `<explicit_inventory>True</explicit_inventory>` that turns on 
explicit inventory tracking. This is required to use the isotopic capabilities in cymetric. 
These simulations take significantly longer to run. 

