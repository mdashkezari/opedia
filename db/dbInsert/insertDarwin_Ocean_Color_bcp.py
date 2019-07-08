
import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import config_vault as cfgv
import pandas as pd
import io
import numpy as np
import glob
import xarray as xr
import os.path

############################
########### OPTS ###########
tableName = 'tblDarwin_Ocean_Color'
rawFilePath = '/media/nrhagen/Drobo/OpediaVault/model/darwin_Ocean_Color/rep/'
netcdf_list = glob.glob(rawFilePath + '*.nc')
exportBase = cfgv.opedia_proj + 'db/dbInsert/export_temp/'
prefix = tableName
export_path = '%s%s.csv' % (exportBase, prefix)
############################
############################


processed_csv_list = glob.glob(rawFilePath + '*darwin_v0.2_cs510_ocean_color*.csv*')
sorted_csvlist = np.sort(processed_csv_list).tolist()

for sorted_csv in sorted_csvlist:
    if os.path.isfile(sorted_csv[:-3] + '_BCP.txt'):
        print(sorted_csv[:-4] + ' already inserted into db. Passing')
        pass
    else:
        print('Inserting ' + sorted_csv[:-4] + ' into db')
        iF.toSQLbcp(sorted_csv, tableName)
        file = open(exportBase + os.path.basename(sorted_csv)[:-3] + '_BCP.txt', "w")
        file.close()
