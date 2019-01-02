#
# """ import raw .csv into df - > run cleaning functions -> export to .csv for faster bulk insert into sql server db"""
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
# import os
# import netcdf as nc
# import numpy as np
# import pandas as pd
# import pyodbc
# import pandas.io.sql as sql
# from datetime import datetime
# import time
# import math
# import insertPrep as ip
# import sqlalchemy as sa
# import turbodbc as todbc
#
#
# def makeBulkFlombaum():
#     path = cfgv.flombaum_raw + 'rep/flombaum.csv'
#     prefix = 'flombaum'
#     df = pd.read_csv(path)
#     df = ip.convertYYYYMMDD(df)
#
#
#     df = ip.removeMissings(['lat', 'lon'], df)   # remove rows with missing lat/lon/abundance
#     df['ID'] = None
#
#     exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
#     export_path = '%s%s.csv' % (exportBase, prefix)
#     print('Export path:', export_path)
#     df.to_csv(export_path, index=False)
#     print(df.head(1))
#     ip.sortByDepthLatLon(df, export_path, 'lon', 'lat', 'depth')
#
#     return export_path
#
#
#
# def turboODBCFlombaum(tablename):
#     dataTitle = 'Flombaum'
#     print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
#     try:
#         bulkPath = ''
#         bulkPath = makeBulkFlombaum()
#         bulkPath = bulkPath
#         print('bulkPath: ', bulkPath, 'tableName: ',  tableName)
#
#
#         connection = todbc.connect(connection_string='Driver={FreeTDS};Server=128.208.239.15;Port=1433;Database=opedia;Uid=nrhagen;Pwd=Rdw10^3pb;')
#         # engine = sa.create_engine('mssql+pyodbc://nrhagen:Rdw10^3pb@128.208.239.15:1433/opedia?driver=FreeTDS')
#         print(connection)
#
#
#         cursor = connection.cursor()
#         print(cursor)
#
#         string = """SELECT TOP (1000) [cruise] ,[time] ,[lat] ,[lon] FROM [Opedia].[dbo].[tblSeaFlow]"""
#
#
#         cursor.execute(string)
#         # for row in cursor:
#         #     print(row)
#         """ import cleaned .csv """
#         df = pd.read_csv(bulkPath, parse_dates=['time'])
#
#         """ convert pandas dataframe to numpy array for ingestion using turbodbc"""
#         dfnp = df.values
#         dfnp_head = dfnp[0,:]
#         print(dfnp_head)
#         # cursor.executemanycolumns("INSERT INTO [dbo].[tblFlombaum] VALUES (?, ?)",
#         #                     dfnp)
#
#         cursor.execute("INSERT INTO TABLE [dbo].[tblFlombaum] VALUES (1995-09-28 00:00:0,-43.0, -264.99, 0.0, 12047.0, 1441.0, nan)")
#
#         # cursor.execute("INSERT INTO TABLE [dbo].[tblFlombaum] VALUES (42, 17)")
#
#         # # df['ID'] = None
#         # print(type(df['time'].iloc[0]))
#         # print(df['time'].iloc[0])
#         # print(engine)
#         # print(df[df['depth'].isnull()])
#         # """ pandas sql insert function """
#         # print('starting table insert.... ')
#         # df.to_sql(tableName, engine, if_exists='replace', index=False, chunksize = 1000)
#
#         #
#         # dc.bulkInsert(bulkPath, tableName)
#
#
#
#     finally:
#         pass
#         # if bulkPath != '':
#         #     os.remove(bulkPath)
#     # print('%s  Done' % datetime.today())
#     return
#
#
# def bulkInsertFlombaum(tableName):
#     dataTitle = 'Flombaum'
#     print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
#     try:
#         bulkPath = ''
#         bulkPath = makeBulkFlombaum()
#         bulkPath = bulkPath
#         print('bulkPath: ', bulkPath, 'tableName: ',  tableName)
#
#
#
#         engine = sa.create_engine('mssql+pyodbc://nrhagen:Rdw10^3pb@128.208.239.15:1433/opedia?driver=FreeTDS')
#
#         """ import cleaned .csv """
#         df = pd.read_csv(bulkPath, parse_dates=['time'])
#         # # df['ID'] = None
#         # print(type(df['time'].iloc[0]))
#         # print(df['time'].iloc[0])
#         # print(engine)
#         # print(df[df['depth'].isnull()])
#         # """ pandas sql insert function """
#         print('starting table insert.... ')
#         df.to_sql(tableName, engine, if_exists='replace', index=False, chunksize = 1000)
#
#         #
#         # dc.bulkInsert(bulkPath, tableName)
#
#
#
#     finally:
#         pass
#         # if bulkPath != '':
#         #     os.remove(bulkPath)
#     # print('%s  Done' % datetime.today())
#     return
#
#
# def toSQLPandasFlombaum(bulkPath, tableName, usr='nrhagen', psw='Rdw10^3pb', ip='128.208.239.15', port='1433', db='Opedia'):
#     pass
#
# tableName = 'tblFlombaum'
# # bulkInsertFlombaum(tableName)
# turboODBCFlombaum(tableName)



""" import raw .csv into df - > run cleaning functions -> export to .csv for faster bulk insert into sql server db"""

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
import os
import netcdf as nc
import numpy as np
import pandas as pd
import pyodbc
import pandas.io.sql as sql
from datetime import datetime
import time
import math
import insertPrep as ip
import sqlalchemy




def makeBulkFlombaum():
    path = cfgv.flombaum_raw + 'rep/flombaum.csv'
    prefix = 'flombaum'
    df = pd.read_csv(path)
    df = ip.convertYYYYMMDD(df)


    df = ip.removeMissings(['time','lat', 'lon','depth'], df)   # remove rows with missing lat/lon/abundance
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    print('Export path:', export_path)
    df.to_csv(export_path, index=False)
    ip.sortByDepthLatLon(df, export_path, 'lon', 'lat', 'depth')

    return export_path





def bulkInsertFlombaum(tableName):
    dataTitle = 'Flombaum'
    print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
    try:
        bulkPath = ''
        bulkPath = makeBulkFlombaum()
        bulkPath = bulkPath
        # print('bulkPath: ', bulkPath, 'tableName: ',  tableName)

        toSQLPandasFlombaum(bulkPath, tableName)

        # dc.bulkInsert(bulkPath, tableName)
    finally:
        pass
        # if bulkPath != '':
        #     os.remove(bulkPath)
    # print('%s  Done' % datetime.today())
    return


# def toSQLPandasFlombaum(bulkPath, tableName, usr='sa', psw='ArmLab2018', ip='10.19.231.219', port='1433', db='Opedia'):
def toSQLPandasFlombaum(bulkPath, tableName, usr='sa', psw='nrhagen', ip='10.19.231.219', port='1433', db='Opedia'):
#         engine = sa.create_engine('mssql+pyodbc://nrhagen:Rdw10^3pb@128.208.239.15:1433/opedia?driver=FreeTDS')

    """ sqlalchemy connection to db """
    engine = sqlalchemy.create_engine('mssql+pyodbc://nrhagen:Rdw10^3pb@128.208.239.15:1433/opedia?driver=FreeTDS')

    # engine = sqlalchemy.create_engine('mssql+pyodbc://'+usr+':'+psw+'@'+ip+':'+port+'/'+db+'?'\
    # +'driver=FreeTDS')


    """ import cleaned .csv """
    df = pd.read_csv(bulkPath, parse_dates=['time'])
    # print(len(df))
    # df = df.head(1000)
    # print(type(df['time'].iloc[0]))
    # print(df['time'].iloc[0])

    """ pandas sql insert function """


    df.to_sql(tableName, engine, if_exists='replace', index=False,
                        dtype={'time': sqlalchemy.DateTime(),
                               'lat': sqlalchemy.types.Float(precision=3, asdecimal=True),
                               'lon': sqlalchemy.types.Float(precision=3, asdecimal=True),
                               'depth': sqlalchemy.types.Float(precision=3, asdecimal=True),
                               'prochloro_abundance': sqlalchemy.types.Float(precision=3, asdecimal=True),
                               'synecho_abundance': sqlalchemy.types.Float(precision=3, asdecimal=True)
                               })



    alter_ID = """ALTER TABLE """ +  tableName + """ ADD [ID][bigint] IDENTITY(1,1) NOT NULL """
    alter_lat = """ALTER TABLE """ +  tableName + """ ALTER COLUMN  [lat] FLOAT  NOT NULL """
    alter_lon = """ALTER TABLE """ +  tableName + """ ALTER COLUMN  [lon] FLOAT  NOT NULL """
    alter_depth = """ALTER TABLE """ +  tableName + """ ALTER COLUMN  [depth] FLOAT  NULL """
    alter_pro = """ALTER TABLE """ +  tableName + """ ALTER COLUMN  [prochloro_abundance] FLOAT  NULL """
    alter_syn = """ALTER TABLE """ +  tableName + """ ALTER COLUMN  [synecho_abundance] FLOAT  NULL """

    db_insert(alter_ID)
    db_insert(alter_lat)
    db_insert(alter_lon)
    db_insert(alter_depth)
    db_insert(alter_pro)


def db_insert(SQL):
    conn = dc.dbConnect()
    cursor = conn.cursor()
    #vals = nanToNone(vals)
    cursor.execute(SQL)
    conn.commit()



tableName = 'tblFlombaum'
bulkInsertFlombaum(tableName)
