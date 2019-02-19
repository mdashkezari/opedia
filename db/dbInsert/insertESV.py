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
    path = cfgv.rep_esv_raw + 'ANT-28-5_all_fractions_deblur_eASVs.tsv'
    prefix = 'esv'
    df = pd.read_csv(path, delimiter="\t")
    df['time']=pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')
    df['time'] = df['time'].dt.date
    df['time']=pd.to_datetime(df['time'], format='%Y-%m-%d')
    df['lat'] = df['lat'].astype(float)
    df['lon'] = df['lon'].astype(float)
    df['depth'] = df['depth'].astype(float)
    removeCols = ['qiime2-ID', 'Cluster_Members', 'Cluster_Type', 'Run', 'Sample', 'ENA-BASE-COUNT', 'ENA-SPOT-COUNT', 'Methods_and_data']
    df.drop(removeCols, inplace=True, axis=1)
    #df = ip.removeMissings(['lat', 'lon', 'abundance'], df)   # remove rows with missing lat/lon/abundance
    df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    print(df.head(1), len(df), export_path)
    df.to_csv(export_path, index=False)
    #ip.mapTo180180(export_path, 'lon')   # only use if necessary
    #ip.sortByDepthLatLon(df, export_path, 'lon', 'lat', 'cruise')
    return export_path



def toSQLbcp(bulkPath, tableName,  usr='sa', psw='Jazireie08', ip='128.208.239.15'):
    str = """bcp Opedia.dbo.""" + tableName + """ in """ + bulkPath + """ -c -t, -U """ + usr + """ -P """ + psw + """ -S """ + ip + """,1433"""
    print(str)
    # os.system(str)


def bulkInsertESV(tableName):
    dataTitle = 'ESV'
    print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
    try:
        # bulkPath = ''
        # bulkPath = ulkESV()
        #print('\t %s  Bulk %s %7.7d ready.' % (datetime.today(), dataTitle, itnum))
        # dc.bulkInsert(filePath=bulkPath, tableName=tableName, usr=usr, psw=psw)
        print('Starting table insert....')
        toSQLbcp(bulkPath, tableName)
    finally:
        pass
    #     if bulkPath != '':
    #         os.remove(bulkPath)
    # print('%s  Done' % datetime.today())
    return




# usr = sys.argv[1]
# psw = sys.argv[2]

tableName = 'tblESV_update'
# bulkPath = 'D:\opedia\db\dbInsert\export\esv.csv'
# toSQLbcp(bulkPath, tableName)
# bulkInsertESV(tableName, usr, psw)
# bulkInsertESV(tableName)
makeBulkESV()
