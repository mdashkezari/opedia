import sys
sys.path.append('../../config')
import config_vault as cfgv
import os
import urllib.request

import datetime
import bz2
from datetime import datetime, date, timedelta
from time import sleep


def get_nrt_avhrr_oi(yr, mn, dy):
    def decompress(path):
        zipfile = bz2.BZ2File(path)
        data = zipfile.read()
        newfilepath = path[:-4]
        open(newfilepath, 'wb').write(data)

    stamp = datetime.strftime(datetime(yr, mn, dy), '%Y%m%d')
    dayn = format(datetime(yr, mn, dy), '%j')
    url = 'ftp://podaac-ftp.jpl.nasa.gov/allData/ghrsst/data/GDS2/L4/GLOB/NCEI/AVHRR_OI/v2/%s/%s/%s120000-NCEI-L4_GHRSST-SSTblend-AVHRR_OI-GLOB-v02.0-fv02.0.nc' % (yr, dayn, stamp)
    path_base = cfgv.nrt_sst_raw + cfgv.nrt_sst_prefix + '%s.nc'
    index = str(yr) + dayn
    path = path_base % (index)
    print('Dowloading AVHRR_OI_SST >>>  date: %s,  DayNumber: %s' % (datetime.strftime(dt, '%Y-%m-%d'),index))
    urllib.request.urlretrieve(url,path)
    #decompress(path)
    #os.remove(path)
    return





if len(sys.argv)!=3:
  print('Enter 2 arguments as follow: Year-Month-Day Year-Month-Day')
  exit()

dt1 = datetime.strptime(sys.argv[1], '%Y-%m-%d')
dt2 = datetime.strptime(sys.argv[2], '%Y-%m-%d')

dt = dt1

while(dt<=dt2):
    try:
        get_nrt_avhrr_oi(dt.year, dt.month, dt.day)
    except Exception as e:
        print('================================')
        print('Error on %s' % datetime.strftime(dt, '%Y-%m-%d'))
        print('Error Message: %s' % e)
        print('Short wait ....')
        sleep(10)
        print('================================')
        get_nrt_avhrr_oi(dt.year, dt.month, dt.day)


    dt = dt + timedelta(days=1)



'''
if len(sys.argv)<>4:
  print('Enter 3 arguments as follow: Year Month Day')
  exit()



###### only get today data #####
today = datetime.datetime.now().date()
get_nrt_adt_ftp(today.year, today.month, today.day)
################################
'''


'''
yr = int(sys.argv[1])
startDay = int(sys.argv[2])
endDay = int(sys.argv[3])


for index in range(startDay,endDay+1):
        dt = dl.daynToDate(yr * 1000 + index)
	get_nrt_adt_ftp(dt.year, dt.month, dt.day)
'''
