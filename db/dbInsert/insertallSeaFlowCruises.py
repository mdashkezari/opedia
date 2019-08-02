
import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import dbCore as dc
import config_vault as cfgv
import pandas as pd
import numpy as np
import os
import numpy as np
import glob
############################
########### OPTS ###########
tableName = 'tblCruise'


def insertSeaFlowCruises():
    server='Rainier'
    tableName = 'tblCruise'
    rawFileName = 'tblCruise_seaflow.csv'
    rawFilePath = cfgv.rep_allSeaFlowCruises_raw
    path = rawFilePath + rawFileName
    prefix = tableName
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df = pd.read_csv(path, sep=',')
    df['Start_Time'], df['End_Time'],df['Lat_Min'], df['Lat_Max'],df['Lon_Min'], df['Lon_Max'],df['Chief_Name'], df['Chief_Email'] = None, None, None, None, None, None,None, None
    df = df[['ID','Name','Nickname','Ship_Name','Start_Time','End_Time', 'Lat_Min', 'Lat_Max', 'Lon_Min', 'Lon_Max','Chief_Name', 'Chief_Email','Keywords']]
    df.to_csv(export_path, index=False,header=False)
    print('export path: ' ,export_path)
    iF.toSQLbcp(export_path, tableName,server)
# df = insertSeaFlowCruises()

def insertSeaFlowCruiseTraj():
    server='Rainier'
    tableName = 'tblCruise_Trajectory'
    rawFilePath = cfgv.rep_allSeaFlowCruises_raw
    os.chdir(rawFilePath)
    sfl_cruise_list = glob.glob('*.sfl*')
    usecols_sfl=['DATE', 'LAT', 'LON']
    for cruise in sfl_cruise_list:
        prefix = cruise[:-8] + '_traj'
        rawFileName = cruise
        path = rawFilePath + rawFileName
        exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
        export_path = '%s%s.csv' % (exportBase, prefix)
        print(cruise)
        Cruise_ID = iF.findID_CRUISE(cruise[:-8])
        df = pd.read_csv(cruise,  sep='\t',usecols = usecols_sfl)
        df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%dT%H:%M:%S')
        df['Cruise_ID'] = Cruise_ID
        df.rename(columns={
        'DATE': 'time',
        'LAT': 'lat',
        'LON': 'lon'}, inplace=True)
        df = df[['Cruise_ID', 'time', 'lat','lon']]
        df = ip.removeMissings(['time','lat', 'lon'], df)
        df = ip.NaNtoNone(df)
        df = ip.colDatatypes(df)
        df = ip.convertYYYYMMDD(df)
        df = ip.removeDuplicates(df)
        df.to_csv(export_path, index=False)
        ip.sortByTimeLatLon(df, export_path, 'time', 'lat', 'lon')
        print('export path: ' ,export_path)
        # print(export_path,tableName)
        iF.toSQLbcp(export_path, tableName,server)



def insertSeaFlowCruises_ST_bounds():
    cruise_ID_list = iF.cruise_ID_list()['ID_list']
    cruise_nickname_list = iF.cruise_ID_list()['Nickname_list']
    server = 'Rainier'

    for cruise_ID,nickname in zip(cruise_ID_list,cruise_nickname_list):
        conn = dc.dbConnect(server)
        cursor = conn.cursor()
        # print(cruise_ID,nickname)
        Start_Time = iF.findMinMaxDate_cruiseID(cruise_ID)['minDate']
        End_Time = iF.findMinMaxDate_cruiseID(cruise_ID)['maxDate']
        Lat_Min = iF.findMinMaxSpatial_cruiseID(cruise_ID)['minlat']
        Lat_Max = iF.findMinMaxSpatial_cruiseID(cruise_ID)['maxlat']
        Lon_Min = iF.findMinMaxSpatial_cruiseID(cruise_ID)['minlon']
        Lon_Max = iF.findMinMaxSpatial_cruiseID(cruise_ID)['maxlon']

        """ Iterate through cruise_ID_list, insert S,T in the row. SQL update?"""
        sql_str = """UPDATE [Opedia].[dbo].[tblCruise] SET Start_Time = '""" + str(Start_Time) + """', End_Time = '""" + str(End_Time) + """', Lat_Min = '""" + str(Lat_Min) + """', Lat_Max = '""" + str(Lat_Max) + """', Lon_Min = '""" + str(Lon_Min) + """', Lon_Max = '""" + str(Lon_Max)  + """' WHERE [ID] = '""" + str(cruise_ID) + """'"""
        # print(sql_str)
        # break
        print('updating the spatiotemporal bounds for: ' + str(cruise_ID) + ' ' + str(nickname))
        cursor.execute(sql_str)
        conn.commit()
        cursor.close()
        conn.close()

# insertSeaFlowCruises_ST_bounds()

def insertSeaFlowCruiseTemperature():
    server='Rainier'
    tableName = 'tblCruise_Temperature'
    rawFilePath = cfgv.rep_allSeaFlowCruises_raw
    os.chdir(rawFilePath)
    sfl_cruise_list = glob.glob('*.sfl*')
    usecols_sfl=['DATE', 'LAT', 'LON','OCEAN TEMP']
    for cruise in sfl_cruise_list:
        prefix = cruise[:-8] + '_temp'
        rawFileName = cruise
        path = rawFilePath + rawFileName
        exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
        export_path = '%s%s.csv' % (exportBase, prefix)
        print(cruise)
        Cruise_ID = iF.findID_CRUISE(cruise[:-8])
        df = pd.read_csv(cruise,  sep='\t',usecols = usecols_sfl)
        df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%dT%H:%M:%S')
        df['DEPTH'] = 5.0
        df['Cruise_ID'] = Cruise_ID
        df.rename(columns={
        'DATE': 'time',
        'LAT': 'lat',
        'LON': 'lon',
        'DEPTH': 'depth',
        'OCEAN TEMP': 'temperature'}, inplace=True)
        df = df[['Cruise_ID', 'time', 'lat','lon','depth','temperature']]
        df = ip.removeMissings(['time','lat', 'lon','depth'], df)
        df = df[pd.to_numeric(df['temperature'], errors='coerce').notnull()]
        df = ip.NaNtoNone(df)
        df = ip.colDatatypes(df)
        df = ip.convertYYYYMMDD(df)
        df = ip.removeDuplicates(df)
        print(df.head())
        if df.empty:
            print(cruise + ' had no temperature values. Not inserted into database')
        else:
            df.to_csv(export_path, index=False)
            ip.sortByTimeLatLon(df, export_path, 'time', 'lat', 'lon')
            print('export path: ' ,export_path)
            # print(export_path,tableName)
            iF.toSQLbcp(export_path, tableName,server)

def insertSeaFlowCruiseSalinity():
    server='Rainier'
    tableName = 'tblCruise_Salinity'
    rawFilePath = cfgv.rep_allSeaFlowCruises_raw
    os.chdir(rawFilePath)
    sfl_cruise_list = glob.glob('*.sfl*')
    usecols_sfl=['DATE', 'LAT', 'LON','SALINITY']
    for cruise in sfl_cruise_list:
        prefix = cruise[:-8] + '_temp'
        rawFileName = cruise
        path = rawFilePath + rawFileName
        exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
        export_path = '%s%s.csv' % (exportBase, prefix)
        print(cruise)
        Cruise_ID = iF.findID_CRUISE(cruise[:-8])
        df = pd.read_csv(cruise,  sep='\t',usecols = usecols_sfl)
        df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%dT%H:%M:%S')
        df['DEPTH'] = 5.0
        df['Cruise_ID'] = Cruise_ID
        df.rename(columns={
        'DATE': 'time',
        'LAT': 'lat',
        'LON': 'lon',
        'DEPTH': 'depth',
        'SALINITY': 'salinity'}, inplace=True)
        df = df[['Cruise_ID', 'time', 'lat','lon','depth','salinity']]
        df = ip.removeMissings(['time','lat', 'lon','depth'], df)
        df = df[pd.to_numeric(df['salinity'], errors='coerce').notnull()]
        df = ip.NaNtoNone(df)
        df = ip.colDatatypes(df)
        df = ip.convertYYYYMMDD(df)
        df = ip.removeDuplicates(df)
        print(df.head())
        if df.empty:
            print(cruise + ' had no salinity values. Not inserted into database')
        else:
            df.to_csv(export_path, index=False)
            ip.sortByTimeLatLon(df, export_path, 'time', 'lat', 'lon')
            print('export path: ' ,export_path)
            # print(export_path,tableName)
            iF.toSQLbcp(export_path, tableName,server)

def insertSeaFlowCruisePAR():
    server='Rainier'
    tableName = 'tblCruise_PAR'
    rawFilePath = cfgv.rep_allSeaFlowCruises_raw
    os.chdir(rawFilePath)
    sfl_cruise_list = glob.glob('*.sfl*')
    usecols_sfl=['DATE', 'LAT', 'LON','PAR']
    for cruise in sfl_cruise_list:
        prefix = cruise[:-8] + '_temp'
        rawFileName = cruise
        path = rawFilePath + rawFileName
        exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
        export_path = '%s%s.csv' % (exportBase, prefix)
        print(cruise)
        Cruise_ID = iF.findID_CRUISE(cruise[:-8])
        df = pd.read_csv(cruise,  sep='\t',usecols = usecols_sfl)
        df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%dT%H:%M:%S')
        df['DEPTH'] = 5.0
        df['Cruise_ID'] = Cruise_ID
        df.rename(columns={
        'DATE': 'time',
        'LAT': 'lat',
        'LON': 'lon',
        'DEPTH': 'depth'}, inplace=True)
        df = df[['Cruise_ID', 'time', 'lat','lon','depth','PAR']]
        df = ip.removeMissings(['time','lat', 'lon','depth'], df)
        df = df[pd.to_numeric(df['PAR'], errors='coerce').notnull()]
        df = ip.NaNtoNone(df)
        df = ip.colDatatypes(df)
        df = ip.convertYYYYMMDD(df)
        df = ip.removeDuplicates(df)

        if df.empty:
            print(cruise + ' had no PAR values. Not inserted into database')
        else:
            df.to_csv(export_path, index=False)
            ip.sortByTimeLatLon(df, export_path, 'time', 'lat', 'lon')
            print('export path: ' ,export_path)
            # print(export_path,tableName)
            iF.toSQLbcp(export_path, tableName,server)

# insertSeaFlowCruises()
# insertSeaFlowCruiseTraj()
# insertSeaFlowCruises_ST_bounds()
insertSeaFlowCruiseTemperature()
insertSeaFlowCruiseSalinity()
insertSeaFlowCruisePAR()
