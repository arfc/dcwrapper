"""
This script contains functions to get various output variables
from Cyclus's sqlite output database
"""

import pandas as pd
import numpy as np
import cymetric as cym
from cymetric import fco_metrics


def initialize_df(scenario_index, scenarios_nums):
    """This function creates a pandas dataframe with scenario_index
    as index title and scenarios_nums as index values.
    This is used to initialize a dataframe to add subsequent columns to.
    INPUT
    scenario_index: title of index
    scenario_nums: list of scenario numbers
    OUTPUT
    df: initialized pandas dataframe
    """
    df = pd.DataFrame(index=scenarios_nums)
    df.index.name = scenario_index
    return df


# sensitivity
def sensitivity(base_case, init_df):
    """ 
    This function takes a dataframe and returns the % difference of each value to the 
    base case value. 
    INPUT 
    base_case: basecase number in string form (str)
    init_df: pandas dataframe
    OUTPUT sa_df = sensitivity analysis pandas dataframe 
    """
    sa_df = init_df.copy()
    df_length = init_df.index.size
    categories = list(init_df)
    N = len(categories)
    row = 0
    for x in range(df_length):
        if init_df.index[x] == base_case:
            basecase_index = row
        row += 1
    for x in range(df_length):
        if init_df.index[x] == base_case:
            for y in range(N):
                sa_df.iloc[x, y] = 0
        else:
            for y in range(N):
                if float(init_df.iloc[basecase_index, y]) == 0:
                    sa_df.iloc[x, y] = np.nan
                else:
                    sa_df.iloc[x, y] = (init_df.iloc[x, y] - init_df.iloc[basecase_index, y]) / \
                        init_df.iloc[basecase_index, y] * 100
    return sa_df


def idlecap(evaluator, demand_eq):
    """
    This function uses cymetric to read the output_sqlite file for 
    total idle capacity value. 
    """
    ep = evaluator.eval('FcoMonthlyElectricityGenerated')
    t = np.arange(0, 1440)
    power = eval(demand_eq)
    diff = list(ep['Energy']) - power
    total = 0
    undersupply_times = {}
    for x in range(len(diff)):
        if diff[x] < 0:
            total -= diff[x]
            undersupply_times[x] = -diff[x]
    last_undersupply = max(k for k, v in undersupply_times.items())
    return total, last_undersupply, undersupply_times
