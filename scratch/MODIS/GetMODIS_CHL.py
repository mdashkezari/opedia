
import sys
import os
import urllib
sys.path.append('../../config')
import config_vault as cfgv



def get_chl(year, day):
  start_index = day / 8
  if day % 8 == 0:
    start_index = start_index - 1
  start_index = (start_index * 8) + 1
		
  end_index = start_index + 7	
  if start_index == 361:
    end_index = 365
  #if year in [2016, 2012, 2008, 2004, 2000, 1996, 1992] and start_index == 361:
  if (year % 4 == 0) and (start_index == 361):
    end_index = 366		
  base_folder = cfgv.nrt_chl_raw
  url = 'http://oceandata.sci.gsfc.nasa.gov/cgi/getfile/A'+str(year)+str(start_index).zfill(3)+str(year)+str(end_index).zfill(3)+'.L3m_8D_CHL_chlor_a_4km.nc'	
  path = base_folder + cfgv.nrt_chl_prefix + str(year) + str(day).zfill(3) + '.nc';
  print('Downloading: ' + url);
  urllib.urlretrieve (url, path);



year = int(sys.argv[1])
startDay = int(sys.argv[2])
endDay = int(sys.argv[3])


#for index in range(0, 360/8 + 1):
for day in range(startDay, endDay+1):
  get_chl(year, day)

