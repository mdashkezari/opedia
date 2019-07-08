import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import config_vault as cfgv
import pandas as pd

############################
########### OPTS ###########

tableName = 'tblKM1709_mesoscope'
rawFilePath = cfgv.rep_KM1709_mesoscope_raw
rawFileName = 'mesoscope_cmap.xlsx'
usecols=['Time',
'Latitude',
'Longitude',
'Depth',
'Station',
'Cast',
'RosPos',
'CTD_Temperature',
'CTD_Salinity',
'CTD_Oxygen',
'CTD_Chloropigment',
'Potential_Temperature',
'Potential_Density',
'Bottle_Oxygen',
'DIC',
'Alkalinity',
'pH',
'PO4',
'NO3+NO2',
'SiO4',
'LLN',
'LLP',
'PC',
'PN',
'PP',
'Psi',
'Chlorophyll',
'Pheopigment',
'Heterotrophic_Bacteria',
'Prochlorococcus',
'Synechococcus',
'Eukaryotes']



def makeKM1709_mesoscope(rawFilePath, rawFileName, tableName):
    path = rawFilePath + rawFileName
    prefix = tableName
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df = pd.read_excel(path,  sep=',',sheet_name='data', usecols=usecols)
    ip.renameCol(df,'Time', 'time')
    ip.renameCol(df,'Latitude', 'lat')
    ip.renameCol(df,'Longitude', 'lon')
    ip.renameCol(df,'Depth', 'depth')
    df = ip.removeMissings(['time','lat', 'lon','depth'], df)
    df = ip.NaNtoNone(df)
    df = ip.colDatatypes(df)
    df = ip.addIDcol(df)
    df = ip.removeDuplicates(df)
    df.to_csv(export_path, index=False)
    ip.sortByTimeLatLonDepth(df, export_path, 'time', 'lat', 'lon', 'depth')
    print('export path: ' ,export_path)
    return export_path


export_path = makeKM1709_mesoscope(rawFilePath, rawFileName, tableName)
iF.toSQLbcp(export_path, tableName)
