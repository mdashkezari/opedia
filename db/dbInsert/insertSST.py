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



def makeBulkSST(itnum, nrt):
    if itnum < 1981244:
        print('Error: SST data is only availabe after 1981224.')
        return
    if nrt:        
        path = cfgv.nrt_sst_raw + cfgv.nrt_sst_prefix + '%7.7d.nc' % itnum   
    else:
        path = 'unknown'
        #path = cfgv.rep_sst_raw + cfgv.rep_sst_prefix + '%7.7d.nc' % itnum   
    
    prefix = 'sst_'
    df = nc.ncToDF(path)
    df = ip.removeColumn(['analysis_error', 'mask', 'sea_ice_fraction', 'lat_bnds', 'lon_bnds'], df)
    if 'time_bnds' in df.columns:
        df = ip.removeColumn(['time_bnds'], df)
    #df = ip.removeMissings(['analysed_sst'], df)   # remove land
    # df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s%d.csv' % (exportBase, prefix, itnum)
    df.to_csv(export_path)
    #ip.mapTo180180(export_path, 'lon')   # only use if necessary
    ip.sortByLatLon(df, export_path, 'lon', 'lat')

    ## 1. only keep records with nv=1 (remove nv=0 records)
    ## 2. drop nv column
    ## 3. unit conversion; kelvin to centigrade
    ## 4. fix time stamp: one or some of the sst files have incorrecty timestamp. 
    df = pd.read_csv(export_path)
    df = df[df['nv'] == 1]
    df = ip.removeColumn(['nv'], df)
    df['analysed_sst'] = df['analysed_sst'] - 273.15
    if itnum in [2016097]:        # this is to account for a little bug in the time variable in the SST netcdf file
        df['time'] = pd.DatetimeIndex(df['time']) + pd.DateOffset(1)
    df.to_csv(export_path, index=False)    
    ####################################################
    return export_path




def bulkInsertSST(itnumStart, itnumEnd, tableName):
    dataTitle = 'SST'
    for itnum in range(itnumStart, itnumEnd+1):   
        print('%s  Inserting Bulk %s %7.7d into %s.' % (datetime.today(), dataTitle, itnum, tableName))
        try:
            bulkPath = ''
            bulkPath = makeBulkSST(itnum, nrt)
            #print('\t %s  Bulk %s %7.7d ready.' % (datetime.today(), dataTitle, itnum))
            # dc.bulkInsert(bulkPath, tableName)
            dc.bcpInsert(bulkPath, tableName)
        finally:
            if bulkPath != '':
                os.remove(bulkPath)    
    return




itnumStart = int(sys.argv[1])
itnumEnd = int(sys.argv[2])
nrt = bool(int(sys.argv[3]))
if nrt:
    tableName = 'tblSST_AVHRR_OI_NRT'
else:
    tableName = 'unknown'


bulkInsertSST(itnumStart, itnumEnd, tableName)