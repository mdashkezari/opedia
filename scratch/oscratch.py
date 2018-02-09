#!/usr/bin/env python

import os
import sys
import time


def scratch_nrt_obs(yr, startDay, endDay):	
	# nrt sla
	os.system('cd scratch/CMEMS; python GetCMEMS_NRT_SLA.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))
	'''
        # nrt uv_sla
        os.system('cd scratch/AVISO; python GetAVISO_NRT_UV_SLA.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))	
        # nrt adt
        os.system('cd scratch/AVISO; python GetAVISO_NRT_ADT.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))
        # nrt uv_adt
        os.system('cd scratch/AVISO; python GetAVISO_NRT_UV_ADT.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))
	'''	
        # nrt chl
        #os.system('cd scratch/MODIS; python GetMODIS_CHL.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))
        os.system('cd scratch/CMEMS; python GetCMEMS_NRT_CHL.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))
        # nrt sst
        os.system('cd scratch/MURSST; python GetMURSST_SST.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))	
        # nrt color
        os.system('cd scratch/CMEMS; python GetCMEMS_NRT_COL.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))
        # nrt armor3d
        os.system('cd scratch/CMEMS; python GetCMEMS_NRT_ARMOR3D.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))
	return



def scratch_rep_obs(yr, startDay, endDay):
	# rep sla
        os.system('cd scratch/CMEMS; python GetCMEMS_REP_SLA.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))
        # rep uv_sla
        os.system('cd scratch/AVISO; python GetAVISO_REP_UV_SLA.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))

        # rep adt
        os.system('cd scratch/AVISO; python GetAVISO_REP_ADT.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))
        # rep uv_adt
        os.system('cd scratch/AVISO; python GetAVISO_REP_UV_ADT.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))

	# rep chl
	os.system('cd scratch/CMEMS; python GetCMEMS_REP_CHL.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))
        # rep color
        os.system('cd scratch/CMEMS; python GetCMEMS_REP_COL.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))
        # rep armor3d
        os.system('cd scratch/CMEMS; python GetCMEMS_REP_ARMOR3D.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))
        return




def scratch_nrt_model(yr, startDay, endDay):
        # nrt/forecast bio (mercator-pisces)
        os.system('cd scratch/CMEMS; python GetCMEMS_NRT_MERCATOR_PISCES.py ' + str(yr) + ' ' + str(startDay) + ' ' + str(endDay))
        return



def scratch_rep_model(yr, startDay, endDay):

        return



if len(sys.argv)<>6:
  print('Enter 5 arguments as follow: NRT(0/1) OBS(0/1) Year StartDay EndDay')
  exit()



nrt = int(sys.argv[1])		## 1 if nrt, 0 if rep
obs = int(sys.argv[2])		## 1 if obs, 0 if model
yr = int(sys.argv[3])
startDay = int(sys.argv[4])
endDay = int(sys.argv[5])


if nrt == 1:
	if obs == 1:
		scratch_nrt_obs(yr, startDay, endDay)
	else:
                scratch_nrt_model(yr, startDay, endDay)
else:
        if obs == 1:
                scratch_rep_obs(yr, startDay, endDay)
        else:
                scratch_rep_model(yr, startDay, endDay)



