import cymetric as cym
from cymetric import timeseries
import signal
import os
import sys
import output as oup


def hlw():
    """
    This function uses cymetric to read the output_sqlite file for 
    final hlw value. 
    """
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
    """
    This function uses cymetric to read the output_sqlite file for 
    final depleted u value. 
    """
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


def idle_cap():
    """
    This function uses cymetric to read the output_sqlite file for 
    total idle capacity value. 
    """
    f = open('output_name.txt', 'r')
    if f.mode == 'r':
        output_sqlite = f.read()
    f.close()
    ev = cym.Evaluator(db=cym.dbopen(output_sqlite), write=True)
    val, val2, val3 = oup.idlecap(ev, '(60000+250*t/12.0)/1000.0')
    f = open('idlecap.txt', 'w+')
    f.write(str(val))
    f.close()
    return val
