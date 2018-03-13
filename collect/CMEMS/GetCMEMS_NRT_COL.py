#!/usr/bin/env python


import os
import sys
sys.path.append('../../config')
import config_vault as cfgv
sys.path.append('../../lib')
import dateLib as dl
from datetime import date
sys.path.append('../../db')
import DML as dml


def download(c1, c4, prefix, yr, startDay, endDay):

  for index in range(startDay,endDay+1):
    dayn = index % 1000
    day_index = dayn / 8
    if dayn % 8 == 0:
      day_index -= 1
    day_index = (day_index * 8) + 1
    tup = dl.daynToDate(yr * 1000 + day_index)

    c2 = str(tup.year) + '-' + str(tup.month).zfill(2) + '-' + str(tup.day).zfill(2)
    c3 = '" -T "'
    c5 = prefix + str(yr)  + str(index).zfill(3) + '.nc'
    command = c1 + c2 + c3 + c2 + c4 + c5
    os.system(command)
  return




def Checklist(startDay, endDay):
  for index in range(startDay,endDay+1):
    dml.updateChecklist(index, dl.daynToDate(index).year, dl.daynToDate(index).month, dl.daynToDate(index).day, 'NRT_COL_Raw', 1)
  return



if len(sys.argv)<>4:
  print('Enter 3 arguments as follow: Day StartDay EndDay')
  exit()

yr = int(sys.argv[1])
startDay = int(sys.argv[2])
endDay = int(sys.argv[3])



c1 = 'python2.7 motu-client.py -u mdehghaniashkez -p Jazireie08 -m http://cmems.isac.cnr.it/mis-gateway-servlet/Motu -s OCEANCOLOUR_GLO_OPTICS_L4_NRT_OBSERVATIONS_009_083-TDS -d dataset-oc-glo-opt-multi-l4-%s_4km_8days-rt-v01 -x -179.97917175293 -X 179.97917175293 -y -89.97917175293 -Y 89.979164123535 -t "'
c4 = '" %s -o %s -f '



c11 = c1 % 'cdm443'
c44 = c4 % ('-v CDM_error -v CDM -v CDM_flags', cfgv.nrt_col_raw)
pfx = cfgv.nrt_col_CDM443_prefix 
download(c11, c44, pfx, yr, startDay, endDay)


c11 = c1 % 'bbp443'
c44 = c4 % ('-v BBP_error -v BBP -v BBP_flags', cfgv.nrt_col_raw)
pfx = cfgv.nrt_col_BBP443_prefix
download(c11, c44, pfx, yr, startDay, endDay)


c11 = c1 % 'kd490'
c44 = c4 % ('-v KD490_error -v KD490 -v KD490_flags', cfgv.nrt_col_raw)
pfx = cfgv.nrt_col_KD490_prefix
download(c11, c44, pfx, yr, startDay, endDay)


c11 = c1 % 'rrs412'
c44 = c4 % ('-v RRS412_error -v RRS412 -v RRS412_flags', cfgv.nrt_col_raw)
pfx = cfgv.nrt_col_RRS412_prefix
download(c11, c44, pfx, yr, startDay, endDay)


c11 = c1 % 'rrs443'
c44 = c4 % ('-v RRS443_error -v RRS443 -v RRS443_flags', cfgv.nrt_col_raw)
pfx = cfgv.nrt_col_RRS443_prefix
download(c11, c44, pfx, yr, startDay, endDay)



c11 = c1 % 'rrs490'
c44 = c4 % ('-v RRS490_error -v RRS490 -v RRS490_flags', cfgv.nrt_col_raw)
pfx = cfgv.nrt_col_RRS490_prefix
download(c11, c44, pfx, yr, startDay, endDay)


c11 = c1 % 'rrs555'
c44 = c4 % ('-v RRS555_error -v RRS555 -v RRS555_flags', cfgv.nrt_col_raw)
pfx = cfgv.nrt_col_RRS555_prefix
download(c11, c44, pfx, yr, startDay, endDay)


c11 = c1 % 'rrs670'
c44 = c4 % ('-v RRS670_error -v RRS670 -v RRS670_flags', cfgv.nrt_col_raw)
pfx = cfgv.nrt_col_RRS670_prefix
download(c11, c44, pfx, yr, startDay, endDay)


c11 = c1 % 'spm'
c44 = c4 % ('-v SPM_error -v SPM -v SPM_flags', cfgv.nrt_col_raw)
pfx = cfgv.nrt_col_SPM_prefix
download(c11, c44, pfx, yr, startDay, endDay)


c11 = c1 % 'zsd'
c44 = c4 % ('-v ZSD_flags -v ZSD', cfgv.nrt_col_raw)
pfx = cfgv.nrt_col_ZSD_prefix
download(c11, c44, pfx, yr, startDay, endDay)








## Update tblChecklist
Checklist(startDay, endDay)



