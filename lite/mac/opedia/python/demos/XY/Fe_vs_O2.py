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


table1 = 'tblPisces_NRT'
field1 = 'Fe'
table2 = 'tblPisces_NRT'
field2 = 'O2'
startDate, endDate = '2016-01-19', '2016-04-19'
lat1, lat2, lon1, lon2 = 30.57, 35.21, -163.43, -156.17   
extV, extVV, extV2, extVV2 = 'depth', '0.494024991989', None, None
t1, y1, y_std1 = TS.timeSeries(table1, field1, startDate, endDate, lat1, lat2, lon1, lon2, extV, extVV, extV2, extVV2)
extV, extVV, extV2, extVV2 = 'depth', '0.494024991989', None, None
t2, y2, y_std2 = TS.timeSeries(table2, field2, startDate, endDate, lat1, lat2, lon1, lon2, extV, extVV, extV2, extVV2)
plot(y1, y2)