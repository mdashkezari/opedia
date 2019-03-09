import sys
sys.path.append('../../config')
import config_vault as cfgv
import os
import datetime
import bz2
from datetime import datetime, date, timedelta
from time import sleep
if sys.version_info[0] >= 3:    # if python3 
    import urllib.request as req
else:
    import urllib as req


def getURL(yr, dayn):
    base = 'https://podaac-opendap.jpl.nasa.gov:443/opendap/allData/smap/L3/RSS/V3/8day_running/SCI/70KM/%d/%s/' % (yr, str(dayn).zfill(3))
    dayn2 = dayn + dayOffset
    lastday = 366 if yr % 4 == 0 else 365
    if dayn2 > lastday:
        yr += 1
        dayn2 = dayn2 - lastday
    fname = 'RSS_smap_SSS_L3_8day_running_70km_%d_%s_FNL_v03.0.nc?' % (yr, str(dayn2).zfill(3))
    vars = 'lon[0:1:1439],lat[0:1:719],time[0:1:0],nobs[0:1:719][0:1:1439],sss_smap[0:1:719][0:1:1439],sss_ref[0:1:719][0:1:1439],gland[0:1:719][0:1:1439],gice[0:1:719][0:1:1439],surtep[0:1:719][0:1:1439]'
    url = base + fname + vars
    return url, yr, dayn2


def get_nrt_sss(yr, mn, dy):
    stamp = datetime.strftime(datetime(yr, mn, dy), '%Y%m%d')
    dayn = format(datetime(yr, mn, dy), '%j')
    url, yr, dayn2 = getURL(yr, int(dayn))
    path_base = cfgv.nrt_sss_raw + cfgv.nrt_sss_prefix + '%s.nc'
    index = str(yr) + str(dayn2).zfill(3)
    path = path_base % (index)
    print('Dowloading SSS >>>  date: %s,  DayNumber: %s' % (datetime.strftime(dt, '%Y-%m-%d'),index))
    req.urlretrieve(url,path)
    return




if len(sys.argv)!=3:
  print('Enter 2 arguments as follow: Year-Month-Day Year-Month-Day')
  exit()

dayOffset = 4

dt1 = datetime.strptime(sys.argv[1], '%Y-%m-%d')
dt2 = datetime.strptime(sys.argv[2], '%Y-%m-%d')

dt1 = dt1 + timedelta(days=-dayOffset)
dt2 = dt2 + timedelta(days=-dayOffset)

dt = dt1

while(dt<=dt2):
    try:
        get_nrt_sss(dt.year, dt.month, dt.day)
    except Exception as e:
        print('================================')
        print('Error on %s' % datetime.strftime(dt, '%Y-%m-%d'))
        print('Error Message: %s' % e)
        print('Short wait ....')
        sleep(10)
        print('================================')
        get_nrt_sss(dt.year, dt.month, dt.day)


    dt = dt + timedelta(days=1)
