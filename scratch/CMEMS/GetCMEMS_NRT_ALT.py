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



def get_rep_uv_sla(yr, mn, dy):
        c1 = 'python motu-client.py -u mdehghaniashkez -p Jazireie08 -m http://motu.sltac.cls.fr/sltac-gateway-servlet/Motu -s SEALEVEL_GLO_PHY_L4_NRT_OBSERVATIONS_008_046-TDS -d dataset-duacs-nrt-global-merged-allsat-phy-l4-v3 -x 0.125 -X -0.125 -y -89.875 -Y 89.875 -t "'
        c3 = '" -T "'
        c4 = '" -v err -v vgosa -v vgos -v sla -v adt -v ugosa -v ugos -o %s -f ' % cfgv.nrt_alt_raw

        c2 = str(yr) + '-' + str(mn).zfill(2) + '-' + str(dy).zfill(2)
        c5 = cfgv.nrt_alt_prefix + str(yr*1000 +  date(yr, mn, dy).timetuple().tm_yday).zfill(3) + '.nc'
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
    get_rep_uv_sla(dt.year, dt.month, dt.day)       # REP velocities (SLA/ADT)

