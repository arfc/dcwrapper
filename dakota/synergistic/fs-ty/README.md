# Fleet share and transition year sensitivity analysis (synergistic)
This folder contains the dakota files and jupyter notebooks that generate 
the results for the synergistic impact of variation of 
fleet share and transition year on the EG01-EG30 transition scenario. 

To run the simulation, type this into the command line: 

`dakota -i fs-ty.in -o fs-ty.out`

This will generate 25 sqlite output files in the 
`../../../cyclus-files/synergistic/fs-ty` directory.
Example name of output file: `fs0ty80.sqlite`. They contain the results for EG01-30 
transition scenario with varying fleet share percentage and transition year. 
Fleet share % varies from 0 to 20%. Transition year varies from 80 to 84 years. 
Use the `fs-ty.ipynb` jupyter notebook to generate 3D surface plots to
analyze environmental impact, resource utilization, 
and goodness of transition evaluation metrics from these sqlite files.
