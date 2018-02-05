import sys
import os
import numpy as np
import pandas as pd
import db
from datetime import datetime, timedelta
import time




def genericDist(table, field, startDate, endDate, lat1, lat2, lon1, lon2, extV, extVV, extV2, extVV2):
    def strToDate(str):
        dt = datetime.strptime(str, '%Y-%m-%d')
        return dt
    dist = np.array([])    
    #startDate = strToDate(startDate)
    #endDate = strToDate(endDate)
    ######### Stored Procedure Query ##########
    query = 'EXEC uspGenericDist ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
    args = [table, field, startDate, endDate, str(lat1), str(lat2), str(lon1), str(lon2), extV, extVV]
    df = db.dbFetchStoredProc(query, args)
    df = pd.DataFrame.from_records(df, columns=['time', 'lat', 'lon', field])
    ###########################################    
    return df


