import os
import numpy as np

itnums = np.array([])
itnums = np.append(itnums, np.arange(2016001, 2016366+1))
itnums = np.append(itnums, np.arange(2017001, 2017365+1))


for itnum in itnums:
    os.system('python insertLCS.py ' + str(int(itnum)) + ' ' + str(int(itnum)) + ' 0')