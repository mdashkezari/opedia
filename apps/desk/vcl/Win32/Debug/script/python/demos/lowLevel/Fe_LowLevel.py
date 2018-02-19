import sys
sys.path.append('../../')
import db
import pandas as pd
import matplotlib.pyplot as plt



def plot(lat, lon, data):
    plt.imshow(data, extent=[lon1, lon2, lat1, lat2], origin='bottom', vmin=0, vmax=1e-4)
    plt.title(field + '\n ' + dt1 + ' - ' + dt2)
    plt.colorbar()
    plt.show()


def prepareQuery(args):
    query = "SELECT [time], lat, lon, depth, %s FROM %s WHERE "
    query = query + "[time]>='%s' AND [time]<='%s' AND "
    query = query + "lat>=%f AND lat<=%f AND "
    query = query + "lon>=%f AND lon<=%f AND "
    query = query + "depth>=%f AND depth<=%f "
    query = query + "ORDER BY [time], lat, lon, depth "
    query = query % args
    return query



table = 'tblPisces_NRT'
field = 'Fe'
dt1 = '2017-06-03'
dt2 = '2017-06-03'
lat1, lat2, lon1, lon2 = 10, 55, -180, -100  
depth1 = 0
depth2 = 1
args = (field, table, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)
query = prepareQuery(args)
df = db.dbFetch(query)        
df = pd.DataFrame.from_records(df, columns=['time', 'lat', 'lon', 'depth', field])
lat = df.lat.unique()
lon = df.lon.unique()
shape = (len(lat), len(lon))
data = df[field].values.reshape(shape)
#df.to_csv(field+'.csv', index=False)    # export data if needed!
plot(lat, lon, data)

