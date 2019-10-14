import sys
import os
sys.path.append('../../../scripts')
import input as inp
import dakota.interfacing as di
import subprocess
import glob

cycdir = '../../../cyclus-files/oat/transition-year/'

# ----------------------------
# Parse Dakota parameters file
# ----------------------------

params, results = di.read_parameters_file()

# -------------------------------
# Convert and send to Cyclus
# -------------------------------

# Edit Cyclus input file
cyclus_template = cycdir+'transition-year.xml.in'
scenario_name = 'ty' + str(int(params['ty'])) #+ '-exp'
variable_dict = {'transition_year': int((params['ty']))}
output_xml = cycdir+'transition-year.xml'
inp.render_input(cyclus_template, variable_dict, output_xml)

# Run Cyclus with edited input file
output_sqlite = cycdir+scenario_name+'.sqlite'
os.system('cyclus -i ' + output_xml + ' -o ' + output_sqlite)
# ----------------------------
# Return the results to Dakota
# ----------------------------

for i, r in enumerate(results.responses()):
    if r.asv.function:
        r.function = 1

results.write()
