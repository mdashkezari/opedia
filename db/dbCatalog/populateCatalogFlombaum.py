

""" set all variables for flombaum table and insert them into supporting tables"""

import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

import sys
sys.path.append('../../config')
import config_vault as cfgv
sys.path.append('../../lib')
import dateLib as dl
sys.path.append('../')
import dbCore as dc

import catalogInsert as cI
import os
import numpy as np
import pandas as pd
import pyodbc
import pandas.io.sql as sql
from datetime import datetime
import time
import math
import sqlalchemy

""" start w/ tblDatasets """

###################################################
tableName = 'tblFlombaum'
Variables = 'prochlorococcus_abundance_flombaum, synechococcus_abundance_flombaum'
Dataset_Name = 'flombaum'


""" dbo.tblDatasets"""

def tblDatasets(): # [ID] [DB],[Dataset_Name],[Dataset_Long_Name],[Variables],[Data_Source],[Distributor],[Description],[Climatology]
    DB = 'Opedia'
    Dataset_Name = 'Flombaum'
    Dataset_Long_Name = 'Global Database of Prochlorococcus and Synechococcus'
    Variables = 'prochlorococcus_abundance_flombaum, synechococcus_abundance_flombaum'
    variable_string = " ".join(Variables)
    Data_Source = 'Pedro Flombaum (pflombaum@cima.fcen.uba.ar)'
    Distributor = 'http://gdps.cima.fcen.uba.ar/ -'
    Description = 'Historical abundance of Prochlorococcus and Synechococcus from 1987 to 2008 from various studies, compiled by Flombaum et al. PNAS 2013.'
    Climatology = 'NULL'

    """ create a tuple out of variables and columns -- in future edit Climatology should be part of insert prep function to reduce repitition """
    if Climatology == 'NULL':
        columnList = """(DB,Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description)"""
        query = (DB,Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description)
    elif Climatology == '1':
        columnList = """(DB,Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology)"""
        query = (DB,Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology)

    print('Inserting Flombaum data into tblDatasets')
    cI.lineInsert('[opedia].[dbo].[tblDatasets]', columnList, query)
    print('Insert Successful')

"""   DELETE FROM [Opedia].[dbo].[tblDatasets] WHERE ID='  '; """



def tblDataset_References():
    """ [Opedia].[dbo].[tblDataset_References] """
    Dataset_Name = 'flombaum'
    reference_list = ['https://doi.org/10.1073/pnas.1307701110']

    IDvar = cI.findID(Dataset_Name, 'tblDatasets')
    columnList = """(Dataset_ID, Reference)"""

    for ref in reference_list:

        query = (IDvar, ref)

        print(columnList, query)
        cI.lineInsert('[opedia].[dbo].[tblDataset_References]', columnList, query)



def tblVariables():

    # """ [Opedia].[dbo].[tblVariables] """

    DB = 'Opedia'
    Dataset_ID = cI.findID(Dataset_Name, 'tblDatasets')
    Table_Name = tableName
    Short_Name_list = ['prochlorococcus_abundance_flombaum', 'synechococcus_abundance_flombaum']
    Long_Name_list = ['Prochlorococcus abundance', 'Synechococcus abundance']
    Unit = 'cells/ml'
    Temporal_Res_ID = '7' # Irregular
    Spatial_Res_ID = '1' # Irregular
    Temporal_Coverage_Begin = '1987-09-17'
    Temporal_Coverage_End = '2008-11-10'
    Lat_Coverage_Begin = 'NULL'
    Lat_Coverage_End = 'NULL'
    Lon_Coverage_Begin = 'NULL'
    Lon_Coverage_End = 'NULL'
    Grid_Mapping = 'NULL'
    Make_ID = '1' # Observation
    Sensor_ID = '2' # in-situ
    Process_ID = '2' # reprocessed
    Study_Domain_ID = '3' # biology
    Keyword_list = ['flombaum prochloro prochlorococcus prochlorococcus_abundance flow cytometry abundance insitu in-situ observation rep reprocessed bio biology cruise cyanobacteria global distributions',
                    'flombaum synecho synechococcus synechococcus_abundance flow cytometry abundance insitu in-situ observation rep reprocessed bio biology cruise cyanobacteria global distributions']
    Comment = 'NULL'

    columnList = """(DB, Dataset_ID, Table_Name, Short_Name, Long_Name, Unit, Temporal_Res_ID, Spatial_Res_ID, Temporal_Coverage_Begin, Temporal_Coverage_End, Lat_Coverage_Begin, Lat_Coverage_End, Lon_Coverage_Begin, Lon_Coverage_End, Grid_Mapping, Make_ID, Sensor_ID, Process_ID, Study_Domain_ID, Keywords,Comment)"""
    for Short_Name, Long_Name, Keywords in zip(Short_Name_list, Long_Name_list, Keyword_list):
        query =     (DB, Dataset_ID, Table_Name, Short_Name, Long_Name, Unit, Temporal_Res_ID, Spatial_Res_ID, Temporal_Coverage_Begin, Temporal_Coverage_End, Lat_Coverage_Begin, Lat_Coverage_End, Lon_Coverage_Begin, Lon_Coverage_End, Grid_Mapping, Make_ID, Sensor_ID, Process_ID, Study_Domain_ID, Keywords, Comment)
        cI.lineInsert('[opedia].[dbo].[tblVariables]', columnList, query)

    #"""DELETE FROM [Opedia].[dbo].[tblVariables]  WHERE [Table_Name] = 'tblFlombaum'"""

tblDatasets()
tblDataset_References()
tblVariables()




# cI.deleteCatalogTables('Flombaum')

#
#
#
# -- DELETE FROM [Opedia].[dbo].[tblDataset_References] WHERE Dataset_ID = '52';
#
# -- DELETE FROM [Opedia].[dbo].[tblVariables] WHERE Table_Name = 'tblFlombaum';
#
#
# -- DELETE FROM [Opedia].[dbo].[tblDatasets] WHERE Dataset_Name = 'Flombaum';
