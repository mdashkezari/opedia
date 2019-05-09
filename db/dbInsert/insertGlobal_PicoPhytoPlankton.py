import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import config_vault as cfgv
import pandas as pd

############################
########### OPTS ###########

tableName = 'tblGlobal_PicoPhytoPlankton'
rawFilePath = cfgv.rep_Global_PicoPhytoPlankton_raw
rawFileName = 'picophyto111130.xlsx'
usecols=['Lat','Long','year','day','PromL', 'SynmL', 'PEukmL','Depth','month','pico_abund','picophyto [ug C/L]']



def makeGlobal_PicoPhytoPlankton(rawFilePath, rawFileName, tableName):
    path = rawFilePath + rawFileName
    prefix = tableName
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df = pd.read_excel(path,  sep=',',sheet_name='data', usecols=usecols)
    df['year']= df['year'].astype('str')
    df['month']= ((df['month'].astype('str')).apply(lambda x: x.zfill(2)))
    df['day']= ((df['day'].astype('str')).apply(lambda x: x.zfill(2)))
    print(len(df))
    df = df[(df['day'] != '-9') & (df['day'] != '-1')]

    df['year'] = df['year'].replace('10', '2010')
    df['year'] = df['year'].replace('11', '2011')
    df['year'] = df['year'].replace('6', '2006')
    # df = df[(df['year'] != '10') & (df['year'] != '11')& (df['year'] != '6')]
    df['time'] = pd.to_datetime(df[['year', 'month', 'day']], format='%Y%m%d')
    ip.renameCol(df,'Lat', 'lat')
    ip.renameCol(df,'Long', 'lon')
    ip.renameCol(df,'Depth', 'depth')
    ip.renameCol(df,'PromL', 'prochlorococcus_abundance')
    ip.renameCol(df,'SynmL', 'synechococcus_abundance')
    ip.renameCol(df,'PEukmL', 'picoeukaryote_abundance')
    ip.renameCol(df,'pico_abund', 'picophytoplankton_abundance')
    ip.renameCol(df,'picophyto [ug C/L]', 'picophytoplankton_biomass')
    ip.removeColumn(['year','day','month'],df)
    df = ip.reorderCol(df,['time','lat','lon','depth','prochlorococcus_abundance','synechococcus_abundance','picoeukaryote_abundance','picophytoplankton_abundance','picophytoplankton_biomass'])
    df = ip.removeMissings(['time','lat', 'lon','depth'], df)
    df = ip.NaNtoNone(df)
    df = ip.colDatatypes(df)
    df = ip.addIDcol(df)
    df = ip.removeDuplicates(df)
    df.to_csv(export_path, index=False)
    ip.sortByTimeLatLonDepth(df, export_path, 'time', 'lat', 'lon', 'depth')
    print('export path: ' ,export_path)
    return export_path


export_path = makeGlobal_PicoPhytoPlankton(rawFilePath, rawFileName, tableName)
iF.toSQLbcp(export_path, tableName)
