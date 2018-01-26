import sys
from datetime import datetime 
from datetime import date 
from datetime import timedelta
import numpy as np
import pyodbc
import pandas.io.sql as sql


def dbConnect():
    try:
        #print('Connecting to Database ...')
        
        
        ###### local DB
        server = 'THEBEAST'
        db = 'Opedia'
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')
        
        '''
        ## THEBEAST Server
        server = '128.208.239.15,1433'
        db = 'Opedia'
        Uid = 'ArmLab'
        psw = 'ArmLab2018'
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Uid=' + Uid + ';Pwd='+ psw )
        '''

        '''
        ## Cloud (Azure) Database
        server = 'oceanatlas.database.windows.net'
        db = 'NPG'
        Uid = 'AdminAtlas@oceanatlas'
        psw = 'Ocean@2016@'
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Uid=' + Uid + ';Pwd='+ psw +';Encrypt=yes')
        '''
        
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



def dateToDayn(dt):
    	dayn = int(format(dt, '%j'))
	dayn += dt.year * 1000
	return dayn

def get_all_available_days():
    dt = date(2011, 12, 31)
    days = []
    while(dt<=date(2017,12,9)):    
        days.append(dt)
        dt = dt + timedelta(days=7)         
    return days


def updateMonthYear(day):
    query = "UPDATE tblPisces_NRT SET [month]=MONTH([time]), [year]=YEAR([time]) WHERE [time]='%s' " % str(day)
    dbExecute(query, [])
    return


days = get_all_available_days()
counter = 0
for day in days:
    counter += 1
    print datetime.today(), '    ', counter, '/' , len(days), '    ', str(day) 
    updateMonthYear(day)




