

import sys
sys.path.append('../../')
import genericDist as gd
import pandas as pd
import matplotlib.pyplot as plt


def hist(y):
    plt.hist(y)
    plt.show()




table = 'tblCHL_OI_REP'
field = 'chl'
startDate, endDate = '2016-06-03', '2016-06-03'
lat1, lat2, lon1, lon2 = 30.57, 35.21, -163.43, -156.17 
extV, extVV, extV2, extVV2 = None, None, None, None
y = gd.genericDist(table, field, startDate, endDate, lat1, lat2, lon1, lon2, extV, extV, extV2, extVV2)
#y.to_csv('dist.csv', index=False)      # save data on disk
hist(y[field])