import sys
import os
sys.path.append(os.path.dirname(__file__))
import numpy as np
import pandas as pd
from scipy.interpolate import griddata
import db
import subset
from common import getPalette, getBounds
import climatology as clim
from datetime import datetime, timedelta
import time
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.palettes import all_palettes
from bokeh.models import LinearColorMapper, BasicTicker, ColorBar
from bokeh.embed import components
import jupyterInline as jup
if jup.jupytered():
    from tqdm import tqdm_notebook as tqdm
else:
    from tqdm import tqdm



def exportData(df, path):
    df.to_csv(path, index=False)    
    return


def sectionMap(tables, variabels, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag):
    data, lats, lons, subs, frameVars = [], [], [], [], []
    xs, ys, zs = [], [], []
    for i in tqdm(range(len(tables)), desc='overall'):
        if not db.hasField(tables[i], 'depth'):
            continue        
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
                
                xs.append(lons)
                ys.append(lats)
                zs.append(depths)

                frameVars.append(variabels[i])
                subs.append(sub)

    bokehSec(data=data, subject=subs, fname=fname, ys=ys, xs=ys, zs=zs, variabels=frameVars)
    return


def regulate(lat, lon, depth, data):
    depth = -1* depth 
    deltaZ = np.min( np.abs( depth - np.roll(depth, -1) ) )
    newDepth =  np.arange(np.min(depth), np.max(depth), deltaZ)        

    if len(lon) > len(lat):
        lon1, depth1 = np.meshgrid(lon, depth)
        lon2, depth2 = np.meshgrid(lon, newDepth)
        lon1 = lon1.ravel()
        lon1 = list(lon1[lon1 != np.isnan])
        depth1 = depth1.ravel()
        depth1 = list(depth1[depth1 != np.isnan])
        data = data.ravel()
        data = list(data[data != np.isnan])
        data = griddata((lon1, depth1), data, (lon2, depth2), method='linear')
    else:   
        lat1, depth1 = np.meshgrid(lat, depth)
        lat2, depth2 = np.meshgrid(lat, newDepth)
        lat1 = lat1.ravel()
        lat1 = list(lat1[lat1 != np.isnan])
        depth1 = depth1.ravel()
        depth1 = list(depth1[depth1 != np.isnan])
        data = data.ravel()
        data = list(data[data != np.isnan])
        data = griddata((lat1, depth1), data, (lat2, depth2), method='linear')

    depth = -1* depth 
    return data




def bokehSec(data, subject, fname, ys, xs, zs, variabels):
    TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
    w = 1000
    h = 500
    p = []
    data_org = list(data)
    for ind in range(len(data_org)):
        data = data_org[ind]
        lon = xs[ind]
        lat = ys[ind]
        depth = zs[ind]      
        
        bounds = getBounds(variabels[ind])
        bounds = (None, None)
        paletteName = getPalette(variabels[ind], 10)

        if bounds[0]==None:
            color_mapper = LinearColorMapper(palette=paletteName)
        else:   
            color_mapper = LinearColorMapper(palette=paletteName, low=bounds[0], high=bounds[1])     

        if len(lon) > len(lat):
            p1 = figure(tools=TOOLS, toolbar_location="above", title=subject[ind], plot_width=w, plot_height=h, x_range=(np.min(lon), np.max(lon)), y_range=(-np.max(depth), -np.min(depth)))
            data = np.nanmean(data, axis=0)
            data = np.transpose(data)
            data = np.squeeze(data)
            p1.xaxis.axis_label = 'Longitude'
            data = regulate(lat, lon, depth, data)
            p1.image(image=[data], color_mapper=color_mapper, x=np.min(lon), y=-np.max(depth), dw=np.max(lon)-np.min(lon), dh=np.max(depth)-np.min(depth))
        else:
            p1 = figure(tools=TOOLS, toolbar_location="above", title=subject[ind], plot_width=w, plot_height=h, x_range=(np.min(lat), np.max(lat)), y_range=(-np.max(depth), -np.min(depth)))
            data = np.nanmean(data, axis=1)
            data = np.transpose(data)
            data = np.squeeze(data)
            p1.xaxis.axis_label = 'Latitude'      
            data = regulate(lat, lon, depth, data)
            p1.image(image=[data], color_mapper=color_mapper, x=np.min(lat), y=-np.max(depth), dw=np.max(lat)-np.min(lat), dh=np.max(depth)-np.min(depth))


        p1.yaxis.axis_label = 'depth [m]'
        color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                        label_standoff=12, border_line_color=None, location=(0,0))
        p1.add_layout(color_bar, 'right')
        p.append(p1)
    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    if not inline:      ## if jupyter is not the caller
        output_file(dirPath + fname + ".html", title="Section Map")
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