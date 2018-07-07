import sys
sys.dont_write_bytecode = True
import os
import db
import pandas as pd
from datetime import datetime
from datetime import timedelta  
import numpy as np
from tqdm import tqdm

def getPiscesDepthLevels():
    query = "SELECT * FROM tblPisces_Depth"
    depthLevs = db.dbFetch(query) 
    return depthLevs


def sourceQuery(srcTable):
    query  = 'SELECT * FROM %s '
    query = query % (srcTable)
    return query


def getSrcDF(DB, source):
    srcDF = None
    if DB:
        query = sourceQuery(source) 
        srcDF = db.dbFetch(query)   
    else:  
        filename, fileExtension = os.path.splitext(source)  
        if fileExtension == '.xlsx':
            srcDF = pd.read_excel(open(source,'rb'), sheetname='data')
        elif fileExtension == '.csv':    
            srcDF = pd.read_csv(source)
        srcDF['time'] = pd.to_datetime(srcDF['time'])
    return srcDF


def matchQuery(table, field, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2):
    args = (field, table, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2)
    query = "SELECT %s FROM %s WHERE "
    query = query + "[time]>='%s' AND [time]<='%s' AND "
    query = query + "lat>=%f AND lat<=%f AND "
    query = query + "lon>=%f AND lon<=%f AND "
    query = query + "depth>=%f AND depth<=%f "
    query = query % args
    return query


def localize(table, field, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2):
    query = matchQuery(table, field, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2)
    df = db.dbFetch(query)        
    return df






def matchSource():
    target = []
    for i in range(len(tables)):
        target.append((tables[i], variables[i]))

    srcDF = getSrcDF(DB, source)
    depthLevs = getPiscesDepthLevels()
    srcDF['dt1'], srcDF['dt2'], srcDF['lat1'], srcDF['lat2'], srcDF['lon1'], srcDF['lon2'], srcDF['depth1'], srcDF['depth2'] = '', '', '', '', '', '', '', ''
    for tar in tqdm(target):
        srcDF[tar[1]] = ''
        srcDF[tar[1]+'_std'] = ''
        for i in tqdm(range(len(srcDF))):
            dt = srcDF.time[i]   
            dt1 = dt - timedelta(days=tMargin) 
            dt2 = dt + timedelta(days=tMargin) 
            lat = srcDF.lat[i]
            lon = srcDF.lon[i]
            depth = srcDF.depth[i]
            ind = np.abs(depthLevs['depth_level']-depth).idxmin()# argmin()
            depth = depthLevs['depth_level'][ind]
            lat1, lat2 = lat - latMargin, lat + latMargin
            lon1, lon2 = lon - lonMargin, lon + lonMargin
            depth1, depth2 = depth - 1, depth + 1
            data = localize(tar[0], tar[1], str(dt1), str(dt2), lat1, lat2, lon1, lon2, depth1, depth2)
            srcDF.loc[i, 'dt1'], srcDF.loc[i, 'dt2'], srcDF.loc[i, 'lat1'], srcDF.loc[i, 'lat2'], srcDF.loc[i, 'lon1'], srcDF.loc[i, 'lon2'], srcDF.loc[i, 'depth1'], srcDF.loc[i, 'depth2'] = dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2
            srcDF.loc[i,tar[1]] = np.mean(data[tar[1]])
            srcDF.loc[i, tar[1]+'_std'] = np.std(data[tar[1]])

    dirPath = os.path.dirname(exportPath)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    srcDF.to_csv(exportPath, index=False)
    print('')
    return





DB = bool(int(sys.argv[1]))
source = sys.argv[2]      
latMargin = float(sys.argv[3])         #meridional margin 
lonMargin = float(sys.argv[3])         #zonal margin 
####depMargin = float(sys.argv[3])         #depth margin 
tMargin = float(sys.argv[4])         #temporal margin 
tables = sys.argv[5].split(',')
variables = sys.argv[6].split(',')   
exportPath = sys.argv[7] 

matchSource()
