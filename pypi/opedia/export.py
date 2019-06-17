"""
Author: Mohammad Dehghani Ashkezari <mdehghan@uw.edu>

Date: 2019-06-15

Function: Store the retrieved data/metadata from the Simons CMAP database on local machine
"""

import os
import sys
sys.path.append(os.path.dirname(__file__))
sys.dont_write_bytecode = True
import pandas as pd
import metadata as meta
from zipfile import ZipFile


def makeDir(directory):     
    if not os.path.exists(directory):
        os.makedirs(directory)
    return 


def expPath(table, variable, prefix, fmt):
    dirPath = './data/'
    makeDir(dirPath)
    if prefix != '':
        prefix += '_'
    base = dirPath + prefix + variable + '_' + table     
    dataPath = base + fmt
    metaPath = base + '_meta' + fmt
    zipPath = base + '.zip'
    return dataPath, metaPath, zipPath


def saveCSV(df, path):
    df.to_csv(path, index=False)
    return


def zip(dataPath, metaPath, zipPath):
    """Zip the data and metadata files."""
    with ZipFile(zipPath, 'w') as ZIP:
        ZIP.write(dataPath)
        ZIP.write(metaPath)
    return

def dump(df, table, variable, prefix='', fmt='.csv'):
    """Save data and metadata files as a single zipped file on local machine."""    
    fmt = fmt.lower().strip()
    dataPath, metaPath, zipPath = expPath(table, variable, prefix, fmt)
    dfMeta = meta.getMetaData(table, variable)

    if fmt == '.csv':
        saveCSV(df, dataPath)   
        saveCSV(dfMeta, metaPath)

    zip(dataPath, metaPath, zipPath)
    os.remove(dataPath)
    os.remove(metaPath)
    return zipPath