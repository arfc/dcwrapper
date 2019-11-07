# Used fuel cooling time, fleet share, and transition year sensitivity analysis (global)
This folder contains the dakota files and jupyter notebooks that generate 
the results for the global impact of variation of used fuel cooling time, 
fleet share, and transition year on the EG01-EG30 transition scenario. 

To run the simulation, type this into the command line: 

`dakota -i sobol.in -o sobol.out`

This will generate sqlite output files in the 
`../../../cyclus-files/sobol` directory.
Example name of output file: `ct1fs0ty80.sqlite`. They contain the results for EG01-30 
transition scenario with varying used fuel cooling time, fleet share percentage 
and transition year. Used fuel cooling time varies from 0 to 8 yrs. 
Fleet share % varies from 0 to 20%. Transition year varies from 80 to 84 years. 
A table with the sobol indices is found at the end of the `sobol.out` dakota
output file. 
