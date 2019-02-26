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



def makeBulkPisces(itnum, nrt):
    if itnum < 2011365:
        print('Error: Mercator-Pisces data is only availabe after 2012.')
        return
    if nrt:        
        path = cfgv.nrt_mercator_pisces_raw + cfgv.nrt_mercator_pisces_prefix + '%7.7d.nc' % itnum   
    else:
        path = 'unknown'
        #path = cfgv.rep_mercator_pisces_raw + cfgv.rep_mercator_pisces_prefix + '%7.7d.nc' % itnum   
    
    prefix = 'pisces_'
    df = nc.ncToDF(path)
    ## arrange the columns: making sure that the columns are arranged in the correct (consistent with the undelying table) order
    df = ip.arrangeColumns(['Fe', 'PP', 'Si', 'NO3', 'CHL', 'PHYC', 'PO4', 'O2'], df)
    df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s%d.csv' % (exportBase, prefix, itnum)
    df.to_csv(export_path)
    #ip.mapTo180180(export_path, 'longitude')   # only use if necessary
    ## sortByDepthLatLon_AddClim will sort the dataframe and will add "month" and "year" coloumns to the dataframe
    ip.sortByDepthLatLon_AddClim(df, export_path, 'longitude', 'latitude', 'depth')
    return export_path




def bulkInsertPisces(itnumStart, itnumEnd, tableName):
    dataTitle = 'Mercator-Pisces'
    for itnum in range(itnumStart, itnumEnd+1, 7):   
        print('%s  Inserting Bulk %s %7.7d into %s.' % (datetime.today(), dataTitle, itnum, tableName))
        try:
            bulkPath = ''
            bulkPath = makeBulkPisces(itnum, nrt)
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
    tableName = 'tblPisces_NRT'
else:
    tableName = 'unknown'


bulkInsertPisces(itnumStart, itnumEnd, tableName)