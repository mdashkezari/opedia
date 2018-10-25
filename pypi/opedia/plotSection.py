import sys
import os
sys.path.append(os.path.dirname(__file__))
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import db
import subset
import climatology as clim
from datetime import datetime, timedelta
import time
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.palettes import all_palettes
from bokeh.models import LinearColorMapper, BasicTicker, ColorBar
from bokeh.embed import components
import jupyterInline as jup



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


def prepareSectionQuery(table, field, date1, lat1, lat2, lon1, lon2, depth1, depth2):
    if clim.isClimatology(table, field):
        query = "SELECT [month], lat, lon, depth, %s FROM %s WHERE "
        query = query + "[month]=%d AND "
    else:
        query = "SELECT [time], lat, lon, depth, %s FROM %s WHERE "
        query = query + "[time]='%s' AND "
    query = query + "lat BETWEEN %f AND %f AND "
    query = query + "lon  BETWEEN %f AND %f AND "
    query = query + "depth BETWEEN %f AND %f "
    query = query + "ORDER BY lat, lon, depth "

    if clim.isClimatology(table, field):
        month = clim.timeToMonth(date1)
        query = query % (field, table, month, float(lat1), float(lat2), float(lon1), float(lon2), float(depth1), float(depth2))
    else:
        query = query % (field, table, date1, float(lat1), float(lat2), float(lon1), float(lon2), float(depth1), float(depth2))
    return query


def exportData(df, path):
    df.to_csv(path, index=False)    
    return


def sectionMap(tables, variabels, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag):
    data, lats, lons, subs, frameVars = [], [], [], [], []
    for i in range(len(tables)):
        if not db.hasField(tables[i], 'depth'):
            continue        
        #query = prepareSectionQuery(tables[i], variabels[i], dt, lat1, lat2, lon1, lon2, depth1, depth2)
        #df = db.dbFetch(query)

        df = subset.section(tables[i], variabels[i], dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)
        if len(df) < 1:
            continue

        ############### export retrieved data ###############
        if exportDataFlag:      # export data
            dirPath = 'data/'
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)                
            exportData(df, path=dirPath + fname + '_' + tables[i] + '_' + variabels[i] + '.csv')
        #####################################################

        times = df[df.columns[0]].unique() 
        lats = df.lat.unique()
        lons = df.lon.unique()
        depths = df.depth.unique()
        shape = (len(lats), len(lons), len(depths))

        hours =  [None]
        if 'hour' in df.columns:
            hours = df.hour.unique()

        unit =  ' [' + db.getVar(tables[i], variabels[i]).iloc[0]['Unit'] + ']'

        for t in times:
            for h in hours:
                frame = df[df[df.columns[0]] == t]
                sub = variabels[i] + unit + ', ' + df.columns[0] + ': ' + str(t) 
                if h != None:
                    frame = frame[frame['hour'] == h]
                    sub = sub + ', hour: ' + str(h) + 'hr'
                try:    
                    shot = frame[variabels[i]].values.reshape(shape)
                except Exception as e:
                    continue    
                data.append(shot)
                frameVars.append(variabels[i])
                subs.append(sub)

    bokehSec(data=data, subject=subs, fname=fname, lat=lats, lon=lons, depth=depths, variabels=frameVars)
    return


def bokehSec(data, subject, fname, lat, lon, depth, variabels):
    TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
    w = 1000
    h = 500
    p = []
    data_org = list(data)
    for ind in range(len(data_org)):
        data = data_org[ind]
        bounds = getBounds(variabels[ind])
        paletteName = getPalette(variabels[ind])
        if bounds[0]==None:
            color_mapper = LinearColorMapper(palette=paletteName)
        else:   
            color_mapper = LinearColorMapper(palette=paletteName, low=bounds[0], high=bounds[1])     


        if len(lon) > len(lat):
            p1 = figure(tools=TOOLS, toolbar_location="above", title=subject[ind], plot_width=w, plot_height=h, x_range=(np.min(lon), np.max(lon)), y_range=(np.min(depth), np.max(depth)))
            data = np.nanmean(data, axis=0)
            data = np.transpose(data)
            data = np.squeeze(data)
            p1.xaxis.axis_label = 'Longitude'
            p1.image(image=[data], color_mapper=color_mapper, x=np.min(lon), y=np.max(depth), dw=np.max(lon)-np.min(lon), dh=np.max(depth)-np.min(depth))
        else:
            p1 = figure(tools=TOOLS, toolbar_location="above", title=subject[ind], plot_width=w, plot_height=h, x_range=(np.min(lat), np.max(lat)), y_range=(np.min(depth), np.max(depth)))
            data = np.nanmean(data, axis=1)
            data = np.transpose(data)
            data = np.squeeze(data)
            p1.xaxis.axis_label = 'Latitude'
            '''
            if ind==0:
                data1 = data
            if ind==1:
                data = data / data1
            '''
            p1.image(image=[data], color_mapper=color_mapper, x=np.min(lat), y=np.min(depth), dw=np.max(lat)-np.min(lat), dh=np.max(depth)-np.min(depth))

        p1.yaxis.axis_label = 'depth [m]'
        color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                        label_standoff=12, border_line_color=None, location=(0,0))
        p1.add_layout(color_bar, 'right')
        p.append(p1)
    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    if not inline:      ## if jupyter is not the caller
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

    sectionMap(tables.split(','), variables.split(','), dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)



inline = jup.inline()   # check if jupyter is calling this script
if __name__ == '__main__':
    main()    