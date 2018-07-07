import sys
import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import db
import timeSeries as TS
import matplotlib.pyplot as plt
from math import pi
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.models import DatetimeTickFormatter
from bokeh.palettes import all_palettes
from bokeh.models import HoverTool
from bokeh.embed import components
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
    df = pd.DataFrame()
    df['lat'] = lats
    df['lon'] = lons
    df['geometry'] = df.apply(lambda x: Point((float(x.lon), float(x.lat))), axis=1)
    df = gpd.GeoDataFrame(df, geometry='geometry')
    dirPath = 'shape/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)       
    df.to_file(dirPath + '%s.shp' % fname, driver='ESRI Shapefile')    
    return

def appendVar(track, t, y, yErr, variable, extV, extVV, extV2, extVV2):
    df = track
    df[variable] = y
    df[variable+'_std'] = yErr
    if extV != None:
        df[extV] = extVV
    if extV2 != None:
        df[extV2] = extVV2
    return df


def exportData(cruiseTrack, t, y, yErr, table, variable, margin, extV, extVV, extV2, extVV2):
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

def colocalize(tables, variables, eddy, spMargin, extV, extVV, extV2, extVV2, exportDataFlag, fname, marker='-'):
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
    for i in tqdm(range(len(tables))):
        ts, ys, y_stds, track_ids = [], np.array([]), np.array([]), np.array([])
        for j in tqdm(range(len(eddy))):
            startDate = eddy.iloc[j]['time']
            endDate = startDate
            lat1 = float(eddy.iloc[j]['lat']) - spMargin
            lat2 = float(eddy.iloc[j]['lat']) + spMargin
            lon1 = float(eddy.iloc[j]['lon']) - spMargin
            lon2 = float(eddy.iloc[j]['lon']) + spMargin           
            t, y, y_std = TS.timeSeries(tables[i], variables[i], startDate, endDate, lat1, lat2, lon1, lon2, extV[i], extVV[i], extV2[i], extVV2[i], fmt=fmt, dt=dt)
            ts.append( datetime.strptime(eddy.iloc[j]['time'], fmt) )
            ys = np.append(ys, y[0])            
            y_stds = np.append(y_stds, y_std[0])
            track_ids = np.append(track_ids, eddy.iloc[j]['track'])
        loadedEddy = appendVar(loadedEddy, ts, ys, y_stds, variables[i], extV[i], extVV[i], extV2[i], extVV2[i])            
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
        #p1.xaxis.axis_label = 'Time'
        p1.yaxis.axis_label = variables[i] + ' [' + db.getVar(tables[i], variables[i]).iloc[0]['Unit'] + ']'
        leg = 'Eddy Centric ' + variables[i]
        if extV[i] != None:
            leg = leg + '   ' + extV[i] + ': ' + ( '%d' % float(extVV[i]) ) 
            if tables[i].find('Pisces') != -1:
                leg = leg + ' ' + 'm'
        fill_alpha = 0.7        
        if tables[i].find('Pisces') != -1:
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
    output_file(dirPath + fname + ".html", title="Eddy")
    show(column(p))
    if exportDataFlag:
        exportData(loadedEddy, ts, ys, y_stds, tables[i], variables[i], spMargin, extV[i], extVV[i], extV2[i], extVV2[i])   
    print('')     
    return














eddyTable = sys.argv[1]
startDate = sys.argv[2]
endDate = sys.argv[3]
lat1 = float(sys.argv[4])
lat2 = float(sys.argv[5])
lon1 = float(sys.argv[6])
lon2 = float(sys.argv[7])
shapeFlag = bool(int(sys.argv[8]))
colocateFlag = bool(int(sys.argv[9]))
cores = getEddies(eddyTable, startDate, endDate, lat1, lat2, lon1, lon2)

if shapeFlag:                       # make shapefile for the tracer's trajectory
    import geopandas as gpd
    from shapely.geometry import Point 
    ### shapefile params
    shapeFname = sys.argv[10]
    ##########################
    dumpEddyShape(cores.lat, cores.lon, shapeFname)

if colocateFlag:                    # colocate the tracer's trajectory on varialble fields
    #### colocalization params
    exportDataFlag = bool(int(sys.argv[11]))
    spMargin = float(sys.argv[12])         #spatial margin 
    tables = sys.argv[13].split(',')
    variables = sys.argv[14].split(',')   
    extV = sys.argv[15].split(',')        #extra condition: var_name
    extVV = sys.argv[16].split(',')       #extra condition: var_val
    extV2 = sys.argv[17].split(',')       #extra condition: var_name
    extVV2 = sys.argv[18].split(',')      #extra condition: var_val  
    fname = sys.argv[19]
    for i in range(len(tables)):
        if extV[i].find('ignore') != -1:
            extV[i]=None
        if extVV[i].find('ignore') != -1:
            extVV[i]=None
        if extV2[i].find('ignore') != -1:
            extV2[i]=None
        if extVV2[i].find('ignore') != -1:
            extVV2[i]=None
    #############################

    colocalize(tables, variables, cores, spMargin, extV, extVV, extV2, extVV2, exportDataFlag, fname, marker='-')








