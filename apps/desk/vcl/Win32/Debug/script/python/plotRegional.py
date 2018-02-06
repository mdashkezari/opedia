import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import db
from datetime import datetime, timedelta
import time
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.palettes import all_palettes
from bokeh.models import LinearColorMapper, BasicTicker, ColorBar
from bokeh.embed import components


def embedComponents(fname, data):
    f = open(fname, 'w')
    f.write(data)
    f.close()
    return

def prepareGMQuery(table, dt):
    query = "SELECT * FROM %s WHERE "
    query = query + "[time]='%s' ORDER BY lat, lon"
    query = query % (table, dt)
    return query


def getBounds(varName):
    bounds = (None, None)
    if varName.find('Fe') != -1:
        bounds = (0, 1e-4)
    elif varName.find('chl') != -1:
        bounds = (0, 5e-1)
    elif varName.find('O2') != -1:
        bounds = (200, 320)
    elif varName.find('PHYC') != -1:
        bounds = (0, 4)
    elif varName.find('PP') != -1:
        bounds = (0, 4e-2)
    elif varName.find('Si') != -1:
        bounds = (10, 30)
    elif varName.find('NO3') != -1:
        bounds = (0, 20)
    elif varName.find('PO4') != -1:
        bounds = (0, 1.5)
    elif varName.find('wind_stress') != -1:
        bounds = (0, 3e-1)
    elif varName.find('sst') != -1:
        bounds = (0, 32)          
    elif varName.find('sla') != -1:
        bounds = (-0.3, 0.3)          
    return bounds

def getPalette(varName):
    paletteName = 'RdBu11'
    if varName.find('Fe') != -1:
        paletteName = 'Viridis256'
    elif varName.find('O2') != -1:
        paletteName = 'Viridis256'
    elif varName.find('PHYC') != -1:
        paletteName = 'Viridis256'
    elif varName.find('PP') != -1:
        paletteName = 'Viridis256'
    elif varName.find('Si') != -1:
        paletteName = 'Viridis256'
    elif varName.find('NO3') != -1:
        paletteName = 'Viridis256'
    elif varName.find('PO4') != -1:
        paletteName = 'Viridis256'
    elif varName.find('chl') != -1:
        paletteName = 'Viridis256'
    elif varName.find('wind_stress') != -1:
        paletteName = 'Plasma256'
    elif varName.find('sst') != -1:
        paletteName = 'Inferno256'
    elif varName.find('sla') != -1:
        paletteName = 'RdBu11'
    return paletteName


def exportData(df, path):
    df.to_csv(path, index=False)    
    return


def RegionalMap(tables, variabels, dt, lat1, lat2, lon1, lon2, arg8, arg9, fname, exportDataFlag):
    '''
    ############# App-Level Query #############
    query = prepareGMQuery(table, dt)
    df = db.dbFetch(query)
    ###########################################
    '''

    ######### Stored Procedure Query ##########
    data = []
    subs = [] 
    for i in range(len(tables)):
        if arg8[i].find('ignore') != -1:
            arg8[i]=None
        if arg9[i].find('ignore') != -1:
            arg9[i]=None
    for i in range(len(tables)):
        args = [tables[i], variabels[i], dt, lat1, lat2, lon1, lon2, arg8[i], arg9[i]]
        query = 'EXEC uspRegionalMap ?, ?, ?, ?, ?, ?, ?, ?, ?'
        df = db.dbFetchStoredProc(query, args)        
        df = pd.DataFrame.from_records(df, columns=['time', 'lat', 'lon', variabels[i]])
        lat = df.lat.unique()
        lon = df.lon.unique()
        shape = (len(lat), len(lon))
        
        if tables[i].find('Vort') != -1: 
            data.append(np.transpose(df[variabels[i]].values.reshape(shape)))
        else:    
            data.append(df[variabels[i]].values.reshape(shape))
        
        unit =  ' [' + db.getVar(tables[i], variabels[i]).iloc[0]['Unit'] + ']'
        if arg8[i] != None:
            if tables[i].find('Wind') != -1:
                sub = variabels[i] + unit + ' ' + dt + ' ' + arg9[i] + 'H'
            if tables[i].find('Pisces') != -1:
                sub = variabels[i] + unit + ' ' + dt + ' Depth: ' + arg9[i] + ' m'
        else:
            sub = variabels[i] + unit + ' ' + dt    
        subs.append(sub)
        if exportDataFlag:      # export data
            dirPath = 'data/'
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)                
            exportData(df, path=dirPath + 'RM_' + tables[i] + '_' + variabels[i] + '.csv')
    bokehGM(data=data, subject=subs, fname=fname, lat=lat, lon=lon, variabels=variabels)
    return


def bokehGM(data, subject, fname, lat, lon, variabels):
    TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
    w = 1000
    h = 500
    p = []
    for ind in range(len(data)):
        p1 = figure(tools=TOOLS, toolbar_location="above", title=subject[ind], plot_width=w, plot_height=h, x_range=(np.min(lon), np.max(lon)), y_range=(np.min(lat), np.max(lat)))
        p1.xaxis.axis_label = 'Longitude'
        p1.yaxis.axis_label = 'Latitude'
        bounds = getBounds(variabels[ind])
        paletteName = getPalette(variabels[ind])
        if bounds[0]==None:
            color_mapper = LinearColorMapper(palette=paletteName)
        else:   
            color_mapper = LinearColorMapper(palette=paletteName, low=bounds[0], high=bounds[1])     
        p1.image(image=[data[ind]], color_mapper=color_mapper, x=np.min(lon), y=np.min(lat), dw=np.max(lon)-np.min(lon), dh=np.max(lat)-np.min(lat))
        color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                        label_standoff=12, border_line_color=None, location=(0,0))
        p1.add_layout(color_bar, 'right')
        p.append(p1)
    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    output_file(dirPath + fname + ".html", title="Regional Map")
    show(column(p))
    return



arg1 = sys.argv[1]      #tables
arg2 = sys.argv[2]      #variables
arg3 = sys.argv[3]      #dt
arg4 = sys.argv[4]      #lat1
arg5 = sys.argv[5]      #lat2
arg6 = sys.argv[6]      #lon1
arg7 = sys.argv[7]      #lon2
fname = sys.argv[8]
exportDataFlag = bool(int(sys.argv[9]))
arg8 = None
arg9 = None
if len(sys.argv)>11:
    arg8 = sys.argv[10]      #extra condition: var_name
    arg9 = sys.argv[11]      #extra condition: var_val

RegionalMap(arg1.split(','), arg2.split(','), arg3, arg4, arg5, arg6, arg7, arg8.split(','), arg9.split(','), fname, exportDataFlag)