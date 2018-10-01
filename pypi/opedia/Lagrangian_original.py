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
   


def prepareQuery(t, lat, lon):
    table = 'tblAltimetry_REP'
    u, v = 'ugos', 'vgos' 
    Xres, Yres = 0.25/2, 0.25/2
    args = (u, v, table, t, lat, Yres, lon, Xres, lat, lon)
    query = "SELECT [time], lat, lon, %s AS u, %s AS v FROM %s WHERE "
    query = query + "[time]='%s' AND "
    query = query + "ABS(lat-(%f))<=%f AND ABS(lon-(%f))<=%f "
    #query = query + "AND %s IS NOT NULL AND %s IS NOT NULL "
    query = query + "ORDER BY ABS(lat-(%f)), ABS(lon-(%f))"
    query = query % args
    return query


def weightedMean(df, lat, lon):
    u, v = 0, 0
    df['r'] = np.power(np.power(df['lat']-lat, 2) + np.power(df['lon']-lon, 2), 0.5)
    n = len(df)
    U, V, R = np.array(df['u']), np.array(df['v']), np.array(df['r'])  
    totalW = 0
    for i in range(n):
        if R[i] != 0:
            totalW = totalW + 1/R[i]
        else:
            return U[i], V[i]          
    for i in range(n):        
        u = u + U[i]/R[i]    
        v = v + V[i]/R[i]
    u = u/totalW    
    v = v/totalW  
    return u, v


def interpolateUV(t, lat, lon):
    query = prepareQuery(t, lat, lon)
    df = db.dbFetch(query)        
    df = pd.DataFrame.from_records(df, columns=['time', 'lat', 'lon', 'u', 'v'])
    n = len(df)
    u, v = 0, 0
    if n == 1:
        u, v = np.array(df['u'])[0], np.array(df['v'])[0]
    else:
        u, v = weightedMean(df, lat, lon)            
    if u == None:
        u = 0
    if v == None:
        v = 0
    return u, v


def propagate(direction, startDate, endDate, lat, lon, fmt, dt):
    def cond(direction, startDate, endDate, t):
        if direction==1:
            res = t<=endDate
        elif direction==-1:
            res = t>=startDate
        return res

    dx = 111180 * np.cos(lat*np.pi/180)
    dy = 111180

    ts, lats, lons = np.array([]), np.array([]), np.array([])
    startDate = datetime.strptime(startDate, fmt)
    endDate = datetime.strptime(endDate, fmt)
    if endDate < startDate:
        swap = startDate
        startDate = endDate
        endDate = swap

    if direction==1:
        t = startDate
    elif direction==-1:
        t = endDate

    ts = np.append(ts, t)
    lats = np.append(lats, lat)
    lons = np.append(lons, lon) 
    
    while cond(direction, startDate, endDate, t):  
        ##### interpolate flowfield at particle's location
        u, v = interpolateUV(t.strftime(fmt), lat, lon)
        ##### advection
        lon = lon + direction*dt*u / dx
        lat = lat + direction*dt*v / dy
        t = t + timedelta(seconds=direction*dt)
        #### update trajectory
        ts = np.append(ts, t)
        lats = np.append(lats, lat)
        lons = np.append(lons, lon)     
    return ts, lats, lons


def dumpTrackShape(lats, lons, fname):
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
    path = dirPath + 'Tracer.csv'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)    
    df.to_csv(path, index=False)    
    return


def plotAlongTrack(dt, fmt, tables, variables, track, spMargin, extV, extVV, extV2, extVV2, exportDataFlag, fname, marker='-', msize=30, clr='purple'):
    p = []
    #fmt = '%Y-%m-%d %H:%M:%S'
    dt = dt/60         # time resolution (minutes)
    loadedTrack = pd.DataFrame(track)
    lw = 2
    w = 800
    h = 400
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'
    for i in tqdm(range(len(tables))):
        ts, ys, y_stds = [], np.array([]), np.array([])
        for j in tqdm(range(len(track))):
            startDate = track.iloc[j]['time'].strftime(fmt)
            endDate = startDate
            lat1 = float(track.iloc[j]['lat']) - spMargin
            lat2 = float(track.iloc[j]['lat']) + spMargin
            lon1 = float(track.iloc[j]['lon']) - spMargin
            lon2 = float(track.iloc[j]['lon']) + spMargin           
            t, y, y_std = TS.timeSeries(tables[i], variables[i], startDate, endDate, lat1, lat2, lon1, lon2, extV[i], extVV[i], extV2[i], extVV2[i], fmt=fmt, dt=dt)
            ts.append(track.iloc[j]['time'])
            ys = np.append(ys, y[0])            
            y_stds = np.append(y_stds, y_std[0])
        loadedTrack = appendVar(loadedTrack, ts, ys, y_stds, variables[i], extV[i], extVV[i], extV2[i], extVV2[i])            
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
        #p1.xaxis.axis_label = 'Time'
        p1.yaxis.axis_label = variables[i] + ' [' + db.getVar(tables[i], variables[i]).iloc[0]['Unit'] + ']'
        leg = 'Along Tracer Track ' + variables[i]
        if extV[i] != None:
            leg = leg + '   ' + extV[i] + ': ' + ( '%d' % float(extVV[i]) ) 
            if tables[i].find('Pisces') != -1:
                leg = leg + ' ' + 'm'
        fill_alpha = 0.07        
        if tables[i].find('Pisces') != -1:
            fill_alpha = 0.3
        cr = p1.circle(ts, ys, fill_color="grey", hover_fill_color="firebrick", fill_alpha=fill_alpha, hover_alpha=0.3, line_color=None, hover_line_color="white", legend=leg, size=msize)
        p1.line(ts, ys, line_color=clr, line_width=lw, legend=leg)
        p1.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))
        p1.xaxis.formatter=DatetimeTickFormatter(
                hours=["%d %B %Y"],
                days=["%d %B %Y"],
                months=["%d %B %Y"],
                years=["%d %B %Y"],
            )
        p1.xaxis.major_label_orientation = pi/4
        p.append(p1)

    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)    
    output_file(dirPath + fname + ".html", title="Lagrangian")
    show(column(p))
    if exportDataFlag:
        exportData(loadedTrack, ts, ys, y_stds, tables[i], variables[i], spMargin, extV[i], extVV[i], extV2[i], extVV2[i])    
    print('')
    return













fmt='%Y-%m-%d'

dt = int(sys.argv[1])           # time step (day seconds)
direction = int(sys.argv[2])    # integration direction (forward/backward in time)
startDate = sys.argv[3]
endDate = sys.argv[4]
lat0 = float(sys.argv[5])
lon0 = float(sys.argv[6])
shapeFlag = bool(int(sys.argv[7]))
colocateFlag = bool(int(sys.argv[8]))

if shapeFlag or colocateFlag:
    ts, lats, lons = propagate(direction, startDate, endDate, lat0, lon0, fmt, dt)

if shapeFlag:                       # make shapefile for the tracer's trajectory
    import geopandas as gpd
    from shapely.geometry import Point 
    ### shapefile params
    shapeFname = sys.argv[9]
    ##########################
    dumpTrackShape(lats, lons, shapeFname)

if colocateFlag:                    # colocate the tracer's trajectory on varialble fields
    #### colocalization params
    exportDataFlag = bool(int(sys.argv[10]))
    spMargin = float(sys.argv[11])         #spatial margin 
    tables = sys.argv[12].split(',')
    variables = sys.argv[13].split(',')   
    extV = sys.argv[14].split(',')        #extra condition: var_name
    extVV = sys.argv[15].split(',')       #extra condition: var_val
    extV2 = sys.argv[16].split(',')       #extra condition: var_name
    extVV2 = sys.argv[17].split(',')      #extra condition: var_val  
    fname = sys.argv[18]
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

    df = pd.DataFrame()
    df['time'] = ts
    df['lat'] = lats
    df['lon'] = lons
    plotAlongTrack(dt, fmt, tables, variables, df, spMargin, extV, extVV, extV2, extVV2, exportDataFlag, fname, marker='-', msize=30, clr='darkturquoise')








