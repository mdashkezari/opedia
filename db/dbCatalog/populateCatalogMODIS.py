

import catalogFunctions as cF

""" MODIS Catalog Table"""

""" Strings """
DB='Opedia'
Dataset_Name = 'tblModis_AOD_REP'

Dataset_Long_Name = 'MODIS Aerosol Optical Depth Reprocessed'
Data_Source = 'LAADS DAAC - Goddard Space Flight Center - NASA'
Distributor = 'https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/l3-atmosphere/MYD08_M3/'
Description = 'MYD08_M3 is a level-3 MODIS gridded atmosphere monthly global joint product'
Climatology = 'NULL'
Temporal_Res_ID = '3' #daily
Spatial_Res_ID = '8' # 1x1 degree
Temporal_Coverage_Begin = cF.findMinMaxDate(Dataset_Name)['minDate']
Temporal_Coverage_End = cF.findMinMaxDate(Dataset_Name)['maxDate']
Lat_Coverage_Begin = cF.findSpatialBounds(Dataset_Name)['minLat']
Lat_Coverage_End = cF.findSpatialBounds(Dataset_Name)['maxLat']
Lon_Coverage_Begin = cF.findSpatialBounds(Dataset_Name)['minLon']
Lon_Coverage_End = cF.findSpatialBounds(Dataset_Name)['maxLon']
Grid_Mapping = 'CRS'
Make_ID = '1' #Observation
Sensor_ID = '1' # Satellite
Process_ID = '2' # Reprocessed
Study_Domain_ID = '1' # Physics
Comment = 'The variable name from the original MODIS dataset was: Deep_Blue_Aerosol_Optical_Depth_Land_Mean_Mean'

""" Lists """
Variables = ['AOD']
reference_list = ['Platnick, S., et al., 2015. MODIS Atmosphere L3 Monthly Product. NASA MODIS Adaptive Processing System, Goddard Space Flight Center, USA' ,'http://dx.doi.org/10.5067/MODIS/MYD08_M3.061']
Short_Name_list = ['AOD']
Long_Name_list = ['Aerosol Optical Depth']
Unit_list = [' ']
Keyword_list = ['AOD Aerosol Optical Depth MODIS Atmosphere Reprocessed Satellite Dust Particles NASA Aqua Terra Global']


# cF.tblDatasets(DB, Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology)
# cF.tblDataset_References(Dataset_Name, reference_list)
# cF.tblVariables(DB, Dataset_Name, Short_Name_list, Long_Name_list, Unit_list, Temporal_Res_ID, Spatial_Res_ID, Temporal_Coverage_Begin, Temporal_Coverage_End, Lat_Coverage_Begin, Lat_Coverage_End, Lon_Coverage_Begin, Lon_Coverage_End, Grid_Mapping,Make_ID, Sensor_ID, Process_ID, Study_Domain_ID, Keyword_list, Comment)
