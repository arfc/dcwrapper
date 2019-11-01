import numpy as np
import sqlite3 as lite


def isotope_total_cum(cur,num,in_dict):
    """ Find total isotopes present in each output stream 
    
    Parameters 
    ----------
    cur: sqlite cursor 
    num: nucid 
    
    Returns 
    -------

    """    
    
    streamlist = ["reprocess_waste","diverted"]
    isotope_total_list = []
    isotope_list = []
    isotope_ttal = 0 
    
    for stream in streamlist:    
        init_yr, init_month, duration, timestep = get_timesteps(cur)
        isotopes = cur.execute('SELECT time, sum(quantity)*massfrac FROM transactions '
                               'INNER JOIN resources '
                               'ON transactions.resourceid = resources.resourceid '
                               'LEFT OUTER JOIN compositions '
                               'ON resources.qualid = compositions.qualid '
                               'WHERE Commodity =:stream AND nucid =:num ' # must specify isotope and stream
                               ' GROUP BY time ',{"stream": stream, "num":num}).fetchall()
        isotope_list = get_timeseries(isotopes,duration,False)
        isotope_total = np.sum(isotope_list)
        isotope_total_list.append(isotope_total)
    
    name = num*0.0001
    in_dict[name] = isotope_total_list
    return in_dict

    
def get_cursor(file_name):
    """Connects and returns a cursor to an sqlite output file
    Parameters
    ----------
    file_name: str
        name of the sqlite file
    Returns
    -------
    sqlite cursor3
    """
    con = lite.connect(file_name)
    con.row_factory = lite.Row
    return con.cursor()


def get_timesteps(cur):
    """Returns simulation start year, month, duration and
    timesteps (in numpy linspace).
    Parameters
    ----------
    cur: sqlite cursor
        sqlite cursor
    Returns
    -------
    init_year: int
        start year of simulation
    init_month: int
        start month of simulation
    duration: int
        duration of simulation
    timestep: list
        linspace up to duration
    """
    info = cur.execute('SELECT initialyear, initialmonth, '
                       'duration FROM info').fetchone()
    init_year = info['initialyear']
    init_month = info['initialmonth']
    duration = info['duration']
    timestep = np.linspace(0, duration - 1, num=duration)

    return init_year, init_month, duration, timestep


def get_timeseries(in_list, duration, kg_to_tons):
    """returns a timeseries list from in_list data.
    Parameters
    ----------
    in_list: list
        list of data to be created into timeseries
        list[0] = time
        list[1] = value, quantity
    duration: int
        duration of the simulation
    kg_to_tons: bool
        if True, list returned has units of tons
        if False, list returned as units of kilograms
    Returns
    -------
    timeseries list of commodities stored in in_list
    """
    value = 0
    value_timeseries = []
    array = np.array(in_list)
    if len(in_list) > 0:
        for i in range(0, duration):
            value = sum(array[array[:, 0] == i][:, 1])
            if kg_to_tons:
                value_timeseries.append(value * 0.001)
            else:
                value_timeseries.append(value)
    return value_timeseries
