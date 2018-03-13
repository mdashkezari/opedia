#!/usr/bin/env python

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

c1 = 'python2.7 motu-client.py -u mit_dehghani -p bos487tc -m http://motu.aviso.altimetry.fr/aviso-gateway-servlet/Motu -s AvisoDT -d dataset-duacs-dt-global-allsat-msla-uv -x -180 -X 180 -y -90 -Y 90 -t "'
c3 = '" -T "'
c4 = '" -v crs -v v -v u -v lon_bnds -v lat_bnds -v nv -o %s -f ' % cfgv.rep_uv_sla_raw

for index in range(startDay,endDay+1):
  tup = date.fromordinal(date(yr, 1, 1).toordinal() + index - 1)
  c2 = str(tup.year) + '-' + str(tup.month).zfill(2) + '-' + str(tup.day).zfill(2)  
  c5 = cfgv.rep_uv_sla_prefix + str(yr)  + str(index).zfill(3) + '.nc'
  command = c1 + c2 + c3 + c2 + c4 + c5
  print('')
  print('Downloading: '+c2)
  print('')
  os.system(command)


