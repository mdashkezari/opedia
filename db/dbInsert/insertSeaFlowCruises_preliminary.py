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




def bulkInsertSeaFlowCruises():
    dataTitle = 'SeaFlow_Cruises'
    print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
    try:
        bulkPath = ''
        bulkPath = cfgv.seaflow_raw + 'SeaFlow_instrument_log.txt'
        #print('\t %s  Bulk %s %7.7d ready.' % (datetime.today(), dataTitle, itnum))
        dc.bulkInsert(bulkPath, tableName, '\t')
    finally:
        if bulkPath != '':
            print('File inserted: ' + bulkPath)
            #os.remove(bulkPath)    
    return



######### README ########
# first save the SeaFlow_instrument_log.xlxs file as text (tab delimited) file
# make sure that the txt file does not have empty rows at the end. This would result in many null records
# then run bulkInsertSeaFlowCruises() to insert the text file to Database
#########################

tableName = 'tblSeaFlow_Cruises'
bulkInsertSeaFlowCruises()