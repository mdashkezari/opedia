
import sys
import pyodbc
import pandas.io.sql as sql


def dbConnect():
    try:
        #print('Connecting to Database ...')
        
        
        ###### local DB
        '''
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


def dbFetch(query):
    conn = dbConnect()
    df = sql.read_sql(query, conn)
    conn.close()
    return df



def dbFetchStoredProc(query, args):
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(query, args)
    df = cur.fetchall()

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