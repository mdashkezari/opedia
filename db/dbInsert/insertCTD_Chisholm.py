
import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import config_vault as cfgv
import pandas as pd

############################
########### OPTS ###########
tableName = 'tblCTD_Chisholm'
rawFilePath = cfgv.rep_BiGRAPA1_CTDData_Chisholm_raw
rawFileName = 'BiGRAPA1_CTDData_2019-03-19_v1.0.xlsx'
############################
############################


def makeCTD_Chisholm(rawFilePath, rawFileName, tableName):
    path = rawFilePath + rawFileName
    prefix = tableName
    df = pd.read_excel(path, 'data')

    df = ip.removeMissings(['time','lat', 'lon','depth'], df)
    df = ip.colDatatypes(df)
    df = ip.NaNtoNone(df)
    df['ID'] = None

    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    ip.sortByDepthLatLon(df, export_path, 'lon', 'lat', 'depth')
    print(df.dtypes)

    df.to_csv(export_path, index=False)
    print('export path: ' ,export_path)
    return export_path

export_path = makeCTD_Chisholm(rawFilePath, rawFileName, tableName)
iF.toSQLbcp(export_path, tableName)
