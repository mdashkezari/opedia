"""
Author: Mohammad Dehghani Ashkezari <mdehghan@uw.edu>

Date: 2019-06-14

Function: Retrieve metadata associated with a variable.
"""

import os
import sys
sys.path.append(os.path.dirname(__file__))
sys.dont_write_bytecode = True
import numpy as np
import pandas as pd
import db


def getReferences(datasetID):
    query = "SELECT Reference FROM dbo.udfDatasetReferences(%d)" % datasetID
    return db.dbFetch(query)


def getMetadata_NoRef(table, variable):
    query = "SELECT * FROM dbo.udfMetaData_NoRef('%s', '%s')" % (variable, table)
    return db.dbFetch(query)


def getMetaData(table, variable):
    """Return a dataframe containing the associated metadata."""
    df = getMetadata_NoRef(table, variable)
    datasetID = df.iloc[0]['Dataset_ID']
    refs = getReferences(datasetID)
    return pd.concat([df, refs], axis=1) 

