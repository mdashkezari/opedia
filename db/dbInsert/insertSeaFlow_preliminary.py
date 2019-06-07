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



def timeStampFormat(cruiseID):
    fmt = '%Y-%m-%dT%H:%M:%S+0000'

    if cruiseID in ['SCOPE_9', 'SCOPE_16', 'SCOPE_17', 'SCOPE_18', 'SCOPE_19']:
        fmt = '%Y-%m-%dT%H:%M:%S-0000'
    elif cruiseID in ['SCOPE_10', 'SCOPE_15']:
        fmt = '%Y-%m-%dT%H:%M:%S-0700'
    elif cruiseID in ['Gradients2.0', 'KM_1', 'DeepDOM']:
        fmt = '%Y-%m-%dT%H:%M:%S+00:00'
    elif cruiseID in ['Thompson_4', 'Thompson_9']:
        #fmt = '%m/%d/%Y %I:%M:%S %p'
        fmt = '%m/%d/%Y %H:%M'
        
    return fmt


def makeBulkSeaFlow():
    path = cfgv.seaflow_raw + 'SeaFlow_colocal.csv'    
    prefix = 'seaflow'
    df = pd.read_csv(path)
    df = ip.removeColumn(['file'], df)
    df = ip.removeMissings(['lat', 'lon', 'abundance'], df)   # remove rows with missing lat/lon/abundance
    df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df.to_csv(export_path, index=False)
    #ip.mapTo180180(export_path, 'lon')   # only use if necessary
    ip.sortByDepthLatLon(df, export_path, 'lon', 'lat', 'cruise')
    return export_path




def bulkInsertSeaFlow(tableName):
    dataTitle = 'SeaFlow'
    print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
    try:
        bulkPath = ''
        bulkPath = makeBulkSeaFlow()
        #print('\t %s  Bulk %s %7.7d ready.' % (datetime.today(), dataTitle, itnum))
        dc.bulkInsert(bulkPath, tableName)
    finally:
        if bulkPath != '':
            os.remove(bulkPath)    
    print('%s  Done' % datetime.today())
    return




tableName = 'tblSeaFlow'
bulkInsertSeaFlow(tableName)