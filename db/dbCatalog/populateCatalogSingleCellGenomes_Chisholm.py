import sys
sys.path.append('../')
import insertFunctions as iF
import config_vault as cfgv
import pandas as pd
import catalogFunctions as cF
sys.path.append('../dbInsert/')
import insertPrep as ip


tableName = 'tblSingleCellGenomes_Chisholm'
rawFilePath = cfgv.rep_SingleCellGenomes_Chisholm_raw
rawFileName = 'SingleCellGenomesOfProchlorococcusSynechococcusAndSympatricMicrobes_2019-04-06_v1.0.xlsx'
############################



dataset_metadata = pd.read_excel(rawFilePath + rawFileName, sheet_name = 1)
vars_metadata = pd.read_excel(rawFilePath + rawFileName,sheet_name = 2)


""" Strings """
DB='Opedia'
Dataset_Name = 'tblSingleCellGenomes_Chisholm'
Dataset_Long_Name = dataset_metadata.iloc[0]['dataset_long_name']
Data_Source = dataset_metadata.iloc[0]['dataset_source']
Distributor = 'https://chisholmlab.mit.edu/'
Description = dataset_metadata.iloc[0]['dataset_description']
Climatology = 'NULL'
Variables =  ', '.join(list(vars_metadata['var_short_name']))
#
reference_list = (dataset_metadata.iloc[0]['dataset_references']).split(",")
# #
DB_list = [DB] * len(vars_metadata)
Dataset_Name_list = [Dataset_Name] * len(vars_metadata)
short_name_list = list(vars_metadata['var_short_name'])
long_name_list = list(vars_metadata['var_long_name'])
unit_list =    list(ip.NaNtoNone(vars_metadata['var_unit']))
#
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
Study_Domain_ID_list = ['6'] * len(vars_metadata)





# print(' DB ' , len(DB), '\n', 'Dataset_Name ' , len(Dataset_Name), '\n', 'Dataset_Long_Name ' , len(Dataset_Long_Name), '\n', 'Variables ' ,
#  len(Variables), '\n', 'Dataset Source ' , len(Data_Source), '\n', 'Distributor ' , len(Distributor), '\n', 'Description ' , len(Description), '\n', 'Climatology ' ,  len(Climatology))
# print(' DB ' , len(DB), '\n', 'Dataset_Name ' , len(Dataset_Name), '\n', 'Dataset_Long_Name ' , len(Dataset_Long_Name), '\n', 'Variables ' ,
#  len(Variables), '\n', 'Dataset Source ' , len(Data_Source), '\n', 'Distributor ' , len(Distributor), '\n', 'Description ' , len(Description), '\n', 'Climatology ' ,  len(Climatology))
Variables = 'More than 50 variables: details can be found in tblVariables'
Data_Source = 'Chisolm Lab - DOI: 10.1038/sdata.2018.154'
reference_list = [Data_Source]

# cF.tblDatasets(DB, Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology)
# cF.tblDataset_References(Dataset_Name, reference_list)
# cF.tblVariables(DB_list, Dataset_Name_list, short_name_list, long_name_list, unit_list,temporal_res_list, spatial_res_list, Temporal_Coverage_Begin_list, Temporal_Coverage_End_list, Lat_Coverage_Begin_list, Lat_Coverage_End_list, Lon_Coverage_Begin_list, Lon_Coverage_End_list, Grid_Mapping_list,Make_ID_list, Sensor_ID_list, Process_ID_list, Study_Domain_ID_list, keyword_list, comment_list)
