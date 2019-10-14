import sys
import os
sys.path.append('../../../scripts')
import input as inp
# import output as oup
import dakota.interfacing as di
import subprocess
import glob

cycdir = '../../../cyclus-files/oat/fleet-share/'

# ----------------------------
# Parse Dakota parameters file
# ----------------------------

params, results = di.read_parameters_file()

# -------------------------------
# Convert and send to Cyclus
# -------------------------------

# Edit Cyclus input file
cyclus_template = cycdir+'fleet-share.xml.in'
scenario_name = 'fs' + str(int(params['fs'])) #+ '-exp'
variable_dict = {'fleet_share_mox': int((params['fs'])),'fleet_share_fr':int((100-params['fs']))}
output_xml = cycdir+'fleet-share.xml'
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
        print('OUT', i, r.function)

results.write()
