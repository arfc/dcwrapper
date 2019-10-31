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
1. Go into the `dakota` directory, depending on the type of sensitivity 
analysis study you plan to conduct, create a folder for your sensitivity 
analysis study in the OAT, synergistic or sobol directory.
2. Follow step 1 to create a folder in the `cyclus-files` directory to hold 
Cyclus input files associated with the new sensitivity analysis study. 

A few things to note: 
* Any new scripts created should go into the `scripts` directory. 

## Dependencies 
Cyclus & it's dependencies: https://github.com/cyclus/cyclus 

Cycamore & it's dependencies: https://github.com/cyclus/cycamore

Cymetric & it's dependencies: https://github.com/cyclus/cymetric

Pyne & it's dependencies: https://github.com/pyne/pyne

Dakota & it's depenencies: https://dakota.sandia.gov/download.html
