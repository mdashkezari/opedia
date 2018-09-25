
from docopt import docopt
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import db
import subset
from datetime import datetime, timedelta
import time
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.palettes import all_palettes
from bokeh.models import LinearColorMapper, BasicTicker, ColorBar
from bokeh.embed import components



def getBounds(varName):
    bounds = (None, None)
    if varName.find('Fe') != -1:
        bounds = (0, 1e-4)
    elif varName.find('chl') != -1:
        bounds = (0, 5e-1)
    elif varName.find('CHL') != -1:
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
    elif varName.find('vort') != -1:
        bounds = (-4e-6, 4e-6)          
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
    elif varName.find('CHL') != -1:
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


def RegionalMap(tables, variabels, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag):
    data, lats, lons, subs, frameVars = [], [], [], [], []
    for i in range(len(tables)):
        df = subset.spaceTime(tables[i], variabels[i], dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)
        if len(df) < 1:
            continue

        ############### export retrieved data ###############
        if exportDataFlag:      
            dirPath = 'data/'
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)     
            exportPath = dirPath + 'RM_' + tables[i] + '_' + variabels[i]               
            exportData(df, path=exportPath + '.csv')
        #####################################################

        times = df[df.columns[0]].unique()  
        lats = df.lat.unique()
        lons = df.lon.unique()
        shape = (len(lats), len(lons))
       
        depths, hours =  [None], [None]
        if 'depth' in df.columns:
            depths = df.depth.unique()
        if 'hour' in df.columns:
            hours = df.hour.unique()

        unit =  ' [' + db.getVar(tables[i], variabels[i]).iloc[0]['Unit'] + ']'
        for t in times:
            for h in hours:
                for z in depths:
                    frame = df[df[df.columns[0]] == t]
                    sub = variabels[i] + unit + ', ' + df.columns[0] + ': ' + str(t) 
                    if h != None:
                        frame = frame[frame['hour'] == h]
                        sub = sub + ', hour: ' + str(h) + 'hr'
                    if z != None:
                        frame = frame[frame['depth'] == z] 
                        sub = sub + ', depth: %2.2f' % z + ' [m]'  
                    try:    
                        shot = frame[variabels[i]].values.reshape(shape)
                    except Exception as e:
                        continue    
                    data.append(shot)
                    frameVars.append(variabels[i])
                    subs.append(sub)

    bokehGM(data=data, subject=subs, fname=fname, lat=lats, lon=lons, variabels=frameVars)
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
    RegionalMap(tables.split(','), variables.split(','), dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)



if __name__ == '__main__':
    main()
    

