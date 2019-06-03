import os
import numpy as np

itnums = np.array([])
itnums = np.append(itnums, np.arange(2002261, 2002365+1))
itnums = np.append(itnums, np.arange(2001001, 2001365+1))
itnums = np.append(itnums, np.arange(2000001, 2000366+1))

itnums = np.append(itnums, np.arange(1999001, 1999365+1))
itnums = np.append(itnums, np.arange(1998001, 1998365+1))
itnums = np.append(itnums, np.arange(1997001, 1997365+1))
itnums = np.append(itnums, np.arange(1996001, 1996366+1))
itnums = np.append(itnums, np.arange(1995001, 1995365+1))
itnums = np.append(itnums, np.arange(1994001, 1994365+1))
itnums = np.append(itnums, np.arange(1993001, 1993365+1))



for itnum in itnums:
    os.system('python insertAltimetry.py ' + str(int(itnum)) + ' ' + str(int(itnum)) + ' 0')
