import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import db
import climatology as clim
import subset
from datetime import datetime, timedelta
import time
from math import pi
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.models import DatetimeTickFormatter
from bokeh.palettes import all_palettes
from bokeh.models import HoverTool
from bokeh.embed import components

def iterative(table):
    it = False
    if table.find('tblDarwin') != -1:
        it = True
    if table.find('tblPisces') != -1:
        it = True
    return it


def exportData(z, y, yErr, table, variable, date1, date2, lat1, lat2, lon1, lon2, fname):
    df = pd.DataFrame()    
    df['depth'] = z
    df[variable] = y
    df[variable+'_std'] = yErr
    if db.isClimatology(table):
        df['month1'] = clim.timeToMonth(date1)  
        df['month2'] = clim.timeToMonth(date2)  
    else:
        df['time1'] = date1
        df['time2'] = date2
    df['lat1'] = lat1
    df['lat2'] = lat2
    df['lon1'] = lon1
    df['lon2'] = lon2
    dirPath = 'data/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    path = dirPath + fname + '_' + table + '_' + variable + '.csv'
    df.to_csv(path, index=False)    
    return


def depthProfile_iterative(table, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag):
    if db.isClimatology(table) and db.hasField(table, 'month'):
        m1 = clim.timeToMonth(dt1)
        m2 = clim.timeToMonth(dt2)
        if m2>m1:
            timesteps = range(m1, m2+1)
        else:
            timesteps = range(m2, m1+1)
        timesteps = ['2016-%2.2d-01' % m for m in timesteps]    
    else:        
        delta = datetime.strptime(dt2, '%Y-%m-%d') - datetime.strptime(dt1, '%Y-%m-%d')
        timesteps = [(datetime.strptime(dt1, '%Y-%m-%d') + timedelta(days=x)).strftime('%Y-%m-%d') for x in range(delta.days+1)]

    zs, ys, y_stds = [], [], []
    for dt in timesteps:
        df = subset.depthProfile(table, field, dt, dt, lat1, lat2, lon1, lon2, depth1, depth2)
        if len(df[field]) < 1:
            continue
        zs.append(df['depth'])
        ys.append(df[field])
        y_stds.append(df[field + '_std'])

    depth = np.mean( np.stack(zs, axis=0), axis=0 )
    y = np.mean( np.stack(ys, axis=0), axis=0 )
    y_std = np.mean( np.stack(y_stds, axis=0), axis=0 )

    if exportDataFlag:
        exportData(depth, y, y_std, table, field, dt1, dt2, lat1, lat2, lon1, lon2, fname)    
    return depth, y, y_std


def depthProfile(table, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag):
    df = subset.depthProfile(table, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)
    if exportDataFlag:
        exportData(df['depth'], df[field], df[field + '_std'], table, field, dt1, dt2, lat1, lat2, lon1, lon2, fname)    
    return df['depth'], df[field], df[field + '_std']


def plotDepthProfile(tables, variables, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag, marker='-', msize=25, clr='orangered'):
    p = []
    lw = 2
    w = 800
    h = 400
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'
    for i in range(len(tables)):
        if not db.hasField(tables[i], 'depth'):
            continue
        if not iterative(tables[i]):    
            depths, y, yErr = depthProfile(tables[i], variables[i], dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)
        else:    
            depths, y, yErr = depthProfile_iterative(tables[i], variables[i], dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
        #p1.xaxis.axis_label = 'Depth'
        p1.yaxis.axis_label = variables[i] + ' [' + db.getVar(tables[i], variables[i]).iloc[0]['Unit'] + ']'
        leg = variables[i]
        cr = p1.circle(depths, y, fill_color="grey", hover_fill_color="firebrick", fill_alpha=0.25, hover_alpha=0.3, line_color=None, hover_line_color="white", legend=leg, size=msize)
        p1.line(depths, y, line_color=clr, line_width=lw, legend=leg)
        p1.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))
        p.append(p1)
    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    output_file(dirPath + fname + ".html", title="Depth Profile")
    show(column(p))    
    return


def main():
    tables = sys.argv[1].split(',')      
    variables = sys.argv[2].split(',')      
    dt1 = sys.argv[3]      
    dt2 = sys.argv[4]
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

    if float(depth1)>float(depth2):
        temp = depth1
        depth1 = depth2
        depth2 = temp

    #tic = time.clock()
    plotDepthProfile(tables, variables, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)
    #toc = time.clock()
    #print('Fetch time: %2.2f s' % (toc-tic))


if __name__ == '__main__':
    main()   