import sys
sys.path.append('../../config')
import config_vault as cfgv
import urllib
import datetime
import gzip
from datetime import date
import os
#from datetime import datetime



def dateToDayn(dt):
        dayn = int(format(dt, '%j'))
        dayn += dt.year * 1000
        return dayn


def daynToDate(dt):
        year = dt / 1000
        dayn = dt % 1000
        dat = date.fromordinal(date(year, 1, 1).toordinal() + dayn - 1)
        return dat


def get_nrt_wind(yr, mn, dy, hour):

        c1 = 'python motuclient.py ' + \
                '--user mdehghaniashkez --pwd Jazireie08 ' + \
                '--motu http://nrt.cmems-du.eu/motu-web/Motu ' + \
                '--service-id WIND_GLO_WIND_L4_NRT_OBSERVATIONS_012_004-TDS ' + \
                '--product-id CERSAT-GLO-BLENDED_WIND_L4-V5-OBS_FULL_TIME_SERIE ' + \
                '--longitude-min -180 --longitude-max 179.75 ' + \
                '--latitude-min -80 --latitude-max 80 --date-min "'

        c3 = '" --date-max "'
        c4 = '" --depth-min 9 --depth-max 11 --variable eastward_wind --variable northward_wind --variable surface_downward_eastward_stress --variable surface_downward_northward_stress --variable wind_speed --variable eastward_wind_rms --variable land_ice_mask --variable northward_wind_rms --variable sampling_length --variable wind_speed_rms --variable wind_stress --out-dir %s --out-name  ' % cfgv.nrt_wind_raw

        c2 = str(yr) + '-' + str(mn).zfill(2) + '-' + str(dy).zfill(2) + ' ' + str(hour).zfill(2) + ':00:00'
        c5 = cfgv.nrt_wind_prefix + str(yr*1000 +  date(yr, mn, dy).timetuple().tm_yday).zfill(3) + '_' + str(hour).zfill(2) + 'h.nc'
        command = c1 + c2 + c3 + c2 + c4 + c5
        os.system(command)

	return






if len(sys.argv)<>3:
  print('Enter 2 arguments as follow: StartDay EndDay')
  exit()

startday = int(sys.argv[1])
endday = int(sys.argv[2])



for index in range(startday, endday+1):
    dt = daynToDate(index)
    get_nrt_wind(dt.year, dt.month, dt.day, 0)       
    get_nrt_wind(dt.year, dt.month, dt.day, 6)       
    get_nrt_wind(dt.year, dt.month, dt.day, 12)       
    get_nrt_wind(dt.year, dt.month, dt.day, 18)       

