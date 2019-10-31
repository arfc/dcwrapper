# Transition year sensitivity analysis (one at a time approach)
This folder contains the dakota files and jupyter notebooks
that generate the results for the impact of variation of transition year
on a EG01-EG30 transition scenario. 

To run the simulation, type this into the command line: 

`dakota -i transition-year.in -o transition-year.out`

This will generate 5 sqlite output files in the 
`../../../cyclus-files/oat/transition-year/` directory. Example name of output file: `ty0.sqlite`.
They contain the results for EG01-30 transition scenario with varying MOX PWR transition year
80,81,82,83,84 years. Use the `transition-year.ipynb` jupyter notebook to analyze 
environmental impact, resource utilization, and goodness of transition evaluation metrics 
from these sqlite files.

To obtain the results for proliferation risk evaluation metrics. We need to run 
the same analysis as above but with `<explicit_inventory>true</explicit_inventory>`
in the control segment of the cyclus input file. 
The distinction between these output files and the non-exp ones is that 
explicit inventory tracking is turned on. 
This is required to use the isotopic capabilities in cymetric. 
These simulations take significantly longer to run. 
To run this simulation, type this into the command line: 

`dakota -i transition-year-exp.in -o transition-year-exp.out`

This will generate 5 sqlite output files in the 
`../../../cyclus-files/oat/transition-year/` directory. Example name of output file: `ty0.sqlite`.
They contain the results for EG01-30 transition scenario with varying MOX PWR transition year
80,81,82,83,84 years. Use the `transition-year-pu.ipynb` jupyter notebook to analyze 
environmental impact, resource utilization, and goodness of transition evaluation metrics 
from these sqlite files.
