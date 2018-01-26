#!/usr/bin/env python

# Get Absolute Dynamic Topography (ADT)    [Standard Name: Sea Surface Height Above Geoid (m)]

import os
import sys
from datetime import date
sys.path.append('../../config')
import config_vault as cfgv


if len(sys.argv)<>4:
  print('Enter 3 arguments as follow: Day StartDay EndDay')
  exit()

yr = int(sys.argv[1])
startDay = int(sys.argv[2])
endDay = int(sys.argv[3])

c1 = 'python2.7 motu-client.py -u mit_dehghani -p bos487tc -m http://motu.aviso.altimetry.fr/aviso-gateway-servlet/Motu -s AvisoDT -d dataset-duacs-dt-global-allsat-madt-h -x 0.125 -X -0.125 -y -89.875 -Y 89.875 -t "'
c3 = '" -T "'
c4 = '" -v crs -v lon_bnds -v lat_bnds -v adt -v nv -o %s -f ' % cfgv.rep_adt_raw

for index in range(startDay,endDay+1):
  tup = date.fromordinal(date(yr, 1, 1).toordinal() + index - 1)
  c2 = str(tup.year) + '-' + str(tup.month).zfill(2) + '-' + str(tup.day).zfill(2)  
  c5 = cfgv.rep_adt_prefix + str(yr)  + str(index).zfill(3) + '.nc'
  command = c1 + c2 + c3 + c2 + c4 + c5
  os.system(command)


