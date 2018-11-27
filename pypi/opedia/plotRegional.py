
from docopt import docopt
import sys
import os
sys.path.append(os.path.dirname(__file__))
import numpy as np
import pandas as pd
import db
import subset
from common import getPalette, getBounds
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


def regionalMap(tables, variabels, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag):
    data, lats, lons, subs, frameVars = [], [], [], [], []
    for i in tqdm(range(len(tables)), desc='overall'):
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

    regionalMap(tables.split(','), variables.split(','), dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)


inline = jup.inline()   # check if jupyter is calling this script
if __name__ == '__main__':
    main()
    

