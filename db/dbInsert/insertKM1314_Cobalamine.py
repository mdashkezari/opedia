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



def makeBulkCobalamin():
    path = cfgv.rep_KM1314_cobalamin_raw + 'KM1314_ParticulateCobalamins_2018_06_12_vPublished.xlsx'    
    prefix = 'KM1314_ParticulateCobalamins_2018_06_12_vPublished'
    
    df = pd.read_excel(open(path,'rb'), sheetname='data')
    df = ip.removeMissings(['time', 'lat', 'lon', 'depth'], df)  
    df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df.to_csv(export_path, index=False)
    #ip.sortByTimeLatLonDepth(df, export_path, 'time', 'lat', 'lon', 'depth')
    return export_path




def bulkInsertKM1314_Cobalamin(tableName):
    dataTitle = 'KM1314_cobalamin'
    print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
    try:
        bulkPath = ''
        bulkPath = makeBulkCobalamin()
        dc.bulkInsert(bulkPath, tableName)
    finally:
        if bulkPath != '':
            os.remove(bulkPath)    
    print('%s  Done' % datetime.today())
    return



fmt = '%Y-%m-%dT%H:%M:%S'
tableName = 'tblCobalamin'
bulkInsertKM1314_Cobalamin(tableName)

