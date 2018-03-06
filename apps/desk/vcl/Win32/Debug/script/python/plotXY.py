import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import db
import timeSeries as TS
import itertools as itt
from datetime import datetime, timedelta
import time
from math import pi
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.models import DatetimeTickFormatter
from bokeh.palettes import all_palettes
from bokeh.models import HoverTool
from bokeh.embed import components


def embedComponents(fname, data):
    f = open(fname, 'w')
    f.write(data)
    f.close()
    return

def exportData(t1, y1, yErr1, t2, y2, yErr2, table1, variable1, table2, variable2, lat1, lat2, lon1, lon2, extV_1, extVV_1, extV2_1, extVV2_1, extV_2, extVV_2, extV2_2, extVV2_2):
    df = pd.DataFrame()
    df['time_X'] = t1
    df[variable1] = y1
    df[variable1+'_std_X'] = yErr1
    df['time_Y'] = t2
    df[variable2] = y2
    df[variable2+'_std_Y'] = yErr2
    df['lat1'] = lat1
    df['lat2'] = lat2
    df['lon1'] = lon1
    df['lon2'] = lon2
    df[extV_1] = extVV_1
    df[extV2_1] = extVV2_1
    df[extV_2] = extVV_2
    df[extV2_2] = extVV2_2
    dirPath = 'data/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    path = dirPath + 'XY_' + table1 + '_' + variable1 + '_vs_' + table2 + '_' + variable2 + '.csv'
    df.to_csv(path, index=False)    
    return

def plotXY(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2,exportDataFlag, extV, extVV, extV2, extVV2, marker='-', msize=15, clr='green'):
    p = []
    lw = 2
    w = 500
    h = 500
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'
    tablePairs = list(itt.combinations(tables, 2))
    variablePairs = list(itt.combinations(variables, 2))
    extVPairs = list(itt.combinations(extV, 2))
    extVVPairs = list(itt.combinations(extVV, 2))
    extV2Pairs = list(itt.combinations(extV2, 2))
    extVV2Pairs = list(itt.combinations(extVV2, 2))
    for i in range(len(tablePairs)):
        t1, y1, y_std1 = TS.timeSeries(tablePairs[i][0], variablePairs[i][0], startDate, endDate, lat1, lat2, lon1, lon2, extVPairs[i][0], extVVPairs[i][0], extV2Pairs[i][0], extVV2Pairs[i][0])
        t2, y2, y_std2 = TS.timeSeries(tablePairs[i][1], variablePairs[i][1], startDate, endDate, lat1, lat2, lon1, lon2, extVPairs[i][1], extVVPairs[i][1], extV2Pairs[i][1], extVV2Pairs[i][1])
        if exportDataFlag:
            exportData(t1, y1, y_std1, t2, y2, y_std2, tablePairs[i][0], variablePairs[i][0], tablePairs[i][1], variablePairs[i][1], lat1, lat2, lon1, lon2, extVPairs[i][0], extVVPairs[i][0], extV2Pairs[i][0], extVV2Pairs[i][0], extVPairs[i][1], extVVPairs[i][1], extV2Pairs[i][1], extVV2Pairs[i][1])
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
        p1.xaxis.axis_label = variablePairs[i][0] + ' [' + db.getVar(tablePairs[i][0], variablePairs[i][0]).iloc[0]['Unit'] + ']'
        p1.yaxis.axis_label = variablePairs[i][1] + ' [' + db.getVar(tablePairs[i][1], variablePairs[i][1]).iloc[0]['Unit'] + ']'
        leg = variablePairs[i][0] + ' / ' + variablePairs[i][1]
        if extVPairs[i][0] != None:
            leg = leg + '   ' + extVPairs[i][0] + ': ' + ( '%d' % float(extVVPairs[i][0]) ) 
            if tablePairs[i][0].find('Pisces') != -1:
                leg = leg + ' ' + 'm'
        if extVPairs[i][1] != None:
            leg = leg + '   ' + extVPairs[i][1] + ': ' + ( '%d' % float(extVVPairs[i][1]) ) 
            if tablePairs[i][1].find('Pisces') != -1:
                leg = leg + ' ' + 'm'
        fill_alpha = 0.6        
        #if tablePairs[i][0].find('Pisces') != -1 or tablePairs[i][1].find('Pisces') != -1:
        #    fill_alpha = 0.3
        cr = p1.circle(y1, y2, fill_color="grey", hover_fill_color="firebrick", fill_alpha=fill_alpha, hover_alpha=0.6, line_color=None, hover_line_color="white", legend=leg, size=msize)
        #p1.line(y1, y2, line_color=clr, line_width=lw, legend=leg)
        p1.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))    
        p.append(p1)
    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    output_file(dirPath + fname + ".html", title="XY")
    show(column(p))
    return


tables = sys.argv[1].split(',')      #tables
variables = sys.argv[2].split(',')      #variables
startDate = sys.argv[3]      #dt1
endDate = sys.argv[4]      #dt2
#startDate = sys.argv[3].split('T')[0]      #dt1
#endDate = sys.argv[4].split('T')[0]      #dt2

lat1 = float(sys.argv[5])      #lat1
lat2 = float(sys.argv[6])      #lat2
lon1 = float(sys.argv[7])      #lon1
lon2 = float(sys.argv[8])      #lon2
fname = sys.argv[9]
exportDataFlag = bool(int(sys.argv[10]))
extV = sys.argv[11].split(',')       #extra condition: var_name
extVV = sys.argv[12].split(',')       #extra condition: var_val
extV2 = sys.argv[13].split(',')       #extra condition: var_name
extVV2 = sys.argv[14].split(',')       #extra condition: var_val



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
plotXY(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, exportDataFlag, extV, extVV, extV2, extVV2)
toc = time.clock()
print('Fetch time: %2.2f s' % (toc-tic))
