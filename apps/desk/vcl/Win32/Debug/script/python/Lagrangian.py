import sys
import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import db
import matplotlib.pyplot as plt

import geopandas as gpd
from shapely.geometry import Point    


def prepareQuery(t, lat, lon):
    table = 'tblAltimetry_REP'
    u, v = 'ugos', 'vgos' 
    Xres, Yres = 0.25/2, 0.25/2
    args = (u, v, table, t, lat, Yres, lon, Xres, lat, lon)
    query = "SELECT [time], lat, lon, %s AS u, %s AS v FROM %s WHERE "
    query = query + "[time]='%s' AND "
    query = query + "ABS(lat-(%f))<=%f AND ABS(lon-(%f))<=%f "
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
    return u, v


def propagate(startDate, endDate, lat, lon, fmt, dt):
    dx = 111180 * np.cos(lat*np.pi/180)
    dy = 111180
    dir = 1

    ts, lats, lons = np.array([]), np.array([]), np.array([])
    startDate = datetime.strptime(startDate, fmt)
    endDate = datetime.strptime(endDate, fmt)
    t = startDate

    ts = np.append(ts, t)
    lats = np.append(lats, lat)
    lons = np.append(lons, lon) 
    while t<=endDate:  
        ##### interpolate flowfield at particle's location
        u, v = interpolateUV(t.strftime(fmt), lat, lon)
        ##### advection
        lon = lon + dir*dt*u / dx
        lat = lat + dir*dt*v / dy
        t = t + timedelta(seconds=dt)
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



dt = 3600 * 24  # time step (day seconds)
fmt='%Y-%m-%d'
startDate = '2015-01-01'
endDate = '2015-01-10'
lat0 = 26
lon0 = -158
fname = 'tracer'




dt = int(sys.argv[1])  # time step (day seconds)
startDate = sys.argv[2]
endDate = sys.argv[3]
lat0 = float(sys.argv[4])
lon0 = float(sys.argv[5])
fname = sys.argv[6]
fmt='%Y-%m-%d'


ts, lats, lons = propagate(startDate, endDate, lat0, lon0, fmt, dt)
dumpTrackShape(lats, lons, fname)






