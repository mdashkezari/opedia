import os
import numpy as np

itnums = np.array([])
itnums = np.append(itnums, np.arange(1993078, 1993365+1))
itnums = np.append(itnums, np.arange(1992001, 1992366+1))
itnums = np.append(itnums, np.arange(1991001, 1991365+1))
itnums = np.append(itnums, np.arange(1990001, 1990365+1))

itnums = np.append(itnums, np.arange(1989001, 1989365+1))
itnums = np.append(itnums, np.arange(1988001, 1988366+1))
itnums = np.append(itnums, np.arange(1987001, 1987365+1))
itnums = np.append(itnums, np.arange(1986001, 1986365+1))
itnums = np.append(itnums, np.arange(1985001, 1985365+1))
itnums = np.append(itnums, np.arange(1984001, 1984366+1))
itnums = np.append(itnums, np.arange(1983001, 1983365+1))
itnums = np.append(itnums, np.arange(1982001, 1982365+1))
itnums = np.append(itnums, np.arange(1981244, 1981365+1))


for itnum in itnums:
    os.system('python insertSST.py ' + str(int(itnum)) + ' ' + str(int(itnum)) + ' 1')
    