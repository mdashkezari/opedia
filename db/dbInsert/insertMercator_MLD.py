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



def makeBulkMLD(itnum, nrt):
    if nrt:        
        path = cfgv.nrt_mercator_mld_raw + cfgv.nrt_mercator_mld_prefix + '%7.7d.nc' % itnum   
    else:
        path = 'unknown'
        #path = cfgv.rep_mercator_pisces_raw + cfgv.rep_mercator_pisces_prefix + '%7.7d.nc' % itnum   
    
    prefix = 'mercator_mld_'
    df = nc.ncToDF(path)
    ## arrange the columns: making sure that the columns are arranged in the correct (consistent with the undelying table) order
    #df = ip.arrangeColumns(['mlotst'], df)
    df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s%d.csv' % (exportBase, prefix, itnum)
    df.to_csv(export_path)
    #ip.mapTo180180(export_path, 'longitude')   # only use if necessary
    ip.sortByLatLon(df, export_path, 'longitude', 'latitude')
    return export_path




def bulkInsertMLD(itnumStart, itnumEnd, tableName):
    dataTitle = 'Mercator-MLD'
    for itnum in range(itnumStart, itnumEnd+1):   
        print('%s  Inserting Bulk %s %7.7d into %s.' % (datetime.today(), dataTitle, itnum, tableName))
        try:
            bulkPath = ''
            bulkPath = makeBulkMLD(itnum, nrt)
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
    tableName = 'tblMercator_MLD_NRT'
else:
    tableName = 'unknown'


bulkInsertMLD(itnumStart, itnumEnd, tableName)