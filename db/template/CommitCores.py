
import pyodbc
import pandas.io.sql as sql
import numpy as np
import pickle
import math


def CoreFieldNames():
    Result = ''
    Result = Result + 'year, '
    Result = Result + 'month, '
    Result = Result + 'day, '
    
    Result = Result + 'eddy_centers_i, '
    Result = Result + 'eddy_centers_j, '
    Result = Result + 'eddy_polarity, '
    Result = Result + 'eddy_radius, '
    Result = Result + 'radius_rv2, '
    Result = Result + 'radius_pv, '
    Result = Result + 'eddy_lat, '
    Result = Result + 'eddy_lon, '
    
    Result = Result + 'phase_integ_fixed, '
    Result = Result + 'phase_integ_full, '
    Result = Result + 'phase_norm_fixed, '
    Result = Result + 'phase_norm_full, '
    Result = Result + 'phase_mean_bkg, '
    Result = Result + 'phase_std_bkg, '
    
    Result = Result + 'sla_mean_fixed, '
    Result = Result + 'sla_mean_full, '
    Result = Result + 'sla_std_fixed, '
    Result = Result + 'sla_std_full, '
    Result = Result + 'sla_mean_bkg, '
    Result = Result + 'sla_std_bkg, '
    
    Result = Result + 'vort_mean_fixed, '
    Result = Result + 'vort_mean_full, '
    Result = Result + 'vort_std_fixed, '
    Result = Result + 'vort_std_full, '
    Result = Result + 'vort_mean_bkg, '
    Result = Result + 'vort_std_bkg, '
    
    Result = Result + 'displacement_mean_fixed, '
    Result = Result + 'displacement_mean_full, '
    Result = Result + 'displacement_std_fixed, '
    Result = Result + 'displacement_std_full, '
    Result = Result + 'displacement_mean_bkg, '
    Result = Result + 'displacement_std_bkg, '
    
    Result = Result + 'ftle_mean_fixed, '
    Result = Result + 'ftle_mean_full, '
    Result = Result + 'ftle_std_fixed, '
    Result = Result + 'ftle_std_full, '
    Result = Result + 'ftle_mean_bkg, '
    Result = Result + 'ftle_std_bkg, '
    
    Result = Result + 'sst_mean_fixed, '
    Result = Result + 'sst_mean_full, '
    Result = Result + 'sst_std_fixed, '
    Result = Result + 'sst_std_full, '
    Result = Result + 'sst_mean_bkg, '
    Result = Result + 'sst_std_bkg, '
    
    Result = Result + 'chl_mean_fixed, '
    Result = Result + 'chl_mean_full, '
    Result = Result + 'chl_std_fixed, '
    Result = Result + 'chl_std_full, '
    Result = Result + 'chl_mean_bkg, '
    Result = Result + 'chl_std_bkg'


    return Result
      


def CoreFieldValues(Att):
    Result = ''
    for i in range(0, len(Att)-1):
        Result = Result + "?, " 
        #Result = Result + "'" + str(Att[i]) + "', "
    #Result = Result + "'" + str(Att[-1]) + "'"        
    Result = Result + "?"    
    return Result


def GetCoreRecord(data, index):
    Result = []
    Result.append(data['year'][index])
    Result.append(data['month'][index])
    Result.append(data['day'][index])
    Result.append(data['eddy_centers_i'][index])
    Result.append(data['eddy_centers_j'][index])
    Result.append(data['eddy_polarity'][index])
    Result.append(data['eddy_radius'][index])
    Result.append(data['radius_rv2'][index])
    Result.append(data['radius_pv'][index])
    Result.append(data['eddy_lat'][index])
    Result.append(data['eddy_lon'][index])
    Result.append(data['phase_integ_fixed'][index])
    Result.append(data['phase_integ_full'][index])
    Result.append(data['phase_norm_fixed'][index])
    Result.append(data['phase_norm_full'][index])
    Result.append(data['phase_mean_bkg'][index])
    Result.append(data['phase_std_bkg'][index])
    Result.append(data['sla_mean_fixed'][index])
    Result.append(data['sla_mean_full'][index])
    Result.append(data['sla_std_fixed'][index])
    Result.append(data['sla_std_full'][index])
    Result.append(data['sla_mean_bkg'][index])
    Result.append(data['sla_std_bkg'][index])
    Result.append(data['vort_mean_fixed'][index])
    Result.append(data['vort_mean_full'][index])
    Result.append(data['vort_std_fixed'][index])
    Result.append(data['vort_std_full'][index])
    Result.append(data['vort_mean_bkg'][index])
    Result.append(data['vort_std_bkg'][index])
    Result.append(data['displacement_mean_fixed'][index])
    Result.append(data['displacement_mean_full'][index])
    Result.append(data['displacement_std_fixed'][index])
    Result.append(data['displacement_std_full'][index])
    Result.append(data['displacement_mean_bkg'][index])
    Result.append(data['displacement_std_bkg'][index])
    Result.append(data['ftle_mean_fixed'][index])
    Result.append(data['ftle_mean_full'][index])
    Result.append(data['ftle_std_fixed'][index])
    Result.append(data['ftle_std_full'][index])
    Result.append(data['ftle_mean_bkg'][index])
    Result.append(data['ftle_std_bkg'][index])
    Result.append(data['sst_mean_fixed'][index])
    Result.append(data['sst_mean_full'][index])
    Result.append(data['sst_std_fixed'][index])
    Result.append(data['sst_std_full'][index])
    Result.append(data['sst_mean_bkg'][index])
    Result.append(data['sst_std_bkg'][index])
    Result.append(data['chl_mean_fixed'][index])
    Result.append(data['chl_mean_full'][index])
    Result.append(data['chl_std_fixed'][index])
    Result.append(data['chl_std_full'][index])
    Result.append(data['chl_mean_bkg'][index])
    Result.append(data['chl_std_bkg'][index])
    return Result


def replace_nans(rec):
    for index, item in enumerate(rec):
        rec[index] = item
        if math.isnan(item):
            rec[index] = None
    return rec
    

def AppendCore(conn, fieldnames, rec):
    cursor = conn.cursor()
    sql = "insert into tblCores ("+fieldnames+") "
    sql = sql + "values ("+CoreFieldValues(rec)+")"
    rec = replace_nans(rec)
    cursor.execute(sql, rec)
    conn.commit()
    return
    
    
# Parameters
server = 'MONAZ-PC'
db = 'Eddy2003_2015'

# Create the connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')


'''
# query db
query = 'SELECT count(*) FROM tblCores'
df = sql.read_sql(query, conn)
df.head()
print(df)
'''



###############  Inserting Cores  #################

core_table_filename = 'F:\Mohammad\eddy_archive\csv\core_table.npz'
temp = np.load(core_table_filename)
data = dict(temp)
temp.close()

fieldnames = CoreFieldNames()
for i in range(0, len(data['year'])):
#for i in range(0, 1):
    rec = GetCoreRecord(data, i)
    AppendCore(conn, fieldnames, rec)
    if i % 1000 == 0:
        print('Record '+str(i)+' Inserted')
        
print('Insertion Completed!')        

######################################################


