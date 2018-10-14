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


def match(geomTable, bkgTable, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, ftleField, ftleValue, bkgField, margin, bkgFlag):       
    query = 'EXEC uspftleMatch ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
    args = [geomTable, ftleField, str(ftleValue), bkgTable, bkgField, startDate, endDate, str(lat1), str(lat2), str(lon1), str(lon2), str(depth1), str(depth2), str(margin), bkgFlag]
    df = db.dbFetchStoredProc(query, args)
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
    import geopandas as gpd
    from shapely.geometry import Point 
    df = pd.DataFrame()
    df['lat'] = lats
    df['lon'] = lons
    df['geometry'] = df.apply(lambda x: Point((float(x.lon), float(x.lat))), axis=1)
    df = gpd.GeoDataFrame(df, geometry='geometry')
    dirPath = 'shape/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)       
    df.to_file(dirPath + '%s.shp' % fname, driver='ESRI Shapefile')    
    
    ## dump the shape file content in a csv file (this will be used by macos app)
    df.to_csv(dirPath + 'shape.csv', index=False)
    return

def appendVar(track, t, y, yErr, variable):
    df = track
    df[variable] = y
    df[variable+'_std'] = yErr
    return df


def exportData(cruiseTrack, t, y, yErr, table, variable, margin):
    df = cruiseTrack
    df['margin'] = margin
    dirPath = 'data/'
    path = dirPath + 'Front.csv'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)    
    df.to_csv(path, index=False)    
    return

def colocalize(ftleTable, ftleField, ftleValue, tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, spMargin, exportDataFlag, fname, bkgComparison, marker='-'):
    fmt='%Y-%m-%d'
    dt = 24*60
    msize=10
    p = []
    lw = 2
    w = 800
    h = 400
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'
    for i in tqdm(range(len(tables))):
        df = match(ftleTable, tables[i], startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, ftleField, ftleValue, variables[i], spMargin, '0')
        if len(df)<1:
            continue

        if i==0:
            loadedFTLE = pd.DataFrame(df)    
        ts, ys, y_stds = df[df.columns[0]], df[variables[i]], ''
        if i>0:
            loadedFTLE = appendVar(loadedFTLE, ts, ys, y_stds, variables[i]) 
        #plot_single_hist(ys, clr='m', labelx='', labely='', leg='', yscale='linear', store_path='', bincount=50)

        ys = ys[~np.isnan(ys)]     # remove nans
        hist, edges = np.histogram(ys, density=False, bins=50)
        if bkgComparison:
            ########## get backgrounf distribution (not matched with fronts)
            dfBkg = match(ftleTable, tables[i], startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, ftleField, ftleValue, variables[i], spMargin, '1')
            ysBkg = dfBkg[variables[i]]
            ysBkg = ysBkg[~np.isnan(ysBkg)]     # remove nans
            histBkg, edgesBkg = np.histogram(ysBkg, density=False, bins=50)
            ################################################################
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
        p1.yaxis.axis_label = 'Density'
        p1.xaxis.axis_label = variables[i] + ' [' + db.getVar(tables[i], variables[i]).iloc[0]['Unit'] + ']'
        leg = variables[i]
        fill_alpha = 0.4   
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
        exportData(loadedFTLE, ts, ys, y_stds, tables[i], variables[i], spMargin)    
    print('')
    return df













def main():
    ftleTable = sys.argv[1]                                     # argument1: ftle table name
    ftleField = sys.argv[2]                                     # argument2: ftle (type) field name
    ftleValue = float(sys.argv[3])                              # argument3: lower bound ftle value
    bkgComparison = bool(int(sys.argv[4]))                      # argument4: < 1 > to compare with the backgound values
    startDate = sys.argv[5]                                     # argument5: within the delimited space-time (start date)    
    endDate = sys.argv[6]                                       # argument6: within the delimited space-time (end date) 
    lat1 = float(sys.argv[7])                                   # argument7: within the delimited space-time (start lat) 
    lat2 = float(sys.argv[8])                                   # argument8: within the delimited space-time (end lat)     
    lon1 = float(sys.argv[9])                                   # argument9: within the delimited space-time (start lon) 
    lon2 = float(sys.argv[10])                                  # argument10: within the delimited space-time (end lon)     
    shapeFlag = bool(int(sys.argv[11]))                         # argument11: < 1 > to generate ftle shape file; < 0 > ignore 
    colocateFlag = bool(int(sys.argv[12]))                      # argument12: < 1 > to colocalize selected variables along the ftle ridges; < 0 > ignore
    fname = sys.argv[13]                                        # argument13: figure filename (and/or shape filename)


    if shapeFlag or colocateFlag:
        cores = getFronts(ftleTable, startDate, endDate, lat1, lat2, lon1, lon2, ftleField, ftleValue)


    # make shapefile for the ftle ridges
    if shapeFlag:                       
        try:
            dumpFrontShape(cores.lat, cores.lon, fname)
        except Exception as e:              
            print("The following error occurred while generating the ftle shape file: ")
            print(e)


    # colocate the ftle ridges on varialble fields
    if colocateFlag:                   
        tables = sys.argv[14].split(',')                        # argument14: comma-separated list of varaible table names
        variables = sys.argv[15].split(',')                     # argument15: comma-separated list of variable names  
        spatialTolerance = float(sys.argv[16])                  # argument16: colocalizer spatial tolerance (+/- degrees)
        exportDataFlag = bool(int(sys.argv[17]))                # argument17: < 1 > export the ftle ridges and colocalized data on disk; < 0 > ignore 
        depth1 = 0
        depth2 = 5

        df = colocalize(ftleTable, ftleField, ftleValue, tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, spatialTolerance, exportDataFlag, fname, bkgComparison, marker='-')
        
        try:
            dumpFrontShape(df.lat, df.lon, fname)
        except Exception as e:              
            print("The following error occurred while generating the colocalized ftle shape file: ")
            print(e)



if __name__ == '__main__':
    main()






