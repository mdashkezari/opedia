
from docopt import docopt
import sys
import os
sys.path.append(os.path.dirname(__file__))
import numpy as np
from scipy.interpolate import griddata
import pandas as pd
import db
import subset
from dashboard import dashboardPanels
import common as com
from datetime import datetime, timedelta
import time
from math import pi
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.palettes import all_palettes
from bokeh.models import HoverTool, LinearColorMapper, BasicTicker, ColorBar, DatetimeTickFormatter
from bokeh.models.annotations import Title
from bokeh.embed import components
import jupyterInline as jup
if jup.jupytered():
    from tqdm import tqdm_notebook as tqdm
else:
    from tqdm import tqdm



def exportData(df, path):
    df.to_csv(path, index=False)    
    return


def structuredMap(df, table, variable, data, lats, lons, subs, frameTables, frameVars):
    times = df[df.columns[0]].unique()  
    lat = df.lat.unique()
    lon = df.lon.unique()
    shape = (len(lat), len(lon))
    
    depths, hours =  [None], [None]
    if 'depth' in df.columns:
        depths = df.depth.unique()
    if 'hour' in df.columns:
        hours = df.hour.unique()

    unit = com.getUnit(table, variable)
    for t in times:
        for h in hours:
            for z in depths:
                frame = df[df[df.columns[0]] == t]
                sub = variable + unit + ', ' + df.columns[0] + ': ' + str(t) 
                if h != None:
                    frame = frame[frame['hour'] == h]
                    sub = sub + ', hour: ' + str(h) + 'hr'
                if z != None:
                    frame = frame[frame['depth'] == z] 
                    sub = sub + ', depth: %2.2f' % z + ' [m]'  
                try:    
                    shot = frame[variable].values.reshape(shape)
                except Exception as e:
                    continue    
                lats.append(lat)
                lons.append(lon)
                data.append(shot)
                frameTables.append(table)
                frameVars.append(variable)
                subs.append(sub)
    return data, lats, lons, subs, frameTables, frameVars



def interpolatedMap(df, table, variable, data, lats, lons, subs, frameTables, frameVars):
    interpMethod = 'linear'
    times = df[df.columns[0]].sort_values().unique()  
    time_sub = df.columns[0] + ': ' + str(times[0]) + ' -- ' + str(times[-1])
    lat = np.array(df.lat)
    lon = np.array(df.lon)
    depths =  [None]
    depth_sub = ''
    if 'depth' in df.columns:
        depths = df.depth.sort_values().unique()    
        depth_sub = ', depth: %2.2f -- %2.2f' % (np.min(df.depth), np.max(df.depth)) + ' [m]'

    unit = com.getUnit(table, variable)
    sub = variable + unit + ', ' + time_sub
    sub = sub + depth_sub

    points = np.stack((lon, lat), axis=1)
    values = np.array(df[variable])

    # ################ uniform grid ################
    res_x, res_y = 0.1, 0.1    # in degrees
    lat_min, lat_max = np.min(df.lat) - res_y, np.max(df.lat) + res_y
    lon_min, lon_max = np.min(df.lon) - res_x, np.max(df.lon) + res_x
    x = np.arange(lon_min, lon_max, res_x)
    y = np.arange(lat_min, lat_max, res_y)

    # ############ grid on all data points #############
    # x = np.array(df.lon.sort_values().unique())
    # y = np.array(df.lat.sort_values().unique())

    grid_x, grid_y = np.meshgrid(x, y)
    interpData = griddata(points, values, (grid_x, grid_y), method=interpMethod)

    lats.append(lat)
    lons.append(lon)
    data.append(interpData)
    frameTables.append(table)
    frameVars.append(variable)
    subs.append(sub)
    return data, lats, lons, subs, frameTables, frameVars


def regionalMap(tables, variabels, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag):
    data, lats, lons, subs, frameTables, frameVars = [], [], [], [], [], []
    for i in tqdm(range(len(tables)), desc='overall'):
        df = subset.spaceTime(tables[i], variabels[i], dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)        
        if len(df) < 1:
            com.printTQDM('%d: No matching entry found: Table: %s, Variable: %s ' % (i+1, tables[i], variabels[i]), err=True )
            continue
        com.printTQDM('%d: %s retrieved (%s).' % (i+1, variabels[i], tables[i]), err=False)

        ############### export retrieved data ###############
        if exportDataFlag:      
            dirPath = 'data/'
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)     
            exportPath = dirPath + 'RM_' + tables[i] + '_' + variabels[i]               
            exportData(df, path=exportPath + '.csv')
        #####################################################

        if com.isGrid(tables[i], variabels[i]):
            data, lats, lons, subs, frameTables, frameVars = structuredMap(df, tables[i], variabels[i], data, lats, lons, subs, frameTables, frameVars)
        else:
            dashboardPanels(df, tables[i], variabels[i])
            # data, lats, lons, subs, frameTables, frameVars = interpolatedMap(df, tables[i], variabels[i], data, lats, lons, subs, frameTables, frameVars)
    
    bokehMap(data=data, subject=subs, fname=fname, lat=lats, lon=lons, tables=frameTables, variabels=frameVars)
    return




def bokehMap(data, subject, fname, lat, lon, tables, variabels):
    TOOLS="crosshair,pan,zoom_in,wheel_zoom,zoom_out,box_zoom,reset,save,"
    p = []
    for ind in range(len(data)):
        w, h = com.canvasRect(dw=np.max(lon[ind])-np.min(lon[ind]), dh=np.max(lat[ind])-np.min(lat[ind]))
        p1 = figure(tools=TOOLS, toolbar_location="right", title=subject[ind], plot_width=w, plot_height=h, x_range=(np.min(lon[ind]), np.max(lon[ind])), y_range=(np.min(lat[ind]), np.max(lat[ind])))
        p1.xaxis.axis_label = 'Longitude'
        p1.yaxis.axis_label = 'Latitude'
        unit = com.getUnit(tables[ind], variabels[ind])
        bounds = com.getBounds(variabels[ind])
        paletteName = com.getPalette(variabels[ind])
        low, high = bounds[0], bounds[1]
        if low == None:
            low, high = np.nanmin(data[ind].flatten()), np.nanmax(data[ind].flatten())
        color_mapper = LinearColorMapper(palette=paletteName, low=low, high=high)
        p1.image(image=[data[ind]], color_mapper=color_mapper, x=np.min(lon[ind]), y=np.min(lat[ind]), dw=np.max(lon[ind])-np.min(lon[ind]), dh=np.max(lat[ind])-np.min(lat[ind]))
        p1.add_tools(HoverTool(
            tooltips=[
                ('longitude', '$x'),
                ('latitude', '$y'),
                (variabels[ind]+unit, '@image'),
            ],
            mode='mouse'
        ))
        color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                        label_standoff=12, border_line_color=None, location=(0,0))
        p1.add_layout(color_bar, 'right')
        p.append(p1)

    if len(p) > 0:
        if not inline:      ## if jupyter is not the caller
            dirPath = 'embed/'
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)        
            output_file(dirPath + fname + ".html", title="Regional Map")
        show(column(p))
    return




def main():
    tables = sys.argv[1]      
    variables = sys.argv[2]      
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

    regionalMap(tables.split(','), variables.split(','), dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)


inline = jup.inline()   # check if jupyter is calling this script
if __name__ == '__main__':
    main()
    

