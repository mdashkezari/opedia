
import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import config_vault as cfgv
import pandas as pd

############################
########### OPTS ###########
tableName = 'AMT13_ProchlorococcusAbundanceAndMetadata_Chisholm'
rawFilePath = cfgv.rep_AMT13Data_Chisholm_raw
rawFileName = 'AMT13_ProchlorococcusAbundanceAndMetadata_2019-02-07_v1.1.xlsx'
############################
############################


def makeAMT13_Chisholm(rawFilePath, rawFileName, tableName):
    path = rawFilePath + rawFileName
    prefix = tableName
    df = pd.read_excel(path, 'data')

    df = ip.removeMissings(['time','lat', 'lon','depth'], df)
    df = ip.colDatatypes(df)
    df['ID'] = None

    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    ip.sortByDepthLatLon(df, export_path, 'lon', 'lat', 'depth')
    df.to_csv(export_path, index=False)
    print('export path: ' ,export_path)
    return export_path

export_path = makeAMT13_Chisholm(rawFilePath, rawFileName, tableName)
iF.toSQLbcp(export_path, tableName)
