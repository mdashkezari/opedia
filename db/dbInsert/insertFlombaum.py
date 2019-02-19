import os
import sys
sys.path.append('../login')
sys.path.append('../../config')
import pandas as pd
import insertPrep as ip
import config_vault as cfgv
import credentials as cr

############################
########### OPTS ###########
tableName = 'tblFlombaum'
############################
############################

""" This function imports the raw .csv, cleans it, builds the leaf structure in storage, then moves the cleaned file"""
def makeBulkFlombaum():
    path = cfgv.flombaum_raw + 'rep/flombaum.csv'
    prefix = 'flombaum'
    df = pd.read_csv(path)
    df = ip.removeMissings(['time','lat', 'lon','depth'], df)
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
    df.to_csv(export_path, index=False)
    print('export path: ' ,export_path)
    return export_path

""" This function uses the sql server BCP utility to insert the cleaned .csv file into the database """
def toSQLbcp(tableName, usr=cr.usr, psw=cr.psw, ip=cr.ip):
    bulkPath = makeBulkFlombaum()

    print('Inserting Bulk %s into %s.' % (tableName[3:], tableName))
    str = """bcp Opedia.dbo.""" + tableName + """ in """ + bulkPath + """ -e error -c -t, -U  """ + usr + """ -P """ + psw + """ -S """ + ip + """,1433"""
    os.system(str)
    print('BCP insert finished')


toSQLbcp(tableName)
