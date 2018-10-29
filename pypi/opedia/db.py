import platform
import sys
sys.dont_write_bytecode = True
import pyodbc
import pandas.io.sql as sql
from pandas import DataFrame


def dbConnect(usr='ArmLab', psw='ArmLab2018', ip='128.208.239.15', port='1433', db='Opedia', TDS_Version='7.3'):
    try:
        server = ip + ',' + port
        if platform.system().lower().find('windows') != -1:
            conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Uid=' + usr + ';Pwd='+ psw )
        elif platform.system().lower().find('darwin') != -1:
            conn = pyodbc.connect('DRIVER=/usr/local/lib/libtdsodbc.so;SERVER=' + server + ';DATABASE=' + db + ';Uid=' + usr + ';Pwd='+ psw )
        elif platform.system().lower().find('linux') != -1:
            conn = pyodbc.connect(DRIVER='/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so', TDS_Version =  TDS_Version , server =  ip , port =  port, uid = usr, pwd = psw)
        #print('Successful database connection')
    except Exception as e:
        print('Database connection error. Error message: '+str(e))        
    return conn


def dbFetch(query):
    conn = dbConnect()
    df = sql.read_sql(query, conn)
    conn.close()
    return df


def dbFetchStoredProc(query, args):
    conn = dbConnect()
    cur = conn.cursor()
    if sys.version_info[0] >= 3:     # if python3 
        args = [ str(a) if a is not None else a for a in args ]
    cur.execute(query, args)
    df = cur.fetchall()
    cols = [column[0] for column in cur.description]
    df = DataFrame.from_records(df, columns=cols)
    conn.close()
    return df


def bulkInsert(filePath, tableName):
    conn = dbConnect()
    cursor = conn.cursor()
    query = "BULK INSERT %s FROM '%s' WITH ( FIELDTERMINATOR = ',', ROWTERMINATOR = '\n', FIRSTROW = 2 ) " % (tableName, filePath)
    cursor.execute(query, [])
    conn.commit()
    return

    
def getVar(tableName, varName):
    query = "SELECT * FROM tblVariables WHERE Table_Name='%s' AND Short_Name='%s'" % (tableName, varName)
    df = dbFetch(query)
    return df

def getTableName(varName):
    ## 
    query = "SELECT * FROM tblVariables WHERE Table_Name='%s' AND Short_Name='%s'" % (tableName, varName)
    df = dbFetch(query)
    return df

def hasField(tableName, field):
    query = "SELECT COL_LENGTH('%s', '%s') AS RESULT " % (tableName, field)
    df = dbFetch(query)
    return False if df['RESULT'][0] == None else True


def isClimatology(tableName):
    return True if tableName.find('_Climatology') != -1 else False    

