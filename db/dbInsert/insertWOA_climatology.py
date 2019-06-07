

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
tableName = 'tblWOA_Climatology'
rawFilePath = cfgv.rep_WOA_climatology_raw
variable_list = ['AOU','density','nitrate','o2sat','oxygen','phosphate','salinity','sea_water_electrical_conductivity','sea_water_sigma','silicate', 'temperature'] # glob.glob(rawFilePath + '*')
month_list = ['01','02','03','04','05','06','07','08','09','10','11','12']
opt_cols_all = [0,1,2,10,11,12,13,14]
opt_cols_vars = [10,11,12,13,14]
exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
prefix = tableName
export_path = '%s%s.csv' % (exportBase, prefix)
# ############################
# ############################
def netcdf_2_dataframe(netcdf_file, opt_cols_all):
    xdf = xr.open_dataset(netcdf_file, decode_times=False)
    df = xdf.to_dataframe()
    df.reset_index(inplace=True)
    df = df[df.nbounds == 0]
    df = df.iloc[:, opt_cols_all]
    df.sort_values(['depth','lat','lon'], ascending=[True, True, True], inplace=True)
    return df

def merge_WOA_variables(month):
    AOU_df = netcdf_2_dataframe(glob.glob(rawFilePath + 'AOU/' + '*' + month +'_01.nc')[0], opt_cols_all)
    density_df = netcdf_2_dataframe(glob.glob(rawFilePath + 'density/' + '*' + month +'_01.nc')[0], opt_cols_all)
    o2sat_df = netcdf_2_dataframe(glob.glob(rawFilePath + 'o2sat/' + '*' + month +'_01.nc')[0], opt_cols_all)
    oxygen_df = netcdf_2_dataframe(glob.glob(rawFilePath + 'oxygen/' + '*' + month +'_01.nc')[0], opt_cols_all)
    salinity_df = netcdf_2_dataframe(glob.glob(rawFilePath + 'salinity/' + '*' + month +'_01v2.nc')[0], opt_cols_all)
    sea_water_electrical_conductivity_df = netcdf_2_dataframe(glob.glob(rawFilePath + 'sea_water_electrical_conductivity/' + '*' + month +'_01.nc')[0], opt_cols_all)
    # sea_water_sigma_df = netcdf_2_dataframe(glob.glob(rawFilePath + 'sea_water_sigma/' + '*' + month +'_01.nc')[0], opt_cols_all)
    temperature_df = netcdf_2_dataframe(glob.glob(rawFilePath + 'temperature/' + '*' + month +'_01v2.nc')[0], opt_cols_all)
    nitrate_df = netcdf_2_dataframe(glob.glob(rawFilePath + 'nitrate/' + '*' + month +'_01.nc')[0], opt_cols_all)
    phosphate_df = netcdf_2_dataframe(glob.glob(rawFilePath + 'phosphate/' + '*' + month +'_01.nc')[0], opt_cols_all)
    silicate_df = netcdf_2_dataframe(glob.glob(rawFilePath + 'silicate/' + '*' + month +'_01.nc')[0], opt_cols_all)

    print('adding AOU columns')
    merged_df = AOU_df
    merged_df.insert(3, 'month', month)
    print('adding density columns')
    merged_df[str(density_df.columns[3])], merged_df[str(density_df.columns[4])], merged_df[str(density_df.columns[5])], merged_df[str(density_df.columns[6])], merged_df[str(density_df.columns[7])] = density_df.iloc[:,3], density_df.iloc[:,4], density_df.iloc[:,5], density_df.iloc[:,6], density_df.iloc[:,7]
    print('adding o2sat columns')
    merged_df[str(o2sat_df.columns[3])], merged_df[str(o2sat_df.columns[4])], merged_df[str(o2sat_df.columns[5])], merged_df[str(o2sat_df.columns[6])], merged_df[str(o2sat_df.columns[7])] = o2sat_df.iloc[:,3], o2sat_df.iloc[:,4], o2sat_df.iloc[:,5], o2sat_df.iloc[:,6], o2sat_df.iloc[:,7]
    print('adding oxygen columns')
    merged_df[str(oxygen_df.columns[3])], merged_df[str(oxygen_df.columns[4])], merged_df[str(oxygen_df.columns[5])], merged_df[str(oxygen_df.columns[6])], merged_df[str(oxygen_df.columns[7])] = oxygen_df.iloc[:,3], oxygen_df.iloc[:,4], oxygen_df.iloc[:,5], oxygen_df.iloc[:,6], oxygen_df.iloc[:,7]
    print('adding salinity columns')
    merged_df[str(salinity_df.columns[3])], merged_df[str(salinity_df.columns[4])], merged_df[str(salinity_df.columns[5])], merged_df[str(salinity_df.columns[6])], merged_df[str(salinity_df.columns[7])] = salinity_df.iloc[:,3], salinity_df.iloc[:,4], salinity_df.iloc[:,5], salinity_df.iloc[:,6], salinity_df.iloc[:,7]
    print('adding sea_water_electrical_conductivity columns')
    merged_df[str(sea_water_electrical_conductivity_df.columns[3])], merged_df[str(sea_water_electrical_conductivity_df.columns[4])], merged_df[str(sea_water_electrical_conductivity_df.columns[5])], merged_df[str(sea_water_electrical_conductivity_df.columns[6])], merged_df[str(sea_water_electrical_conductivity_df.columns[7])] = sea_water_electrical_conductivity_df.iloc[:,3], sea_water_electrical_conductivity_df.iloc[:,4], sea_water_electrical_conductivity_df.iloc[:,5], sea_water_electrical_conductivity_df.iloc[:,6], sea_water_electrical_conductivity_df.iloc[:,7]
    # print('adding sea_water_sigma columns')
    # merged_df[str(sea_water_sigma_df.columns[3])], merged_df[str(sea_water_sigma_df.columns[4])], merged_df[str(sea_water_sigma_df.columns[5])], merged_df[str(sea_water_sigma_df.columns[6])], merged_df[str(sea_water_sigma_df.columns[7])] = sea_water_sigma_df.iloc[:,3], sea_water_sigma_df.iloc[:,4], sea_water_sigma_df.iloc[:,5], sea_water_sigma_df.iloc[:,6], sea_water_sigma_df.iloc[:,7]
    print('adding temperature columns')
    merged_df[str(temperature_df.columns[3])], merged_df[str(temperature_df.columns[4])], merged_df[str(temperature_df.columns[5])], merged_df[str(temperature_df.columns[6])], merged_df[str(temperature_df.columns[7])] = temperature_df.iloc[:,3], temperature_df.iloc[:,4], temperature_df.iloc[:,5], temperature_df.iloc[:,6], temperature_df.iloc[:,7]

    print('adding nitrate columns')
    merged_df[str(nitrate_df.columns[3])], merged_df[str(nitrate_df.columns[4])], merged_df[str(nitrate_df.columns[5])], merged_df[str(nitrate_df.columns[6])], merged_df[str(nitrate_df.columns[7])] = nitrate_df.iloc[:,3], nitrate_df.iloc[:,4], nitrate_df.iloc[:,5], nitrate_df.iloc[:,6], nitrate_df.iloc[:,7]
    print('adding phosphate columns')
    merged_df[str(phosphate_df.columns[3])], merged_df[str(phosphate_df.columns[4])], merged_df[str(phosphate_df.columns[5])], merged_df[str(phosphate_df.columns[6])], merged_df[str(phosphate_df.columns[7])] = phosphate_df.iloc[:,3], phosphate_df.iloc[:,4], phosphate_df.iloc[:,5], phosphate_df.iloc[:,6], phosphate_df.iloc[:,7]
    print('adding silicate columns')
    merged_df[str(silicate_df.columns[3])], merged_df[str(silicate_df.columns[4])], merged_df[str(silicate_df.columns[5])], merged_df[str(silicate_df.columns[6])], merged_df[str(silicate_df.columns[7])] = silicate_df.iloc[:,3], silicate_df.iloc[:,4], silicate_df.iloc[:,5], silicate_df.iloc[:,6], silicate_df.iloc[:,7]
    merged_df.rename(columns={
    'A_an': 'AOU_WOA_clim',
    'A_mn': 'AOU_stat_mean_WOA_clim',
    'A_dd': 'AOU_num_obs_WOA_clim',
    'A_sd': 'AOU_stdev_WOA_clim',
    'A_se': 'AOU_stderr_WOA_clim',
    'I_an': 'density_WOA_clim',
    'I_mn': 'density_stat_mean_WOA_clim',
    'I_dd': 'density_num_obs_WOA_clim',
    'I_sd': 'density_stdev_WOA_clim',
    'O_an': 'o2sat_WOA_clim',
    'O_mn': 'o2sat_stat_mean_WOA_clim',
    'O_dd': 'o2sat_num_obs_WOA_clim',
    'O_sd': 'o2sat_stdev_WOA_clim',
    'O_se': 'o2sat_stderr_WOA_clim',
    'o_an': 'oxygen_WOA_clim',
    'o_mn': 'oxygen_stat_mean_WOA_clim',
    'o_dd': 'oxygen_num_obs_WOA_clim',
    'o_sd': 'oxygen_stdev_WOA_clim',
    'o_se': 'oxygen_stderr_WOA_clim',
    's_an': 'salinity_WOA_clim',
    's_mn': 'salinity_stat_mean_WOA_clim',
    's_dd': 'salinity_num_obs_WOA_clim',
    's_sd': 'salinity_stdev_WOA_clim',
    's_se': 'salinity_stderr_WOA_clim',
    'C_an': 'conductivity_WOA_clim',
    'C_mn': 'conductivity_stat_mean_WOA_clim',
    'C_dd': 'conductivity_num_obs_WOA_clim',
    'C_sd': 'conductivity_stdev_WOA_clim',
    't_an': 'sea_water_temp_WOA_clim',
    't_mn': 'sea_water_temp_stat_mean_WOA_clim',
    't_dd': 'sea_water_temp_num_obs_WOA_clim',
    't_sd': 'sea_water_temp_stdev_WOA_clim',
    't_se': 'sea_water_temp_stderr_WOA_clim',
    'n_an': 'nitrate_WOA_clim',
    'n_mn': 'nitrate_stat_mean_WOA_clim',
    'n_dd': 'nitrate_num_obs_WOA_clim',
    'n_sd': 'nitrate_stdev_WOA_clim',
    'n_se': 'nitrate_stderr_WOA_clim',
    'p_an': 'phosphate_WOA_clim',
    'p_mn': 'phosphate_stat_mean_WOA_clim',
    'p_dd': 'phosphate_num_obs_WOA_clim',
    'p_sd': 'phosphate_stdev_WOA_clim',
    'p_se': 'phosphate_stderr_WOA_clim',
    'i_an': 'silicate_WOA_clim',
    'i_mn': 'silicate_stat_mean_WOA_clim',
    'i_dd': 'silicate_num_obs_WOA_clim',
    'i_sd': 'silicate_stdev_WOA_clim',
    'i_se': 'silicate_stderr_WOA_clim'}, inplace=True)
    return merged_df

def makeWOA_climatology(rawFilePath, tableName):
    for month in month_list: # ie 1 = jan
        print('Month: ' + month)
        df = merge_WOA_variables(month)
        df = ip.removeColumn(['I_gp', 'C_gp'], df)
        df = ip.removeMissings(['lat', 'lon', 'depth'], df)
        df = ip.NaNtoNone(df)
        df = ip.addIDcol(df)
        df.sort_values(['lat', 'lon', 'depth'], ascending=[True, True, True], inplace=True)

        df.to_csv(exportBase + tableName + '_' +  month + '.csv', index=False)
        print('export path: ' , exportBase + tableName + '_' +  month + '.csv')
        iF.toSQLbcp(exportBase + tableName + '_' +  month + '.csv', tableName)
makeWOA_climatology(rawFilePath,  tableName)
# export_path = makeSingleCellGenomes_Chisholm(rawFilePath, rawFileName, tableName)
# iF.toSQLbcp(export_path, tableName)
