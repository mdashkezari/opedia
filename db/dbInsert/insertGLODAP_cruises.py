
import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
sys.path.append('../../config')
import config_vault as cfgv
import pandas as pd
import numpy as np

############################
########### OPTS ###########
tableName = 'tblGLODAP'
rawFilePath = cfgv.rep_GLODAP_raw
rawFileName = 'GLODAPv2.2019_Merged_Master_File.csv'
rawFileName_expocodes = 'EXPOCODES.txt'
usecols=['cruise','station','cast','year','month','day','hour','minute','latitude','longitude','bottle','pressure','depth','temperature','theta','salinity','sigma0','sigma1','sigma2','sigma3','sigma4','gamma','oxygen','aou','nitrate','nitrite','silicate','phosphate','tco2','talk','phts25p0','phtsinsitutp','cfc11','pcfc11','cfc12','pcfc12','cfc113','pcfc113','ccl4','pccl4','sf6','psf6','c13','c14','c14err','h3','h3err','he3','he3err','he','heerr','neon','neonerr','o18','toc','doc','don','tdn','chla']
usecols_rearange=['time','lat','lon','depth','pressure','depth','temperature','theta_potential_temperature','salinity','sigma0_potential_density','sigma1_potential_density_ref_1000_dbar','sigma2_potential_density_ref_2000_dbar','sigma3_potential_density_ref_3000_dbar','sigma4_potential_density_ref_4000_dbar','gamma_neutral_density','oxygen','aou','nitrate','nitrite','silicate','phosphate','tco2','talk','phts25p0_pH_25C_0dbar','phtsinsitutp_pH_insitu','cfc11','pcfc11','cfc12','pcfc12','cfc113','pcfc113','ccl4','pccl4','sf6','psf6','c13','c14','c14err','h3','h3err','he3','he3err','he','heerr','neon','neonerr','o18','toc','doc','don','tdn','chla','cruise_expocode']
############################
############################

def makeGLODAP(rawFilePath, rawFileName, tableName):
    path = rawFilePath + rawFileName
    prefix = tableName
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df = pd.read_csv(path, sep=',',usecols=usecols)

    df['year']= df['year'].astype('int').astype('str') # removing ending zero, then str
    df['month']= df['month'].astype('int').astype('str')
    df['day']= df['day'].astype('int').astype('str')
    df['hour']= df['hour'].astype('int').astype('str')
    df['minute']= df['minute'].astype('int').astype('str')
    df['second'] = '0'
    #construct datetime
    df['time'] = pd.to_datetime(df[['year', 'month', 'day', 'hour', 'minute', 'second']], format='%Y%m%dT%H%M%S')

    ip.renameCol(df,'latitude', 'lat')
    ip.renameCol(df,'longitude', 'lon')
    # renaming Variables
    ip.renameCol(df,'theta', 'theta_potential_temperature')
    ip.renameCol(df,'sigma0', 'sigma0_potential_density')
    ip.renameCol(df,'sigma1', 'sigma1_potential_density_ref_1000_dbar')
    ip.renameCol(df,'sigma2', 'sigma2_potential_density_ref_2000_dbar')
    ip.renameCol(df,'sigma3', 'sigma3_potential_density_ref_3000_dbar')
    ip.renameCol(df,'sigma4', 'sigma4_potential_density_ref_4000_dbar')

    ip.renameCol(df,'gamma', 'gamma_neutral_density')
    ip.renameCol(df,'TAlk', 'TAlk_total_alkalinity')
    ip.renameCol(df,'phts25p0', 'phts25p0_pH_25C_0dbar')
    ip.renameCol(df,'phtsinsitutp', 'phtsinsitutp_pH_insitu')
    ip.renameCol(df,'latitude', 'lat')
    ip.renameCol(df,'latitude', 'lat')
    ip.renameCol(df,'latitude', 'lat')
    ip.renameCol(df,'latitude', 'lat')
    ip.renameCol(df,'latitude', 'lat')
    ip.renameCol(df,'latitude', 'lat')



    #import cruise data to ID file and do join
    expocodes= pd.read_csv(rawFilePath + rawFileName_expocodes, sep='\t', names=['cruise_ID', 'expocode'])
    df = pd.merge(df,expocodes, left_on = 'cruise',right_on = 'cruise_ID')
    df = df.drop('cruise_ID',1)
    ip.renameCol(df,'expocode', 'cruise_expocode')

    df = ip.arrangeColumns(usecols_rearange, df)
    df = ip.removeMissings(['time','lat', 'lon', 'depth'], df)
    df = ip.NaNtoNone(df)
    df = ip.colDatatypes(df)
    df = ip.convertYYYYMMDD(df)
    df = ip.addIDcol(df)
    df.to_csv(export_path, index=False)
    ip.sortByTimeLatLonDepth(df, export_path, 'time', 'lat', 'lon', 'depth')
    print('export path: ' ,export_path)
    return export_path, df

# df = makeGLODAP(rawFilePath, rawFileName, tableName)

export_path, df = makeGLODAP(rawFilePath, rawFileName, tableName)


#
iF.toSQLbcp(export_path, tableName)
