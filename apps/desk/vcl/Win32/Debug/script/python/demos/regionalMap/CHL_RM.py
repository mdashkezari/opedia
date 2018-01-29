import sys
sys.path.append('../../')
import db
import pandas as pd
import matplotlib.pyplot as plt


def plot(lat, lon, data):
    plt.imshow(data, extent=[lon1, lon2, lat1, lat2], origin='bottom', cmap=plt.cm.jet, vmin=0, vmax=5e-1)
    plt.title(field + '\n ' + dt)
    plt.colorbar()
    plt.show()



table = 'tblCHL_OI_REP'
field = 'chl'
dt = '2016-01-19'
lat1, lat2, lon1, lon2 = 10, 55, -180, -100  
extV, extVV = None, None
args = [table, field, dt, lat1, lat2, lon1, lon2, extV, extVV]
query = 'EXEC uspRegionalMap ?, ?, ?, ?, ?, ?, ?, ?, ?'
df = db.dbFetchStoredProc(query, args)        
df = pd.DataFrame.from_records(df, columns=['lat', 'lon', field])
lat = df.lat.unique()
lon = df.lon.unique()
shape = (len(lat), len(lon))
data = df[field].values.reshape(shape)
plot(lat, lon, data)