import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import config_vault as cfgv
import pandas as pd

############################
########### OPTS ###########

tableName = 'tblCruises'
rawFilePath = cfgv.rep_gradients_2_raw
rawFileName_sfl = 'gradients2_seaflow.csv'
rawFileName_r2r_nav = 'gradients2_r2r_nav.csv'

############################

usecols_sfl=['DATE', 'LAT', 'LON', 'CONDUCTIVITY', 'SALINITY','OCEAN TEMP','PAR']
usecols_r2r_nav=['iso_time','ship_longitude','ship_latitude']

# df_sfl = pd.read_csv(rawFilePath + rawFileName_sfl,  sep='\t',usecols = ['DATE', 'LAT', 'LON', 'CONDUCTIVITY', 'SALINITY','OCEAN TEMP','PAR'])
# df_r2r_nav = pd.read_csv(rawFilePath + rawFileName_r2r_nav,  sep=',', skiprows=16)

""" merge the two with null values for temp/SALINITY etc  on missing times """

def makeGradients2(rawFilePath, rawFileName_sfl,rawFileName_r2r_nav, tableName):
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    df_sfl = pd.read_csv(rawFilePath + rawFileName_sfl,  sep='\t',usecols = usecols_sfl)
    df_r2r_nav = pd.read_csv(rawFilePath + rawFileName_r2r_nav,  sep=',', skiprows=16,usecols = usecols_r2r_nav)

    df_sfl['DATE'] = pd.to_datetime(df_sfl['DATE'], format='%Y-%m-%dT%H:%M:%S')
    df_r2r_nav['iso_time'] = pd.to_datetime(df_r2r_nav['iso_time'], format='%Y-%m-%dT%H:%M:%S', errors = 'coerce')

    df_sfl.rename(columns={
    'DATE': 'time',
    'LAT': 'lat',
    'LON': 'lon',
    'CONDUCTIVITY': 'conductivity',
    'SALINITY': 'salinity',
    'OCEAN TEMP': 'temperature'}, inplace=True)

    df_r2r_nav.rename(columns={
    'iso_time': 'time',
    'ship_latitude': 'lat',
    'ship_longitude': 'lon'}, inplace=True)

    return df_sfl, df_r2r_nav
    # df = ip.NaNtoNone(df)
    # df = ip.colDatatypes(df)
    # df = ip.convertYYYYMMDD(df)
    # df = ip.addIDcol(df)
    # df = ip.removeDuplicates(df)
    # df['lon'] = df['lon'].abs()
    # df.to_csv(export_path, index=False)
    # ip.mapTo180180(export_path, 'lon')
    # ip.sortByTimeLatLonDepth(df, export_path, 'time', 'lat', 'lon', 'depth')
    # print('export path: ' ,export_path)
    # return export_path
#
#
#
df_sfl, df_r2r_nav = makeGradients2(rawFilePath, rawFileName_sfl,rawFileName_r2r_nav, tableName)
# iF.toSQLbcp(export_path, tableName)
