# Spent fuel cooling time sensitivity analysis (one at a time approach)
This folder contains the dakota files and jupyter notebooks
that generate the results for the impact of variation of spent 
fuel cooling time on a EG01-EG30 transition scenario. 

To run the simulation, type this into the command line: 

`dakota -i cooling-time.in -o cooling-time.out`

This will generate 5 sqlite output files in the 
`../../../cyclus-files/oat/cooling-time/` directory.
Example name of output file: `ct0.sqlite`. They contain the results for EG01-30 
transition scenario with varying cooling times of 0, 2, 4, 6, and 8 years. 
Use the `cooling-time.ipynb` jupyter notebook to analyze environmental impact, resource utilization, 
and goodness of transition evaluation metrics from these sqlite files.

To obtain the results for proliferation risk evaluation metrics we need to run 
the same analysis as above but with `<explicit_inventory>true</explicit_inventory>`
in the control segment of the cyclus input file. 
The distinction between these output files and the non-exp ones is that 
explicit inventory tracking is turned on. 
This is required to use the isotopic capabilities in cymetric. 
These simulations take significantly longer to run. 
To run this simulation, type this into the command line: 

`dakota -i cooling-time-exp.in -o cooling-time-exp.out`

This will generate 5 sqlite output files in the 
`../../../cyclus-files/oat/cooling-time/` directory.
Example name of output file: `ct0-exp.sqlite`. They contain the results for EG01-30 
transition scenario with varying cooling times of 0, 2, 4, 6, and 8 years 
with explicit inventory. 
Use the `cooling-time-pu.ipynb` jupyter notebook to analyze the proliferation risk
evaluation metric from these sqlite files.

