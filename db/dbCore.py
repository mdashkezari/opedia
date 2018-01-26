import sys
sys.path.append('../config')
import config_vault as cfgv
sys.path.append('../lib')
import dateLib as dl
import numpy as np
import pandas as pd
import pyodbc
import pandas.io.sql as sql



def dbConnect(local=True):
    try:
        if local: 
			## Local Database
			server = 'THEBEAST'
			db = 'Opedia'
			conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')
        else: 
			## Cloud (Azure) Database			
			server = 'oceanatlas.database.windows.net'
			db = 'Opedia'
			Uid = 'AdminAtlas@oceanatlas'
			psw = 'Ocean@2016@'
			conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Uid=' + Uid + ';Pwd='+ psw +';Encrypt=yes')
        
        #print('Successful Database Connection')
    except Exception as e:
        print('Error in Database Connection. Error message: '+str(e))        
    return conn




def dbExecute(sql, vals):
	conn = dbConnect()
	cursor = conn.cursor()
	#vals = nanToNone(vals)
	cursor.execute(sql, vals)
	conn.commit()		
	return




def dbRead(query):
	conn = dbConnect()
	dframe = sql.read_sql(query, conn)
	conn.close()
	return dframe



def bulkInsert(filePath, tableName, determinator=','):
	conn = dbConnect()
	cursor = conn.cursor()	
	query = "BULK INSERT %s FROM '%s' WITH ( FIELDTERMINATOR = '%s', ROWTERMINATOR = '\n', FIRSTROW = 2 ) " % (tableName, filePath, determinator)
	cursor.execute(query, [])
	conn.commit()
	return
