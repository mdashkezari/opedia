"""
Author: Mohammad Dehghani Ashkezari <mdehghan@uw.edu>

Date: Summer 2017

Function: Plot distribution of variables within a predefined space-time domain.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
import numpy as np
import pandas as pd
import db
import subset
import common as com
import export
from datetime import datetime, timedelta
import time
from math import pi
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.models import DatetimeTickFormatter
from bokeh.palettes import all_palettes
from bokeh.models import HoverTool
from bokeh.embed import components
import jupyterInline as jup
if jup.jupytered():
    from tqdm import tqdm_notebook as tqdm
else:
    from tqdm import tqdm



def exportData(y, table, variable, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2):
    df = pd.DataFrame()
    df[variable] = y
    timeField = 'time'
    if db.isClimatology(table) and db.hasField(table, 'month'):
        timeField = 'month'
    df['start_'+timeField] = startDate
    df['end_'+timeField] = endDate
    df['lat1'] = lat1
    df['lat2'] = lat2
    df['lon1'] = lon1
    df['lon2'] = lon2
    if db.hasField(table, 'depth'):
        df['depth1'] = depth1
        df['depth2'] = depth2
    # dirPath = 'data/'
    # if not os.path.exists(dirPath):
    #     os.makedirs(dirPath)        
    # path = dirPath + 'Hist_' + table + '_' + variable + '.csv'
    # df.to_csv(path, index=False)    

    export.dump(df, table, variable, prefix='Hist', fmt='.csv')
    return


def plotDist(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag, marker='-', msize=30, clr='purple'):
    p = []
    lw = 2
    w = 800
    h = 400
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'
    for i in tqdm(range(len(tables)), desc='overall'):
        y = subset.spaceTime(tables[i], variables[i], startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2) 
        if len(y) < 1:
            com.printTQDM('%d: No matching entry found: Table: %s, Variable: %s ' % (i+1, tables[i], variables[i]), err=True )
            continue
        com.printTQDM('%d: %s retrieved (%s).' % (i+1, variables[i], tables[i]), err=False)
        y = y[variables[i]]
        if exportDataFlag:
            exportData(y, tables[i], variables[i], startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2)
        try:    
            y = y[~np.isnan(y)]     # remove nans
        except Exception as e:
            continue    
        hist, edges = np.histogram(y, density=True, bins=50)
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
        p1.yaxis.axis_label = 'Density'
        p1.xaxis.axis_label = variables[i] + ' [' + db.getVar(tables[i], variables[i]).iloc[0]['Unit'] + ']'
        leg = variables[i]
        fill_alpha = 0.4   
        cr = p1.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="dodgerblue", line_color=None, hover_fill_color="firebrick", fill_alpha=fill_alpha, hover_alpha=0.7, hover_line_color="white", legend=leg)
        p1.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='mouse'))
        p.append(p1)
    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    if not inline:      ## if jupyter is not the caller
        output_file(dirPath + fname + ".html", title="Histogram")
    show(column(p))
    return


def main():
    tables = sys.argv[1].split(',')      
    variables = sys.argv[2].split(',')      
    startDate = sys.argv[3]      
    endDate = sys.argv[4]      
    lat1 = sys.argv[5]   
    lat2 = sys.argv[6]   
    lon1 = sys.argv[7]     
    lon2 = sys.argv[8]   
    depth1 = sys.argv[9]      
    depth2 = sys.argv[10]        
    fname = sys.argv[11]
    exportDataFlag = bool(int(sys.argv[12]))

    if float(lat1)>float(lat2):
        temp = lat1
        lat1 = lat2
        lat2 = temp

    if float(lon1)>float(lon2):
        temp = lon1
        lon1 = lon2
        lon2 = temp

    if datetime.strptime(startDate, '%Y-%m-%d')>datetime.strptime(endDate, '%Y-%m-%d'):
        temp = startDate
        startDate = endDate
        endDate = temp

    plotDist(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)


inline = jup.inline()   # check if jupyter is calling this script
if __name__ == '__main__':
    main()