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



def makeBulkALT(itnum, nrt):
    if itnum < 1993001:
        print('Error: Altimetry data is only available after 1993.')
        return
    if nrt:        
        path = cfgv.nrt_alt_raw + cfgv.nrt_alt_prefix + '%7.7d.nc' % itnum   
    else:
        path = cfgv.rep_alt_raw + cfgv.rep_alt_prefix + '%7.7d.nc' % itnum   
    
    prefix = 'alt_'
    df = nc.ncToDF(path)
    df = ip.removeColumn(['err'], df)
    #df = ip.removeMissings(['sla'], df)   # remove land

    ## arrange the columns: making sure that the columns are arranged in the correct (consistent with the undelying table) order
    df = ip.arrangeColumns(['vgosa', 'vgos', 'sla', 'adt', 'ugosa', 'ugos'], df)
    # df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s%d.csv' % (exportBase, prefix, itnum)
    df.to_csv(export_path)
    ip.mapTo180180(export_path, 'longitude')   # only use if necessary
    ip.sortByLatLon(df, export_path, 'longitude', 'latitude')
    return export_path




def bulkInsertALT(itnumStart, itnumEnd, tableName):
    dataTitle = 'Altimetry'
    for itnum in range(itnumStart, itnumEnd+1):   
        print('%s  Inserting Bulk %s %7.7d into %s.' % (datetime.today(), dataTitle, itnum, tableName))
        try:
            bulkPath = ''
            bulkPath = makeBulkALT(itnum, nrt)
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
    tableName = 'tblAltimetry_NRT'
else:
    tableName = 'tblAltimetry_REP'


bulkInsertALT(itnumStart, itnumEnd, tableName)