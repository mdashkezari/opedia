import os, os.path
import sys
sys.path.append('../login')
sys.path.append('../../config')
import pandas as pd
import config_vault as cfgv
import credentials as cr
sys.path.append('../')
import dbCore as dc

def toSQLbcp(export_path, tableName,  server):
    if server == 'Rainier':
        usr=cr.usr_rainier
        psw=cr.psw_rainier
        ip=cr.ip_rainier
        port = cr.port_rainier
    else:
        usr=cr.usr_beast
        psw=cr.psw_beast
        ip=cr.ip_beast
        port = cr.port_beast

    print('Inserting Bulk %s into %s.' % (tableName[3:], tableName))
    str = """bcp Opedia.dbo.""" + tableName + """ in """ + export_path + """ -e error -c -t, -U  """ + usr + """ -P """ + psw + """ -S """ + ip + """,""" + port
    os.system(str)
    print('BCP insert finished')

def findID_CRUISE(cruiseName):
    """ this function pulls the ID value from the [tblCruises]"""
    server = 'Rainier'
    conn = dc.dbConnect(server)
    cursor = conn.cursor()
    cur_str = """select [ID] FROM [Opedia].[dbo].[tblCruise] WHERE [Name] like '%""" + cruiseName + """%'"""
    cursor.execute(cur_str)
    IDvar = (cursor.fetchone()[0])
    return IDvar

def cruise_ID_list():
    server = 'Rainier'
    conn = dc.dbConnect(server)
    cursor = conn.cursor()
    cur_str = """select [ID], [Nickname] FROM [Opedia].[dbo].[tblCruise]"""
    cursor.execute(cur_str)
    IDlist = (cursor.fetchall())
    newID_list = [x[0] for x in IDlist]
    newNickname_list = [x[1] for x in IDlist]

    return {'ID_list':newID_list,'Nickname_list':newNickname_list}


def findMinMaxDate_cruiseID(ID):
    server = 'Rainier'
    conn = dc.dbConnect(server)
    cursor = conn.cursor()
    cur_str_min = """select min(time) FROM [Opedia].[dbo].[tblCruise_Trajectory] where Cruise_ID = '""" + str(ID) + """'"""
    cur_str_max = """select max(time) FROM [Opedia].[dbo].[tblCruise_Trajectory] where Cruise_ID = '""" + str(ID) + """'"""
    cursor.execute(cur_str_min)
    minDate = (cursor.fetchone()[0])
    cursor.execute(cur_str_max)
    maxDate = (cursor.fetchone()[0])
    return {'minDate':minDate,'maxDate':maxDate}

def findMinMaxSpatial_cruiseID(ID):
    server = 'Rainier'
    conn = dc.dbConnect(server)
    cursor = conn.cursor()
    cur_str_minlat = """select min(lat) FROM [Opedia].[dbo].[tblCruise_Trajectory] where Cruise_ID = '""" + str(ID) + """'"""
    cur_str_maxlat = """select max(lat) FROM [Opedia].[dbo].[tblCruise_Trajectory] where Cruise_ID = '""" + str(ID) + """'"""
    cur_str_minlon = """select min(lon) FROM [Opedia].[dbo].[tblCruise_Trajectory] where Cruise_ID = '""" + str(ID) + """'"""
    cur_str_maxlon = """select max(lon) FROM [Opedia].[dbo].[tblCruise_Trajectory] where Cruise_ID = '""" + str(ID) + """'"""
    cursor.execute(cur_str_minlat)
    minlat = (cursor.fetchone()[0])
    cursor.execute(cur_str_maxlat)
    maxlat = (cursor.fetchone()[0])
    cursor.execute(cur_str_minlon)
    minlon = (cursor.fetchone()[0])
    cursor.execute(cur_str_maxlon)
    maxlon = (cursor.fetchone()[0])
    return {'minlat':minlat,'maxlat':maxlat,'minlon':minlon,'maxlon':maxlon}

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
