"""
Author: Mohammad Dehghani Ashkezari <mdehghan@uw.edu>

Date: Spring 2018

Function: Generate module for climatological data sets.
"""

import sys
sys.dont_write_bytecode = True
import db

def isClimatology(tableName, varName=None):
    res = db.isClimatology(tableName)
    '''
    query = "SELECT Climatology FROM tblVariables "
    query = query + "JOIN tblDatasets ON [tblVariables].Dataset_ID=[tblDatasets].ID "    
    query = query + "WHERE Table_Name='%s' AND Short_Name='%s' "    
    query = query % (tableName, varName)
    df = db.dbFetch(query)
    res = df.Climatology[0]
    '''
    return 

def timeToMonth(dt):
    # assumption: dt is string and has the following format:  YYYY-MM-dd ....
    month = int(dt.split('-')[1])
    return month