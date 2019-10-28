import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MaxNLocator
import numpy as np
from math import pi
import output as oup


def format_dataframe(dat_file,column_names,index):
    """ This function formats a dakota output dat file into an easily readable format 
    INPUT 
    dat_file: path to dat file (str)
    column_names = list of names corresponding to what the user wants each column to be named
                   (list of str)
    index = list of input variable names to be index (list of str)
    OUTPUT 
    df: formatted pandas dataframe 
    """
    df = pd.read_csv(dat_file,sep='\s+',names=column_names)
    df = df.iloc[1:]
    df = df.drop(columns='id')
    df = df.set_index(index)
    return df 

def initialize_df(scenario_index,scenarios_nums):
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


def threed_plot(df,commod,arrange):
    """ This function creates a 3D surf plot from the dataframe for the 
    input commod. 
    INPUT VARIABLES 
    df: pandas dataframe with results 
    commod: name of commod to plot from pandas dataframe 
    arrange: Boolean. True if you want (x,y) orientation, False if you want 
    (y,x) orientation for the x,y variables in the 3D plot. 
    """
    fig = plt.figure(figsize=(10,7))
    ax = plt.axes(projection='3d')

    # Data for a three-dimensional line
    if arrange: 
        x = [int(i)/12 for i in list(df.index.get_level_values(1).values)]
        y = [int(i) for i in list(df.index.get_level_values(0).values)]
        ax.set_xlabel(df.index.names[1]+' [yr]')
        ax.set_ylabel(df.index.names[0]+' [%]')
    else:
        y = [int(i)/12 for i in list(df.index.get_level_values(1).values)]
        x = [int(i) for i in list(df.index.get_level_values(0).values)]
        ax.set_ylabel(df.index.names[1]+' [yr]')
        ax.set_xlabel(df.index.names[0]+' [%]')
    z = [float(i) for i in list(df[commod].values)]
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.zaxis.set_major_locator(MaxNLocator(5))
    ax.set_title('3D plot of '+commod)
    ax.set_zlabel(commod+' [kg]')
    ax.dist = 11
    ax.plot_trisurf(x,y,z, cmap=plt.cm.viridis, linewidth=0.2, alpha= 0.3)
    surf=ax.plot_trisurf(x,y, z, cmap=plt.cm.viridis, linewidth=0.2)
    fig.colorbar( surf, shrink=0.5, aspect=5)
    fig.savefig(commod, bbox_inches='tight')
    return