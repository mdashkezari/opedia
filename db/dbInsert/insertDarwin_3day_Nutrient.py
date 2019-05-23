import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import config_vault as cfgv
import pandas as pd
import glob
import xarray as xr
import os.path

############################
########### OPTS ###########
tableName = 'tblDarwin_Nutrient_3day'
rawFilePath = '/media/nrhagen/Drobo/OpediaVault/model/darwin_3day/'
netcdf_list = glob.glob(rawFilePath + '*.nc')
exportBase = cfgv.opedia_proj + 'db/dbInsert/export_temp/'
prefix = tableName
export_path = '%s%s.csv' % (exportBase, prefix)
############################
############################
path = sys.argv[1]

if os.path.isfile(exportBase + os.path.basename(path)[:-3] + '_DONE.txt'): #checks .txt 'catalog' file exists before reprocessing
    sys.exit(0)
else:
    xdf = xr.open_dataset(path)
    df = xdf.to_dataframe()
    df.reset_index(inplace=True) # converts netcdf dims to cols
    df = ip.renameCol(df, 'lat_c', 'lat')
    df = ip.renameCol(df, 'lon_c', 'lon')
    df = ip.renameCol(df, 'dep_c', 'depth')
    df = ip.convertcolDatatype(df,['FeT', 'PO4', 'DIN', 'SiO2', 'O2'])
    # df = ip.removeMissings(['time','lat', 'lon', 'depth'], df)
    df = ip.arrangeColumns(['time','lat', 'lon','depth', 'FeT', 'PO4', 'DIN', 'SiO2', 'O2'], df)
    df = ip.NaNtoNone(df)
    df = ip.addIDcol(df)
    df = ip.colDatatypes(df)
    df.sort_values(['time', 'lat', 'lon', 'depth'], ascending=[True, True, True, True], inplace=True)
    df.to_csv(exportBase + os.path.basename(path)[:-3] + '.csv', mode='a', chunksize=1000000, index=False)

    # writes .txt file to catalog which files processed
    file = open(exportBase + os.path.basename(path)[:-3] + '_DONE.txt', "w")
    file.close()
