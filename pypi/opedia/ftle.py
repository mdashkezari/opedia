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
import matplotlib.pyplot as plt
from tqdm import tqdm

   
def plot_single_hist(data, clr='m', labelx='', labely='', leg='', yscale='linear', store_path='', bincount=50):   
    if len(filter(None, data)) < 1:
        return
    if np.isnan(np.nansum(data)):   # if all values are nans
        return
    plt.clf()	
    bins = np.linspace(np.nanmin(data), np.nanmax(data), bincount)
    lw = 1

    ss = len(data)
    data=np.nan_to_num(data)

    plt.hist(data, bins=bins, color=clr, histtype='step', linewidth=lw, alpha=1)
    plt.hist(data, bins=bins, color=clr, label=[leg + str(', Sample Size: ') + str(ss)], histtype='stepfilled', alpha=0.25)
    if len(labelx) > 0:
        plt.xlabel(labelx)
    if len(labely) > 0:
        plt.ylabel(labely)
    if len(leg) > 0:
        le = plt.legend()
        le.set_frame_on(False)
    plt.gca().set_yscale(yscale)    
    plt.axis([None, None, 0, None])
    plt.tight_layout()
    plt.show(block=True)
    #if len(store_path) > 0:
    #    plt.savefig(store_path, format='png', dpi=300, transparent=plot_transparency)
    return


def prepareQuery(table, startDate, endDate, lat1, lat2, lon1, lon2, ftleField, ftleValue):
    args = (table, startDate, endDate, lat1, lat2, lon1, lon2, ftleField, ftleValue)
    query = "SELECT [time], lat, lon FROM %s WHERE "
    query = query + "[time]>='%s' AND [time]<='%s' AND "
    query = query + "lat>=%f AND lat<=%f AND "
    query = query + "lon>=%f AND lon<=%f AND "
    query = query + "%s>=%f "
    query = query + "ORDER BY [time], lat, lon"
    query = query % args
    return query


def getFronts(table, startDate, endDate, lat1, lat2, lon1, lon2, ftleField, ftleValue):
    query = prepareQuery(table, startDate, endDate, lat1, lat2, lon1, lon2, ftleField, ftleValue)
    df = db.dbFetch(query)        
    df = pd.DataFrame.from_records(df, columns=['time', 'lat', 'lon'])    
    return df


def match(geomTable, bkgTable, startDate, enDate, lat1, lat2, lon1, lon2, extV, extVV, ftleField, ftleValue, bkgField, margin):       
    ######### Stored Procedure Query ##########
    query = 'EXEC uspftleMatch ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
    args = [geomTable, ftleField, ftleValue, bkgTable, bkgField, startDate, endDate, str(lat1), str(lat2), str(lon1), str(lon2), str(margin), extV, extVV]
    df = db.dbFetchStoredProc(query, args)
    df = pd.DataFrame.from_records(df, columns=['time', 'lat', 'lon', bkgField])
    ###########################################   
    return df


def bkg(geomTable, bkgTable, startDate, enDate, lat1, lat2, lon1, lon2, extV, extVV, ftleField, ftleValue, bkgField, margin):       
    ######### Stored Procedure Query ##########
    query = 'EXEC uspftleBkg ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
    args = [geomTable, ftleField, ftleValue, bkgTable, bkgField, startDate, endDate, str(lat1), str(lat2), str(lon1), str(lon2), str(margin), extV, extVV]
    df = db.dbFetchStoredProc(query, args)
    df = pd.DataFrame.from_records(df, columns=['time', 'lat', 'lon', bkgField])
    ###########################################   
    return df


def match_temptable(geomTable, bkgTable, startDate, lat1, lat2, lon1, lon2, ftleField, ftleValue, bkgField, margin):
    args = (geomTable, startDate, lat1, lat2, lon1, lon2, ftleField, ftleValue, bkgTable, startDate, lat1, lat2, lon1, lon2, bkgField, margin, margin)
    query = ''
    query = query + "DROP TABLE IF EXISTS #tblGeometry; "
    query = query + "DROP TABLE IF EXISTS #tblBkg; "
    query = query + "SELECT * INTO #tblGeometry FROM %s WHERE [time]='%s' AND lat>=%f AND lat<=%f AND lon>=%f AND lon<=%f AND %s>=%f; "
    query = query + "SELECT * INTO #tblBkg FROM %s WHERE [time]='%s' AND lat>=%f AND lat<=%f AND lon>=%f AND lon<=%f; "
    query = query + "SELECT [#tblBkg].[time], [#tblBkg].lat, [#tblBkg].lon, [#tblBkg].%s FROM #tblBkg WHERE EXISTS "
    query = query + "(SELECT [#tblGeometry].[time], [#tblGeometry].lat, [#tblGeometry].lon FROM #tblGeometry WHERE "
    query = query + "[#tblGeometry].[time]=[#tblBkg].[time] AND ABS([#tblGeometry].lat-([#tblBkg].lat))<=%f AND ABS([#tblGeometry].lon-([#tblBkg].lon))<=%f)"
    query = query % args
    df = db.dbFetch(query)        
    df = pd.DataFrame.from_records(df, columns=['time', 'lat', 'lon'])    
    return df


def dumpFrontShape(lats, lons, fname):
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
    path = dirPath + 'Front.csv'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)    
    df.to_csv(path, index=False)    
    return

def colocalize(ftleTable, ftleValue, tables, variables, startDate, lat1, lat2, lon1, lon2, spMargin, extV, extVV, extV2, extVV2, exportDataFlag, fname, marker='-'):
    def spectrum(ind):
        colList = ['grey', 'purple', 'darkturquoise', 'black', 'red', 'blue', 'pink', 'lime', 'green', 'orange']
        ind = ind % len(colList)
        col = colList[ind]
        return col

    fmt='%Y-%m-%d'
    dt = 24*60
    msize=10
    p = []
    
    lw = 2
    w = 800
    h = 400
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'
    for i in tqdm(range(len(tables))):
        df = match(ftleTable, tables[i], startDate, endDate, lat1, lat2, lon1, lon2, extV[i], extVV[i], ftleField, ftleValue, variables[i], spMargin)
        if i==0:
            loadedFTLE = pd.DataFrame(df)    
        ts, ys, y_stds = df.time, df[variables[i]], ''
        '''
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
        '''
        if i>0:
            loadedFTLE = appendVar(loadedFTLE, ts, ys, y_stds, variables[i], extV[i], extVV[i], extV2[i], extVV2[i]) 
        #plot_single_hist(ys, clr='m', labelx='', labely='', leg='', yscale='linear', store_path='', bincount=50)

        ys = ys[~np.isnan(ys)]     # remove nans
        hist, edges = np.histogram(ys, density=False, bins=50)
        if bkgComparison:
            ########## get backgrounf distribution (not matched with fronts)
            dfBkg = bkg(ftleTable, tables[i], startDate, endDate, lat1, lat2, lon1, lon2, extV[i], extVV[i], ftleField, ftleValue, variables[i], spMargin)
            ysBkg = dfBkg[variables[i]]
            ysBkg = ysBkg[~np.isnan(ysBkg)]     # remove nans
            histBkg, edgesBkg = np.histogram(ysBkg, density=False, bins=50)
            ################################################################
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
        p1.yaxis.axis_label = 'Density'
        p1.xaxis.axis_label = variables[i] + ' [' + db.getVar(tables[i], variables[i]).iloc[0]['Unit'] + ']'
        leg = variables[i]
        if extV[i] != None:
            leg = leg + '   ' + extV[i] + ': ' + ( '%d' % float(extVV[i]) ) 
            if tables[i].find('Pisces') != -1:
                leg = leg + ' ' + 'm'
        fill_alpha = 0.9   
        cr = p1.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="dodgerblue", line_color=None, hover_fill_color="firebrick", fill_alpha=fill_alpha, hover_alpha=0.7, hover_line_color="white", legend=leg + ' on fronts')
        if bkgComparison:        
            cr = p1.quad(top=histBkg, bottom=0, left=edgesBkg[:-1], right=edgesBkg[1:], fill_color="purple", line_color=None, hover_fill_color="firebrick", fill_alpha=fill_alpha, hover_alpha=0.7, hover_line_color="white", legend='background')        
        p1.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='mouse'))
        p.append(p1)

    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)    
    output_file(dirPath + fname + ".html", title="Front")
    show(column(p))
    if exportDataFlag:
        exportData(loadedFTLE, ts, ys, y_stds, tables[i], variables[i], spMargin, extV[i], extVV[i], extV2[i], extVV2[i])    
    print('')
    return df














ftleTable = sys.argv[1]
ftleField = sys.argv[2]
ftleValue = float(sys.argv[3])
bkgComparison = bool(int(sys.argv[4]))
startDate = sys.argv[5]
endDate = sys.argv[6]
lat1 = float(sys.argv[7])
lat2 = float(sys.argv[8])
lon1 = float(sys.argv[9])
lon2 = float(sys.argv[10])
shapeFlag = bool(int(sys.argv[11]))
colocateFlag = bool(int(sys.argv[12]))

if shapeFlag:                       # make shapefile for the tracer's trajectory
    import geopandas as gpd
    from shapely.geometry import Point 
    cores = getFronts(ftleTable, startDate, endDate, lat1, lat2, lon1, lon2, ftleField, ftleValue)
    ### shapefile params
    shapeFname = sys.argv[13]
    ##########################
    dumpFrontShape(cores.lat, cores.lon, shapeFname)

if colocateFlag:                    # colocate the tracer's trajectory on varialble fields
    #### colocalization params
    exportDataFlag = bool(int(sys.argv[14]))
    spMargin = float(sys.argv[15])         #spatial margin 
    tables = sys.argv[16].split(',')
    variables = sys.argv[17].split(',')   
    
    extV = sys.argv[18].split(',')        #extra condition: var_name
    extVV = sys.argv[19].split(',')       #extra condition: var_val
    extV2 = sys.argv[20].split(',')       #extra condition: var_name
    extVV2 = sys.argv[21].split(',')      #extra condition: var_val  
    fname = sys.argv[22]
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

    df = colocalize(ftleTable, ftleValue, tables, variables, startDate, lat1, lat2, lon1, lon2, spMargin, extV, extVV, extV2, extVV2, exportDataFlag, fname, marker='-')
    dumpFrontShape(df.lat, df.lon, shapeFname)








