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
from datetime import datetime, timedelta
import time
import math
import insertPrep as ip



def convertJulians(df, julianLabels):
    offset = datetime(1988, 10, 1).date()
    for julianLabel in julianLabels:
        jul_ind = df.columns.get_loc(julianLabel)
        for i in range(len(df)):
            df.iloc[i, jul_ind] = offset + timedelta(days=int(df.iloc[i, jul_ind]))
    return df


def makeBulkCTD_HOT():
    path = cfgv.rep_hot_raw + 'ctd.csv'    
    prefix = 'ctd_hot'
    missingValue = -9 
    df = pd.read_csv(path)   
    if ' ' in df.columns:
        df.drop(' ', axis=1, inplace=True)
    df = df.drop(df.index[[0]])   ## remove the units row    
    df.columns = df.columns.str.replace(' ','')   
    df = df.apply(pd.to_numeric)
    df = df.replace(missingValue, '')

    df = convertJulians(df, ['julian'])

    ## Are the below lat/lon values correct?
    df['lat'] = 22.75
    df['lon'] = -158
    df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df.to_csv(export_path, index=False)
    return export_path



def bulkInsertCTD_HOT(tableName):
    dataTitle = 'HOT_CTD'
    print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
    try:
        bulkPath = ''
        bulkPath = makeBulkCTD_HOT()
        dc.bulkInsert(bulkPath, tableName)
    finally:
        if bulkPath != '':
            os.remove(bulkPath)    
    print('%s  Done' % datetime.today())
    return



tableName = 'tblHOT_CTD'
bulkInsertCTD_HOT(tableName)

