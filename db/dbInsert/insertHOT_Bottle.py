import sys
sys.path.append('../../config')
import config_vault as cfgv
sys.path.append('../../lib')
import dateLib as dl
sys.path.append('../')
import dbCore as dc
import os
import netcdf as nc
import numpy as np
import pandas as pd
import pyodbc
import pandas.io.sql as sql
from datetime import datetime
import time
import math
import insertPrep as ip

def stationLoc(station):
    ## Are the below lat/lon values correct? has any one of them changed over years?
    ## http://hahana.soest.hawaii.edu/hot/locations.html
    if station == 'aloha':
        station_lat = 22.75
        station_lon = -158
    elif station == 'hale':    
        station_lat = 22.458
        station_lon = -158.13
    elif station == 'kahe':    
        station_lat = 22.343
        station_lon = -158.273
    elif station == 'kaena':    
        station_lat = 21.847
        station_lon = -158.363
    elif station == 'whots50':    
        station_lat = 22.75
        station_lon = -157.9
    elif station == 'whots52':    
        station_lat = 22.67
        station_lon = -157.95
    else:
        print('ERROR: unknown station name: %s ' % station)
        sys.exit()    

    return station_lat, station_lon

def formatDate_Columns(df, dateLabels, fmt='%m%d%y'):
    date_len = 6    
    for dateLabel in dateLabels:
        date_ind = df.columns.get_loc(dateLabel)
        df[dateLabel] =df[dateLabel].astype(int)
        df[dateLabel] =df[dateLabel].astype(str)
        df[dateLabel] = df[dateLabel].str.strip()
        for i in range(len(df)):        
            df.iloc[i, date_ind] = ('0'*(date_len-len(df.iloc[i, date_ind]))) + df.iloc[i, date_ind]
        df[dateLabel] =  pd.to_datetime(df[dateLabel], format=fmt)
    return df


def makeBulkBottle_HOT(station):
    path = cfgv.rep_hot_raw + 'bottle_%s.csv' % station    
    missingValue = -9 
    df = pd.read_csv(path)   
    if ' ' in df.columns:
        df.drop(' ', axis=1, inplace=True)
    df = df.drop(df.index[[0]])   ## remove the units row    
    df.columns = df.columns.str.replace(' ','')   
    df = df.apply(pd.to_numeric)
    df = df.replace(missingValue, '')
    df = ip.removeMissings(['date'], df) 
    formatDate_Columns(df, ['date'])
    station_lat, station_lon = stationLoc(station)
    df['lat'] = station_lat
    df['lon'] = station_lon
    return df

    
    
def combine(dfs):
    prefix = 'bot_hot'
    df = pd.concat(dfs).reset_index(drop=True)
    df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df.to_csv(export_path, index=False)
    return export_path



def bulkInsertBottle_HOT(tableName):
    dataTitle = 'HOT_Bottle'
    print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
    try:
        bulkPath = ''
        stations = ['aloha', 'kahe', 'kaena', 'hale', 'whots50', 'whots52']
        dfs = []
        for station in stations:
            dfs.append(makeBulkBottle_HOT(station))
        bulkPath = combine(dfs) 
        dc.bulkInsert(bulkPath, tableName)
    finally:
        if bulkPath != '':
            os.remove(bulkPath)    
    print('%s  Done' % datetime.today())
    return



tableName = 'tblHOT_Bottle'
bulkInsertBottle_HOT(tableName)

