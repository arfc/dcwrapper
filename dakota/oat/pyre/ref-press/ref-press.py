sys.path.append('../../../../scripts')
import glob
import subprocess
import dakota.interfacing as di
import sys
import os
import input as inp

cycdir = '../../../../cyclus-files/oat/pyre/ref-press/'

# ----------------------------
# Parse Dakota parameters file
# ----------------------------

params, results = di.read_parameters_file()

# -------------------------------
# Convert and send to Cyclus
# -------------------------------

# Edit Cyclus input file
cyclus_template = cycdir + 'ref-press.xml.in'
scenario_name = 'press' + str(int(params['press']))  # + '-exp'
variable_dict = {'refining_pressure': int((params['press']))}
output_xml = cycdir + 'ref-press.xml'
inp.render_input(cyclus_template, variable_dict, output_xml)

# Run Cyclus with edited input file
output_sqlite = cycdir + scenario_name + '.sqlite'
os.system('cyclus -i ' + output_xml + ' -o ' + output_sqlite)
# ----------------------------
# Return the results to Dakota
# ----------------------------

for i, r in enumerate(results.responses()):
    if r.asv.function:
        r.function = 1

results.write()
