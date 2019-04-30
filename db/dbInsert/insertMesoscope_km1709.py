
import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import config_vault as cfgv
import pandas as pd

############################
########### OPTS ###########
tableName = 'tblMesoscope_km1709'
rawFilePath = cfgv.rep_km1709_MESOSCOPE_raw
rawFileName = 'mesoscope_cmap.xlsx'
############################
############################



def makeMesoscope_km1709(rawFilePath, rawFileName, tableName):
    path = rawFilePath + rawFileName
    prefix = tableName
    df = pd.read_excel(path, 'data')
    df = ip.removeMissings(['time','lat', 'lon','depth'], df)
    df = ip.colDatatypes(df)
    df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d')
    df['ID'] = None
    df = ip.removeDuplicates(df)
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df.to_csv(export_path, index=False)
    ip.sortByTimeLatLonDepth(df, export_path, 'time', 'lat', 'lon', 'depth')
    df.to_csv(export_path, index=False)
    print('export path: ' ,export_path)
    return export_path


export_path = makeMesoscope_km1709(rawFilePath, rawFileName, tableName)
iF.toSQLbcp(export_path, tableName)
