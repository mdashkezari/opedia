import sys
import os
import platform
import numpy as np
import pandas as pd
import pyodbc
import pandas.io.sql as sql
sys.path.append('login')
import credentials as cr



def dbConnect(server,db='Opedia', TDS_Version='7.3'):
    if server == 'Rainier':
        usr=cr.usr_rainier
        psw=cr.psw_rainier
        ip=cr.ip_rainier
        port = cr.port_rainier
    else:
        usr=cr.usr_beast
        psw=cr.psw_beast
        ip=cr.ip_beast
        port = cr.port_beast

    server = ip + ',' + port

    if platform.system().lower().find('windows') != -1:
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Uid=' + usr + ';Pwd='+ psw )
    elif platform.system().lower().find('darwin') != -1:
        conn = pyodbc.connect('DRIVER=/usr/local/lib/libtdsodbc.so;SERVER=' + server + ';DATABASE=' + db + ';Uid=' + usr + ';Pwd='+ psw )
    elif platform.system().lower().find('linux') != -1:
        conn = pyodbc.connect(DRIVER='/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so', TDS_Version =  TDS_Version , server =  ip , port =  port, uid = usr, pwd = psw)

    return conn

'''
def dbConnect(local=True):
    try:
        if local:
			## Local Database
			server = 'THEBEAST'
			db = 'Opedia'
			conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')
        else:
			## Cloud (Azure) Database
			server = ''
			db = ''
			Uid = ''
			psw = ''
			conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Uid=' + Uid + ';Pwd='+ psw +';Encrypt=yes')
        #print('Successful Database Connection')
    except Exception as e:
        print('Error in Database Connection. Error message: '+str(e))
    return conn
'''



def dbExecute(sql, vals):
	conn = dbConnect()
	cursor = conn.cursor()
	#vals = nanToNone(vals)
	cursor.execute(sql, vals)
	conn.commit()
	return




def dbRead(query, usr=cr.usr_rainier, psw=cr.psw_rainier, ip=cr.ip_rainier, port=cr.port_rainier, db='Opedia', TDS_Version='7.3'):
	conn = dbConnect('Rainier')
	dframe = sql.read_sql(query, conn)
	conn.close()
	return dframe



def bulkInsert(filePath, tableName, determinator=',', usr='ArmLab', psw='ArmLab2018', ip='128.208.239.15', port='1433', db='Opedia', TDS_Version='7.3'):
	conn = dbConnect(usr=usr, psw=psw, ip=ip, port=port, db=db, TDS_Version=TDS_Version)
	cursor = conn.cursor()
	query = "BULK INSERT %s FROM '%s' WITH ( FIELDTERMINATOR = '%s', ROWTERMINATOR = '\n', FIRSTROW = 2 ) " % (tableName, filePath, determinator)
	cursor.execute(query, [])
	conn.commit()
	return


def bcpInsert(filePath, tableName, determinator=',', usr='ArmLab', psw='ArmLab2018', ip='128.208.239.15', port='1433', db='Opedia', TDS_Version='7.3'):
    str = """bcp """ + db + """.dbo.""" + tableName + """ in """ + filePath + """ -e error -c -t, -U  """ + usr + """ -P """ + psw + """ -S """ + ip + ""","""+ port
    os.system(str)
    # print('BCP insert finished')
