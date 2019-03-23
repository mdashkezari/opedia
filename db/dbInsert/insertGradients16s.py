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



def makeBulkESV():
    path = cfgv.rep_gradients_16s_raw + 'Gproks.csv'    
    prefix = 'esv'
    df = pd.read_csv(path, delimiter="\t")
    df['Date_sampled']=pd.to_datetime(df['Date_sampled'])
    df['Date_sampled'] = df['Date_sampled'].dt.date
    df['Date_sampled']=pd.to_datetime(df['Date_sampled'], format='%Y-%m-%d')
    df['lat'] = df['lat'].astype(float)
    df['lon'] = df['lon'].astype(float)
    df['depth_m'] = df['depth_m'].astype(float)
    removeCols = ['taxonomy']
    df.drop(removeCols, inplace=True, axis=1)

    ## arrange the columns: making sure that the columns are arranged in the correct (consistent with the undelying table) order
    #df = ip.arrangeColumns(['Date_sampled', 'Lat', 'Lon', 'Depth_m', 'OTU', 'count', 'Domain', 'Kingdom', 'Phylum', 'Class', 'Order', 'Genus', 'Species'], df)

    df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df.to_csv(export_path, index=False)
    #ip.mapTo180180(export_path, 'lon')   # only use if necessary
    #ip.sortByDepthLatLon(df, export_path, 'lon', 'lat', 'cruise')
    return export_path




def bulkInsertESV(tableName, usr, psw):
    dataTitle = 'ESV'
    print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
    try:
        bulkPath = ''
        bulkPath = makeBulkESV()
        #print('\t %s  Bulk %s %7.7d ready.' % (datetime.today(), dataTitle, itnum))
        # dc.bulkInsert(filePath=bulkPath, tableName=tableName, usr=usr, psw=psw)
    finally:
        pass
        # if bulkPath != '':
            # os.remove(bulkPath)    
    print('%s  Done' % datetime.today())
    return




usr = sys.argv[1]
psw = sys.argv[2]

tableName = 'tblESV'
bulkInsertESV(tableName, usr, psw)