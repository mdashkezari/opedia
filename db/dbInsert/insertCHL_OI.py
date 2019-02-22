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


def downsampleCHL(export_path):
    def rebin(a, shape):
        sh = shape[0],a.shape[0]//shape[0],shape[1],a.shape[1]//shape[1]
        return a.reshape(sh).mean(-1).mean(1)
    currShape = (8640, 4320)
    newShape = (1440, 720)    
    df = pd.read_csv(export_path)
    lat = np.array(df['lat']).reshape(currShape)
    lon = np.array(df['lon']).reshape(currShape)
    dt = np.array(df['time']).reshape(currShape)    
    chl = np.array(df['CHL']).reshape(currShape)    
    lat = rebin(lat, newShape)
    lon = rebin(lon, newShape)
    chl = rebin(chl, newShape)    
    newDF = pd.DataFrame()
    newDF['lat'] = pd.Series(lat.flatten())
    newDF['lon'] = pd.Series(lon.flatten())
    newDF['time'] = dt[1, 1]
    newDF['chl'] = pd.Series(chl.flatten())
    newDF['ID'] = None
    newDF.to_csv(export_path, index = False)    
    return newDF


def makeBulkCHL(itnum, nrt):
    if itnum < 1998001:
        print('Error: CHL data is only availabe after 1998.')
        return
    if nrt:        
        path = cfgv.nrt_chl_raw + cfgv.nrt_chl_prefix + '%7.7d.nc' % itnum   
    else:
        path = cfgv.rep_chl_raw + cfgv.rep_chl_prefix + '%7.7d.nc' % itnum   
    
    prefix = 'chl_oi_'
    df = nc.ncToDF(path)
    df = ip.removeColumn(['CHL_error'], df)
    #df = ip.removeMissings(['CHL'], df)   # remove land
    df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s%d.csv' % (exportBase, prefix, itnum)
    df.to_csv(export_path)
    
    ## seems like the code below is only needed for the NRT product
    ## longitude range in NRT products: 0 - 360
    if nrt:
        ip.mapTo180180(export_path, 'lon')   # only use if necessary
    
    ###df = downsampleCHL(export_path)
    ip.sortByLatLon(df, export_path, 'lon', 'lat')
    return export_path




def bulkInsertCHL(itnumStart, itnumEnd, tableName):
    dataTitle = 'CHL'
    for itnum in range(itnumStart, itnumEnd+1):   
        print('%s  Inserting Bulk %s %7.7d into %s.' % (datetime.today(), dataTitle, itnum, tableName))
        try:
            bulkPath = ''
            bulkPath = makeBulkCHL(itnum, nrt)
            #print('\t %s  Bulk %s %7.7d ready.' % (datetime.today(), dataTitle, itnum))
            dc.bulkInsert(bulkPath, tableName)
        finally:
            if bulkPath != '':
                os.remove(bulkPath)    
    return




itnumStart = int(sys.argv[1])
itnumEnd = int(sys.argv[2])
nrt = bool(int(sys.argv[3]))
if nrt:
    tableName = 'tblCHL_OI_NRT'
else:
    tableName = 'tblCHL_OI_REP'


bulkInsertCHL(itnumStart, itnumEnd, tableName)