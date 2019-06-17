"""
Author: Mohammad Dehghani Ashkezari <mdehghan@uw.edu>

Date: Summer 2017

Function: Cross match multiple data sets within a predefined space-time domain.
"""

import sys
sys.dont_write_bytecode = True
import os
sys.path.append(os.path.dirname(__file__))
import db
import subset
import pandas as pd
from datetime import datetime
from datetime import timedelta  
import numpy as np
import jupyterInline as jup
if jup.jupytered():
    from tqdm import tqdm_notebook as tqdm
else:
    from tqdm import tqdm



def getModelDepthLevels(tableName):
    query = "SELECT * FROM %s" % tableName
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
            srcDF = pd.read_excel(open(source,'rb'), sheet_name='data')
        elif fileExtension == '.csv':    
            srcDF = pd.read_csv(source)
        srcDF['time'] = pd.to_datetime(srcDF['time'])
    return srcDF


def matchSource(DB, source, tMargin, latMargin, lonMargin, depthMargin, tables, variables, exportPath):
    target = []
    for i in range(len(tables)):
        target.append((tables[i], variables[i]))
    srcDF = getSrcDF(DB, source)
    if not 'depth' in srcDF.columns:
        srcDF['depth'] = 0
    #depthLevs = getModelDepthLevels('tblPisces_Depth')
    #depthLevs = getModelDepthLevels('tblDarwin_Depth')
    srcDF['dt1'], srcDF['dt2'], srcDF['lat1'], srcDF['lat2'], srcDF['lon1'], srcDF['lon2'], srcDF['depth1'], srcDF['depth2'] = '', '', '', '', '', '', '', ''
    for tar in tqdm(target, desc='overall'):
        srcDF[tar[1]] = ''
        srcDF[tar[1]+'_std'] = ''
        for i in tqdm(range(len(srcDF)), desc=tar[1]):
            dt = srcDF.time[i]   
            dt1 = dt - timedelta(days=tMargin) 
            dt2 = dt + timedelta(days=tMargin) 
            lat = srcDF.lat[i]
            lon = srcDF.lon[i]
            depth = srcDF.depth[i]
            lat1, lat2 = lat - latMargin, lat + latMargin
            lon1, lon2 = lon - lonMargin, lon + lonMargin
            depth1, depth2 = depth - depthMargin, depth + depthMargin

            ##### matching to the closest model depth layer 
            ##### "depthLevs" array has to hold the model's depth levels  #####
            '''
            ind = np.abs(depthLevs['depth_level']-depth).idxmin()# argmin()
            depth = depthLevs['depth_level'][ind]
            depth1, depth2 = depth - 1, depth + 1
            '''
            ####################################################################

            data = subset.spaceTime(tar[0], tar[1], str(dt1), str(dt2), lat1, lat2, lon1, lon2, depth1, depth2)
            srcDF.loc[i, 'dt1'], srcDF.loc[i, 'dt2'], srcDF.loc[i, 'lat1'], srcDF.loc[i, 'lat2'], srcDF.loc[i, 'lon1'], srcDF.loc[i, 'lon2'], srcDF.loc[i, 'depth1'], srcDF.loc[i, 'depth2'] = dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2
            srcDF.loc[i,tar[1]] = np.mean(data[tar[1]])
            srcDF.loc[i, tar[1]+'_std'] = np.std(data[tar[1]])

    dirPath = os.path.dirname(exportPath)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
    srcDF.to_csv(exportPath, index=False)
    print('')
    return



def main():
    DB = bool(int(sys.argv[1]))                         # argument1: < 1 > if source data exists in the database. < 0 > if the source data set is a spreadsheet file on disk.
    source = sys.argv[2]                                # argument2: the source table name (or full filename)      
    temporalTolerance = float(sys.argv[3])              # argument3: colocalizer temporal tolerance (+/- degrees)
    latTolerance = float(sys.argv[4])                   # argument4: colocalizer meridional tolerance (+/- degrees)
    lonTolerance = float(sys.argv[5])                   # argument5: colocalizer zonal tolerance (+/- degrees) 
    depthTolerance = float(sys.argv[6])                 # argument6: colocalizer depth tolerance (+/- degrees)
    tables = sys.argv[7].split(',')                     # argument7: comma-separated list of varaible table names 
    variables = sys.argv[8].split(',')                  # argument8: comma-separated list of variable names   
    exportPath = sys.argv[9]                            # argument9: path to save the colocalized data set 

    matchSource(DB, source, temporalTolerance, latTolerance, lonTolerance, depthTolerance, tables, variables, exportPath)



####################################### Example ################################################
#                                                                                              #   
#   python colocalize.py 0 d:/data.csv 5 0.5 0.5 5 tblPisces_NRT NO3 d:/data_colocalized.csv   # 
#                                                                                              #
################################################################################################

if __name__ == '__main__':
    main()