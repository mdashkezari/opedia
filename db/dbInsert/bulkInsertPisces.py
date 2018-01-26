import os
from datetime import date 
from datetime import timedelta
import numpy as np


def dateToDayn(dt):
    	dayn = int(format(dt, '%j'))
	dayn += dt.year * 1000
	return dayn

def get_all_available_days():
    dt = date(2011, 12, 31)
    days = []
    while(dt<=date.today()):    
        days.append(dt)
        dt = dt + timedelta(days=7)         
    return days



days = get_all_available_days()
for i in np.arange(len(days)-1, -1, -1):
    os.system('python insertPisces.py ' + str(dateToDayn(days[i])) + ' ' + str(dateToDayn(days[i])) + ' 1')
