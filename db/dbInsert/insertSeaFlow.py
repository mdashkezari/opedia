
import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import config_vault as cfgv
import pandas as pd
import numpy as np
############################
######### PREP #############
# df_pub = pd.read_excel(rawFilePath + 'SeaFlow_ScientificData_2019-05-22.xlsx', sheet_name='data', index_col=None, nrows=10)
# df_unpub = pd.read_excel(rawFilePath +'SeaFlow_unpublished_2019-05-22.xlsx' , sheet_name='data', index_col=None,nrows=10)
# df = pd.concat([df_pub,df_unpub])
# df = pd.to_csv(rawFilePath + 'SeaFlow_concatenated_2019-05-22.csv', sep=',',index=False)


############################
########### OPTS ###########
tableName = 'tblSeaFlow'
rawFilePath = cfgv.rep_seaflow_raw
rawFileName = 'SeaFlow_concatenated_2019-05-22.csv'
############################
############################

def makeSeaFlow(rawFilePath, rawFileName, tableName):
    path = rawFilePath + rawFileName
    prefix = tableName
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df = pd.read_csv(path, sep=',')
    df = df[df['flag'] == 0]

    df['prochloro_abundance'] = np.where(((df['pop'] == 'prochloro') & (df['quantile'] == 50)), df['abundance'], np.nan)
    df['prochloro_diameter'] = np.where(df['pop'] == 'prochloro', df['diam_mid'], np.nan)
    df['prochloro_carbon_content'] = np.where(df['pop'] == 'prochloro', df['Qc_mid'], np.nan)
    df['prochloro_biomass'] = df['prochloro_abundance'].astype(float) * df['prochloro_carbon_content'].astype(float)

    df['synecho_abundance'] = np.where(((df['pop'] == 'synecho') & (df['quantile'] == 50)), df['abundance'], np.nan)
    df['synecho_diameter'] = np.where(df['pop'] == 'synecho', df['diam_mid'], np.nan)
    df['synecho_carbon_content'] = np.where(df['pop'] == 'synecho', df['Qc_mid'], np.nan)
    df['synecho_biomass'] = df['synecho_abundance'] * df['synecho_carbon_content']

    df['croco_abundance'] = np.where(((df['pop'] == 'croco') & (df['quantile'] == 50)), df['abundance'], np.nan)
    df['croco_diameter'] = np.where(df['pop'] == 'croco', df['diam_mid'], np.nan)
    df['croco_carbon_content'] = np.where(df['pop'] == 'croco', df['Qc_mid'], np.nan)
    df['croco_biomass'] = df['croco_abundance'] * df['croco_carbon_content']

    df['picoeuk_abundance'] = np.where(((df['pop'] == 'picoeuk') & (df['quantile'] == 50)), df['abundance'], np.nan)
    df['picoeuk_diameter'] = np.where(df['pop'] == 'picoeuk', df['diam_mid'], np.nan)
    df['picoeuk_carbon_content'] = np.where(df['pop'] == 'picoeuk', df['Qc_mid'], np.nan)
    df['picoeuk_biomass'] = df['picoeuk_abundance'] * df['picoeuk_carbon_content']

    df['unknown_abundance'] = np.where(((df['pop'] == 'unknown') & (df['quantile'] == 50)), df['abundance'], np.nan)
    df['unknown_diameter'] = np.where(df['pop'] == 'unknown', df['diam_mid'], np.nan)
    df['unknown_carbon_content'] = np.where(df['pop'] == 'unknown', df['Qc_mid'], np.nan)
    df['unknown_biomass'] = df['unknown_abundance'] * df['unknown_carbon_content']

    df['total_abundance'] = np.where(((df['pop'] != 'beads') & (df['quantile'] == 50)), df['abundance'], np.nan)
    df['total_carbon_content'] = np.where(df['pop'] != 'beads', df['Qc_mid'], np.nan)
    df['total_biomass'] = df['total_abundance'] * df['total_carbon_content']

    df = ip.arrangeColumns(['time', 'lat', 'lon', 'depth', 'prochloro_abundance', 'prochloro_diameter', 'prochloro_carbon_content', 'prochloro_biomass','synecho_abundance', 'synecho_diameter', 'synecho_carbon_content', 'synecho_biomass','croco_abundance', 'croco_diameter', 'croco_carbon_content', 'croco_biomass','picoeuk_abundance', 'picoeuk_diameter', 'picoeuk_carbon_content', 'picoeuk_biomass','unknown_abundance', 'unknown_diameter', 'unknown_carbon_content', 'unknown_biomass','total_biomass', 'par'], df)

    df = ip.removeMissings(['time','lat', 'lon'], df)
    df = ip.NaNtoNone(df)
    df = ip.colDatatypes(df)
    df = ip.convertYYYYMMDD(df)
    df = ip.addIDcol(df)
    df.to_csv(export_path, index=False)
    ip.sortByTimeLatLon(df, export_path, 'time', 'lat', 'lon')
    print('export path: ' ,export_path)
    return export_path


export_path = makeSeaFlow(rawFilePath, rawFileName, tableName)
iF.toSQLbcp(export_path, tableName)
