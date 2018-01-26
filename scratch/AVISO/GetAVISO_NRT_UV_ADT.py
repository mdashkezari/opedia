#!/usr/bin/env python

import sys
import urllib
import datetime
import gzip
from datetime import date
sys.path.append('../../config')
import config_vault as cfgv
sys.path.append('../../lib')
import dateLib as dl
sys.path.append('../../db')
import DML as dml



def get_nrt_uv_adt_ftp(yr, mn, dy):
	url_base = 'ftp://mit_dehghani:bos487tc@ftp.aviso.altimetry.fr/global/near-real-time/grids/madt/all-sat-merged/uv/nrt_global_allsat_madt_uv_%s.nc.gz'
        path_base = cfgv.nrt_uv_adt_raw + cfgv.nrt_uv_adt_prefix + '%d.nc.gz'

        dt0 = datetime.date(yr,mn,dy)
        dt = datetime.date(yr,mn,dy)
        dt += datetime.timedelta(days=0)

        index = dt0.strftime('%Y%m%d') + '_' + dt.strftime('%Y%m%d')
        url = url_base % index
        path = path_base % int( yr*1000 +  date(yr, mn, dy).timetuple().tm_yday  )

        print ('Downloading UV ADT: '+index)
        urllib.urlretrieve(url,path)

        inF = gzip.open(path, 'rb')
        outF = open(path[:-3], 'wb')
        outF.write( inF.read() )
        inF.close()
        outF.close()

	return



if len(sys.argv)<>4:
  print('Enter 3 arguments as follow: Year Month Day')
  exit()


###### only get today data #####
today = datetime.datetime.now().date()
get_nrt_uv_adt_ftp(today.year, today.month, today.day)

dml.updateChecklist(dl.dateToDayn(today), today.year, today.month, today.day, 'NRT_UV_ADT_Raw', 1)
################################


'''
yr = int(sys.argv[1])
startDay = int(sys.argv[2])
endDay = int(sys.argv[3])


for index in range(startDay,endDay+1):
        dt = dl.daynToDate(yr * 1000 + index)
        get_nrt_uv_adt_ftp(dt.year, dt.month, dt.day)
'''
