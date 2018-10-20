import sys
import os
sys.path.append(os.path.dirname(__file__))
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


try:
    import jupyterInline
except Exception as e:
    print("Error while loading jupyter inline!")
    print(e)


def exportData(t1, y1, yErr1, t2, y2, yErr2, table1, variable1, table2, variable2, lat1, lat2, lon1, lon2, depth1, depth2):
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
    if db.hasField(table1, 'depth') or db.hasField(table2, 'depth'):
        df['depth1'] = depth1
        df['depth2'] = depth2
    dirPath = 'data/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    path = dirPath + 'XY_' + table1 + '_' + variable1 + '_vs_' + table2 + '_' + variable2 + '.csv'
    df.to_csv(path, index=False)    
    return

def plotXY(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag, marker='-', msize=15, clr='green'):
    p = []
    lw = 2
    w = 500
    h = 500
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'
    tablePairs = list(itt.combinations(tables, 2))
    variablePairs = list(itt.combinations(variables, 2))
    for i in range(len(tablePairs)):
        t1, y1, y_std1 = TS.timeSeries(tablePairs[i][0], variablePairs[i][0], startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2)
        t2, y2, y_std2 = TS.timeSeries(tablePairs[i][1], variablePairs[i][1], startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2)
        if exportDataFlag:
            exportData(t1, y1, y_std1, t2, y2, y_std2, tablePairs[i][0], variablePairs[i][0], tablePairs[i][1], variablePairs[i][1], lat1, lat2, lon1, lon2, depth1, depth2)

        if len(t1)<1 or len(y1)<1 or len(t2)<1 or len(y2)<1:
            continue
        if (len(t1)-len(t2) != 0) or (len(y1)-len(y2) != 0):   
            continue
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
        p1.xaxis.axis_label = variablePairs[i][0] + ' [' + db.getVar(tablePairs[i][0], variablePairs[i][0]).iloc[0]['Unit'] + ']'
        p1.yaxis.axis_label = variablePairs[i][1] + ' [' + db.getVar(tablePairs[i][1], variablePairs[i][1]).iloc[0]['Unit'] + ']'
        leg = variablePairs[i][0] + ' / ' + variablePairs[i][1]
        fill_alpha = 0.3       
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


def main():
    tables = sys.argv[1].split(',')      
    variables = sys.argv[2].split(',')      
    startDate = sys.argv[3]      
    endDate = sys.argv[4]      
    #startDate = sys.argv[3].split('T')[0]      
    #endDate = sys.argv[4].split('T')[0]      
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

    #tic = time.clock()
    plotXY(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)
    #toc = time.clock()
    #print('Fetch time: %2.2f s' % (toc-tic))





if __name__ == '__main__':
    main()