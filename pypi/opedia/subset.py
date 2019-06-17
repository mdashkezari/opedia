"""
Author: Mohammad Dehghani Ashkezari <mdehghan@uw.edu>

Date: Fall 2017

Function: Retrieve data within a predefined space-time domain. The retrieved data is in form of pandas dataframe.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
import db
import validate



def spaceTime(tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2):
    if not validate.stringCheck(tablesName, field): return None
    args = [tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2]
    query = 'EXEC uspSpaceTime ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
    df = db.dbFetchStoredProc(query, args)   
    return df


def timeSeries(tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2):
    if not validate.stringCheck(tablesName, field): return None
    args = [tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2]
    query = 'EXEC uspTimeSeries ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
    df = db.dbFetchStoredProc(query, args)
    return df


def depthProfile(tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2):
    if not validate.stringCheck(tablesName, field): return None
    args = [tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2]
    query = 'EXEC uspDepthProfile ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
    df = db.dbFetchStoredProc(query, args)
    return df


def section(tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2):
    if not validate.stringCheck(tablesName, field): return None
    args = [tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2]
    query = 'EXEC uspSectionMap ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
    df = db.dbFetchStoredProc(query, args)
    return df



def spaceTimeList(tablesNames, fields, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2):
    df, dfs = None, []
    if not validate.listCheck(tablesNames, fields):
        return dfs
    for i in range(len(tablesNames)):    
        df = spaceTime(tablesNames[i], fields[i], dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)
        dfs.append(df)
    return dfs


def timeSeriesList(tablesNames, fields, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2):
    df, dfs = None, []    
    if not validate.listCheck(tablesNames, fields):
        return dfs
    for i in range(len(tablesNames)):    
        df = timeSeries(tablesNames[i], fields[i], dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)
        dfs.append(df)
    return dfs


def depthProfileList(tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2):
    df, dfs = None, []
    if not validate.listCheck(tablesNames, fields):
        return dfs
    for i in range(len(tablesNames)):    
        df = depthProfile(tablesNames[i], fields[i], dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)
        dfs.append(df)
    return dfs


def sectionList(tablesName, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2):
    df, dfs = None, []
    if not validate.listCheck(tablesNames, fields):
        return dfs
    for i in range(len(tablesNames)):    
        df = section(tablesNames[i], fields[i], dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)
        dfs.append(df)
    return dfs
