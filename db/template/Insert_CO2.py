import pandas as pd 
import matplotlib
import matplotlib.pylab as plt
import numpy as np
import pyodbc
import pandas.io.sql as sql


def generate_revised_socat():
    socat = pd.read_csv('SOCAT_tracks_gridded_monthly_v4.csv')
    socat = socat.fillna(method='ffill')
    
    years = np.array([])
    months = np.array([])
    days = np.array([])
    
    for i in range(0, len(socat)):    
        temp = socat.time[i].split('T')[0].split('-')
        years = np.append(years, int(temp[0]))
        months = np.append(months, int(temp[1]))
        days = np.append(days, int(temp[2]))
        if i % 50000 == 0:
            print(i, len(socat))
                
    socat.year = years
    socat.month = months
    socat.day = days
    socat.to_csv('revised_SOCAT_tracks_gridded_monthly_v4.csv', index=False)
    return


def db_connect():
    try:
        # Local database
        
        #print('Connecting to Database ...')
        server = 'MONAZ-PC'
        db = 'Eddy2003_2015'
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')
        #print('Successful Database Connection')
        
        '''
        ## Cloud (Azure) Databe
        server = 'oceanatlas.database.windows.net'
        db = 'Eddy2003_2015'
        Uid = 'AdminAtlas@oceanatlas'
        psw = 'Ocean@2016@'
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Uid=' + Uid + ';Pwd='+ psw +';Encrypt=yes')
        '''
        
    except Exception as e:
        print('Error in Database Connectio. Error message: '+str(e))
        
    return conn




def UpdateCO2(co2, yr, mn, lat, lon):
    conn = db_connect()
    cursor = conn.cursor()
    sql = "UPDATE tblCores SET CO2_mean_surface=?"
    sql = sql + " WHERE year=? AND month=? AND ABS(eddy_lon-?)<=0.5 AND ABS(eddy_lat-?)<=0.5"
    cursor.execute(sql, co2, yr, mn, lon, lat)
    conn.commit()
    conn.close()
    return







#generate_revised_socat()
socat = pd.read_csv('revised_SOCAT_tracks_gridded_monthly_v4.csv')

for i in range(0, len(socat)):
    if socat.year[i] < 2003:
        continue
    
    UpdateCO2(socat.co2_weighted[i], socat.year[i], socat.month[i], socat.lat[i], socat.lon[i])
    print(i, len(socat))

