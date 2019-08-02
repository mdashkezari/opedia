
import numpy as np
import pandas as pd
import sys
sys.path.append('../')
import dbCore as dc
import catalogInsert as cI

sys.path.append('../login')
import credentials as cr


""" Supporting/catalog table insert functions"""

def lineInsert(tableName, columnList ,query, determinator=',', server = 'Rainier'):
    conn = dc.dbConnect(server)
    cursor = conn.cursor()
    insertQuery = """INSERT INTO %s %s VALUES %s """ % (tableName, columnList, query)
    print(insertQuery)
    cursor.execute(insertQuery)
    conn.commit()


def findID(datasetName, catalogTable, server = 'Rainier'):
    """ this function pulls the ID value from the [tblDatasets] for the tblDataset_References to use """
    conn = dc.dbConnect(server)
    cursor = conn.cursor()
    cur_str = """select [ID] FROM [Opedia].[dbo].[""" + catalogTable + """] WHERE [Dataset_Name] = '""" + datasetName + """'"""
    cursor.execute(cur_str)
    IDvar = (cursor.fetchone()[0])
    return IDvar

def findVariables(datasetName, catalogTable,server = 'Rainier'):
    conn = dc.dbConnect(server)
    cursor = conn.cursor()
    cur_str = """select [Variables] FROM [Opedia].[dbo].[""" + catalogTable + """] WHERE [Dataset_Name] = '""" + datasetName + """'"""
    cursor.execute(cur_str)
    IDvar = (cursor.fetchone()[0])
    varlist = IDvar.split(',')
    return varlist

def deleteCatalogTables(datasetName,server = 'Rainier'):
    contYN = input('Are you sure you want to delete all of the catalog tables for ' + datasetName + ' ?  [yes/no]: ' )
    if contYN == 'yes':
        """ delete tblVariables, then tblDataset_References then finally tblDatasets """
        print('connecting to database...')
        conn = dc.dbConnect(usr=usr, psw=psw)
        cursor = conn.cursor()
        print('db connection successful')

        Dataset_ID = str(findID(datasetName, catalogTable = 'tblDatasets'))
        print('Dataset ID used to remove catalog tables: ', Dataset_ID)

        cur_str = """DELETE FROM [Opedia].[dbo].[tblVariables] WHERE [Dataset_ID] = """ + Dataset_ID
        cursor.execute(cur_str)
        print('-- Instances of ' + datasetName + ' removed from tblVariables')

        cur_str = """DELETE FROM [Opedia].[dbo].[tblDataset_References] WHERE [Dataset_ID] = """ + Dataset_ID
        cursor.execute(cur_str)
        print('-- Instances of ' + datasetName + ' removed from tblDataset_References')

        cur_str = """DELETE FROM [Opedia].[dbo].[tblDatasets] WHERE [ID] = """ + Dataset_ID
        cursor.execute(cur_str)
        print('-- Instances of ' + datasetName + ' removed from tblDatasets')
        print('Commiting changes...')
        conn.commit()
        conn.rollback()
        print('Changes to dB commited')
    else:
        print('Catalog tables for ' + datasetName + ' not deleted')


def tblDatasets(DB, Dataset_Name, Dataset_Long_Name, Variables, variable_string, Data_Source, Distributor, Description, Climatology): # [ID] [DB],[Dataset_Name],[Dataset_Long_Name],[Variables],[Data_Source],[Distributor],[Description],[Climatology]
    """ create a tuple out of variables and columns -- in future edit Climatology should be part of insert prep function to reduce repitition """
    if Climatology == 'NULL':
        query = (DB,Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description)
    elif Climatology == '1':
        columnList = """(DB,Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology)"""
        query = (DB,Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology)
    print('Inserting Flombaum data into tblDatasets')
    lineInsert('[opedia].[dbo].[tblDatasets]', columnList, query)
    print('Insert Successful')

def tblDataset_References(Dataset_Name, reference_list):
    IDvar = findID(Dataset_Name, 'tblDatasets')
    columnList = """(Dataset_ID, Reference)"""
    for ref in reference_list:
        query = (IDvar, ref)
        print(columnList, query)
        cI.lineInsert('[opedia].[dbo].[tblDataset_References]', columnList, query)

def tblVariables(DB, Table_Name, Short_Name_list, Long_Name_list, Unit, Temporal_Res_ID, Spatial_Res_ID, Temporal_Coverage_Begin, Temporal_Coverage_End, Lat_Coverage_Begin, Lat_Coverage_End, Lon_Coverage_Begin, Lon_Coverage_End, Grid_Mapping,Make_ID, Sensor_ID, Process_ID, Study_Domain_ID, Keyword_list, Comment):
    Dataset_ID = cI.findID(Dataset_Name, 'tblDatasets')
    columnList = """(DB, Dataset_ID, Table_Name, Short_Name, Long_Name, Unit, Temporal_Res_ID, Spatial_Res_ID, Temporal_Coverage_Begin, Temporal_Coverage_End, Lat_Coverage_Begin, Lat_Coverage_End, Lon_Coverage_Begin, Lon_Coverage_End, Grid_Mapping, Make_ID, Sensor_ID, Process_ID, Study_Domain_ID, Keywords,Comment)"""
    for Short_Name, Long_Name, Keywords in zip(Short_Name_list, Long_Name_list, Keyword_list):
        query =     (DB, Dataset_ID, Table_Name, Short_Name, Long_Name, Unit, Temporal_Res_ID, Spatial_Res_ID, Temporal_Coverage_Begin, Temporal_Coverage_End, Lat_Coverage_Begin, Lat_Coverage_End, Lon_Coverage_Begin, Lon_Coverage_End, Grid_Mapping, Make_ID, Sensor_ID, Process_ID, Study_Domain_ID, Keywords, Comment)
        lineInsert('[opedia].[dbo].[tblVariables]', columnList, query)
