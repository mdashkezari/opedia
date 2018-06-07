import sys
sys.path.append('../../config')
import config_vault as cfgv
sys.path.append('../../lib')
import dateLib as dl
sys.path.append('../')
import dbCore as dc
import os
import netcdf as nc
import numpy as np
import pandas as pd
import pyodbc
import pandas.io.sql as sql
from datetime import datetime
import time
import math
import insertPrep as ip
import calendar



def bulkInsert_Darwin_Climatology(tableName, path):
    try:
        for month in range(1, 13):
            print('%s  Bulk insert into %s; month: %s.' % (datetime.today(), tableName, calendar.month_name[month]))
            bulkPath = path % month
            dc.bulkInsert(bulkPath, tableName)
    finally:
        pass
    print('%s  Done' % datetime.today())
    return



basePath = 'H:/Dropbox/darwinData/'

tableName = 'tblDarwin_Nutrient_Climatology'
path = basePath + 'darwin_nutrient_climatology_month_%2.2d.csv'
bulkInsert_Darwin_Climatology(tableName, path)

tableName = 'tblDarwin_Chl_Climatology'
path = basePath + 'darwin_chl_climatology_month_%2.2d.csv'
bulkInsert_Darwin_Climatology(tableName, path)

tableName = 'tblDarwin_Plankton_Climatology'
path = basePath + 'darwin_planktonClass_climatology_month_%2.2d.csv'
bulkInsert_Darwin_Climatology(tableName, path)