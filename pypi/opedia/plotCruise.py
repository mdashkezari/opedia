import os
import sys
sys.dont_write_bytecode = True
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import db
import timeSeries as TS
from datetime import datetime, date, timedelta
import time
from math import pi
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.models import DatetimeTickFormatter
from bokeh.palettes import all_palettes
from bokeh.models import HoverTool
from bokeh.embed import components
import itertools as itt


def removeNA(df, subset):
    df = df.dropna(subset=subset)
    return df

def indexTime(df, frm='%Y-%m-%d %H:%M:%S'):
    df['time'] = pd.to_datetime(df['time'], format=frm)
    df.index = df['time']
    del df['time']
    return df

def CruiseQuery(table, cruise):
    query = "SELECT [time], lat, lon FROM %s WHERE "
    query = query + "cruise='%s' "
    query = query % (table, cruise)
    return query

def getCruiseTrack(DB_Cruise, source, cruise):
    df = None
    if DB_Cruise:
        query = CruiseQuery(source, cruise)
        df = db.dbFetch(query)
    else:
        df = pd.read_csv(source)    
    return df

def resample(df, resampTau):
    if resampTau != '0':
        df = indexTime(df)
        df = df.resample(resampTau).mean()
        df.reset_index(level=0, inplace=True)
        df = removeNA(df, ['lat', 'lon'])        
    return df

def dumpCruiseShape(dfShape, source, cruise, fname):
    import geopandas as gpd
    from shapely.geometry import Point 
    del dfShape['time']  
    dfShape['geometry'] = dfShape.apply(lambda x: Point((float(x.lon), float(x.lat))), axis=1)
    dfShape = gpd.GeoDataFrame(dfShape, geometry='geometry')
    dirPath = 'shape/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)       
    dfShape.to_file(dirPath + '%s.shp' % fname, driver='ESRI Shapefile')    
    
    ## dump the shape file content in a csv file (this will be used by macos app)
    dfShape.to_csv(dirPath + 'shape.csv', index=False)
    return

def resampleToTimeStep(resampTau):
    if resampTau != '0':
        unit = resampTau[-1]
        sp = resampTau.split(unit)
        factor = sp[0]
        if len(factor) == 0:
            factor = 1
        else:
            factor = int(factor)
        if unit == 'T':
            dt = 1
        elif unit == 'H':
            dt = 60
        elif unit == 'D':
            dt = 24*60
        dt = factor * dt            
    else:
        dt = None    
    return dt

def appendVar(cruiseTrack, t, y, yErr, variable):
    df = cruiseTrack
    df[variable] = y
    df[variable+'_std'] = yErr
    return df

def exportData(cruiseTrack, t, y, yErr, cruiseName, margin):
    df = cruiseTrack
    df['margin'] = margin
    dirPath = 'data/'
    path = dirPath + 'Cruise_' + cruiseName + '.csv'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)    
    df.to_csv(path, index=False)    
    return


def plotAlongTrack(tables, variables, cruiseName, resampTau, track, spMargin, depth1, depth2, fname, exportDataFlag, marker='-', msize=30, clr='purple'):
    p = []
    fmt = '%Y-%m-%d %H:%M:%S'
    dt = resampleToTimeStep(resampTau)         # time step (minutes)
    loadedTrack = pd.DataFrame(track)
    lw = 2
    w = 800
    h = 400
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'
    for i in range(len(tables)):
        ts, ys, y_stds = [], np.array([]), np.array([])
        for j in range(len(track)):
            startDate = track.iloc[j]['time'].strftime(fmt)
            endDate = startDate
            lat1 = float(track.iloc[j]['lat']) - spMargin
            lat2 = float(track.iloc[j]['lat']) + spMargin
            lon1 = float(track.iloc[j]['lon']) - spMargin
            lon2 = float(track.iloc[j]['lon']) + spMargin           
            t, y, y_std = TS.timeSeries(tables[i], variables[i], startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fmt=fmt, dt=dt)
            ts.append(track.iloc[j]['time'])
            ys = np.append(ys, y[0])            
            y_stds = np.append(y_stds, y_std[0])
        loadedTrack = appendVar(loadedTrack, ts, ys, y_stds, variables[i])       
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
        #p1.xaxis.axis_label = 'Time'
        p1.yaxis.axis_label = variables[i] + ' [' + db.getVar(tables[i], variables[i]).iloc[0]['Unit'] + ']'
        leg = 'Along Track (' + cruiseName + ') ' + variables[i]
        fill_alpha = 0.3        
        cr = p1.circle(ts, ys, fill_color="grey", hover_fill_color="firebrick", fill_alpha=fill_alpha, hover_alpha=0.3, line_color=None, hover_line_color="white", legend=leg, size=msize)
        p1.line(ts, ys, line_color=clr, line_width=lw, legend=leg)
        p1.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))
        p1.xaxis.formatter=DatetimeTickFormatter(
                hours=["%d %B %Y %H:%M:%S"],
                days=["%d %B %Y %H:%M:%S"],
                months=["%d %B %Y %H:%M:%S"],
                years=["%d %B %Y %H:%M:%S"],
            )
        p1.xaxis.major_label_orientation = pi/4
        p.append(p1)
    
    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)    
    output_file(dirPath + fname + ".html", title="Along Track")
    show(column(p))

    ############### export retrieved data ###############
    if exportDataFlag:
        exportData(loadedTrack, ts, ys, y_stds, cruiseName, spMargin)   
    #####################################################     
    return loadedTrack

def mutualTrends(loadedTrack, tables, variables, cruise, msize=20):
    if len(variables)<2:
        print('Error: at least 2 variables are needed to plot mutual trends.')
        return
    fname = 'MutualTrends_AlongTrack_' + cruise    
    tablePairs = list(itt.combinations(tables, 2))
    variablePairs = list(itt.combinations(variables, 2))
    p = []
    lw = 2
    w = 500
    h = 500
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'
    for i in range(len(tablePairs)):
        t1, y1, y_std1 = loadedTrack['time'], loadedTrack[variablePairs[i][0]], loadedTrack[variablePairs[i][0] + '_std']
        t2, y2, y_std2 = loadedTrack['time'], loadedTrack[variablePairs[i][1]], loadedTrack[variablePairs[i][1] + '_std']
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
        p1.xaxis.axis_label = variablePairs[i][0] + ' [' + db.getVar(tablePairs[i][0], variablePairs[i][0]).iloc[0]['Unit'] + ']'
        p1.yaxis.axis_label = variablePairs[i][1] + ' [' + db.getVar(tablePairs[i][1], variablePairs[i][1]).iloc[0]['Unit'] + ']'
        leg = variablePairs[i][0] + ' / ' + variablePairs[i][1] + ' (%s) ' % cruise        
        fill_alpha = 0.6        
        cr = p1.circle(y1, y2, fill_color="grey", hover_fill_color="firebrick", fill_alpha=fill_alpha, hover_alpha=0.6, line_color=None, hover_line_color="white", legend=leg, size=msize)
        #p1.line(y1, y2, line_color=clr, line_width=lw, legend=leg)        
        p1.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))    
        p.append(p1)
    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    output_file(dirPath + fname + ".html", title="Mutual Trends")
    show(column(p))
    return



def main():
    DB_Cruise = bool(int(sys.argv[1]))                 # argument1: < 1 > if cruise trajectory already exists in DB. < 0 > if arbiturary cruise file (e.g. virtual) 
    source = sys.argv[2]                               # argument2: cruise table name or path to csv trajectory file    
    cruise = sys.argv[3]                               # argument3: cruise name, or file name of the csv trajectory file     
    resampTau = sys.argv[4]                            # argument4: resample the cruise trajectory making trajectory time-space resolution coarser: e.g. '6H' (6 hourly), '3T' (3 minutes), ... '0' (ignore)  
    shapeFlag = bool(int(sys.argv[5]))                 # argument5: < 1 > to generate cruise trajectory shape file; < 0 > ignore
    colocateFlag = bool(int(sys.argv[6]))              # argument6: < 1 > to colocalize selected variables along the cruise trajectory; < 0 > ignore
    fname = sys.argv[7]                                # argument7: figure filename (and/or shape filename)
    
    if shapeFlag or colocateFlag:
        df = getCruiseTrack(DB_Cruise, source, cruise)
        df = resample(df, resampTau) 

    ## generates cruise track shapefile 
    if shapeFlag:    
        try:            
            dumpCruiseShape(df.copy(), source, cruise, fname)
        except Exception as e:              
            print("The following error occurred while generating the cruise shape file: ")
            print(e)


    ## generates along track plot
    if colocateFlag: 
        tables = sys.argv[8].split(',')                # argument8: comma-separated list of varaible table names                                     
        variables = sys.argv[9].split(',')             # argument9: comma-separated list of variable names
        spatialTolerance = float(sys.argv[10])         # argument10: colocalizer spatial tolerance (+/- degrees) 
        depth1 = 0
        depth2 = 5        
        exportDataFlag = bool(int(sys.argv[11]))       # argument11: < 1 > export the cruise trajectory and colocalized data on disk; < 0 > ignore 
        loadedTrack = plotAlongTrack(tables, variables, cruise, resampTau, df, spatialTolerance, depth1, depth2, fname, exportDataFlag, marker='-', msize=30, clr='darkturquoise')
        mutualTrends(loadedTrack, tables, variables, cruise)









if __name__ == "__main__":
    main()