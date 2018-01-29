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
import os.path

'''
if len(sys.argv)<>4:
  print('Enter 3 arguments as follow: Day StartDay EndDay')
  exit()

yr = int(sys.argv[1])
startDay = int(sys.argv[2])
endDay = int(sys.argv[3])

c1 = 'python motu-client.py -u mdehghaniashkez -p Jazireie08 -m http://nrtcmems.mercator-ocean.fr/motu-web/Motu -s GLOBAL_ANALYSIS_FORECAST_BIO_001_014-TDS -d dataset-global-analysis-forecast-bio-001-014 -x -180 -X 179.5 -y -89 -Y 90 -t "'
c3 = '" -T "'
c4 = '" -z 0.493 -Z 5727.918 -v Fe -v PP -v Si -v NO3 -v CHL -v PHYC -v PO4 -v O2 -o %s -f ' % cfgv.nrt_mercator_pisces_raw

for index in range(startDay,endDay+1):
  d0 = date(2011, 12, 31)
  d1 = dl.daynToDate(yr * 1000 + index)
  days = (d1 - d0).days
  days = days - (days % 7) 
  tup = d0 + timedelta(days=days)


  #tup = date.fromordinal(date(yr, 1, 1).toordinal() + index - 1)
  c2 = str(tup.year) + '-' + str(tup.month).zfill(2) + '-' + str(tup.day).zfill(2) + ' 12:00:00' 
  c5 = cfgv.nrt_mercator_pisces_prefix + str(yr)  + str(index).zfill(3) + '.nc'
  command = c1 + c2 + c3 + c2 + c4 + c5
  os.system(command)
'''





####################


def get_all_available_days():
  dt = date(2011, 12, 31)
  days = []
  while(dt<=date.today()):    
    days.append(dt)
    dt = dt + timedelta(days=7)         
  return days

def piscesFileExist(days=get_all_available_days()):
      for dt in days:
        path = cfgv.nrt_mercator_pisces_raw + cfgv.nrt_mercator_pisces_prefix + str(dl.dateToDayn(dt)) + '.nc'
        print path
        if not os.path.isfile(path):
              print('The following file not found in the opedia vault: ' + path + ', Date: ' + dt.strftime('%Y-%m-%d'))
      return

def get_nrt_mercator_pisces_raw(dt):
      
  c1 = 'python motu-client.py -u mdehghaniashkez -p Jazireie08 -m http://nrtcmems.mercator-ocean.fr/motu-web/Motu -s GLOBAL_ANALYSIS_FORECAST_BIO_001_014-TDS -d dataset-global-analysis-forecast-bio-001-014 -x -180 -X 179.5 -y -89 -Y 90 -t "'
  c3 = '" -T "'
  c4 = '" -z 0.493 -Z 5727.918 -v Fe -v PP -v Si -v NO3 -v CHL -v PHYC -v PO4 -v O2 -o %s -f ' % cfgv.nrt_mercator_pisces_raw

  c2 = str(dt.year) + '-' + str(dt.month).zfill(2) + '-' + str(dt.day).zfill(2) + ' 12:00:00' 
  c5 = cfgv.nrt_mercator_pisces_prefix + str(dl.dateToDayn(dt)) + '.nc'
  command = c1 + c2 + c3 + c2 + c4 + c5
  os.system(command)

  return



####### Check which files are missing
piscesFileExist()
#####################################



if len(sys.argv)<>3:
    print('Enter 2 arguments as follow: Year-Month-Day Year-Month-Day')
    exit()

dt1 = datetime.strptime(sys.argv[1], '%Y-%m-%d')
dt2 = datetime.strptime(sys.argv[2], '%Y-%m-%d')
dt = dt1
while(dt<=dt2):    
    try:
        dayn = dl.dateToDayn(dt)
        print('Dowloading Mercator_Pisces >>>  date: %s,  DayNumber: %s' % (datetime.strftime(dt, '%Y-%m-%d'), dayn))
        get_nrt_mercator_pisces_raw(dt)
    except Exception as e:
        print('================================')
        print('Error on %s' % datetime.strftime(dt, '%Y-%m-%d'))
        print('Error Message: %s' % e.message)
        print('Short wait ....')
        sleep(10)
        print('================================')
        get_nrt_mercator_pisces_raw(dt)
        
        
    dt = dt + timedelta(days=7)
