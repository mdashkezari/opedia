"""
Author: Mohammad Dehghani Ashkezari <mdehghan@uw.edu>

Date: Summer 2017

Function:
Retrieve eddy trajectories within a predefined space-time domain. 
The trajectories may then be colocalized with other data sets.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import db
import timeSeries as TS
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


def prepareQuery(table, startDate, endDate, lat1, lat2, lon1, lon2):
    args = (table, startDate, endDate, lat1, lat2, lon1, lon2)
    query = "SELECT track, [time], lat, lon FROM %s WHERE "
    query = query + "[time]>='%s' AND [time]<='%s' AND "
    query = query + "lat>=%f AND lat<=%f AND "
    query = query + "lon>=%f AND lon<=%f "
    query = query + "ORDER BY track, [time]"
    query = query % args
    return query


def getEddies(table, startDate, endDate, lat1, lat2, lon1, lon2):
    query = prepareQuery(table, startDate, endDate, lat1, lat2, lon1, lon2)
    df = db.dbFetch(query)        
    df = pd.DataFrame.from_records(df, columns=['track', 'time', 'lat', 'lon'])    
    return df


def dumpEddyShape(lats, lons, fname):
    dirPath = 'shape/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)       
    df = pd.DataFrame()
    df['lat'] = lats
    df['lon'] = lons
    ## dump the shape file content in a csv file (this will be used by macos app)
    df.to_csv(dirPath + 'shape.csv', index=False)

    try:
        import geopandas as gpd
        from shapely.geometry import Point 
        df['geometry'] = df.apply(lambda x: Point((float(x.lon), float(x.lat))), axis=1)
        df = gpd.GeoDataFrame(df, geometry='geometry')
        df.to_file(dirPath + '%s.shp' % fname, driver='ESRI Shapefile')    
    except Exception as e:
        print('dumpEddyShape Error: ')    
        print(e)   
    return

def appendVar(track, t, y, yErr, variable):
    df = track
    df[variable] = y
    df[variable+'_std'] = yErr
    return df


def exportData(cruiseTrack, t, y, yErr, table, variable, margin):
    df = cruiseTrack
    df['margin'] = margin
    dirPath = 'data/'
    path = dirPath + 'EddyCentric.csv'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)    
    df.to_csv(path, index=False)    
    return

def findFirstAndLast(arr, x) :
    first = -1
    last = -1
    n = len(arr)
    for i in range(0,n) :
        if (x != arr[i]) :
            continue
        if (first == -1) :
            first = i
        last = i
    return first, last     

def colocalize(tables, variables, eddy, spMargin, depth1, depth2, exportDataFlag, fname, marker='-'):
    def spectrum(ind):
        colList = ['grey', 'purple', 'darkturquoise', 'black', 'red', 'blue', 'pink', 'lime', 'green', 'orange']
        ind = ind % len(colList)
        col = colList[ind]
        return col

    fmt='%Y-%m-%d'
    dt = 24*60
    msize=10
    p = []
    loadedEddy = pd.DataFrame(eddy)
    tracks = eddy.track.unique()
    lw = 2
    w = 800
    h = 400
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'
    for i in tqdm(range(len(tables)), desc='overall'):
        ts, ys, y_stds, track_ids = [], np.array([]), np.array([]), np.array([])
        for j in tqdm(range(len(eddy)), desc=variables[i]):
            startDate = eddy.iloc[j]['time']
            endDate = startDate
            lat1 = float(eddy.iloc[j]['lat']) - spMargin
            lat2 = float(eddy.iloc[j]['lat']) + spMargin
            lon1 = float(eddy.iloc[j]['lon']) - spMargin
            lon2 = float(eddy.iloc[j]['lon']) + spMargin           
            t, y, y_std = TS.timeSeries(tables[i], variables[i], startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fmt=fmt, dt=dt)
            ts.append( datetime.strptime(str(eddy.iloc[j]['time']), fmt) )
            ys = np.append(ys, y[0])            
            y_stds = np.append(y_stds, y_std[0])
            track_ids = np.append(track_ids, eddy.iloc[j]['track'])
        loadedEddy = appendVar(loadedEddy, ts, ys, y_stds, variables[i])            
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
        #p1.xaxis.axis_label = 'Time'
        p1.yaxis.axis_label = variables[i] + ' [' + db.getVar(tables[i], variables[i]).iloc[0]['Unit'] + ']'
        leg = 'Eddy Centric ' + variables[i]
        fill_alpha = 0.7

        for ind in range(len(tracks)):
            track = tracks[ind]
            first, last = findFirstAndLast(track_ids, track)
            filCol = spectrum(ind)
            cr = p1.circle(ts[first:last+1], ys[first:last+1], fill_color=filCol, hover_fill_color="firebrick", fill_alpha=fill_alpha, hover_alpha=0.3, line_color=None, hover_line_color="white", legend=leg, size=msize)
            p1.line(ts[first:last+1], ys[first:last+1], line_color=filCol, line_width=lw, legend=leg)           
        #p1.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))

        p1.xaxis.formatter=DatetimeTickFormatter(
                days=["%d %B %Y"],
                months=["%d %B %Y"],
                years=["%d %B %Y"],
            )
        p1.xaxis.major_label_orientation = pi/4
        p.append(p1)

    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)    
    if not inline:      ## if jupyter is not the caller
        output_file(dirPath + fname + ".html", title="Eddy")
    show(column(p))
    if exportDataFlag:
        exportData(loadedEddy, ts, ys, y_stds, tables[i], variables[i], spMargin)   
    print('')     
    return


def main():
    eddyTable = sys.argv[1]                                     # argument1: eddy table name
    startDate = sys.argv[2]                                     # argument2: eddy cores within the delimited space-time (start date)
    endDate = sys.argv[3]                                       # argument3: eddy cores within the delimited space-time (end date)   
    lat1 = float(sys.argv[4])                                   # argument4: eddy cores within the delimited space-time (start lat)
    lat2 = float(sys.argv[5])                                   # argument5: eddy cores within the delimited space-time (end lat)               
    lon1 = float(sys.argv[6])                                   # argument6: eddy cores within the delimited space-time (start lon)
    lon2 = float(sys.argv[7])                                   # argument7: eddy cores within the delimited space-time (end lon)
    shapeFlag = bool(int(sys.argv[8]))                          # argument8: < 1 > to generate eddy trajectory shape file; < 0 > ignore 
    colocateFlag = bool(int(sys.argv[9]))                       # argument9: < 1 > to colocalize selected variables along the eddy trajectories; < 0 > ignore
    fname = sys.argv[10]                                        # argument10: figure filename (and/or shape filename)

    if shapeFlag or colocateFlag:
        cores = getEddies(eddyTable, startDate, endDate, lat1, lat2, lon1, lon2)

    # make shapefile for the eddy trajectories
    if shapeFlag:                       
        try:
            dumpEddyShape(cores.lat, cores.lon, fname)
        except Exception as e:              
            print("The following error occurred while generating the eddy shape file: ")
            print(e)

    # colocate the eddy trajectories on varialble fields
    if colocateFlag:                    
        tables = sys.argv[11].split(',')                        # argument11: comma-separated list of varaible table names                          
        variables = sys.argv[12].split(',')                     # argument12: comma-separated list of variable names
        spatialTolerance = float(sys.argv[13])                  # argument13: colocalizer spatial tolerance (+/- degrees)  
        exportDataFlag = bool(int(sys.argv[14]))                # argument14: < 1 > export the eddy trajectories and colocalized data on disk; < 0 > ignore 
        depth1 = 0
        depth2 = 5        
        colocalize(tables, variables, cores, spatialTolerance, depth1, depth2, exportDataFlag, fname, marker='-')




inline = jup.inline()   # check if jupyter is calling this script
if __name__ == '__main__':
    main()


