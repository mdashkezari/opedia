
import os
import sys
sys.path.append('../../config')
import config_vault as cfgv
import glob
outputdir = cfgv.rep_WOA_raw #'/media/nrhagen/Drobo/OpediaVault/observation/in-situ/cruise/WOA/rep/'


# variable_list = ['temperature', 'salinity', 'density','silicate', 'phosphate', 'oxygen', 'o2sat', 'nitrate','conductivivity', 'AOU' ]
variable_list = ['density']

decade_list_str = ['5564', '6574', '7584', '8594','95A4', 'A5B2']

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
        for decade in decade_list_str:
            print('collecting 1.00 degree data for ' + variable + ' for ' + decade)
            wget_str = 'wget -N -nH -nd -r -e robots=off --no-parent --force-html -A.nc http://data.nodc.noaa.gov/woa/WOA13/DATAv2/' + variable + '/netcdf/' + decade  + '/' + spatial_res + '/' + ' ' +  '-P' + outputdir + variable
            print(wget_str)
            run_wget_collect(wget_str)

getWOA_data()
