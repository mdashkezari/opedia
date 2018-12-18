
""" import raw .csv into df - > run cleaning functions -> export to .csv for faster bulk insert into sql server db"""

import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

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
import sqlalchemy




def makeBulkFlombaum():
    path = cfgv.flombaum_raw + 'rep/flombaum.csv'
    prefix = 'flombaum'
    df = pd.read_csv(path)
    df = ip.convertYYYYMMDD(df)


    df = ip.removeMissings(['lat', 'lon'], df)   # remove rows with missing lat/lon/abundance
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    print('Export path:', export_path)
    df.to_csv(export_path, index=False)
    print(df.head(1 ))
    ip.sortByDepthLatLon(df, export_path, 'lon', 'lat', 'depth')

    return export_path





def bulkInsertFlombaum(tableName):
    dataTitle = 'Flombaum'
    print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
    try:
        bulkPath = ''
        bulkPath = makeBulkFlombaum()
        bulkPath = bulkPath
        # print('bulkPath: ', bulkPath, 'tableName: ',  tableName)

        toSQLPandasFlombaum(bulkPath, tableName)

        # dc.bulkInsert(bulkPath, tableName)
    finally:
        pass
        # if bulkPath != '':
        #     os.remove(bulkPath)
    # print('%s  Done' % datetime.today())
    return


def toSQLPandasFlombaum(bulkPath, tableName, usr='sa', psw='ArmLab2018', ip='10.19.231.219', port='1433', db='Opedia'):

    """ sqlalchemy connection to db """
    engine = sqlalchemy.create_engine('mssql+pyodbc://'+usr+':'+psw+'@'+ip+':'+port+'/'+db+'?'\
    +'driver=FreeTDS')


    """ import cleaned .csv """
    df = pd.read_csv(bulkPath, parse_dates=['time'])
    # print(type(df['time'].iloc[0]))
    # print(df['time'].iloc[0])

    """ pandas sql insert function """
    df.to_sql(tableName, engine, if_exists='replace', index=False)


tableName = 'tblFlombaum'
bulkInsertFlombaum(tableName)
