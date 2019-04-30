
import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import config_vault as cfgv
import pandas as pd

############################
########### OPTS ###########
tableName = 'tblSingleCellGenomes_Chisholm'
rawFilePath = cfgv.rep_SingleCellGenomes_Chisholm_raw
rawFileName = 'SingleCellGenomesOfProchlorococcusSynechococcusAndSympatricMicrobes_2019-04-06_v1.0.xlsx'
############################
############################

def makeSingleCellGenomes_Chisholm(rawFilePath, rawFileName, tableName):
    path = rawFilePath + rawFileName
    prefix = tableName
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df = pd.read_excel(path, 'data')
    df = ip.removeMissings(['time','lat', 'lon','depth'], df)
    df = ip.NaNtoNone(df)
    df = ip.colDatatypes(df)
    df = ip.convertYYYYMMDD(df)
    df = ip.addIDcol(df)
    df = ip.removeDuplicates(df)
    df.to_csv(export_path, index=False)
    ip.sortByTimeLatLonDepth(df, export_path, 'time', 'lat', 'lon', 'depth')
    df.to_csv(export_path, index=False)
    print('export path: ' ,export_path)
    return export_path


export_path = makeSingleCellGenomes_Chisholm(rawFilePath, rawFileName, tableName)
iF.toSQLbcp(export_path, tableName)
