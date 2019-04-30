
import sys
sys.path.append('../')
import insertFunctions as iF
import config_vault as cfgv
import pandas as pd
import catalogFunctions as cF
sys.path.append('../dbInsert/')
import insertPrep as ip


tableName = 'tblFlombaum'
rawFilePath = cfgv.rep_flombaum_raw
rawFileName = 'flombaum.xlsx'
############################

dataset_metadata = pd.read_excel(rawFilePath + rawFileName, sheet_name = 1)
vars_metadata = pd.read_excel(rawFilePath + rawFileName,sheet_name = 2)



""" Strings """
DB='Opedia'
Dataset_Name = 'tblFlombaum'
Dataset_Long_Name = dataset_metadata.iloc[0]['dataset_long_name']
Data_Source = dataset_metadata.iloc[0]['dataset_source']
Distributor = 'Pedro Flombaum (pflombaum@cima.fcen.uba.ar)'
Description = dataset_metadata.iloc[0]['dataset_description']
Climatology = 'NULL'
Variables =  ', '.join(list(vars_metadata['var_short_name']))
#
reference_list = (dataset_metadata.iloc[0]['dataset_references']).split(",")
# # #
DB_list = [DB] * len(vars_metadata)
Dataset_Name_list = [Dataset_Name] * len(vars_metadata)
short_name_list = list(vars_metadata['var_short_name'])
long_name_list = list(vars_metadata['var_long_name'])
unit_list =    list(ip.NaNtoNone(vars_metadata['var_unit']))
# #
spatial_res_list = list('1') * len(vars_metadata)# Irregular
temporal_res_list = list('1') * len(vars_metadata) # Irregular
#
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
Study_Domain_ID_list = ['9','9']


# print(' DB ' , len(DB), '\n', 'Dataset_Name ' , len(Dataset_Name), '\n', 'Dataset_Long_Name ' , len(Dataset_Long_Name), '\n', 'Variables ' ,
#  len(Variables), '\n', 'Dataset Source ' , len(Data_Source), '\n', 'Distributor ' , len(Distributor), '\n', 'Description ' , len(Description), '\n', 'Climatology ' ,  len(Climatology))
# print(' DB ' , len(DB), '\n', 'Dataset_Name ' , len(Dataset_Name), '\n', 'Dataset_Long_Name ' , len(Dataset_Long_Name), '\n', 'Variables ' ,
#  len(Variables), '\n', 'Dataset Source ' , len(Data_Source), '\n', 'Distributor ' , len(Distributor), '\n', 'Description ' , len(Description), '\n', 'Climatology ' ,  len(Climatology))
# print(len(DB_list),len(Dataset_Name_list),len(short_name_list),len(long_name_list),len(unit_list),len(temporal_res_list),len(spatial_res_list),len(Temporal_Coverage_Begin_list),len(Temporal_Coverage_End_list),len(Lat_Coverage_Begin_list),len(Lat_Coverage_End_list),len(Lon_Coverage_Begin_list),len(Lon_Coverage_End_list),len(Grid_Mapping_list),len(Make_ID_list),len(Sensor_ID_list),len(Process_ID_list),len(Study_Domain_ID_list),len(keyword_list),len(comment_list))



# cF.tblDatasets(DB, Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology)
# cF.tblDataset_References(Dataset_Name, reference_list)
# cF.tblVariables(DB_list, Dataset_Name_list, short_name_list, long_name_list, unit_list,temporal_res_list, spatial_res_list, Temporal_Coverage_Begin_list, Temporal_Coverage_End_list, Lat_Coverage_Begin_list, Lat_Coverage_End_list, Lon_Coverage_Begin_list, Lon_Coverage_End_list, Grid_Mapping_list,Make_ID_list, Sensor_ID_list, Process_ID_list, Study_Domain_ID_list, keyword_list, comment_list)











































#
# """ set all variables for flombaum table and insert them into supporting tables"""
#
# import warnings
# warnings.filterwarnings("ignore", message="numpy.dtype size changed")
# warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
#
# import sys
# sys.path.append('../../config')
# import config_vault as cfgv
# sys.path.append('../../lib')
# import dateLib as dl
# sys.path.append('../')
# import dbCore as dc
#
# import catalogInsert as cI
# import os
# import numpy as np
# import pandas as pd
# import pyodbc
# import pandas.io.sql as sql
# from datetime import datetime
# import time
# import math
# import sqlalchemy
#
# """ start w/ tblDatasets """
#
# ###################################################
# tableName = 'tblFlombaum'
# Variables = 'prochlorococcus_abundance_flombaum, synechococcus_abundance_flombaum'
# Dataset_Name = 'flombaum'
#
#
# """ dbo.tblDatasets"""
#
# def tblDatasets(): # [ID] [DB],[Dataset_Name],[Dataset_Long_Name],[Variables],[Data_Source],[Distributor],[Description],[Climatology]
#     DB = 'Opedia'
#     Dataset_Name = 'Flombaum'
#     Dataset_Long_Name = 'Global Database of Prochlorococcus and Synechococcus'
#     Variables = 'prochlorococcus_abundance_flombaum, synechococcus_abundance_flombaum'
#     variable_string = " ".join(Variables)
#     Data_Source = 'Pedro Flombaum (pflombaum@cima.fcen.uba.ar)'
#     Distributor = 'http://gdps.cima.fcen.uba.ar/ -'
#     Description = 'Historical abundance of Prochlorococcus and Synechococcus from 1987 to 2008 from various studies, compiled by Flombaum et al. PNAS 2013.'
#     Climatology = 'NULL'
#
#     """ create a tuple out of variables and columns -- in future edit Climatology should be part of insert prep function to reduce repitition """
#     if Climatology == 'NULL':
#         columnList = """(DB,Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description)"""
#         query = (DB,Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description)
#     elif Climatology == '1':
#         columnList = """(DB,Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology)"""
#         query = (DB,Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology)
#
#     print('Inserting Flombaum data into tblDatasets')
#     cI.lineInsert('[opedia].[dbo].[tblDatasets]', columnList, query)
#     print('Insert Successful')
#
# """   DELETE FROM [Opedia].[dbo].[tblDatasets] WHERE ID='  '; """
#
#
#
# def tblDataset_References():
#     """ [Opedia].[dbo].[tblDataset_References] """
#     Dataset_Name = 'flombaum'
#     reference_list = ['https://doi.org/10.1073/pnas.1307701110']
#
#     IDvar = cI.findID(Dataset_Name, 'tblDatasets')
#     columnList = """(Dataset_ID, Reference)"""
#
#     for ref in reference_list:
#
#         query = (IDvar, ref)
#
#         print(columnList, query)
#         cI.lineInsert('[opedia].[dbo].[tblDataset_References]', columnList, query)
#
#
#
# def tblVariables():
#
#     # """ [Opedia].[dbo].[tblVariables] """
#
#     DB = 'Opedia'
#     Dataset_ID = cI.findID(Dataset_Name, 'tblDatasets')
#     Table_Name = tableName
#     Short_Name_list = ['prochlorococcus_abundance_flombaum', 'synechococcus_abundance_flombaum']
#     Long_Name_list = ['Prochlorococcus abundance', 'Synechococcus abundance']
#     Unit = 'cells/ml'
#     Temporal_Res_ID = '7' # Irregular
#     Spatial_Res_ID = '1' # Irregular
#     Temporal_Coverage_Begin = '1987-09-17'
#     Temporal_Coverage_End = '2008-11-10'
#     Lat_Coverage_Begin = 'NULL'
#     Lat_Coverage_End = 'NULL'
#     Lon_Coverage_Begin = 'NULL'
#     Lon_Coverage_End = 'NULL'
#     Grid_Mapping = 'NULL'
#     Make_ID = '1' # Observation
#     Sensor_ID = '2' # in-situ
#     Process_ID = '2' # reprocessed
#     Study_Domain_ID = '3' # biology
#     Keyword_list = ['flombaum prochloro prochlorococcus prochlorococcus_abundance flow cytometry abundance insitu in-situ observation rep reprocessed bio biology cruise cyanobacteria global distributions',
#                     'flombaum synecho synechococcus synechococcus_abundance flow cytometry abundance insitu in-situ observation rep reprocessed bio biology cruise cyanobacteria global distributions']
#     Comment = 'NULL'
#
#     columnList = """(DB, Dataset_ID, Table_Name, Short_Name, Long_Name, Unit, Temporal_Res_ID, Spatial_Res_ID, Temporal_Coverage_Begin, Temporal_Coverage_End, Lat_Coverage_Begin, Lat_Coverage_End, Lon_Coverage_Begin, Lon_Coverage_End, Grid_Mapping, Make_ID, Sensor_ID, Process_ID, Study_Domain_ID, Keywords,Comment)"""
#     for Short_Name, Long_Name, Keywords in zip(Short_Name_list, Long_Name_list, Keyword_list):
#         query =     (DB, Dataset_ID, Table_Name, Short_Name, Long_Name, Unit, Temporal_Res_ID, Spatial_Res_ID, Temporal_Coverage_Begin, Temporal_Coverage_End, Lat_Coverage_Begin, Lat_Coverage_End, Lon_Coverage_Begin, Lon_Coverage_End, Grid_Mapping, Make_ID, Sensor_ID, Process_ID, Study_Domain_ID, Keywords, Comment)
#         cI.lineInsert('[opedia].[dbo].[tblVariables]', columnList, query)
#
#     #"""DELETE FROM [Opedia].[dbo].[tblVariables]  WHERE [Table_Name] = 'tblFlombaum'"""
#
# tblDatasets()
# tblDataset_References()
# tblVariables()
#
#
#
#
# cI.deleteCatalogTables('Flombaum')
#
# #
# #
# #
# # -- DELETE FROM [Opedia].[dbo].[tblDataset_References] WHERE Dataset_ID = '52';
# #
# # -- DELETE FROM [Opedia].[dbo].[tblVariables] WHERE Table_Name = 'tblFlombaum';
# #
# #
# # -- DELETE FROM [Opedia].[dbo].[tblDatasets] WHERE Dataset_Name = 'Flombaum';
