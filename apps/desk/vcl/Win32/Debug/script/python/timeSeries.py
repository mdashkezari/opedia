import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import db
from datetime import datetime, timedelta
import time



def makeDailyTS(date1, date2):
    def strToDate(str):
        dt = datetime.strptime(str, '%Y-%m-%d')
        return dt
    def dateToStr(dt):
        str = dt.strftime('%Y-%m-%d')
        return str
    dt = strToDate(date1)
    dt2 = strToDate(date2)
    TS = []
    while dt<=dt2:
        TS.append(dt)
        dt = dt + timedelta(days=1)
    return TS

def make6HourlyTS(date1, date2, hour1, hour2):
    def strToDate(str):
        dt = datetime.strptime(str, '%Y-%m-%d')
        return dt
    def dateToStr(dt):
        str = dt.strftime('%Y-%m-%d')
        return str
    dt = strToDate(date1) + timedelta(hours=hour1)
    dt2 = strToDate(date2) + timedelta(hours=hour2)
    TS = []
    while dt<=dt2:
        TS.append(dt)
        dt = dt + timedelta(hours=6)
    return TS


def timeSeries(table, field, startDate, endDate, lat1, lat2, lon1, lon2, arg8_name, arg8_val, extV2, extVV2):
    y = np.array([])
    y_std = np.array([])
    t = makeDailyTS(startDate, endDate)
    
    #if table.find('Wind') != -1:
    #    t = make6HourlyTS(startDate, endDate, int(arg8_val), int(extVV2))
    
    for dt in t:
        ######### Stored Procedure Query ##########
        query = 'EXEC uspTimeSeries ?, ?, ?, ?, ?, ?, ?, ?, ?'
        args = [table, field, dt, str(lat1), str(lat2), str(lon1), str(lon2), arg8_name, arg8_val]
        
        #if field.find('Wind') != -1:
        #    args = [table, field, date(dt), str(lat1), str(lat2), str(lon1), str(lon2), extV2, dt.hour]
        
        df = db.dbFetchStoredProc(query, args)
        df = pd.DataFrame.from_records(df, columns=['lat', 'lon', field])
        ###########################################
        

        try:
            if len(df[field]) > 0:                
                tempY = np.nanmean(df[field])
            else:
                tempY = np.nan
        except:
            tempY = np.nan   

        if abs(tempY) > 1e30:       ## remove outliers (extremes)
            tempY = np.nan   
            
        y = np.append(y, tempY)

        try:
            if len(df[field]) > 0:
                tempY_std = np.nanstd(df[field])
            else:
                tempY_std = np.nan
        except:
            tempY_std = np.nan        

        if abs(tempY_std) > 1e30:       ## remove outliers (extremes)
            tempY_std = np.nan   

        y_std = np.append(y_std, tempY_std)
    return t, y, y_std


