import sys
sys.path.append('../')
import insertFunctions as iF
import config_vault as cfgv
import pandas as pd
import catalogFunctions as cF
sys.path.append('../dbInsert/')
import insertPrep as ip

tableName = 'tblDarwin_Phytoplankton'
rawFileName = cfgv.code_darwin_Phytoplankton_raw + 'darwin_phytoplankton_metadata.xlsx'
############################
DB_id = '94'
var_id_list = ['1277','1278','1279','1280','1281']

dataset_metadata = pd.read_excel(rawFileName, sheet_name = 'dataset_meta_data')
vars_metadata = pd.read_excel(rawFileName,sheet_name = 'vars_meta_data')

""" Strings """
DB='Opedia'
Table_Name = 'tblDarwin_Phytoplankton'
Dataset_Name = 'tblDarwin_Phytoplankton'#dataset_metadata.iloc[0]['dataset_short_name']
Dataset_Long_Name = dataset_metadata.iloc[0]['dataset_long_name']
Data_Source = dataset_metadata.iloc[0]['dataset_doi']
Distributor = 'http://darwinproject.mit.edu'
Description = dataset_metadata.iloc[0]['dataset_description']
Climatology = 'NULL'
Variables =  ', '.join(list(vars_metadata['var_short_name']))
reference_list = (dataset_metadata.iloc[0]['dataset_references']).split(",")


DB_list = [DB] * len(vars_metadata)
Dataset_Name_list = [Dataset_Name] * len(vars_metadata)
short_name_list = list(vars_metadata['var_short_name'])
long_name_list = list(vars_metadata['var_long_name'])
unit_list = list(ip.NaNtoNone(vars_metadata['var_unit']))

spatial_res_list = list('2') * len(vars_metadata)# 1/2 x 1/2
temporal_res_list = list('9') * len(vars_metadata) # Three days

keyword_list = list(vars_metadata['var_short_name'] + ', ' + vars_metadata['var_keywords'])
comment_list = list(ip.NaNtoNone(vars_metadata['var_comment']))
# Temporal_Coverage_Begin_list = '1994-01-03' * len(vars_metadata)
# Temporal_Coverage_End_list = '2015-12-30' * len(vars_metadata)
Lat_Coverage_Begin_list = ['-90'] * len(vars_metadata)
Lat_Coverage_End_list = ['90'] * len(vars_metadata)
Lon_Coverage_Begin_list = ['-180'] * len(vars_metadata)
Lon_Coverage_End_list = ['180'] * len(vars_metadata)
Temporal_Coverage_Begin_list = [cF.findMinMaxDate(Table_Name)['minDate']]  * len(vars_metadata)
Temporal_Coverage_End_list = [cF.findMinMaxDate(Table_Name)['maxDate']] * len(vars_metadata)
# Lat_Coverage_Begin_list = [cF.findSpatialBounds(Table_Name)['minLat']] * len(vars_metadata)
# Lat_Coverage_End_list = [cF.findSpatialBounds(Table_Name)['maxLat']] * len(vars_metadata)
# Lon_Coverage_Begin_list = [cF.findSpatialBounds(Table_Name)['minLon']] * len(vars_metadata)
# Lon_Coverage_End_list = [cF.findSpatialBounds(Table_Name)['maxLon']] * len(vars_metadata)
Grid_Mapping_list = ['CRS']  * len(vars_metadata)
Make_ID_list = ['2'] * len(vars_metadata)#Model
Sensor_ID_list = ['3'] * len(vars_metadata) # Blend
Process_ID_list = ['2'] * len(vars_metadata) # Reprocessed
Study_Domain_ID_list = ['4'] * len(vars_metadata)

# print(DB_list, Dataset_Name_list, short_name_list, long_name_list, unit_list,temporal_res_list, spatial_res_list, Temporal_Coverage_Begin_list, Temporal_Coverage_End_list, Lat_Coverage_Begin_list, Lat_Coverage_End_list, Lon_Coverage_Begin_list, Lon_Coverage_End_list, Grid_Mapping_list,Make_ID_list, Sensor_ID_list, Process_ID_list, Study_Domain_ID_list, keyword_list, comment_list)
# print(len(DB_list),len(Dataset_Name_list),len(short_name_list),len(long_name_list),len(unit_list),len(temporal_res_list),len(spatial_res_list),len(Temporal_Coverage_Begin_list),len(Temporal_Coverage_End_list),len(Lat_Coverage_Begin_list),len(Lat_Coverage_End_list),len(Lon_Coverage_Begin_list),len(Lon_Coverage_End_list),len(Grid_Mapping_list),len(Make_ID_list),len(Sensor_ID_list),len(Process_ID_list),len(Study_Domain_ID_list),len(keyword_list),len(comment_list))
# print('DB: ', DB, '\n', '\n', 'Dataset_Name: ', Dataset_Name, '\n', '\n', 'Dataset_Long_Name: ',Dataset_Long_Name, '\n', '\n', 'Variables: ',Variables, '\n', '\n', 'Data_Source: ', Data_Source, '\n', '\n', 'Distributor: ', Distributor, '\n', '\n', 'Description: ', Description, '\n', '\n', 'Climatology: ',Climatology)

# print(DB_list, Dataset_Name_list, short_name_list, long_name_list, unit_list,temporal_res_list, spatial_res_list, Temporal_Coverage_Begin_list, Temporal_Coverage_End_list, Lat_Coverage_Begin_list, Lat_Coverage_End_list, Lon_Coverage_Begin_list, Lon_Coverage_End_list, Grid_Mapping_list,Make_ID_list, Sensor_ID_list, Process_ID_list, Study_Domain_ID_list, keyword_list, comment_list)
# print(len(DB_list),len(Dataset_Name_list),len(short_name_list),len(long_name_list),len(unit_list),len(temporal_res_list),len(spatial_res_list),len(Temporal_Coverage_Begin_list),len(Temporal_Coverage_End_list),len(Lat_Coverage_Begin_list),len(Lat_Coverage_End_list),len(Lon_Coverage_Begin_list),len(Lon_Coverage_End_list),len(Grid_Mapping_list),len(Make_ID_list),len(Sensor_ID_list),len(Process_ID_list),len(Study_Domain_ID_list),len(keyword_list),len(comment_list))
# print(DB_list, '\n', '\n', Dataset_Name_list, '\n', '\n', short_name_list, '\n', '\n', long_name_list, '\n', '\n', unit_list, '\n', '\n',temporal_res_list, '\n', '\n', spatial_res_list, '\n', '\n', Temporal_Coverage_Begin_list, '\n', '\n', Temporal_Coverage_End_list, '\n', '\n', Lat_Coverage_Begin_list, '\n', '\n', Lat_Coverage_End_list, '\n', '\n', Lon_Coverage_Begin_list, '\n', '\n', Lon_Coverage_End_list, '\n', '\n', Grid_Mapping_list, '\n', '\n',Make_ID_list, '\n', '\n', Sensor_ID_list, '\n', '\n', Process_ID_list, '\n', '\n', Study_Domain_ID_list, '\n', '\n', keyword_list, '\n', '\n', comment_list)

# cF.tblDatasets(DB_id, DB,Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology)
# cF.tblDataset_References(Dataset_Name, reference_list)
