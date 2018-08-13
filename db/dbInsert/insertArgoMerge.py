import os
import sys
sys.path.append('../../config')
import config_vault as cfgv
sys.path.append('../../collect/ARGO')
import argo
import pandas as pd
import numpy as np
from netCDF4 import Dataset
import netcdf as nc
from datetime import datetime
from datetime import timedelta 
sys.path.append('../../lib')
import dateLib as dl
sys.path.append('../')
import dbCore as dc
import time




def addParam(cols, param):
    cols.append(param)
    cols.append(param+'_QC')
    cols.append(param+'_ADJUSTED')
    cols.append(param+'_ADJUSTED_QC')
    cols.append(param+'_ADJUSTED_ERROR')
    return cols    


def mergeTemplate():
    cols = []
    cols.append('float_id')
    cols.append('cycle')
    cols.append('time')
    cols.append('lat')
    cols.append('lon')
    cols.append('depth')
    cols.append('POSITION_QC')
    cols.append('DIRECTION')
    cols.append('DATA_MODE')
    cols.append('DATA_CENTRE')
    
    ## refrence table 3  (argo user manual)
    cols = addParam(cols, 'CNDC')               # electric conductivity    
    cols = addParam(cols, 'PRES')               #pressure    
    cols = addParam(cols, 'PSAL')               #salinity    
    cols = addParam(cols, 'TEMP')               #temperature
    cols = addParam(cols, 'DOXY')               #dissolved oxygen 
    cols = addParam(cols, 'BBP')                #particle backscattering at x nm        
    cols = addParam(cols, 'BBP470')             #particle backscattering at 470 nm        
    cols = addParam(cols, 'BBP532')             #particle backscattering at 532 nm        
    cols = addParam(cols, 'BBP700')             #particle backscattering at 700 nm        
    cols = addParam(cols, 'TURBIDITY')          #turbidity 
    cols = addParam(cols, 'CP')                 #particle beam attenuation at x nm        
    cols = addParam(cols, 'CP660')              #particle beam attenuation at 660 nm        
    cols = addParam(cols, 'CHLA')               #chlorophyll_a        
    cols = addParam(cols, 'CDOM')               #concentration of colored dissolved organic matter         
    cols = addParam(cols, 'NITRATE')            #nitrate        
    cols = addParam(cols, 'BISULFIDE')          #bisulfide        
    cols = addParam(cols, 'PH_IN_SITU_TOTAL')   #ph        
    cols = addParam(cols, 'DOWN_IRRADIANCE')    #downwelling irradiance at x nm            
    cols = addParam(cols, 'DOWN_IRRADIANCE380') #downwelling irradiance at 380 nm            
    cols = addParam(cols, 'DOWN_IRRADIANCE412') #downwelling irradiance at 412 nm            
    cols = addParam(cols, 'DOWN_IRRADIANCE443') #downwelling irradiance at 443 nm            
    cols = addParam(cols, 'DOWN_IRRADIANCE490') #downwelling irradiance at 490 nm            
    cols = addParam(cols, 'DOWN_IRRADIANCE555') #downwelling irradiance at 555 nm            
    cols = addParam(cols, 'UP_IRRADIANCE')      #upwelling irradiance at x nm            
    cols = addParam(cols, 'UP_IRRADIANCE412')   #upwelling irradiance at 412 nm            
    cols = addParam(cols, 'UP_IRRADIANCE443')   #upwelling irradiance at 443 nm            
    cols = addParam(cols, 'UP_IRRADIANCE490')   #upwelling irradiance at 490 nm            
    cols = addParam(cols, 'UP_IRRADIANCE555')   #upwelling irradiance at 555 nm            
    cols = addParam(cols, 'DOWNWELLING_PAR')    #downwelling photosynthetic available radiation

    cols.append('ID')
    df = pd.DataFrame(columns=cols)    
    return df





def fillMergeDF(df, path, floatID_str, cycle_str):    
    net = Dataset(path, 'r')
    #dimensions
    N_PROF = net.dimensions['N_PROF'].size
    N_PARAM = net.dimensions['N_PARAM'].size
    N_LEVELS = net.dimensions['N_LEVELS'].size
    N_CALIB = net.dimensions['N_CALIB'].size

    #date of file creation
    DATE_CREATION = ''.join(net.variables['DATE_CREATION'][:])
    #date of update of this file
    DATE_UPDATE = ''.join(net.variables['DATE_UPDATE'][:])
    #date of reference for Julian days
    REFERENCE_DATE_TIME = ''.join(net.variables['REFERENCE_DATE_TIME'][:])
    REFERENCE_DATE_TIME_FORMAT = net.variables['REFERENCE_DATE_TIME'].conventions
    #cycle number per profile
    CYCLE_NUMBER = net.variables['CYCLE_NUMBER'][:]
    #float id, per profile
    PLATFORM_NUMBER = []
    for pro in range(N_PROF):
        PLATFORM_NUMBER.append(''.join(str(v) if v != '--' else '' for v in net.variables['PLATFORM_NUMBER'][pro, :]))

    
    #list of parameters per profile
    STATION_PARAMETERS = []
    for pro in range(N_PROF):
        vs = []
        for par in range(N_PARAM): 
            v = net.variables['STATION_PARAMETERS'][pro, par , :]
            if str(v[0]) != '--':
                vs.append(''.join(v))
        STATION_PARAMETERS.append(vs) 

    #list of profile directions
    DIRECTION = []
    for pro in range(N_PROF):
        DIRECTION.append(net.variables['DIRECTION'][pro])

    #list of data centres (per profile)
    DATA_CENTRE = []
    for pro in range(N_PROF):
        DATA_CENTRE.append(''.join(net.variables['DATA_CENTRE'][pro, :]))

    #list of (general) data mode per profile
    DATA_MODE = []
    for pro in range(N_PROF):
        DATA_MODE.append(net.variables['DATA_MODE'][pro])

    #list of parameter data modes per profile
    PARAM_DATA_MODE = []
    for pro in range(N_PROF):
        dms = []
        for par in range(N_PARAM): 
            v = net.variables['PARAMETER_DATA_MODE'][pro, par]
            if str(v) != '--':
                dms.append(''.join(v))
        PARAM_DATA_MODE.append(dms) 

    #list of float type (per profile)
    PLATFORM_TYPE = []
    for pro in range(N_PROF):
        PLATFORM_TYPE.append(''.join(str(v) if v != '--' else '' for v in net.variables['PLATFORM_TYPE'][pro, :]))

    #list of julian day per profile
    JULD = []
    for pro in range(N_PROF):
        JULD.append(net.variables['JULD'][pro])

    #list of julian day qc per profile
    JULD_QC = []
    for pro in range(N_PROF):
        JULD_QC.append(net.variables['JULD_QC'][pro])

    #list of latitude per profile
    LATITUDE = []
    for pro in range(N_PROF):
        LATITUDE.append(net.variables['LATITUDE'][pro])

    #list of latitude per profile
    LONGITUDE = []
    for pro in range(N_PROF):
        LONGITUDE.append(net.variables['LONGITUDE'][pro])

    #list of position qc per profile
    POSITION_QC = []
    for pro in range(N_PROF):
        POSITION_QC.append(net.variables['POSITION_QC'][pro])

    #list of positioning system (per profile)
    POSITIONING_SYSTEM = []
    for pro in range(N_PROF):
        POSITIONING_SYSTEM.append(''.join(str(v) if v != '--' else '' for v in net.variables['POSITIONING_SYSTEM'][pro, :]))

    #list of vertical sampling scheme (per profile)
    VERTICAL_SAMPLING_SCHEME = []
    for pro in range(N_PROF):
        VERTICAL_SAMPLING_SCHEME.append(''.join(str(v) if v != '--' else '' for v in net.variables['VERTICAL_SAMPLING_SCHEME'][pro, :]))




    #unique list of parameters between all profiles of the current file
    UNIQUE_PARAMS = []
    for i in range(N_PROF):
        UNIQUE_PARAMS = UNIQUE_PARAMS + STATION_PARAMETERS[i]
    UNIQUE_PARAMS = list(set(UNIQUE_PARAMS))    

   
    for param in UNIQUE_PARAMS:
        val = net.variables[param][:].flatten()
        val_qc = net.variables[param+'_QC'][:].flatten()
        val_adj = net.variables[param+'_ADJUSTED'][:].flatten()
        val_adj_qc = net.variables[param+'_ADJUSTED_QC'][:].flatten()
        val_adj_err = net.variables[param+'_ADJUSTED_ERROR'][:].flatten()
        df[param] = val
        df[param+'_QC'] = val_qc
        df[param+'_ADJUSTED'] = val_adj
        df[param+'_ADJUSTED_QC'] = val_adj_qc
        df[param+'_ADJUSTED_ERROR'] = val_adj_err

    for param in UNIQUE_PARAMS:
        replacement = np.nan
        df[param].replace(net.variables[param]._FillValue, replacement, inplace=True)
        df[param+'_ADJUSTED'].replace(net.variables[param+'_ADJUSTED']._FillValue, replacement, inplace=True)
        df[param+'_ADJUSTED_ERROR'].replace(net.variables[param+'_ADJUSTED_ERROR']._FillValue, replacement, inplace=True)

    
    fmt= '%Y%m%d%H%M%S'
    JULD = [datetime.strptime(REFERENCE_DATE_TIME, fmt)+timedelta(days=float(v)) for v in JULD]
    df['time'] = np.repeat(JULD, N_LEVELS)
    df['lat'] = np.repeat(LATITUDE, N_LEVELS)
    df['lon'] = np.repeat(LONGITUDE, N_LEVELS)
    df['depth'] = df['PRES']
    df['POSITION_QC'] = np.repeat([int(v) for v in POSITION_QC], N_LEVELS)
    df['float_id'] = np.repeat([int(v) for v in PLATFORM_NUMBER], N_LEVELS)
    df['cycle'] = np.repeat(CYCLE_NUMBER, N_LEVELS)
    df['DIRECTION'] = np.repeat(DIRECTION, N_LEVELS)
    df['DATA_MODE'] = np.repeat(DATA_MODE, N_LEVELS)
    df['DATA_CENTRE'] = np.repeat(DATA_CENTRE, N_LEVELS)
    
    ### remove all rows with empty PRES value
    df.dropna(subset=['PRES'], inplace=True) 
    ##########################################

    ## remove all (potential) columns added after "ID". example: DOXY2 (duplicate sensors, see section 3.3.1 at user manual ver 3.2)
    id_index = df.columns.get_loc("ID")
    if len(df.columns)>id_index+1:
        df.drop(df.columns[id_index+1:], axis=1, inplace=True)
    ##########################################

    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    exportPath = '%s%s_%s.csv' % (exportBase, floatID_str, cycle_str)
    #exportPath = '%sargo_merge.csv' % (exportBase)
    df.to_csv(exportPath, index=False)
    net.close()
    return df, exportPath



def bulkInsertArgoMerge(tableName):
    profs = argo.loadArgoMerge(dataMode='D', ocean='all')
    for i in range(len(profs)):
        mergeDF = mergeTemplate()
        fname = profs.iloc[i,0].split('/')[-1]
        floatID = (fname.split('_')[0])[2:]
        cycle = (fname.split('_')[1]).split('.')[0]
        path = cfgv.rep_merge_argo_raw + fname
        mergeDF, bulkPath = fillMergeDF(mergeDF, path, floatID, cycle)

        print('%s  Argo_Merge profile (index: %d, name: %s)' % (datetime.today(), i, fname))
        try:
            dc.bulkInsert(bulkPath, tableName)
        finally:
            removed = False
            while not removed:
                try:
                    os.remove(bulkPath)    
                    removed = True
                except:
                    time.sleep(3)
                    removed = False
        print('%s  Done' % datetime.today())
    return




tableName = 'tblArgoMerge_REP'
bulkInsertArgoMerge(tableName)