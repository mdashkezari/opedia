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
        #Version 5
        c1 = 'python motu-client.py -u mdehghaniashkez -p Jazireie08 -m http://cmems.isac.cnr.it/mis-gateway-servlet/Motu -s WIND_GLO_WIND_L4_NRT_OBSERVATIONS_012_004-TDS -d CERSAT-GLO-BLENDED_WIND_L4-V5-OBS_FULL_TIME_SERIE -x -180 -X 179.75 -y -80 -Y 80 -t "'
        #Version 3
        #c1 = 'python motu-client.py -u mdehghaniashkez -p Jazireie08 -m http://cmems.isac.cnr.it/mis-gateway-servlet/Motu -s WIND_GLO_WIND_L4_NRT_OBSERVATIONS_012_004-TDS -d CERSAT-GLO-BLENDED_WIND_L4-V3-OBS_FULL_TIME_SERIE -x -180 -X 179.75 -y -80 -Y 80 -t "'
        c3 = '" -T "'
        c4 = '" -z 9 -Z 11 -v wind_speed_rms -v eastward_wind_rms -v wind_stress -v land_ice_mask -v surface_downward_eastward_stress -v eastward_wind -v sampling_length -v surface_downward_northward_stress -v wind_speed -v northward_wind -v northward_wind_rms -o  %s -f ' % cfgv.nrt_wind_raw

        c2 = str(yr) + '-' + str(mn).zfill(2) + '-' + str(dy).zfill(2) + ' ' + str(hour).zfill(2) + ':00:00'
        c5 = cfgv.nrt_wind_prefix + str(yr*1000 +  date(yr, mn, dy).timetuple().tm_yday).zfill(3) + '_' + str(hour).zfill(2) + 'h.nc'
        command = c1 + c2 + c3 + c2 + c4 + c5
        os.system(command)

	return






if len(sys.argv)<>3:
  print('Enter 2 arguments as follow: StartDay EndDay Hour')
  exit()

startday = int(sys.argv[1])
endday = int(sys.argv[2])



for index in range(startday, endday+1):
    dt = daynToDate(index)
    get_nrt_wind(dt.year, dt.month, dt.day, 0)       
    get_nrt_wind(dt.year, dt.month, dt.day, 6)       
    get_nrt_wind(dt.year, dt.month, dt.day, 12)       
    get_nrt_wind(dt.year, dt.month, dt.day, 18)       

