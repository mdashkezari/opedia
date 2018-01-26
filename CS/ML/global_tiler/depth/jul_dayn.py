#!/usr/bin/env python

import sys
import numpy as np
import scipy.io as sio
from datetime import datetime
from datetime import date
from datetime import timedelta
import jdcal
import math




def dateToDayn(dt):
        dayn = int(format(dt, '%j'))
        dayn += dt.year * 1000
        return dayn


def daynToDate(dt):
        year = dt / 1000
        dayn = dt % 1000
        dat = date.fromordinal(date(year, 1, 1).toordinal() + dayn - 1)
        return dat


def daynToJul(dn):
        dt = daynToDate(dn)
        jd = sum(jdcal.gcal2jd(dt.year, dt.month, dt.day))
        jd = math.ceil(jd)
        jd = int(jd)
        return jd



def chelton_cores():
        path = '/nobackup1/mdehghani/CS_Trunk/ML/chelton_eddies/chelton_v4.mat'
        data = sio.loadmat(path)

	j1 = data['j1']
	'''
        track = data['track']
        n = data['n']
        cyc = data['cyc']
        lat = data['lat']
        lon = data['lon']
        A = data['A']
        L = data['L']
        U = data['U']
	'''
        return j1


def savemat(data, block):
        path = '/nobackup1/mdehghani/CS_Trunk/ML/chelton_eddies/chelton_v4_yearDay_%2.2d.mat' % block
        sio.savemat(path, data)
	return


def load_block(block):
        path = '/nobackup1/mdehghani/CS_Trunk/ML/chelton_eddies/chelton_v4_yearDay_%2.2d.mat' % block
        data = sio.loadmat(path)
        yearDayn = data['yearDayn']
        return yearDayn


def compile_blocks():
	dns = {}
	dayn = np.array([])

	for i in range(0, 23):
		dn = load_block(i)
		dayn = np.append(dayn, dn)
		print('%d block merged' % i)
	
	dns['yearDayn'] = dayn
        path = '/nobackup1/mdehghani/CS_Trunk/ML/chelton_eddies/chelton_v4_yearDay.mat'
        sio.savemat(path, dns)
	return




#############################
#compile_blocks()
#sys.exit()
#############################






block = int(sys.argv[1])
block_len = 1000000

juls = chelton_cores()
recs = len(juls)
dns = {}
dayn = np.array([])

a = block * block_len
b = (block+1) * block_len
if a > recs:
	sys.exit()
if b > recs:
	b = recs

#for i in range(0, recs):
for i in range(a, b):
	jul = jdcal.jd2gcal(juls[i], 0)
	dn = dateToDayn(date(jul[0], jul[1], jul[2]))
	dayn = np.append(dayn, dn)

	if i % 100000 == 0:
		print('%d out of %d,  %2.2f%%' % (i, recs, 100.0*i/float(recs)))

dns['yearDayn'] = dayn
savemat(dns, block)


