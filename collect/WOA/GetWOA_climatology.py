
import os
import sys
sys.path.append('../../config')
import config_vault as cfgv
import glob
outputdir = cfgv.rep_WOA_climatology_raw


variable_list = ['temperature', 'salinity', 'density','silicate', 'phosphate', 'oxygen', 'o2sat', 'nitrate','conductivivity', 'sea_water_electrical_conductivity', 'sea_water_sigma', 'sea_water_temperature','AOU' ]


spatial_res = '1.00'


def makedir(outputdir, variable):
    try:
        os.chdir(outputdir + variable)
    except:
        os.mkdir(outputdir + variable)
        os.chdir(outputdir + variable)

def run_wget_collect(wget_str):
    os.system(wget_str)

def getWOA_data():
    for variable in variable_list:
        makedir(outputdir, variable)
        if (variable == 'conductivity' or variable == 'density' or variable == 'salinity' or variable == 'sea_water_electrical_conductivity' or variable == 'sea_water_sigma' or variable == 'sea_water_temperature' or variable == 'temperature'):
            print('collecting 1.00 degree data for ' + variable)
            wget_str = 'wget -N -nH -nd -r -e robots=off --no-parent --force-html -A.nc http://data.nodc.noaa.gov/woa/WOA13/DATAv2/' + variable + '/netcdf/decav/' + spatial_res + '/ ' +  '-P ' + outputdir + variable
            print(wget_str)
            run_wget_collect(wget_str)
        else:
            print('collecting 1.00 degree data for ' + variable)
            wget_str = 'wget -N -nH -nd -r -e robots=off --no-parent --force-html -A.nc http://data.nodc.noaa.gov/woa/WOA13/DATAv2/' + variable + '/netcdf/all/' + spatial_res  + '/ ' +  '-P ' + outputdir + variable
            print(wget_str)
            run_wget_collect(wget_str)

getWOA_data()
