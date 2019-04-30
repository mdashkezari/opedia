
import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import config_vault as cfgv
import pandas as pd
import glob
import os
import xarray as xr

############################
########### OPTS ###########
tableName = 'tblDarwin_3day'
rawFilePath = cfgv.rep_darwin_3day_raw
rawFileName = 'Chl050.0001.nc'
############################
############################


def makeDarwin_3day(rawFilePath, rawFileName, tableName):
    path = rawFilePath + rawFileName
    prefix = tableName
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    xdf = xr.open_dataset(path)
    for date in list(xdf.tim.values):
        print(date)
        xdf_select = xdf.sel(tim=date)
        df_select = xdf_select.to_dataframe()
        df_select.to_csv(rawFilePath + rawFileName[:-3] + '_' + str(date)[0:10] + '.csv', sep=',')


    csv_list = glob.glob(rawFilePath + '*.csv')
    for datafile in csv_list:
        df = pd.read_csv(datafile)
        df = ip.renameCol(df, 'tim', 'time')
        df = ip.renameCol(df, 'lat_c', 'lat')
        df = ip.renameCol(df, 'lon_c', 'lon')
        df = ip.removeMissings(['time','lat', 'lon'], df)
        df = ip.removeDuplicates(df)
        df = ip.arrangeColumns(['time','lat', 'lon', 'Chl050'], df)
        df = ip.NaNtoNone(df)
        df = ip.colDatatypes(df)
        df = ip.convertYYYYMMDD(df)
        df = ip.addIDcol(df)
        df = ip.removeDuplicates(df)
        print(df.head())
        df.to_csv(exportBase + os.path.basename(datafile), index=False)
        ip.sortByTimeLatLon(df, exportBase + os.path.basename(datafile), 'time', 'lat', 'lon')
        df.to_csv(exportBase + os.path.basename(datafile), index=False)
        export_path = (exportBase + os.path.basename(datafile))

        print('export path: ' ,export_path)
        iF.toSQLbcp(export_path, tableName)



export_path = makeDarwin_3day(rawFilePath, rawFileName, tableName)
iF.toSQLbcp(export_path, tableName)
