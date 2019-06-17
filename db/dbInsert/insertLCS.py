import sys
sys.path.append('../../config')
import config_vault as cfgv
sys.path.append('../../lib')
import dateLib as dl
sys.path.append('../')
import dbCore as dc
import os
import netcdf as nc
import numpy as np
import pandas as pd
import pyodbc
import pandas.io.sql as sql
from datetime import datetime
import time
import math
import insertPrep as ip
import scipy.io
import os.path

def getLCSPath(nrt, forward, sla, itnum):   
    if nrt:
        if forward:             
            if sla:
                ftlePath = cfgv.nrt_ftle_fw_sla_raw + cfgv.nrt_ftle_fw_sla_prefix + '%10.10d.mat' % itnum
            else:    
                ftlePath = cfgv.nrt_ftle_fw_adt_raw + cfgv.nrt_ftle_fw_adt_prefix + '%10.10d.mat' % itnum
        else:   
            if sla:
                ftlePath = cfgv.nrt_ftle_bw_sla_raw + cfgv.nrt_ftle_bw_sla_prefix + '%10.10d.mat' % itnum
            else:    
                ftlePath = cfgv.nrt_ftle_bw_adt_raw + cfgv.nrt_ftle_bw_adt_prefix + '%10.10d.mat' % itnum
    else:
        if forward:             
            if sla:
                ftlePath = cfgv.rep_ftle_fw_sla_raw + cfgv.rep_ftle_fw_sla_prefix + '%10.10d.mat' % itnum
            else:    
                ftlePath = cfgv.rep_ftle_fw_adt_raw + cfgv.rep_ftle_fw_adt_prefix + '%10.10d.mat' % itnum
        else:   
            if sla:
                ftlePath = cfgv.rep_ftle_bw_sla_raw + cfgv.rep_ftle_bw_sla_prefix + '%10.10d.mat' % itnum
            else:    
                ftlePath = cfgv.rep_ftle_bw_adt_raw + cfgv.rep_ftle_bw_adt_prefix + '%10.10d.mat' % itnum       
    return ftlePath


def matToDF(nrt, forward, sla, itnum):
    path = getLCSPath(nrt, forward, sla, itnum)
    if not os.path.isfile(path):
        df = pd.DataFrame()
        df['lat'] = None
        df['lon'] = None
        df['time'] = None
        df['ftle'] = None
        df['disp'] = None
        return    

    mat = scipy.io.loadmat(path)
    lon = mat['lon']   
    lat = mat['lat']
    ftle = mat['ftle']    
    disp = mat['displacement']    
    Xres = mat['Xres']
    Yres = mat['Yres']
    dt = dl.daynToDate(itnum)

    ftle = np.transpose(ftle)
    disp = np.transpose(disp)
    lon = np.arange(np.min(lon), np.max(lon), Xres)
    lat = np.arange(np.min(lat), np.max(lat), Yres)

    LON, LAT = np.meshgrid(lon, lat)
    df = pd.DataFrame()
    df['lat'] = pd.Series(LAT.flatten())
    df['lon'] = pd.Series(LON.flatten())
    df['time'] = dt
    df['ftle'] = pd.Series(ftle.flatten())
    df['disp'] = pd.Series(disp.flatten())
    return df


def makeBulkLCS(itnum, nrt):
    if itnum < 1993001:
        print('Error: LCS is only available after 1993.')
        return

    if not nrt:
        # df_bw_adt = matToDF(nrt=nrt, forward=False, sla=False, itnum=itnum)
        # df_fw_adt = matToDF(nrt=nrt, forward=True, sla=False, itnum=itnum)
        df_fw_sla = matToDF(nrt=nrt, forward=True, sla=True, itnum=itnum)
    df_bw_sla = matToDF(nrt=nrt, forward=False, sla=True, itnum=itnum)
    
    prefix = 'LCS_'
    df = pd.DataFrame()
    df['lat'] = df_bw_sla['lat']
    df['lon'] = df_bw_sla['lon']
    df['time'] = df_bw_sla['time']

    if nrt:
        df['ftle_bw_sla'] = df_bw_sla['ftle']
        df['disp_bw_sla'] = df_bw_sla['disp']
    else:
        # df['ftle_bw_adt'] = df_bw_adt['ftle']
        # df['disp_bw_adt'] = df_bw_adt['disp']
        # df['ftle_fw_adt'] = df_fw_adt['ftle']
        # df['disp_fw_adt'] = df_fw_adt['disp']

        df['ftle_bw_sla'] = df_bw_sla['ftle']
        df['disp_bw_sla'] = df_bw_sla['disp']
        df['ftle_fw_sla'] = df_fw_sla['ftle']
        df['disp_fw_sla'] = df_fw_sla['disp']

    # df['ID'] = None
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s%d.csv' % (exportBase, prefix, itnum)
    df.to_csv(export_path, index=False)
    ip.mapTo180180(export_path, 'lon')   # only use if necessary
    ip.sortByLatLon(df, export_path, 'lon', 'lat')
    return export_path




def bulkInsertLCS(itnumStart, itnumEnd, tableName):
    dataTitle = 'LCS'
    for itnum in range(itnumStart, itnumEnd+1):   
        print('%s  Inserting Bulk %s %7.7d into %s.' % (datetime.today(), dataTitle, itnum, tableName))
        try:
            bulkPath = ''
            bulkPath = makeBulkLCS(itnum, nrt)
            #print('\t %s  Bulk %s %7.7d ready.' % (datetime.today(), dataTitle, itnum))
            # dc.bulkInsert(bulkPath, tableName)
            dc.bcpInsert(bulkPath, tableName)
        finally:
            if bulkPath != '':
                os.remove(bulkPath)    
    return




itnumStart = int(sys.argv[1])
itnumEnd = int(sys.argv[2])
nrt = bool(int(sys.argv[3]))
if nrt:
    tableName = 'tblLCS_NRT'
else:
    tableName = 'tblLCS_REP'


bulkInsertLCS(itnumStart, itnumEnd, tableName)