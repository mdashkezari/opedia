import os, os.path
import sys
sys.path.append('../login')
sys.path.append('../../config')
import pandas as pd
import insertPrep as ip
import config_vault as cfgv
import credentials as cr

def toSQLbcp(rawFileName, tableName, opt_remove_cols="",  usr=cr.usr, psw=cr.psw, ip=cr.ip):
    bulkPath = cleanStrucCSV(rawFileName, tableName, opt_remove_cols="")
    print('Inserting Bulk %s into %s.' % (tableName[3:], tableName))
    str = """bcp Opedia.dbo.""" + tableName + """ in """ + bulkPath + """ -e error -c -t, -U  """ + usr + """ -P """ + psw + """ -S """ + ip + """,1433"""
    os.system(str)
    print('BCP insert finished')



def cleanStrucCSV(rawFileName, tableName, opt_remove_cols=""):
    path = getattr(cfgv, 'rep_' + tableName[3:].lower() + '_raw') + rawFileName
    if os.path.isfile(path):
        pass
    else:
        path = getattr(cfgv, 'nrt_' + tableName[3:].lower() + '_raw') + rawFileName
    prefix = tableName
    df = pd.read_csv(path)
    df = ip.removeMissings(['time','lat', 'lon','depth'], df)
    df['time']=pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')
    df['time'] = df['time'].dt.date
    df['time']=pd.to_datetime(df['time'], format='%Y-%m-%d')
    df['lat'] = df['lat'].astype(float)
    df['lon'] = df['lon'].astype(float)
    df['depth'] = df['depth'].astype(float)
    if opt_remove_cols != "":
        df.drop(removeCols, inplace=True, axis=1)
    df = ip.NaNtoNone(df)
    df['ID'] = None

    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df.to_csv(export_path, index=False)
    print('export path: ' ,export_path)
    return export_path



def cleanStrucXLSX(rawFileName, tableName):
    path = getattr(cfgv, 'rep_' + tableName[3:].lower() + '_raw') + rawFileName
    if os.path.isfile(path):
        pass
    else:
        path = getattr(cfgv, 'nrt_' + tableName[3:].lower() + '_raw') + rawFileName
    prefix = tableName
    df = pd.read_excel(path)
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
