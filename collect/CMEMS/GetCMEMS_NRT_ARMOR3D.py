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
sys.path.append('../../db')
import DML as dml



if len(sys.argv)<>4:
  print('Enter 3 arguments as follow: Day StartDay EndDay')
  exit()

yr = int(sys.argv[1])
startDay = int(sys.argv[2])
endDay = int(sys.argv[3])

c1 = 'python2.7 motu-client.py -u mdehghaniashkez -p Jazireie08 -m http://motu.mfcglo-obs.cls.fr/mfcglo-armor-gateway-servlet/Motu -s GLOBAL_ANALYSIS_PHYS_001_020-TDS -d dataset-armor-3d-v4-cmems-v2 -x 0.125 -X -0.125 -y -82.125 -Y 89.875 -t "'
c3 = '" -T "'
c4 = '" -z 0 -Z 5500.0001 -v zvelocity -v height -v mvelocity -v salinity -v temperature -o %s -f ' % cfgv.nrt_armor3d_raw

for index in range(startDay,endDay+1):
  d0 = date(2014, 1, 1)
  d1 = dl.daynToDate(yr * 1000 + index)
  days = (d1 - d0).days
  days = days - (days % 7) 
  tup = d0 + timedelta(days=days)


  c2 = str(tup.year) + '-' + str(tup.month).zfill(2) + '-' + str(tup.day).zfill(2)
  c5 = cfgv.nrt_armor3d_prefix + str(yr)  + str(index).zfill(3) + '.nc'
  command = c1 + c2 + c3 + c2 + c4 + c5
  os.system(command)

  dml.updateChecklist(index, dl.daynToDate(index).year, dl.daynToDate(index).month, dl.daynToDate(index).day, 'NRT_ARMOR3D_Raw', 1)
