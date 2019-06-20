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



def makeBulkCHL(itnum, nrt):
    if itnum < 1998001:
        print('Error: CHL data is only availabe after 1998.')
        return
    if nrt:        
        path = cfgv.nrt_chl_8day_raw + cfgv.nrt_chl_8day_prefix + '%7.7d.nc' % itnum   
    else:
        path = cfgv.rep_chl_8day_raw + cfgv.rep_chl_8day_prefix + '%7.7d.nc' % itnum   
    
    prefix = 'chl_8day_'
    df = nc.ncToDF(path)
    df = ip.removeColumn(['CHL_error'], df)
    #df = ip.removeMissings(['CHL'], df)   # remove land
    # df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s%d.csv' % (exportBase, prefix, itnum)
    df.to_csv(export_path)
    
    ## seems like the code below is only needed for the NRT product
    ## longitude range in NRT products: 0 - 360
    if nrt:
        ip.mapTo180180(export_path, 'lon')   # only use if necessary
    
    ip.sortByLatLon(df, export_path, 'lon', 'lat')
    return export_path




def bulkInsertCHL(itnumStart, itnumEnd, tableName):
    dataTitle = 'CHL'
    ## specific to this data set: data files always start at the first day of the year
    ## and the increment with 8 day intervals
    for itnum in range(itnumStart, itnumEnd+1, 8):   
        print('%s  Inserting Bulk %s %7.7d into %s.' % (datetime.today(), dataTitle, itnum, tableName))
        try:
            bulkPath = ''
            bulkPath = makeBulkCHL(itnum, nrt)

            dc.bulkInsert(bulkPath, tableName, usr='', psw='')
        finally:
            if bulkPath != '':
                os.remove(bulkPath)    
    return




itnumStart = int(sys.argv[1])
itnumEnd = int(sys.argv[2])
nrt = bool(int(sys.argv[3]))
if nrt:
    tableName = ''
else:
    tableName = 'tblCHL_REP'


bulkInsertCHL(itnumStart, itnumEnd, tableName)