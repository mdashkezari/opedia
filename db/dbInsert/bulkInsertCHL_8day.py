import os
import numpy as np

itnums = np.array([])
itnums = np.append(itnums, np.arange(2015001, 2015361+1, 8))
itnums = np.append(itnums, np.arange(2014001, 2014361+1, 8))
itnums = np.append(itnums, np.arange(2013001, 2013361+1, 8))
itnums = np.append(itnums, np.arange(2012001, 2012361+1, 8))
itnums = np.append(itnums, np.arange(2011001, 2011361+1, 8))
itnums = np.append(itnums, np.arange(2010001, 2010361+1, 8))
itnums = np.append(itnums, np.arange(2009001, 2009361+1, 8))
itnums = np.append(itnums, np.arange(2008001, 2008361+1, 8))
itnums = np.append(itnums, np.arange(2007001, 2007361+1, 8))
itnums = np.append(itnums, np.arange(2006001, 2006361+1, 8))
itnums = np.append(itnums, np.arange(2005001, 2005361+1, 8))
itnums = np.append(itnums, np.arange(2004001, 2004361+1, 8))
itnums = np.append(itnums, np.arange(2003001, 2003361+1, 8))
itnums = np.append(itnums, np.arange(2002001, 2002361+1, 8))
itnums = np.append(itnums, np.arange(2001001, 2001361+1, 8))
itnums = np.append(itnums, np.arange(2000001, 2000361+1, 8))
itnums = np.append(itnums, np.arange(1999001, 1999361+1, 8))
itnums = np.append(itnums, np.arange(1998001, 1998361+1, 8))




for itnum in itnums:
    os.system('python insertCHL_8day.py ' + str(int(itnum)) + ' ' + str(int(itnum)) + ' 0')