import sys
sys.path.append('../')
import insertFunctions as iF
import config_vault as cfgv
import pandas as pd
import catalogFunctions as cF
sys.path.append('../dbInsert/')
import insertPrep as ip


""" Mesoscope km 1709 data Catalog Table"""
tableName = 'tblkm1709_mesoscope'
rawFilePath = cfgv.rep_KM1709_mesoscope_raw
rawFileName = 'mesoscope_cmap.xlsx'
############################


dataset_metadata = pd.read_excel(rawFilePath + rawFileName, sheet_name = 1)
vars_metadata = pd.read_excel(rawFilePath + rawFileName,sheet_name = 2)

""" Strings """
DB='Opedia'
Dataset_Name = 'tblkm1709_mesoscope'
Dataset_Long_Name = dataset_metadata.iloc[0]['dataset_long_name']
Data_Source = dataset_metadata.iloc[0]['dataset_source']
Distributor = 'http://scope.soest.hawaii.edu/data/mesoscope/mesoscope.html'
Description = dataset_metadata.iloc[0]['dataset_description']
Climatology = 'NULL'
Variables =  ', '.join(list(vars_metadata['var_short_name']))
#
reference_list = (dataset_metadata.iloc[0]['dataset_references']).split(",")
#
DB_list = [DB] * len(vars_metadata)
Dataset_Name_list = [Dataset_Name] * len(vars_metadata)
short_name_list = list(vars_metadata['var_short_name'])
long_name_list = list(vars_metadata['var_long_name'])
unit_list =    list(ip.NaNtoNone(vars_metadata['var_unit']))

spatial_res_list = list('1') * len(vars_metadata)# Irregular
temporal_res_list = list('1') * len(vars_metadata) # Irregular

keyword_list = list(vars_metadata['var_keywords'])
comment_list = list(ip.NaNtoNone(vars_metadata['var_comment']))
Temporal_Coverage_Begin_list = [cF.findMinMaxDate(Dataset_Name)['minDate']]  * len(vars_metadata)
Temporal_Coverage_End_list = [cF.findMinMaxDate(Dataset_Name)['maxDate']] * len(vars_metadata)
Lat_Coverage_Begin_list = [cF.findSpatialBounds(Dataset_Name)['minLat']] * len(vars_metadata)
Lat_Coverage_End_list = [cF.findSpatialBounds(Dataset_Name)['maxLat']] * len(vars_metadata)
Lon_Coverage_Begin_list = [cF.findSpatialBounds(Dataset_Name)['minLon']] * len(vars_metadata)
Lon_Coverage_End_list = [cF.findSpatialBounds(Dataset_Name)['maxLon']] * len(vars_metadata)
Grid_Mapping_list = ['CRS']  * len(vars_metadata)
Make_ID_list = ['1'] * len(vars_metadata)#Observation
Sensor_ID_list = ['2'] * len(vars_metadata) # In-Situ
Process_ID_list = ['2'] * len(vars_metadata) # Reprocessed
Study_Domain_ID_list = ['1','1','1','1','1','1', '3','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4']







#
# cF.tblDatasets(DB, Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology)
# cF.tblDataset_References(Dataset_Name, reference_list)
# cF.tblVariables(DB_list, Dataset_Name_list, short_name_list, long_name_list, unit_list,temporal_res_list, spatial_res_list, Temporal_Coverage_Begin_list, Temporal_Coverage_End_list, Lat_Coverage_Begin_list, Lat_Coverage_End_list, Lon_Coverage_Begin_list, Lon_Coverage_End_list, Grid_Mapping_list,Make_ID_list, Sensor_ID_list, Process_ID_list, Study_Domain_ID_list, keyword_list, comment_list)
