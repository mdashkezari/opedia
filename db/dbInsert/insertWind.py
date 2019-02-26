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



def makeBulkWind(itnum, nrt, hour):
    if itnum < 2012320:
        print('Error: Wind data is only availabe after 2012320.')
        return
    if nrt:        
        path = cfgv.nrt_wind_raw + cfgv.nrt_wind_prefix + '%7.7d_%2.2dh.nc' % (itnum, hour)   
    else:
        path = 'unknown'
        #path = cfgv.rep_wind_raw + cfgv.rep_wind_prefix + '%7.7d_%2.2dh.nc' % (itnum, hour)   
    
    prefix = 'wind_'
    df = nc.ncToDF(path)
    df = ip.removeColumn(['land_ice_mask', 'sampling_length'], df)
    #df = ip.removeMissings(['wind_stress'], df)   # remove land

    ## arrange the columns: making sure that the columns are arranged in the correct (consistent with the undelying table) order
    df = ip.arrangeColumns(['wind_speed_rms', 'eastward_wind_rms', 'wind_stress', 'eastward_wind', 'surface_downward_eastward_stress', 'wind_speed', 'surface_downward_northward_stress', 'northward_wind', 'northward_wind_rms'], df)

    df['hour'] = hour
    df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s%d_%2.2dh.csv' % (exportBase, prefix, itnum, hour)
    df.to_csv(export_path)
    #ip.mapTo180180(export_path, 'longitude')   # only use if necessary
    ip.sortByLatLon(df, export_path, 'longitude', 'latitude')

    ########### drop depth column ###############
    df = pd.read_csv(export_path)
    df = ip.removeColumn(['depth'], df)
    df.to_csv(export_path, index=False)    
    ##############################################
    return export_path




def bulkInsertWind(itnumStart, itnumEnd, tableName):
    def insertHourly(itnum, hour, tableName, nrt):
        try:
            bulkPath = ''
            bulkPath = makeBulkWind(itnum, nrt, hour)
            dc.bulkInsert(bulkPath, tableName)
            print('\t %s  Bulk %s %7.7d_%2.2dh inserted.' % (datetime.today(), dataTitle, itnum, hour))
        finally:
            if bulkPath != '':
                os.remove(bulkPath)    
        return        

    dataTitle = 'Wind'
    for itnum in range(itnumStart, itnumEnd+1):
        print('%s  Inserting Bulk %s %7.7d into %s.' % (datetime.today(), dataTitle, itnum, tableName))
        insertHourly(itnum, 0, tableName, nrt)
        insertHourly(itnum, 6, tableName, nrt)
        insertHourly(itnum, 12, tableName, nrt)
        insertHourly(itnum, 18, tableName, nrt)

    return




itnumStart = int(sys.argv[1])
itnumEnd = int(sys.argv[2])
nrt = bool(int(sys.argv[3]))
if nrt:
    tableName = 'tblWind_NRT'
else:
    tableName = 'unknown'


bulkInsertWind(itnumStart, itnumEnd, tableName)