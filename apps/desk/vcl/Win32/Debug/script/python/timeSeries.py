import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import db
import genericDist as gd
from datetime import datetime, timedelta
import time



def timeSeries(table, field, startDate, endDate, lat1, lat2, lon1, lon2, extV, extVV, extV2, extVV2, fmt='%Y-%m-%d', dt=24*60):
    #dt = 24*60         # time resolution (minutes)    
    y = np.array([])
    y_std = np.array([])
    ts = []    
    startDate = datetime.strptime(startDate, fmt)
    endDate = datetime.strptime(endDate, fmt)
    t = startDate
    while t<=endDate:        
        ts.append(t)
        t1 = t
        t2 = t + timedelta(minutes=dt) + timedelta(seconds=-1)
        df = gd.genericDist(table, field, t1, t2, lat1, lat2, lon1, lon2, extV, extVV, extV2, extVV2)        
        t = t + timedelta(minutes=dt)
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
    return ts, y, y_std


