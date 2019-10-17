import external_cym
import multiprocessing
import output as oup
import input as inp
import sys
import os
import signal
import dakota.interfacing as di
import subprocess
import glob
sys.path.append('../../../scripts')

cycdir = '../../../cyclus-files/synergistic/fs-ty/'

# ----------------------------
# Parse Dakota parameters file
# ----------------------------
params, results = di.read_parameters_file()

# -------------------------------
# Convert and send to Cyclus
# -------------------------------

# Edit Cyclus input file
cyclus_template = cycdir + 'fs-ty.xml.in'
scenario_name = 'fs' + str(int(params['fs'])) + 'ty' + str(int(params['ty']))
variable_dict = {'fleet_share_mox': int((params['fs'])),
                 'fleet_share_fr': int((100 - params['fs'])),
                 'transition_year': int((params['ty']))}
output_xml = cycdir + 'fs-ty.xml'
inp.render_input(cyclus_template, variable_dict, output_xml)

# Run Cyclus with edited input file
output_sqlite = cycdir + scenario_name + '.sqlite'
os.system('cyclus -i ' + output_xml + ' -o ' + output_sqlite)
#output_sqlite = cycdir + 'wow.sqlite'

# ----------------------------
# Return the results to Dakota
# ----------------------------

#ev = cym.Evaluator(db=cym.dbopen(output_sqlite),write=True)
f = open('output_name.txt', 'w+')
f.write(output_sqlite)
f.close()

p = multiprocessing.Process(target=external_cym.hlw)
p.start()
fresh = False
while fresh == False:
    if os.path.exists('hlw.txt'):
        if os.stat('hlw.txt').st_size > 0:
            print('hi')
            fresh = True
            p.terminate()

f = open('hlw.txt', 'r')
if f.mode == 'r':
    hlw = f.read()
f.close()


q = multiprocessing.Process(target=external_cym.dep_u)
q.start()
fresh = False
while fresh == False:
    if os.path.exists('depu.txt'):
        if os.stat('depu.txt').st_size > 0:
            print('hi')
            fresh = True
            p.terminate()

f = open('depu.txt', 'r')
if f.mode == 'r':
    depleted_u = f.read()
f.close()

p = multiprocessing.Process(target=external_cym.idlecapp)
p.start()
fresh = False
while fresh == False:
    if os.path.exists('idlecap.txt'):
        if os.stat('idlecap.txt').st_size > 0:
            print('hihihi')
            fresh = True
            p.terminate()

f = open('idlecap.txt', 'r')
if f.mode == 'r':
    idlecap = f.read()
f.close()


for i, r in enumerate(results.responses()):
    if r.asv.function:
        if i == 0:
            r.function = hlw
        if i == 1:
            r.function = depleted_u
        if i == 2:
            r.function = idlecap

if os.path.exists('depu.txt'):
    os.remove('depu.txt')
if os.path.exists('hlw.txt'):
    os.remove('hlw.txt')
if os.path.exists('idlecap.txt'):
    os.remove('idlecap.txt')

results.write()
