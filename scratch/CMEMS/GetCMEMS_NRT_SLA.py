#!/usr/bin/env python


import os
import sys
sys.path.append('../../config')
import config_vault as cfgv
from datetime import date
sys.path.append('../../lib')
import dateLib as dl
sys.path.append('../../db')
import DML as dml


if len(sys.argv)<>4:
  print('Enter 3 arguments as follow: Day StartDay EndDay')
  exit()

yr = int(sys.argv[1])
startDay = int(sys.argv[2])
endDay = int(sys.argv[3])

c1 = 'python2.7 motu-client.py -u mdehghaniashkez -p Jazireie08 -m http://motu.sltac.cls.fr/sltac-gateway-servlet/Motu -s SEALEVEL_GLO_SLA_MAP_L4_NRT_OBSERVATIONS_008_026-TDS -d dataset-duacs-nrt-global-merged-allsat-msla-l4 -x 0.125 -X -0.125 -y -89.875 -Y 89.875 -t "'
c3 = '" -T "'
c4 = '" -v crs -v lon_bnds -v lat_bnds -v sla -v nv -o %s -f ' % cfgv.nrt_sla_raw

for index in range(startDay,endDay+1):
  tup = date.fromordinal(date(yr, 1, 1).toordinal() + index - 1)
  c2 = str(tup.year) + '-' + str(tup.month).zfill(2) + '-' + str(tup.day).zfill(2)  
  c5 = cfgv.nrt_sla_prefix + str(yr)  + str(index).zfill(3) + '.nc'
  command = c1 + c2 + c3 + c2 + c4 + c5
  os.system(command)

  dml.updateChecklist(index, dl.daynToDate(index).year, dl.daynToDate(index).month, dl.daynToDate(index).day, 'NRT_SLA_Raw', 1)
