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
    dataTitle = 'Lineage'
    print('%s  Inserting Bulk %s into %s.' % (datetime.today(), dataTitle, tableName))
    try:
        bulkPath = cfgv.rep_lineage_raw + 'lineages-2018-03-12.csv'
        dc.bulkInsert(bulkPath, tableName)
    finally:
        pass
    print('%s  Done' % datetime.today())
    return




tableName = 'tblLineage'
bulkInsertLineage(tableName)