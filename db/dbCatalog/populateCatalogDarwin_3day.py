import sys
sys.path.append('../')
import insertFunctions as iF
import config_vault as cfgv
import pandas as pd
import catalogFunctions as cF
sys.path.append('../dbInsert/')
import insertPrep as ip

tableName = 'tblDarwin_3day'
rawFilePath = cfgv.rep_darwin_3day_raw
rawFileName = 'SingleCellGenomesOfProchlorococcusSynechococcusAndSympatricMicrobes_2019-04-06_v1.0.xlsx'
############################

""" MODIS Catalog Table"""

""" Strings """
DB=['Opedia']
Dataset_Name = 'tblDarwin_3day'
Dataset_Long_Name = 'Darwin Biogeochemistry 3 Day Averaged Model'
Data_Source = 'http://darwinproject.mit.edu'
Distributor = 'Chl050 -- This product has been provided by the Simons Collaboration on Computational Biogeochemical Modeling of Marine Ecosystems (https://cbiomes.org/)'
Description = '"The Darwin Project is an initiative to advance the development and application of novel models of marine microbes and microbial communities, identifying the relationships of individuals and communities to their environment, connecting cellular-scale processes to global microbial community structure."      http://darwinproject.mit.edu/'


Climatology = ['NULL']
Temporal_Res_ID = ['9'] #Three days
Spatial_Res_ID = ['3'] # 1/4x1/4 degree
Temporal_Coverage_Begin = [cF.findMinMaxDate(Dataset_Name)['minDate']]
Temporal_Coverage_End = [cF.findMinMaxDate(Dataset_Name)['maxDate']]
Lat_Coverage_Begin = [cF.findSpatialBounds(Dataset_Name)['minLat']]
Lat_Coverage_End = [cF.findSpatialBounds(Dataset_Name)['maxLat']]
Lon_Coverage_Begin = [cF.findSpatialBounds(Dataset_Name)['minLon']]
Lon_Coverage_End = [cF.findSpatialBounds(Dataset_Name)['maxLon']]
Grid_Mapping = ['CRS']
Make_ID = ['2'] #Model
Sensor_ID = ['3'] # Satellite
Process_ID = ['2'] # Reprocessed
Study_Domain_ID = ['4'] # Physics
Comment = ['Test dataset and variable for 3 day averaged darwin data']

""" Lists """
Variables = ['Chl050_darwin_3day']
reference_list = ['http://doi.org/10.5281/zenodo.2621539']
Short_Name_list = ['Chl050_darwin_3day']
Long_Name_list = ['Chl050 concentration (3 day)']
Unit_list = ['mg Chl']
Keyword_list = ['Chl050_darwin_3day Chl050 concentration (3 day) chl050 chl chlorophyll rep reprocessed model darwin mit mitgcm nutrient bio chem biogo biogeochemistry biogeochem ecology blend']
Dataset_Name = ['tblDarwin_3day']

# cF.tblDatasets(DB, Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology)
# cF.tblDataset_References(Dataset_Name, reference_list)
# cF.tblVariables(DB, Dataset_Name, Short_Name_list, Long_Name_list, Unit_list, Temporal_Res_ID, Spatial_Res_ID, Temporal_Coverage_Begin, Temporal_Coverage_End, Lat_Coverage_Begin, Lat_Coverage_End, Lon_Coverage_Begin, Lon_Coverage_End, Grid_Mapping,Make_ID, Sensor_ID, Process_ID, Study_Domain_ID, Keyword_list, Comment)
