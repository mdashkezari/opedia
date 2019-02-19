
import numpy as np
import pandas as pd
import sys
sys.path.append('../')
import dbCore as dc

""" Supporting/catalog table insert functions"""

def lineInsert(tableName, columnList ,query, determinator=',', usr='nrhagen', psw='Rdw10^3pb'):
    conn = dc.dbConnect(usr=usr, psw=psw)
    cursor = conn.cursor()
    insertQuery = """INSERT INTO %s %s VALUES %s """ % (tableName, columnList, query)
    cursor.execute(insertQuery)
    conn.commit()


def findID(datasetName, catalogTable, usr='nrhagen', psw='Rdw10^3pb'):
    """ this function pulls the ID value from the [tblDatasets] for the tblDataset_References to use """
    """input tablename ['flombaum'] and catalog table table ['tblDatasets'], output ID? """

    conn = dc.dbConnect(usr=usr, psw=psw)
    cursor = conn.cursor()
    cur_str = """select [ID] FROM [Opedia].[dbo].[""" + catalogTable + """] WHERE [Dataset_Name] = '""" + datasetName + """'"""
    cursor.execute(cur_str)
    IDvar = (cursor.fetchone()[0])
    return IDvar

def findVariables(datasetName, catalogTable, usr='nrhagen', psw='Rdw10^3pb'):
    """ this function pulls the ID value from the [tblDatasets] for the tblDataset_References to use """
    """input tablename ['flombaum'] and catalog table table ['tblDatasets'], output ID? """

    conn = dc.dbConnect(usr=usr, psw=psw)
    cursor = conn.cursor()
    cur_str = """select [Variables] FROM [Opedia].[dbo].[""" + catalogTable + """] WHERE [Dataset_Name] = '""" + datasetName + """'"""
    cursor.execute(cur_str)
    IDvar = (cursor.fetchone()[0])
    varlist = IDvar.split(',')
    return varlist

def deleteCatalogTables(datasetName, usr='nrhagen', psw='Rdw10^3pb'):
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
