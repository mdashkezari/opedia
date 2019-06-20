#!/usr/bin/env python


""" collection script for 8day 25km res chl data """

import os
import sys
sys.path.append('../../config')
import config_vault as cfgv
from datetime import date
from time import sleep




def raw_file_exists(folder, prefix, itnum, file_format):
	res = False
	path = '%s%s%7.7d%s' % (folder, prefix, itnum, file_format)
	if os.path.isfile(path):
		res = True
	return res


def halt(txt='Fatal error!'):
    print(txt, file=sys.stderr)
    sys.exit(1)


if len(sys.argv)!=5:
	print('Enter 4 arguments as follow: StartYear EndYear StartDay EndDay')
	exit()



## specific to this data set:  the first file at each year always starts at Jan, 1s 
## and then steps forwad with 8day intervals 


start_yr = int(sys.argv[1])
end_yr = int(sys.argv[2])
startDay = int(sys.argv[3])
endDay = int(sys.argv[4])


c1 = 'python motuclient.py ' + \
      '--user mdehghaniashkez --pwd Jazireie08 ' + \
      '--motu http://my.cmems-du.eu/motu-web/Motu ' + \
      '--service-id OCEANCOLOUR_GLO_CHL_L4_REP_OBSERVATIONS_009_082-TDS ' + \
      '--product-id dataset-oc-glo-chl-multi-l4-gsm_25km_8days-rep-v02 ' + \
      '--longitude-min -179.9791717529297 --longitude-max 179.9791717529297 ' + \
      '--latitude-min -89.97917175292969 --latitude-max 89.97916412353516 --date-min "'
c3 = '" --date-max "'
c4 = '" --variable CHL --variable CHL_error --out-dir %s --out-name ' % cfgv.rep_chl_8day_raw

#for index in range(startDay,endDay+1):
year_range = range(start_yr, end_yr)
for yr in year_range:
	index = startDay
	while index <= endDay:
		print('*************')
		print('Downloading: ' + str(yr*1000+index) )
		print('*************')
		tup = date.fromordinal(date(yr, 1, 1).toordinal() + index - 1)
		c2 = str(tup.year) + '-' + str(tup.month).zfill(2) + '-' + str(tup.day).zfill(2)
		c5 = cfgv.rep_chl_8day_prefix + str(yr)  + str(index).zfill(3) + '.nc'
		command = c1 + c2 + c3 + c2 + c4 + c5
		os.system(command)
		sleep(1)
		if raw_file_exists(cfgv.rep_chl_8day_raw, cfgv.rep_chl_8day_prefix, yr*1000+index, '.nc'):
			index = index + 8
		else:
			print('Not Successful in downloading: ' + str(yr*1000+index) )
			halt()
			# index = index + 1
