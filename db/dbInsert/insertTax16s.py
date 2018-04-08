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




def bulkInsertLineage(tableName):
    dataTitle = 'tax16s'
    print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
    try:
        bulkPath = cfgv.rep_tax16s_raw + 'diel1.bf100_id99.rain_sig_all.bf100.vs_MarRef.uniq_taxids.csv'
        dc.bulkInsert(bulkPath, tableName)
    finally:
        pass
    print('%s  Done' % datetime.today())
    return




tableName = 'tblRyan'
bulkInsertLineage(tableName)