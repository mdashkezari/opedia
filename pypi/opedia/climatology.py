import sys
sys.dont_write_bytecode = True
import db

def isClimatology(tableName, varName):
    query = "SELECT Climatology FROM tblVariables "
    query = query + "JOIN tblDatasets ON [tblVariables].Dataset_ID=[tblDatasets].ID "    
    query = query + "WHERE Table_Name='%s' AND Short_Name='%s' "    
    query = query % (tableName, varName)
    df = db.dbFetch(query)
    return df.Climatology[0]

def timeToMonth(dt):
    # assumption: dt is string and has the following format:  YYYY-MM-dd ....
    month = int(dt.split('-')[1])
    return month