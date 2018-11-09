import sys
import os
sys.path.append(os.path.dirname(__file__))
import numpy as np
import pandas as pd
import db
import timeSeries as TS
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



def exportData(t, y, yErr, table, variable, lat1, lat2, lon1, lon2, extV, extVV, extV2, extVV2):
    df = pd.DataFrame()
    df['month'] = t
    df[variable] = y
    df[variable+'_std'] = yErr
    df['lat1'] = lat1
    df['lat2'] = lat2
    df['lon1'] = lon1
    df['lon2'] = lon2
    df[extV] = extVV
    df[extV2] = extVV2
    dirPath = 'data/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    path = dirPath + 'Monthly_' + table + '_' + variable + '.csv'
    df.to_csv(path, index=False)    
    return


def plotMonthly(tables, variables, lat1, lat2, lon1, lon2, extV, extVV, extV2, extVV2, exportDataFlag, marker='-', msize=30, clr='purple'):
    p = []
    lw = 2
    w = 800
    h = 400
    months = range(1, 13)
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'
    for i in tqdm(range(len(tables)), desc='overall'):
        monthly = np.array([])
        monthly_std = np.array([])
        for mon in tqdm(months, desc=variables[i]):
            mon = int(mon)
            args = [tables[i], variables[i], mon, lat1, lat2, lon1, lon2, extV[i], extVV[i]]
            query = 'EXEC uspMonthly ?, ?, ?, ?, ?, ?, ?, ?, ?'
            df = db.dbFetchStoredProc(query, args)        
            df = pd.DataFrame.from_records(df, columns=['lat', 'lon', variables[i]])
            ############# removing outlier values ################
            vals = df[variables[i]]
            vals = vals[abs(vals)<1e30]         # remove outliers
            ######################################################
            monthly = np.append(monthly, np.nanmean(vals))
            monthly_std = np.append(monthly_std, np.nanstd(vals))
        if exportDataFlag:
            exportData(months, monthly, monthly_std, tables[i], variables[i], lat1, lat2, lon1, lon2, extV[i], extVV[i], extV2[i], extVV2[i])            
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
        #p1.xaxis.axis_label = 'Month'
        p1.yaxis.axis_label = variables[i] + ' [' + db.getVar(tables[i], variables[i]).iloc[0]['Unit'] + ']'
        leg = variables[i]
        if extV[i] != None:
            leg = leg + '   ' + extV[i] + ': ' + ( '%d' % float(extVV[i]) ) 
            if tables[i].find('Pisces') != -1:
                leg = leg + ' ' + 'm'
        fill_alpha = 0.07        
        if tables[i].find('Pisces') != -1:
            fill_alpha = 0.3
        cr = p1.circle(months, monthly, fill_color="grey", hover_fill_color="firebrick", fill_alpha=fill_alpha, hover_alpha=0.3, line_color=None, hover_line_color="white", legend=leg, size=msize)
        p1.line(months, monthly, line_color=clr, line_width=lw, legend=leg)
        p1.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))
        p.append(p1)
    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    if not inline:      ## if jupyter is not the caller
        output_file(dirPath + fname + ".html", title="Monthly Trend")
    show(column(p))
    return








inline = jup.inline()   # check if jupyter is calling this script


tables = sys.argv[1].split(',')      #tables
variables = sys.argv[2].split(',')      #variables
lat1 = float(sys.argv[3])      #lat1
lat2 = float(sys.argv[4])      #lat2
lon1 = float(sys.argv[5])      #lon1
lon2 = float(sys.argv[6])      #lon2
fname = sys.argv[7]
exportDataFlag = bool(int(sys.argv[8]))
extV = sys.argv[9].split(',')       #extra condition: var_name
extVV = sys.argv[10].split(',')       #extra condition: var_val
extV2 = sys.argv[11].split(',')       #extra condition: var_name
extVV2 = sys.argv[12].split(',')       #extra condition: var_val



if float(lat1)>float(lat2):
    temp = lat1
    lat1 = lat2
    lat2 = temp

if float(lon1)>float(lon2):
    temp = lon1
    lon1 = lon2
    lon2 = temp



for i in range(len(tables)):
    if extV[i].find('ignore') != -1:
        extV[i]=None
    if extVV[i].find('ignore') != -1:
        extVV[i]=None
    if extV2[i].find('ignore') != -1:
        extV2[i]=None
    if extVV2[i].find('ignore') != -1:
        extVV2[i]=None


tic = time.clock()
plotMonthly(tables, variables, lat1, lat2, lon1, lon2, extV, extVV, extV2, extVV2, exportDataFlag)
toc = time.clock()
print('Fetch time: %2.2f s' % (toc-tic))
