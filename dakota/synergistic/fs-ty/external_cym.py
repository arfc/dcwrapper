import cymetric as cym
from cymetric import timeseries
import signal
import os
import sys
sys.path.append('../../../scripts')
import output as oup


def hlw():
    f = open('output_name.txt', 'r')
    if f.mode == 'r':
        output_sqlite = f.read()
    f.close()
    ev = cym.Evaluator(db=cym.dbopen(output_sqlite), write=True)
    val = cym.timeseries.transactions(ev,
                                      commodities=['lwrreprocessingwaste',
                                                   'moxreprocessingwaste',
                                                   'frreprocessingwaste'])[
        'Mass'].cumsum().iloc[-1]
    with open('hlw.txt', 'w') as f:
        f.write(str(val))
    return val


def dep_u():
    f = open('output_name.txt', 'r')
    if f.mode == 'r':
        output_sqlite = f.read()
    f.close()
    ev = cym.Evaluator(db=cym.dbopen(output_sqlite), write=True)
    val = cym.timeseries.transactions(ev,
                                      commodities=['enrichmentwaste'])['Mass'].cumsum().iloc[-1]
    print(val)
    f = open('depu.txt', 'w+')
    f.write(str(val))
    f.close()
    return val


def idlecapp():
    f = open('output_name.txt', 'r')
    if f.mode == 'r':
        output_sqlite = f.read()
    f.close()
    ev = cym.Evaluator(db=cym.dbopen(output_sqlite), write=True)
    val, val2, val3 = oup.idlecap(ev, '(60000+250*t/12)/1000')
    f = open('idlecap.txt', 'w+')
    f.write(str(val))
    f.close()
    return val
