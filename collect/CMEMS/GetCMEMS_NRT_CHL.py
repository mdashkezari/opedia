#!/usr/bin/env python


import os
import sys
sys.path.append('../../config')
import config_vault as cfgv
from datetime import date
sys.path.append('../../db')
#import DML as dml
from time import sleep


def raw_file_exists(folder, prefix, itnum, file_format):
        res = False
        path = '%s%s%7.7d%s' % (folder, prefix, itnum, file_format)
        if os.path.isfile(path):
                res = True
        return res




if len(sys.argv)!=4:
  print('Enter 3 arguments as follow: Year StartDay EndDay')
  exit()

yr = int(sys.argv[1])
startDay = int(sys.argv[2])
endDay = int(sys.argv[3])


c1 = 'python motuclient.py ' + \
      '--user mdehghaniashkez --pwd Jazireie08 ' + \
      '--motu http://nrt.cmems-du.eu/motu-web/Motu ' + \
      '--service-id OCEANCOLOUR_GLO_CHL_L4_NRT_OBSERVATIONS_009_033-TDS ' + \
      '--product-id dataset-oc-glo-chl-multi-l4-oi_4km_daily-rt-v02 ' + \
      '--longitude-min 0.125 --longitude-max -0.125 ' + \
      '--latitude-min -89.875 --latitude-max 89.875 --date-min "'

c3 = '" --date-max "'
c4 = '" --variable CHL --variable CHL_error --out-dir %s --out-name  ' % cfgv.nrt_chl_raw

#for index in range(startDay,endDay+1):
index = startDay
while index <= endDay:
  print('*************')
  print('Downloading: ' + str(yr*1000+index) )
  print('*************')
  tup = date.fromordinal(date(yr, 1, 1).toordinal() + index - 1)
  c2 = str(tup.year) + '-' + str(tup.month).zfill(2) + '-' + str(tup.day).zfill(2)
  c5 = cfgv.nrt_chl_prefix + str(yr)  + str(index).zfill(3) + '.nc'
  command = c1 + c2 + c3 + c2 + c4 + c5
  os.system(command)
  sleep(1)
  if raw_file_exists(cfgv.nrt_chl_raw, cfgv.nrt_chl_prefix, yr*1000+index, '.nc'):
        index = index + 1
  else:
        print('Not Successful in downloading: ' + str(yr*1000+index) )

  #dml.updateChecklist(index, dl.daynToDate(index).year, dl.daynToDate(index).month, dl.daynToDate(index).day, 'NRT_CHL_Raw', 1)
