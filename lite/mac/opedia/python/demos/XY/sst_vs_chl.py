import sys
sys.path.append('../../')
import timeSeries as TS
import pandas as pd
import matplotlib.pyplot as plt


def plot(y1, y2):
    plt.plot(y1, y2, 'o')
    plt.xlabel(field1)
    plt.ylabel(field2)
    plt.show()


table1 = 'tblSST_AVHRR_OI_NRT'
field1 = 'sst'
table2 = 'tblCHL_OI_REP'
field2 = 'chl'
startDate, endDate = '2016-01-19', '2016-02-19'
lat1, lat2, lon1, lon2 = 30.57, 35.21, -163.43, -156.17   
extV, extVV, extV2, extVV2 = None, None, None, None
t1, y1, y_std1 = TS.timeSeries(table1, field1, startDate, endDate, lat1, lat2, lon1, lon2, extV, extVV, extV2, extVV2)
t2, y2, y_std2 = TS.timeSeries(table2, field2, startDate, endDate, lat1, lat2, lon1, lon2, extV, extVV, extV2, extVV2)
plot(y1, y2)