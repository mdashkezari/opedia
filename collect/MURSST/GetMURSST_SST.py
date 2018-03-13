
import sys
import os
import urllib
import datetime
sys.path.append('../../config')
import config_vault as cfgv
sys.path.append('../../lib')
import dateLib as dl
sys.path.append('../../db')
import DML as dml


def get_sst_year(year):
  start_index = 1
  end_index = 365	
  dt = datetime.datetime(year, 1, 1, 0, 0, 0)
  #if year in [2016, 2012, 2008, 2004, 2000, 1996, 1992]:
  if year % 4 == 0:	
    end_index = 366		
  base_folder = cfgv.nrt_sst_raw

  dt += datetime.timedelta(days=-1)
  for day in range(start_index, end_index+1):
    dt += datetime.timedelta(days=1)
    dts = datetime.date.strftime(dt, "%Y%m%d")
    url = 'ftp://podaac-ftp.jpl.nasa.gov/allData/ghrsst/data/GDS2/L4/GLOB/JPL/MUR/v4.1/'+str(year)+'/'+str(day).zfill(3)+'/'+dts+'090000-JPL-L4_GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1.nc'	
    path = base_folder + cfgv.nrt_sst_prefix + str(year) +  str(day).zfill(3)+'.nc';
    print('Downloading: ' + url);
    urllib.urlretrieve (url, path);



def get_sst_day(year, day):
  dt = datetime.datetime(year, 1, 1, 0, 0, 0)
  base_folder = cfgv.nrt_sst_raw

  dt += datetime.timedelta(days=day-1)
  dts = datetime.date.strftime(dt, "%Y%m%d")
  url = 'ftp://podaac-ftp.jpl.nasa.gov/allData/ghrsst/data/GDS2/L4/GLOB/JPL/MUR/v4.1/'+str(year)+'/'+str(day).zfill(3)+'/'+dts+'090000-JPL-L4_GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1.nc' 
  path = base_folder + cfgv.nrt_sst_prefix + str(year) + str(day).zfill(3)+'.nc';
  print('Downloading: ' + url);
  urllib.urlretrieve (url, path);




#year = int(sys.argv[1])
#for year in range(2003, 2015):
#get_sst_year(year)


year = int(sys.argv[1])
day_start = int(sys.argv[2])
day_end = int(sys.argv[3])
for day in range(day_start, day_end+1):
  get_sst_day(year, day)

  dml.updateChecklist(day, dl.daynToDate(day).year, dl.daynToDate(day).month, dl.daynToDate(day).day, 'NRT_SST_Raw', 1) 
