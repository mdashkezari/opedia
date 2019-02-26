#!/usr/bin/env python


import os
import sys
sys.path.append('../../config')
import config_vault as cfgv
sys.path.append('../../lib')
import dateLib as dl
from datetime import date
from datetime import datetime
from datetime import timedelta
from time import sleep




def get_nrt_mercator_mld(dt):
  c1 = 'python motuclient.py ' + \
      '--user mdehghaniashkez --pwd Jazireie08 ' + \
      '--motu http://nrt.cmems-du.eu/motu-web/Motu ' + \
      '--service-id GLOBAL_ANALYSIS_FORECAST_PHY_001_024-TDS ' + \
      '--product-id global-analysis-forecast-phy-001-024 ' + \
      '--longitude-min -180 --longitude-max 179.9166717529297 ' + \
      '--latitude-min -80 --latitude-max 90 --date-min "'

  c3 = '" --date-max "'
  c4 = '" --depth-min 0.493 --depth-max 0.4942 --variable mlotst --out-dir %s --out-name ' % cfgv.nrt_mercator_mld_raw

  c2 = str(dt.year) + '-' + str(dt.month).zfill(2) + '-' + str(dt.day).zfill(2) + ' 12:00:00'
  c5 = cfgv.nrt_mercator_mld_prefix + str(dl.dateToDayn(dt)) + '.nc'
  command = c1 + c2 + c3 + c2 + c4 + c5
  os.system(command)
  return




if len(sys.argv)!=3:
    print('Enter 2 arguments as follow: Year-Month-Day Year-Month-Day')
    exit()

dt1 = datetime.strptime(sys.argv[1], '%Y-%m-%d')
dt2 = datetime.strptime(sys.argv[2], '%Y-%m-%d')
dt = dt1
while(dt<=dt2):
    try:
        dayn = dl.dateToDayn(dt)
        print('Dowloading Mercator_Pisces >>>  date: %s,  DayNumber: %s' % (datetime.strftime(dt, '%Y-%m-%d'), dayn))
        get_nrt_mercator_mld(dt)
    except Exception as e:
        print('================================')
        print('Error on %s' % datetime.strftime(dt, '%Y-%m-%d'))
        print('Error Message: %s' % e.message)
        print('Short wait ....')
        sleep(10)
        print('================================')
        get_nrt_mercator_mld(dt)


    dt = dt + timedelta(days=1)
