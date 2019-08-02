
import numpy as np
import pandas as pd
import sys
sys.path.append('../')
import dbCore as dc
import catalogInsert as cI
sys.path.append('../login')
import credentials as cr


""" Supporting/catalog table insert functions"""

def lineInsert(tableName, columnList ,query, determinator=',', server = 'Rainier',usr=cr.usr_rainier, psw=cr.psw_rainier):
    conn = dc.dbConnect(usr=usr, psw=psw)
    cursor = conn.cursor()
    insertQuery = """INSERT INTO %s %s VALUES %s """ % (tableName, columnList, query)
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

def findMinMaxDate(tableName):
    cur_str = 'select min(time), max(time) FROM [Opedia].[dbo].[' + tableName + ']'
    df = dc.dbRead(cur_str)
    dates = df.iloc[0].values
    minDate = pd.to_datetime(str(dates[0])).strftime('%Y-%m-%d')
    maxDate = pd.to_datetime(str(dates[1])).strftime('%Y-%m-%d')
    return {'minDate':minDate,
     'maxDate':maxDate}


def findSpatialBounds(tableName):
    cur_str = 'select min(lat), max(lat), min(lon), max(lon) FROM [Opedia].[dbo].[' + tableName + ']'
    df = dc.dbRead(cur_str)
    dates = df.iloc[0].values
    return {'minLat':dates[0],
     'maxLat':dates[1],  'minLon':dates[2],  'maxLon':dates[3]}


def remove_duplicatesCatalogTables(usr='nrhagen', psw='Rdw10^3pb'):
    catalogTableList = [
     'tblDatasets', 'tblDataset_References', 'tblVariables']
    conn = dc.dbConnect(usr=usr, psw=psw)
    cursor = conn.cursor()
    cur_str_tblDatasets = '\n        WITH list_duplicates (Dataset_Name, Dataset_Long_Name, duplicate_count) AS\n        (\n            SELECT Dataset_Name, Dataset_Long_Name,\n        ROW_NUMBER() OVER(PARTITION BY Dataset_Name, Dataset_Long_Name ORDER BY Dataset_Name, Dataset_Long_Name) AS duplicate_count\n        FROM tblDatasets_copy)\n        DELETE FROM list_duplicates WHERE duplicate_count > 1\n        '
    cur_str_tblDataset_References = '\n        WITH list_duplicates (Dataset_ID, Reference, duplicate_count) AS\n        (\n            SELECT Dataset_ID, Reference,\n        ROW_NUMBER() OVER(PARTITION BY Dataset_ID, Reference ORDER BY Dataset_ID, Reference) AS duplicate_count\n        FROM tblDataset_References_copy)\n        DELETE FROM list_duplicates WHERE duplicate_count > 1\n        '
    cur_str_tblVariables = '\n        WITH list_duplicates (Table_Name, Short_Name, Long_Name, duplicate_count) AS\n        (\n            SELECT Table_Name, Short_Name, Long_Name,\n        ROW_NUMBER() OVER(PARTITION BY Table_Name, Short_Name, Long_Name ORDER BY Table_Name, Short_Name, Long_Name) AS duplicate_count\n        FROM tblVariables_copy)\n        DELETE FROM list_duplicates WHERE duplicate_count > 1\n        '
    cursor.execute(tblDatasets)
    cursor.execute(tblDataset_References)
    cursor.execute(tblVariables)

def findVariables(datasetName, catalogTable,server = 'Rainier',usr=cr.usr_rainier, psw=cr.psw_rainier):
    conn = dc.dbConnect(usr=usr, psw=psw)
    cursor = conn.cursor()
    cur_str = """select [Variables] FROM [Opedia].[dbo].[""" + catalogTable + """] WHERE [Dataset_Name] = '""" + datasetName + """'"""
    cursor.execute(cur_str)
    IDvar = (cursor.fetchone()[0])
    varlist = IDvar.split(',')
    return varlist

def deleteCatalogTables(datasetName,server = 'Rainier',usr=cr.usr_rainier, psw=cr.psw_rainier):
    contYN = input('Are you sure you want to delete all of the catalog tables for ' + datasetName + ' ?  [yes/no]: ' )
    if contYN == 'yes':
        """ delete tblVariables, then tblDataset_References then finally tblDatasets """
        print('connecting to database...')
        conn = dc.dbConnect(usr=usr, psw=psw)
        cursor = conn.cursor()
        print('db connection successful')

        Dataset_ID = str(findID(datasetName, catalogTable = 'tblDatasets')) #datasetName
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


def tblDatasets(DB_id,DB, Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology):
    """ create a tuple out of variables and columns -- in future edit Climatology should be part of insert prep function to reduce repitition """
    if Climatology == 'NULL':
        query = (DB_id,DB, Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description)
        columnList = '(ID, DB,Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description)'
        print('Inserting data into tblDatasets')
        # print('[opedia].[dbo].[tblDatasets]', columnList, query)
        cI.lineInsert('[opedia].[dbo].[tblDatasets]', columnList, query)
    else:
        if Climatology == '1':
            columnList = '(ID, DB,Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology)'
            query = (DB_id,DB, Dataset_Name, Dataset_Long_Name, Variables, Data_Source, Distributor, Description, Climatology)
        print('Inserting data into tblDatasets')
        cI.lineInsert('[opedia].[dbo].[tblDatasets]', columnList, query)

def tblDataset_References(Dataset_Name, reference_list):
    IDvar = findID(Dataset_Name, 'tblDatasets')
    columnList = '(Dataset_ID, Reference)'
    for ref in reference_list:
        query = (IDvar, ref)
        cI.lineInsert('[opedia].[dbo].[tblDataset_References]', columnList, query)
    print('Inserting data into tblDataset_References')


def tblVariables(var_id_list,DB_list, Dataset_Name_list, short_name_list, long_name_list, unit_list, temporal_res_list, spatial_res_list, Temporal_Coverage_Begin_list, Temporal_Coverage_End_list, Lat_Coverage_Begin_list, Lat_Coverage_End_list, Lon_Coverage_Begin_list, Lon_Coverage_End_list, Grid_Mapping_list, Make_ID_list, Sensor_ID_list, Process_ID_list, Study_Domain_ID_list, keyword_list, comment_list):
    Dataset_ID_raw = cI.findID(Dataset_Name_list[0], 'tblDatasets')
    dataset_ID_list = [Dataset_ID_raw] * len(DB_list)
    columnList = '(ID,DB, Dataset_ID, Table_Name, Short_Name, Long_Name, Unit, Temporal_Res_ID, Spatial_Res_ID, Temporal_Coverage_Begin, Temporal_Coverage_End, Lat_Coverage_Begin, Lat_Coverage_End, Lon_Coverage_Begin, Lon_Coverage_End, Grid_Mapping, Make_ID, Sensor_ID, Process_ID, Study_Domain_ID, Keywords,Comment)'
    for ID, DB, dataset_ID, Dataset_Name, short_name, long_name, unit, temporal_res, spatial_res, Temporal_Coverage_Begin, Temporal_Coverage_End, Lat_Coverage_Begin, Lat_Coverage_End, Lon_Coverage_Begin, Lon_Coverage_End, Grid_Mapping, Make_ID, Sensor_ID, Process_ID, Study_Domain_ID, keyword, comment in zip(var_id_list,DB_list, dataset_ID_list, Dataset_Name_list, short_name_list, long_name_list, unit_list, temporal_res_list, spatial_res_list, Temporal_Coverage_Begin_list, Temporal_Coverage_End_list, Lat_Coverage_Begin_list, Lat_Coverage_End_list, Lon_Coverage_Begin_list, Lon_Coverage_End_list, Grid_Mapping_list, Make_ID_list, Sensor_ID_list, Process_ID_list, Study_Domain_ID_list, keyword_list, comment_list):
        query = (ID,DB, dataset_ID, Dataset_Name, short_name, long_name, unit, temporal_res, spatial_res, Temporal_Coverage_Begin, Temporal_Coverage_End, Lat_Coverage_Begin, Lat_Coverage_End, Lon_Coverage_Begin, Lon_Coverage_End, Grid_Mapping, Make_ID, Sensor_ID, Process_ID, Study_Domain_ID, keyword, comment)
        cI.lineInsert('[opedia].[dbo].[tblVariables]', columnList, query)
    print('Inserting data into tblVariables')
