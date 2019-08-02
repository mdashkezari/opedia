
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
pd.options.mode.chained_assignment = None

############################
########### OPTS ###########
tableName = 'tblCruise'

""" time, lat, lon, temp,sal,par
AMT12 is when format changes
"""
def createMasterAMT():
    master_df = pd.DataFrame(columns = ['Cruise_name','time', 'lat', 'lon', 'temp', 'temp_flag', 'salinity', 'salinity_flag', 'PAR', 'PAR_flag'])
    rawFilePath = cfgv.rep_AMT_cruises_raw
    os.chdir(rawFilePath)
    AMT_list = np.sort(glob.glob('*.csv*'))
    for AMT_cruise in AMT_list:
        df = pd.read_csv(AMT_cruise, sep=',')
        #first exception, merge year+time into datetime col with format
        if 'year' in df.columns:
            try:
                df['time'] = pd.to_datetime(df['year'] + ' ' + df['time'], format='%d/%m/%Y %H:%M:%S')
                del df['year']
            except:
                df['time'] = pd.to_datetime(df['year'] + ' ' + df['time'], format='%Y/%m/%d %H:%M:%S')
                del df['year']

        if 'PAR' not in df.columns:
            df['PAR'] = None
            df['PAR_flag'] = None
        df['Cruise_name'] = 'AMT_' + AMT_cruise[0:2]

        """ checks spatial flags, other flags can be checked in specific inserts"""
        df = df[(df['lat_flag'] !='I') & (df['lat_flag'] !='M')  & (df['lat_flag'] !='N') & (df['lat_flag'] !='L')]
        df = df[(df['lon_flag'] !='I') & (df['lon_flag'] !='M')  & (df['lon_flag'] !='N') & (df['lat_flag'] !='L')]
        df = df[['Cruise_name','time', 'lat', 'lon',  'temp', 'temp_flag', 'salinity', 'salinity_flag', 'PAR', 'PAR_flag']]

        master_df = master_df.append(df)

    # master_df.to_csv('amt/master_AMT.csv',sep = ',',index=False)
    return master_df

# df = createMasterAMT()

# createMasterAMT()
def insertAMTCruises():
    server='Rainier'
    cruise = 'AMT_cruises'
    tableName = 'tblCruise'
    rawFileName = 'tblCruise_AMT.csv'
    rawFilePath = cfgv.rep_AMT_cruises_raw + 'amt/'

    path = rawFilePath + rawFileName
    prefix = tableName +  '_' + cruise
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df = pd.read_csv(path, sep=',')
    df.to_csv(export_path, index=False)
    iF.toSQLbcp(export_path, tableName,server)

def insertAMTCruiseTraj():
    server='Rainier'
    tableName = 'tblCruise_Trajectory'
    usecols = ['Cruise_name','time','lat','lon']
    rawFilePath = cfgv.rep_AMT_cruises_raw + 'amt/'
    rawFileName = 'master_AMT.csv'
    path = rawFilePath + rawFileName
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    os.chdir(rawFilePath)

    df = pd.read_csv(rawFilePath +  rawFileName,  sep=',',usecols = usecols)
    for Cruise_name in df['Cruise_name'].unique():
        export_path = '%s%s.csv' % (exportBase,Cruise_name)

        print(Cruise_name)

        cruise_df = df[df['Cruise_name'] == Cruise_name] #selects only df of cruise
        Cruise_ID = iF.findID_CRUISE(Cruise_name[0:3]  + Cruise_name[-2:])
        cruise_df['Cruise_ID'] = Cruise_ID
        cruise_df = ip.removeMissings(['time','lat', 'lon'], cruise_df)
        cruise_df = ip.convertYYYYMMDD(cruise_df)
        cruise_df = ip.NaNtoNone(cruise_df)
        cruise_df = ip.colDatatypes(cruise_df)
        cruise_df = ip.convertYYYYMMDD(cruise_df)
        cruise_df = ip.removeDuplicates(cruise_df)
        cruise_df = cruise_df[['Cruise_ID','time','lat','lon']]
        cruise_df.to_csv(export_path, index=False)
        ip.sortByTimeLatLon(cruise_df, export_path, 'time', 'lat', 'lon')

        print('export path: ' ,Cruise_name + export_path)
        iF.toSQLbcp(export_path, tableName,server)
        # print(df.head(1))
        # return cruise_df



def insertAMTCruises_ST_bounds():
    cruise_ID_list = iF.cruise_ID_list()['ID_list']
    cruise_nickname_list = iF.cruise_ID_list()['Nickname_list']
    server = 'Rainier'
    # print(cruise_ID_list, cruise_nickname_list)
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

# insertAMTCruises_ST_bounds()

def insertAMTCruiseTemperature():
    server='Rainier'
    tableName = 'tblCruise_Temperature'
    usecols = ['Cruise_name','time','lat','lon','temp', 'temp_flag']
    rawFilePath = cfgv.rep_AMT_cruises_raw + 'amt/'
    rawFileName = 'master_AMT.csv'
    path = rawFilePath + rawFileName
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    os.chdir(rawFilePath)

    df = pd.read_csv(rawFilePath +  rawFileName,  sep=',',usecols = usecols)
    for Cruise_name in df['Cruise_name'].unique():
        export_path = '%s%s%s.csv' % (exportBase,Cruise_name,tableName)

        print(Cruise_name)

        cruise_df = df[df['Cruise_name'] == Cruise_name] #selects only df of cruise
        Cruise_ID = iF.findID_CRUISE(Cruise_name[0:3]  + Cruise_name[-2:])
        cruise_df['Cruise_ID'] = Cruise_ID
        cruise_df = cruise_df[(cruise_df['temp_flag'] !='N') & (cruise_df['temp_flag'] !='S')  & (cruise_df['temp_flag'] !='M') & (cruise_df['temp_flag'] !='L')]
        cruise_df = ip.removeMissings(['time','lat', 'lon'], cruise_df)
        cruise_df = ip.convertYYYYMMDD(cruise_df)
        cruise_df = ip.colDatatypes(cruise_df)
        cruise_df = ip.convertYYYYMMDD(cruise_df)
        cruise_df = ip.removeDuplicates(cruise_df)
        cruise_df = ip.renameCol(cruise_df, 'temp', 'temperature')
        cruise_df = cruise_df[['Cruise_ID','time','lat','lon','temperature']]
        cruise_df = cruise_df.dropna(subset=['temperature'])
        cruise_df = ip.NaNtoNone(cruise_df)

        if cruise_df.empty:
            print(Cruise_name + ' had no temperature values. Not inserted into database')
        else:
            cruise_df.to_csv(export_path, index=False)
            ip.sortByTimeLatLon(cruise_df, export_path, 'time', 'lat', 'lon')
            print('export path: ' ,export_path)
            iF.toSQLbcp(export_path, tableName,server)


def insertAMTCruiseSalinity():
    server='Rainier'
    tableName = 'tblCruise_Salinity'
    usecols = ['Cruise_name','time','lat','lon','salinity', 'salinity_flag']
    rawFilePath = cfgv.rep_AMT_cruises_raw + 'amt/'
    rawFileName = 'master_AMT.csv'
    path = rawFilePath + rawFileName
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    os.chdir(rawFilePath)

    df = pd.read_csv(rawFilePath +  rawFileName,  sep=',',usecols = usecols)
    for Cruise_name in df['Cruise_name'].unique():
        export_path = '%s%s%s.csv' % (exportBase,Cruise_name,tableName)

        cruise_df = df[df['Cruise_name'] == Cruise_name] #selects only df of cruise
        Cruise_ID = iF.findID_CRUISE(Cruise_name[0:3]  + Cruise_name[-2:])
        cruise_df['Cruise_ID'] = Cruise_ID
        cruise_df = cruise_df[(cruise_df['salinity_flag'] !='N') & (cruise_df['salinity_flag'] !='S')  & (cruise_df['salinity_flag'] !='M') & (cruise_df['salinity_flag'] !='L')]
        # print(Cruise_name,cruise_df['salinity_flag'].value_counts())

        cruise_df = ip.removeMissings(['time','lat', 'lon'], cruise_df)
        cruise_df = ip.convertYYYYMMDD(cruise_df)
        cruise_df = ip.colDatatypes(cruise_df)
        cruise_df = ip.convertYYYYMMDD(cruise_df)
        cruise_df = ip.removeDuplicates(cruise_df)
        cruise_df = cruise_df[['Cruise_ID','time','lat','lon','salinity']]
        cruise_df = cruise_df.dropna(subset=['salinity'])
        cruise_df = ip.NaNtoNone(cruise_df)
        if cruise_df.empty:
            print(Cruise_name + ' had no salinity values. Not inserted into database')
        else:
            cruise_df.to_csv(export_path, index=False)
            ip.sortByTimeLatLon(cruise_df, export_path, 'time', 'lat', 'lon')
            print('export path: ' ,export_path)
            # print(export_path,tableName)
            iF.toSQLbcp(export_path, tableName,server)


def insertAMTCruisePAR():
    server='Rainier'
    tableName = 'tblCruise_PAR'
    usecols = ['Cruise_name','time','lat','lon','PAR', 'PAR_flag']
    rawFilePath = cfgv.rep_AMT_cruises_raw + 'amt/'
    rawFileName = 'master_AMT.csv'
    path = rawFilePath + rawFileName
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    os.chdir(rawFilePath)

    df = pd.read_csv(rawFilePath +  rawFileName,  sep=',',usecols = usecols)
    for Cruise_name in df['Cruise_name'].unique():
        export_path = '%s%s%s.csv' % (exportBase,Cruise_name,tableName)
        print(Cruise_name)
        cruise_df = df[df['Cruise_name'] == Cruise_name] #selects only df of cruise
        Cruise_ID = iF.findID_CRUISE(Cruise_name[0:3]  + Cruise_name[-2:])
        cruise_df['Cruise_ID'] = Cruise_ID
        # print(Cruise_name,cruise_df['PAR_flag'].value_counts())

        cruise_df = cruise_df[(cruise_df['PAR_flag'] !='N') & (cruise_df['PAR_flag'] !='S')  & (cruise_df['PAR_flag'] !='M') & (cruise_df['PAR_flag'] !='L')]
        cruise_df = ip.removeMissings(['time','lat', 'lon'], cruise_df)
        cruise_df = ip.convertYYYYMMDD(cruise_df)
        cruise_df = ip.colDatatypes(cruise_df)
        cruise_df = ip.convertYYYYMMDD(cruise_df)
        cruise_df = ip.removeDuplicates(cruise_df)
        cruise_df = cruise_df[['Cruise_ID','time','lat','lon','PAR']]
        cruise_df.dropna(subset=['PAR'],inplace=True)
        cruise_df = ip.NaNtoNone(cruise_df)


        if cruise_df.empty:
            print(Cruise_name + ' had no PAR values. Not inserted into database')
        else:
            cruise_df.to_csv(export_path, index=False)
            ip.sortByTimeLatLon(cruise_df, export_path, 'time', 'lat', 'lon')
            print('export path: ' ,export_path)
            # print(export_path,tableName)
            iF.toSQLbcp(export_path, tableName,server)

# insertAMTCruises()
# insertAMTCruiseTraj()
# insertAMTCruises_ST_bounds()
# insertAMTCruiseTemperature()
# insertAMTCruiseSalinity()
insertAMTCruisePAR()
