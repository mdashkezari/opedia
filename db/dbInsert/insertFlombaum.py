

""" import raw .csv into df - > run cleaning functions -> export to .csv for faster bulk insert into sql server db"""

import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

import sys
sys.path.append('../../config')
import config_vault as cfgv
sys.path.append('../../lib')
# import dateLib as dl
sys.path.append('../')
import dbCore as dc
import os
import numpy as np
import pandas as pd
import pyodbc
import pandas.io.sql as sql
from datetime import datetime
import time
import math
import insertPrep as ip
import sqlalchemy
#
#
# #os.system("windows command")


def makeBulkFlombaum():
    path = cfgv.flombaum_raw + 'rep/flombaum.csv'
    prefix = 'flombaum'
    df = pd.read_csv(path)
    df = ip.removeMissings(['time','lat', 'lon','depth'], df)   # remove rows with missing lat/lon/abundance

    df['time']=pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')
    df['time'] = df['time'].dt.date
    df['time']=pd.to_datetime(df['time'], format='%Y-%m-%d')
    df['lat'] = df['lat'].astype(float)
    df['lon'] = df['lon'].astype(float)
    df['depth'] = df['depth'].astype(float)

    df = ip.NaNtoNone(df)

    df['ID'] = None

    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    print('Export path:', export_path)
    # ip.sortByDepthLatLon(df, export_path, 'lon', 'lat', 'depth')

    # df = df.head(1)
    print(df.head(1))

    # df.drop('time', axis=1, inplace=True)
    # df = df[pd.notnull(df['prochloro_abundance'])]
    # df = df[pd.notnull(df['synecho_abundance'])]

    df.to_csv(export_path, index=False)
    print('export path' ,export_path)
    # print(df.head(1))

    return export_path





def bulkInsertFlombaum(tableName):
    dataTitle = 'Flombaum'
    print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
    try:
        bulkPath = ''
        bulkPath = makeBulkFlombaum()
        bulkPath = bulkPath
        # print('bulkPath: ', bulkPath, 'tableName: ',  tableName)

        toSQLbcp(bulkPath, tableName)

        # dc.bulkInsert(bulkPath, tableName)
    finally:
        pass
        # if bulkPath != '':
        #     os.remove(bulkPath)
    # print('%s  Done' % datetime.today())
    return

# def toSQLbcp(bulkPath, tableName, usr='nrhagen', psw='Rdw10^3pb', ip='128.208.239.15'):
def toSQLbcp(bulkPath, tableName, usr='sa', psw='Jazireie08', ip='128.208.239.15'):

    # str = """bcp Opedia.dbo.""" + tableName + """ in """ + bulkPath + """ -c -t, -U """ + usr + """ -P """ + psw + """ -S """ + ip + """,1433"""
    str = """bcp Opedia.dbo.""" + tableName + """ in """ + bulkPath + """ -e error -c -t, -U  """ + usr + """ -P """ + psw + """ -S """ + ip + """,1433"""
    # str = """bcp Opedia.dbo.""" + tableName + """ in """ + bulkPath + """ -e error -w -t, -U """ + usr + """ -P """ + psw + """ -S """ + ip + """,1433"""

    print(str)
    os.system(str)




def db_insert(SQL):
    conn = dc.dbConnect()
    cursor = conn.cursor()
    #vals = nanToNone(vals)
    cursor.execute(SQL)
    conn.commit()



tableName = 'tblFlombaum'
bulkInsertFlombaum(tableName)
