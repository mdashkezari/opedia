import db
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date 
from datetime import timedelta
import numpy as np
import random
import time
from multiprocessing import Process, Value, Array
import atexit



def dateToDayn(dt):
    	dayn = int(format(dt, '%j'))
	dayn += dt.year * 1000
	return dayn

def get_all_available_days():
    dt = date(2013, 1, 5)
    days = []
    while(dt<=date(2017, 2, 1)):    
        days.append(dt)
        dt = dt + timedelta(days=7)         
    return days


def plot(field, dt, lat, lon, data):
    try:
        plt.clf()
        plt.imshow(data, extent=[lon.min(), lon.max(), lat.min(), lat.max()], origin='bottom')
        plt.title(field + '\n ' + dt)
        #plt.colorbar()
        fname = field + '_' + dt
        plt.tight_layout()
        plt.savefig('./pics/%s.png' % fname, dpi=300, transparent=True)
        #plt.show(block=False)
    except Exception as e:
        print('Error in plot: ' + str(e))    
    return


def call(table, field, dt1, dt2, lat1, lat2, lon1, lon2, extV, extVV, savePlot, saveData):
    ############################################
    tic = time.clock()    
    args = [table, field, dt1, lat1, lat2, lon1, lon2, extV, extVV]
    query = 'EXEC uspRegionalMap ?, ?, ?, ?, ?, ?, ?, ?, ?'
    df = db.dbFetchStoredProc(query, args)        
    elapsed = ( time.clock() - tic )  # elapsed time
    ############################################
    
    df = pd.DataFrame.from_records(df, columns=['time', 'lat', 'lon', field])
    lat = df.lat.unique()
    lon = df.lon.unique()
    shape = (len(lat), len(lon))
    data = df[field].values.reshape(shape)
    if saveData:
        df.to_csv('./data/'+field+'_'+dt1+'.csv', index=False)    # export
    if savePlot:    
        plot(field, dt1, lat, lon, data)     # plot    
    return elapsed


def job():
    days = get_all_available_days()
    dt = str(random.choice(days))
    fetchTime = np.array([])
    lat1, lat2, lon1, lon2 = 10, 50, -180, -100 

    table = 'tblPisces_NRT'
    field = 'NO3'
    extV, extVV = 'depth', '0.494024991989'
    elapsed = call(table, field, dt, dt, lat1, lat2, lon1, lon2, extV, extVV, savePlot, saveData)
    fetchTime = np.append(fetchTime, elapsed)


    table = 'tblSST_AVHRR_OI_NRT'
    field = 'sst'
    extV, extVV = None, None
    elapsed = call(table, field, dt, dt, lat1, lat2, lon1, lon2, extV, extVV, savePlot, saveData)
    fetchTime = np.append(fetchTime, elapsed)


    table = 'tblWind_NRT'
    field = 'wind_stress'
    extV, extVV = 'hour', '12'
    elapsed = call(table, field, dt, dt, lat1, lat2, lon1, lon2, extV, extVV, savePlot, saveData)
    fetchTime = np.append(fetchTime, elapsed)


    table = 'tblAltimetry_REP'
    field = 'adt'
    extV, extVV = None, None
    elapsed = call(table, field, dt, dt, lat1, lat2, lon1, lon2, extV, extVV, savePlot, saveData)
    fetchTime = np.append(fetchTime, elapsed)

    print('')
    print(fetchTime.mean())
    return fetchTime    


def submitJobs(jobs):
    for j in range(jobs):
        p = Process(target=job, args=())
        p.start()
    return








#########################################################################
jobs = 100            # number of concurrent batch queries (each batch involves 4 regional queries)   
savePlot = False      # True to save plot on disk; False otherwise
saveData = False      # True to save data on disk; False otherwise
if __name__ == '__main__':          
    itnum = Value('i', 0)
    print('%d batch queries runing concurrently ...' % (jobs)) 
    submitJobs(jobs)
#########################################################################

