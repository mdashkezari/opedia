import sys
sys.path.append('../../')
import db
import pandas as pd
import matplotlib.pyplot as plt


def plot(lat, lon, data):
    plt.imshow(data, extent=[lon1, lon2, lat1, lat2], origin='bottom', vmin=0, vmax=1e-4)
    plt.title(field + '\n ' + dt)
    plt.colorbar()
    plt.show()



table = 'tblPisces_NRT'
field = 'Fe'
dt = '2017-06-03'
lat1, lat2, lon1, lon2 = 10, 55, -180, -100  
extV, extVV = 'depth', '0.494024991989'
args = [table, field, dt, lat1, lat2, lon1, lon2, extV, extVV]
query = 'EXEC uspRegionalMap ?, ?, ?, ?, ?, ?, ?, ?, ?'
df = db.dbFetchStoredProc(query, args)        
df = pd.DataFrame.from_records(df, columns=['time', 'lat', 'lon', field])
lat = df.lat.unique()
lon = df.lon.unique()
shape = (len(lat), len(lon))
data = df[field].values.reshape(shape)
#df.to_csv(field+'.csv', index=False)    # export data if needed!
plot(lat, lon, data)