
import pyodbc
import pandas.io.sql as sql
import numpy as np
import pickle
import math
from datetime import datetime
from datetime import timedelta
from geopy.distance import vincenty

def itnum2date(itnum):
    year = int(itnum / 1000)
    nday = int(itnum % 1000)
    nday -= 1
    dt = datetime(year,1,1,0)
    dt = dt + timedelta(days=nday)
    return dt


def AttributeFieldNames():
    Result = ''
    Result = Result + 'track_id_attributes, '
    Result = Result + 'year, '
    Result = Result + 'month, '
    Result = Result + 'day, '
    Result = Result + 'lat, '
    Result = Result + 'lon, '
    Result = Result + 'radius, '
    Result = Result + 'displacement, '
    Result = Result + 'velocity, '
    Result = Result + 'acceleration, '
    Result = Result + 'age_percentile, '
    Result = Result + 'days_to_go, '
    Result = Result + 'phase_integ_fixed, '
    Result = Result + 'phase_norm_fixed, '
    Result = Result + 'phase_integ_full, '
    Result = Result + 'phase_norm_full, '
    Result = Result + 'sla_mean_fixed, '
    Result = Result + 'sla_std_fixed, '
    Result = Result + 'sla_mean_full, '
    Result = Result + 'sla_std_full, '
    Result = Result + 'vort_mean_fixed, '
    Result = Result + 'vort_std_fixed, '
    Result = Result + 'vort_mean_full, '
    Result = Result + 'vort_std_full, '
    Result = Result + 'displacement_mean_fixed, '
    Result = Result + 'displacement_std_fixed, '
    Result = Result + 'displacement_mean_full, '
    Result = Result + 'displacement_std_full, '
    Result = Result + 'ftle_mean_fixed, '
    Result = Result + 'ftle_std_fixed, '
    Result = Result + 'ftle_mean_full, '
    Result = Result + 'ftle_std_full, '
    Result = Result + 'sst_mean_fixed, '
    Result = Result + 'sst_std_fixed, '
    Result = Result + 'sst_mean_full, '
    Result = Result + 'sst_std_full, '
    Result = Result + 'chl_mean_fixed, '
    Result = Result + 'chl_std_fixed, '
    Result = Result + 'chl_mean_full, '
    Result = Result + 'chl_std_full, '


    Result = Result + 'phase_mean_bkg, '
    Result = Result + 'phase_std_bkg, '
    Result = Result + 'sla_mean_bkg, '
    Result = Result + 'sla_std_bkg, '
    Result = Result + 'vort_mean_bkg, '
    Result = Result + 'vort_std_bkg, '
    Result = Result + 'displacement_mean_bkg, '
    Result = Result + 'displacement_std_bkg, '
    Result = Result + 'ftle_mean_bkg, '
    Result = Result + 'ftle_std_bkg, '
    Result = Result + 'sst_mean_bkg, '
    Result = Result + 'sst_std_bkg, '
    Result = Result + 'chl_mean_bkg, '
    Result = Result + 'chl_std_bkg'
    return Result


def TrackFieldNames():
    Result = ''
    Result = Result + 'eddy_polarity, '
    Result = Result + 'lifetime, '
    Result = Result + 'propagation, '
    Result = Result + 'mean_velocity, '
    Result = Result + 'birth_year, '
    Result = Result + 'birth_month, '
    Result = Result + 'birth_day, '
    Result = Result + 'death_year, '
    Result = Result + 'death_month, '
    Result = Result + 'death_day, '
    Result = Result + 'min_lat, '
    Result = Result + 'max_lat, '
    Result = Result + 'min_lon, '
    Result = Result + 'max_lon, '
    Result = Result + 'min_radius, '
    Result = Result + 'max_radius '    
    return Result
      


def FieldValues(Att):
    Result = ''
    for i in range(0, len(Att)-1):
        Result = Result + "?, " 
        #Result = Result + "'" + str(Att[i]) + "', "
    #Result = Result + "'" + str(Att[-1]) + "'"        
    Result = Result + "?"    
    return Result


def GetKinematics(Trajectory):
    total_propagation = 0
    displacement = np.array([0])    
    velocity = np.array([0])    
    acceleration = np.array([0, 0])    
    for i in range(1, len(Trajectory)):
        lat = Trajectory[i-1][3]
        lon = Trajectory[i-1][4]
        if lon > 180:
            lon = lon -360
        ll1 = (lat, lon)

        lat = Trajectory[i][3]
        lon = Trajectory[i][4]
        if lon > 180:
            lon = lon -360
        ll2 = (Trajectory[i][3], Trajectory[i][4])
        
        d = vincenty(ll1, ll2).meters / 1000
        total_propagation = total_propagation + d
        t = Trajectory[i][0]-Trajectory[i-1][0]            
        displacement = np.append(displacement, d)
        velocity = np.append(velocity, d / t)
        if i > 1:
            a = (velocity[-1] - velocity[-2]) / t
            acceleration = np.append(acceleration, a)
    return total_propagation, displacement, velocity, acceleration


def GetLatsLons(Trajectory):
    lats, lons = np.array([]), np.array([])
    for i in range(0, len(Trajectory)):
        lats = np.append(lats, Trajectory[i][3])
        lons = np.append(lons, Trajectory[i][4])
    return lats, lons


def GetRs(Radius):
    Rs = np.array([])
    for i in range(0, len(Radius)):
        Rs = np.append(Rs, Radius[i][1])
    return Rs


def GetAges(Trajectory, lifetime):
    age_percentile, days_to_go, age = np.array([]), np.array([]), np.array([1])
    year, dayn = np.array([]), np.array([])
    for i in range(0, len(Trajectory)):
        year = np.append(year, int(Trajectory[i][0] / 1000))
        dayn = np.append(dayn, int(Trajectory[i][0] % 1000))
        
    curr_year = year[0] 
    for i in range(1, len(year)):
        if year[i] == curr_year:
            val = dayn[i] - dayn[i-1] + age[-1]                    
        else:
            curr_year = year[i]
            val = dayn[i] + age[-1]
        age = np.append(age, val)        
        
    for i in range(0, len(age)):
        age_percentile = np.append(age_percentile, age[i]/lifetime)
        days_to_go = np.append(days_to_go, lifetime - age[i])
        
    return age_percentile, days_to_go


def GetAttributeRecord(track_id, lat, lon, radius, displacement, velocity, acceleration, age_percentile, days_to_go, Attributes):
    Att_Rec = []
    Att_Rec.append(track_id)
    Att_Rec.append(itnum2date(Attributes[0]).year)
    Att_Rec.append(itnum2date(Attributes[0]).month)
    Att_Rec.append(itnum2date(Attributes[0]).day)
    Att_Rec.append(lat)
    Att_Rec.append(lon)
    Att_Rec.append(radius)
    Att_Rec.append(displacement)
    Att_Rec.append(velocity)
    Att_Rec.append(acceleration)    
    Att_Rec.append(age_percentile)
    Att_Rec.append(days_to_go)    
    for i in range(1, len(Attributes)):
        Att_Rec.append(Attributes[i])
    return Att_Rec



def replace_nans(rec):
    for index, item in enumerate(rec):
        rec[index] = item
        if math.isnan(item):
            rec[index] = None
    return rec
    

def AppendTrack(conn, table, fieldnames, rec):
    cursor = conn.cursor()
    sql = "INSERT INTO %s (%s) " % (table, fieldnames)
    sql = sql + "VALUES ("+FieldValues(rec)+");"
    rec = replace_nans(rec)

    rec[0] = int(rec[0])

    cursor.execute(sql, rec)
    conn.commit()
    return



def GetTrackRecord(data):
    TrackRec = []
    y1, m1, d1 = itnum2date(data[0]).year, itnum2date(data[0]).month, itnum2date(data[0]).day
    y2, m2, d2 = itnum2date(data[2]).year, itnum2date(data[2]).month, itnum2date(data[2]).day
    pol = data[1]
    lifetime = data[6] - data[5] + 1    
    total_propagation, displacement, velocity, acceleration = GetKinematics(data[3])    
    lats, lons = GetLatsLons(data[3])
    Rs = GetRs(data[4])
    age_percentile, days_to_go = GetAges(data[3], lifetime)    
    
    TrackRec.append(pol)    # polarity
    TrackRec.append(lifetime)    # lifetime
    TrackRec.append(total_propagation)    # propagation
    TrackRec.append(total_propagation / lifetime)    # mean velocity (km/day)
    TrackRec.append(y1)     #birth_year 
    TrackRec.append(m1)     #birth_month 
    TrackRec.append(d1)     #birth_day 
    TrackRec.append(y2)     #death_year 
    TrackRec.append(m2)     #death_month 
    TrackRec.append(d2)     #death_day 
    TrackRec.append(np.nanmin(lats))     #min_lat 
    TrackRec.append(np.nanmax(lats))     #max_lat 
    TrackRec.append(np.nanmin(lons))     #min_lon 
    TrackRec.append(np.nanmax(lons))     #max_lon 
    TrackRec.append(np.nanmin(Rs))     #min_radius 
    TrackRec.append(np.nanmax(Rs))     #max_radius
    return TrackRec, lats, lons, Rs, displacement, velocity, acceleration, age_percentile, days_to_go


def GetLastTrackID(conn):
    query = 'SELECT TOP 1 track_id FROM tblTracks ORDER BY track_id DESC'
    df = sql.read_sql(query, conn)
    ID = np.array(df['track_id'])[0]
    return ID
    
    
# Parameters
server = 'MONAZ-PC'
db = 'Eddy2003_2015_lost6'

# Create the connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')
'''
# query db
query = 'SELECT count(*) FROM tblTracks'
df = sql.read_sql(query, conn)
df.head()
print(df)
'''


###############  Inserting Tracks  #################

track_fieldnames = TrackFieldNames()
attribute_fieldnames = AttributeFieldNames()
Track_Error = 0
Att_Error = 0
TrackCount = 0
for index in range(1, 2164):
    eddy_archive_filename = 'J:/trajectories/life_g4_lost6_travel50/eddy_archive_%10.10d.pck' % index
    f = open(eddy_archive_filename, 'r')
    data = pickle.load(f)
    print('Eddy Archive '+str(index))
    for i in range(0, len(data)):
        try:
            TrackRec, lats, lons, Rs, displacement, velocity, acceleration, age_percentile, days_to_go = GetTrackRecord(data[i])
            AppendTrack(conn, 'tblTracks', track_fieldnames, TrackRec)
            LastID = GetLastTrackID(conn)
        except Exception as e:
            Track_Error += 1            
            print('Track Error: ' , str(e))


        try:
            for j in range(0, len(data[i][7])):
                Att_Rec = GetAttributeRecord(LastID, lats[j], lons[j], Rs[j], displacement[j], velocity[j], acceleration[j], age_percentile[j], days_to_go[j], data[i][7][j])
                AppendTrack(conn, 'tblAttributes', attribute_fieldnames, Att_Rec)
        except Exception as e:
            Att_Error += 1            
            print('Attribute Error: ' , str(e))

        TrackCount += 1
        if TrackCount % 1000 == 0:
            print('Track '+str(TrackCount)+' Inserted') 
            
print('Insertion Completed!')   
print('Track Error: ' + str(Track_Error))     
print('Attribute Error: ' + str(Att_Error)) 
######################################################

