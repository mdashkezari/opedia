import os
import numpy as np

itnums = np.array([])
itnums = np.append(itnums, np.arange(2017340, 2017365+1))
itnums = np.append(itnums, np.arange(2018001, 2018365+1))




for itnum in itnums:
    os.system('python insertWind.py ' + str(int(itnum)) + ' ' + str(int(itnum)) + ' 1')