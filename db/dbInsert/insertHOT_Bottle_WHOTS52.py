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


def formatDate_Columns(df, dateLabels, fmt='%m%d%y'):
    date_len = 6    
    for dateLabel in dateLabels:
        date_ind = df.columns.get_loc(dateLabel)
        df[dateLabel] =df[dateLabel].astype(int)
        df[dateLabel] =df[dateLabel].astype(str)
        df[dateLabel] = df[dateLabel].str.strip()
        for i in range(len(df)):        
            df.iloc[i, date_ind] = ('0'*(date_len-len(df.iloc[i, date_ind]))) + df.iloc[i, date_ind]
        df[dateLabel] =  pd.to_datetime(df[dateLabel], format=fmt)
    return df


def makeBulkBottle_WHOTS52_HOT():
    path = cfgv.rep_hot_raw + 'bottle_whots52.csv'    
    prefix = 'bot_whots52_hot'
    missingValue = -9 
    df = pd.read_csv(path)   
    if ' ' in df.columns:
        df.drop(' ', axis=1, inplace=True)
    df = df.drop(df.index[[0]])   ## remove the units row    
    df.columns = df.columns.str.replace(' ','')   
    df = df.apply(pd.to_numeric)
    df = df.replace(missingValue, '')
    df = ip.removeMissings(['date'], df) 

    formatDate_Columns(df, ['date'])

    ## Are the below lat/lon values correct? 
    ## http://hahana.soest.hawaii.edu/hot/locations.html
    df['lat'] = 22.67
    df['lon'] = -157.95
    df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df.to_csv(export_path, index=False)
    return export_path



def bulkInsertBottle_WHOTS52_HOT(tableName):
    dataTitle = 'HOT_Bottle_WHOTS52'
    print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
    try:
        bulkPath = ''
        bulkPath = makeBulkBottle_WHOTS52_HOT()
        dc.bulkInsert(bulkPath, tableName)
    finally:
        if bulkPath != '':
            os.remove(bulkPath)    
    print('%s  Done' % datetime.today())
    return



tableName = 'tblHOT_Bottle_WHOTS52'
bulkInsertBottle_WHOTS52_HOT(tableName)

