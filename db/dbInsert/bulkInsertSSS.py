import os
import numpy as np

itnums = np.array([])
itnums = np.append(itnums, np.arange(2015090, 2015365+1))
itnums = np.append(itnums, np.arange(2016001, 2016366+1))
itnums = np.append(itnums, np.arange(2017001, 2017365+1))
itnums = np.append(itnums, np.arange(2018001, 2018365+1))
itnums = np.append(itnums, np.arange(2019001, 2019051+1))




for itnum in itnums:
    os.system('python insertSSS.py ' + str(int(itnum)) + ' ' + str(int(itnum)) + ' 1')