import sys
import os
sys.path.append(os.path.dirname(__file__))
import db


def spaceTime(tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2):
    args = [tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2]
    query = 'EXEC uspSpaceTime ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
    df = db.dbFetchStoredProc(query, args)   
    return df


def timeSeries(tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2):
    args = [tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2]
    query = 'EXEC uspTimeSeries ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
    df = db.dbFetchStoredProc(query, args)
    return df


def depthProfile(tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2):
    args = [tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2]
    query = 'EXEC uspDepthProfile ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
    df = db.dbFetchStoredProc(query, args)
    return df


def section(tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2):
    args = [tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2]
    query = 'EXEC uspSectionMap ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
    df = db.dbFetchStoredProc(query, args)
    return df