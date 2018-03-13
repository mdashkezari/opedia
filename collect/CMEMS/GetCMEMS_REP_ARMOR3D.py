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

if len(sys.argv)<>4:
  print('Enter 3 arguments as follow: Year StartDay EndDay')
  exit()

yr = int(sys.argv[1])
startDay = int(sys.argv[2])
endDay = int(sys.argv[3])

c1 = 'python2.7 motu-client.py -u mdehghaniashkez -p Jazireie08 -m http://motu.mfcglo-obs.cls.fr/mfcglo-armor-gateway-servlet/Motu -s GLOBAL_REP_PHYS_001_013-TDS -d dataset-armor-3d-rep-weekly-v3-1-myocean -x 0 -X -0.25 -y -82 -Y 90 -t "'
c3 = '" -T "'
c4 = '" -z 0 -Z 5500.0001 -v zvelocity -v height -v mvelocity -v salinity -v temperature -o %s -f ' % cfgv.rep_armor3d_raw

for index in range(startDay,endDay+1):
  d0 = date(1993, 1, 6)
  d1 = dl.daynToDate(yr * 1000 + index)
  days = (d1 - d0).days
  days = days - (days % 7) 
  tup = d0 + timedelta(days=days)


  c2 = str(tup.year) + '-' + str(tup.month).zfill(2) + '-' + str(tup.day).zfill(2)
  print(c2)
  c5 = cfgv.rep_armor3d_prefix + str(yr)  + str(index).zfill(3) + '.nc'
  command = c1 + c2 + c3 + c2 + c4 + c5
  os.system(command)


