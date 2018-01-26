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
import scipy.io



def matToDF(path, itnum):
    mat = scipy.io.loadmat(path)
    lon = mat['lon']   
    lat = mat['lat']
    data = mat['vort']    
    dt = dl.daynToDate(itnum)

    LON, LAT = np.meshgrid(lon, lat)
    df = pd.DataFrame()
    df['lat'] = pd.Series(LAT.flatten())
    df['lon'] = pd.Series(LON.flatten())
    df['time'] = dt
    df['vort'] = pd.Series(data.flatten())
    return df


def makeBulkVort(itnum, nrt):
    if itnum < 1993001:
        print('Error: Relative Vorticity is only available after 1993.')
        return
    if nrt:        
        path = cfgv.nrt_vort_sla_raw + cfgv.nrt_vort_sla_prefix + '%10.10d.mat' % itnum   
    else:
        path = cfgv.rep_vort_sla_raw + cfgv.rep_vort_sla_prefix + '%10.10d.mat' % itnum   
    
    prefix = 'vort_sla_'
    df = matToDF(path, itnum)
    #df = ip.removeColumn(['err'], df)
    #df = ip.removeMissings(['vort'], df)   # remove land
    df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s%d.csv' % (exportBase, prefix, itnum)
    df.to_csv(export_path, index=False)
    ip.mapTo180180(export_path, 'lon')   # only use if necessary
    ip.sortByLatLon(df, export_path, 'lon', 'lat')
    return export_path




def bulkInsertVort(itnumStart, itnumEnd, tableName):
    dataTitle = 'Vorticity'
    for itnum in range(itnumStart, itnumEnd+1):   
        print('%s  Inserting Bulk %s %7.7d into %s.' % (datetime.today(), dataTitle, itnum, tableName))
        try:
            bulkPath = ''
            bulkPath = makeBulkVort(itnum, nrt)
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
    tableName = 'tblVort_NRT'
else:
    tableName = 'tblVort_REP'


bulkInsertVort(itnumStart, itnumEnd, tableName)