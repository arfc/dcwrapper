# dcwrapper
Dakota-Cyclus Wrapper 
This repository contains examples of Cyclus sensitivity analysis 
studies conducted with a Dakota wrapper. 
Cyclus interfaces with Dakota using a Python interface. 

To run the simple test case, run the following from this directory: 
```
bash
cd dakota/test/ 
dakota -i dakota_test.in -o dakota_test.out
```

The structure of each sensitivity analysis study in this repository 
is as follows: 
1. For each sensitivity analysis study, their Dakota input files goes 
into the `dakota` directory. Depending on the type of sensitivity 
analysis study you plan to conduct, create a folder for your sensitivity 
analysis study in the OAT, synergistic or sobol directory.
2. For each sensitivity analysis study, their Cyclus input files goes into 
the `cyclus-files` directory. 
Follow step 1 to create a folder in the `cyclus-files` directory to hold the 
Cyclus input files associated with the new sensitivity analysis study. 

A few things to note: 
* Any new scripts created should go into the `scripts` directory. 

## Dependencies 
Cyclus & its dependencies: https://github.com/cyclus/cyclus 

Cycamore & its dependencies: https://github.com/cyclus/cycamore

Cymetric & its dependencies: https://github.com/cyclus/cymetric

Pyne & its dependencies: https://github.com/pyne/pyne

Dakota & its depenencies: https://dakota.sandia.gov/download.html
