# Fleet share sensitivity analysis (one at a time approach)
This folder contains the dakota files and jupyter notebooks
that generate the results for the impact of variation of fleet 
share on a EG01-EG30 transition scenario. 

To run the simulation, type this into the command line: 

`dakota -i fleet-share.in -o fleet-share.out`

This will generate 5 sqlite output files in the 
`../../../cyclus-files/oat/fleet-share/` directory. 
Example name of output file: `fs0.sqlite`.
They contain the results for EG01-30 transition scenario with varying MOX PWR fleet share
percentage 0,5,10,15,20 % of MOX PWRs and SFRs. 
Use the `fleet-share.ipynb` jupyter notebook to analyze environmental impact, resource utilization, 
and goodness of transition evaluation metrics from these sqlite files.

To obtain the results for proliferation risk evaluation metrics we need to run 
the same analysis as above but with `<explicit_inventory>true</explicit_inventory>`
in the control segment of the cyclus input file. 
The distinction between these output files and the non-exp ones is that 
explicit inventory tracking is turned on. 
This is required to use the isotopic capabilities in cymetric. 
These simulations take significantly longer to run. 
To run this simulation, type this into the command line: 

`dakota -i fleet-share-exp.in -o fleet-share-exp.out`

This will generate 5 sqlite output files in the 
`../../../cyclus-files/oat/fleet-share/` directory. Example name of output file: `fs0-exp.sqlite`.
They contain the results for EG01-30 transition scenario with varying MOX PWR fleet share
percentage 0,5,10,15,20 %. 
Use the `fleet-share-pu.ipynb` jupyter notebook to analyze environmental impact, resource utilization, 
and goodness of transition evaluation metrics from these sqlite files.

