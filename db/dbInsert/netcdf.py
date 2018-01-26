
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import xarray as xr


def ncdisp(path):
    def begin():
        print('\n')
        print('************************************************************')
    def end():
        print('************************************************************')
        print('\n')

    nc = Dataset(path, 'r')
    begin()
    print('\t File format: %s' % nc. data_model)
    end()

    begin()
    print('\t Dimentions: %s' % str(nc.dimensions))
    end()

    begin()
    for index, i in enumerate(nc.variables):
        print('%d. Variable: %s' % (index+1, i))
        print(str(nc.variables[i]))
        #print('\t Unit: ' + nc.variables[i].units)
        #print('\t Shape: ' + str(nc.variables[i].shape))
        #print('\t Scale Factor: ' + str(nc.variables[i].scale_factor))
        #print('\t Add Offset: ' + str(nc.variables[i].add_offset))
        print('\n')
    end()

    nc.close()
    return



def ncread(path, varName):
    nc = Dataset(path, 'r')
    data = nc.variables[varName][:].squeeze()
    nc.close()
    return data
    


def ncFillValue(path, varName, fillName='_FillValue'):
    nc = Dataset(path, 'r')
    fillVal = nc.variables[varName]._FillValue
    nc.close()
    return fillVal



def ncToDF(path):
    ds = xr.open_dataset(path)
    df = ds.to_dataframe()

    '''
    ############## slice North Pacific gyre (remove if need global) ##############
    lat1 = 10
    lat2 = 60
    lon1 = -170
    lon2 = -120
    if path.find('sla_') != -1 or path.find('uv_') != -1:
        lon1 = lon1 + 360
        lon2 = lon2 + 360
    #df = df.iloc[(df['lat'] >= lat1) & (df['lat'] <= lat2) & (df['lon'] >= lon1) & (df['lon'] <= lon2)]
    df = df.iloc[(df.index.get_level_values('lat') >= lat1) & (df.index.get_level_values('lat') <= lat2) & (df.index.get_level_values('lon') >= lon1) & (df.index.get_level_values('lon')<= lon2)]
    ##############################################################################
    '''
    return df
