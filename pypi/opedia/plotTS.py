import sys
import os
sys.path.append(os.path.dirname(__file__))
import numpy as np
import pandas as pd
import db
import common as com
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




def exportData(t, y, yErr, table, variable, lat1, lat2, lon1, lon2, depth1, depth2):
    df = pd.DataFrame()
    timeField = 'time'
    if db.isClimatology(table) and db.hasField(table, 'month'):
        timeField = 'month'
    df[timeField] = t
    df[variable] = y
    df[variable+'_std'] = yErr
    df['lat1'] = lat1
    df['lat2'] = lat2
    df['lon1'] = lon1
    df['lon2'] = lon2
    if db.hasField(table, 'depth'):
        df['depth1'] = depth1
        df['depth2'] = depth2
    dirPath = 'data/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    path = dirPath + 'TS_' + table + '_' + variable + '.csv'
    df.to_csv(path, index=False)    
    return



def plotTS(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag, marker='-', msize=20, clr='purple'):
    p = []
    lw = 2
    w = 800
    h = 400
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'
    for i in tqdm(range(len(tables)), desc='overall'):
        dt = com.temporalRes(tables[i])
        t, y, yErr = TS.timeSeries(tables[i], variables[i], startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fmt='%Y-%m-%d', dt=dt*24*60)
        if exportDataFlag:
            exportData(t, y, yErr, tables[i], variables[i], lat1, lat2, lon1, lon2, depth1, depth2)
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
        #p1.xaxis.axis_label = 'Time'
        p1.yaxis.axis_label = variables[i] + ' [' + db.getVar(tables[i], variables[i]).iloc[0]['Unit'] + ']'
        leg = variables[i]
        fill_alpha = 0.3        
        cr = p1.circle(t, y, fill_color="grey", hover_fill_color="firebrick", fill_alpha=fill_alpha, hover_alpha=0.3, line_color=None, hover_line_color="white", legend=leg, size=msize)
        p1.line(t, y, line_color=clr, line_width=lw, legend=leg)
        p1.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))
        if not db.isClimatology(tables[i]):
            p1.xaxis.formatter=DatetimeTickFormatter(
                    hours=["%d %B %Y"],
                    days=["%d %B %Y"],
                    months=["%d %B %Y"],
                    years=["%d %B %Y"],
                )
            p1.xaxis.major_label_orientation = pi/4
        elif db.hasField(tables[i], 'month'):
            p1.xaxis.axis_label = 'Month'

        #p1.xaxis.visible = False
        p.append(p1)
    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    if not inline:      ## if jupyter is not the caller
        output_file(dirPath + fname + ".html", title="TimeSeries")
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

    #tic = time.clock()
    plotTS(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)
    #toc = time.clock()
    #print('Fetch time: %2.2f s' % (toc-tic))





inline = jup.inline()   # check if jupyter is calling this script
if __name__ == '__main__':
    main()