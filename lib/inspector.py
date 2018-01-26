#!/usr/bin/env python


import os
import sys
sys.path.append('../config')
import config_vault as cfgv
import numpy as np
import os.path


def compiled_file_exist(itnums):
        for itnum in itnums:
                path = '/nobackup1/mdehghani/CS_Trunk/ML/identified_eddies/AVISO_sla_global/compiled/%10.10d.npz'
                if not os.path.isfile(path % itnum):
                        print('Not Found: ' + path % itnum)
        return


def eddML_file_exist(itnums):
        row_tiles = 2
        col_tiles = 4
        for itnum in itnums:
                for i in range(1, row_tiles+1):
                        for j in range(1, col_tiles+1):
                                path = '/nobackup1/mdehghani/CS_Trunk/ML/identified_eddies/%10.10d_%d_%d.npz'
                                if not os.path.isfile(path % (itnum,i,j)):
                                        print('Not Found: ' + path % (itnum,i,j))
        return


def pic_file_exist(itnums, folder):
        for itnum in itnums:
                path = '/nobackup1/mdehghani/CS_Trunk/ML/identified_eddies/AVISO_sla_global/pics/%s%10.10d.png'
                if not os.path.isfile(path % (folder,itnum)):
                        print('Not Found: ' + path % (folder,itnum))
        return


def mat_file_exist(itnums, folder):
        row_tiles = 2
        col_tiles = 4
        for itnum in itnums:
                for i in range(1, row_tiles+1):
                        for j in range(1, col_tiles+1):
                                path = '/nobackup1/mdehghani/CS_Trunk/ML/%s%10.10d_%d_%d.mat'
                                if not os.path.isfile(path % (folder,itnum,i,j)):
                                        print('Not Found: ' + path % (folder,itnum,i,j))
        return



def inspect_input_mats(itnums):
	######################  Check if input mat files (vphase, vort, ssh) exist   ###############
	mat_file_exist(itnums, 'vphase/vphase_2pi_')
	mat_file_exist(itnums, 'vort/vorticity_')
	mat_file_exist(itnums, 'ssh/ssh_')
	mat_file_exist(itnums, 'ftle/ftle_')
	mat_file_exist(itnums, 'displacement/displacement_')
	mat_file_exist(itnums, 'chl/chl_')
	mat_file_exist(itnums, 'sst/sst_')
	############################################################################################
	return


def inspect_maps(itnums):
	######################  Check if generated map files (vphase, vort, ssh) exist   ###############
	pic_file_exist(itnums, 'phase/phase_')
	pic_file_exist(itnums, 'vort/vort_')
	pic_file_exist(itnums, 'sla/sla_')
	pic_file_exist(itnums, 'ftle/ftle_')
	pic_file_exist(itnums, 'displacement/displacement_')
	pic_file_exist(itnums, 'chl/chl_')
	pic_file_exist(itnums, 'sst/sst_')
	############################################################################################
	return













############################## Opedia Inspection  ###############################

def raw_file_exists(folder, prefix, itnums, file_format):
        for itnum in itnums:
                path = '%s%s%7.7d%s' % (folder, prefix, itnum, file_format)
                if not os.path.isfile(path):
                        print('Not Found: ' + path)
        return



def tile_file_exists(folder, prefix, itnums, file_format):
        row_tiles = 2
        col_tiles = 4
        for itnum in itnums:
                for i in range(1, row_tiles+1):
                        for j in range(1, col_tiles+1):
                                path = '%s%s%10.10d_%d_%d%s' % (folder, prefix, itnum, i, j, file_format)
                                if not os.path.isfile(path):
                                        print('Not Found: ' + path)
        return


def inspect_raws(itnums):
	#raw_file_exists(cfgv.rep_chl_raw, cfgv.rep_chl_prefix, itnums, '.nc')
        raw_file_exists(cfgv.rep_armor3d_raw, cfgv.rep_armor3d_prefix, itnums, '.nc')
        return

def inspect_tiles(itnums):
        #tile_file_exists(cfgv.rep_chl_tile, cfgv.rep_chl_prefix, itnums, '.mat')
	tile_file_exists(cfgv.rep_armor3d_tile, cfgv.rep_armor3d_prefix + 'mld_', itnums, '.mat')
        tile_file_exists(cfgv.rep_armor3d_tile, cfgv.rep_armor3d_prefix + 'salinity_', itnums, '.mat')
        return

#################################################################################





itnums = np.array([])
'''
itnums = np.append(itnums, range(2015001, 2015361))
'''
itnums = np.append(itnums, range(2014001, 2014366))
itnums = np.append(itnums, range(2013001, 2013366))
itnums = np.append(itnums, range(2012001, 2012367))
itnums = np.append(itnums, range(2011001, 2011366))
itnums = np.append(itnums, range(2010001, 2010366))
itnums = np.append(itnums, range(2009001, 2009366))
itnums = np.append(itnums, range(2008001, 2008367))
itnums = np.append(itnums, range(2007001, 2007366))
itnums = np.append(itnums, range(2006001, 2006366))
'''
itnums = np.append(itnums, range(2005001, 2005366))
itnums = np.append(itnums, range(2004001, 2004367))
itnums = np.append(itnums, range(2003001, 2003366))
itnums = np.append(itnums, range(2002001, 2002366))
itnums = np.append(itnums, range(2001001, 2001366))
itnums = np.append(itnums, range(2000001, 2000367))
itnums = np.append(itnums, range(1999001, 1999366))
itnums = np.append(itnums, range(1998001, 1998366))
itnums = np.append(itnums, range(1997001, 1997366))
itnums = np.append(itnums, range(1996001, 1996367))
itnums = np.append(itnums, range(1995001, 1995366))
itnums = np.append(itnums, range(1994001, 1994366))
itnums = np.append(itnums, range(1993001, 1993366))
'''


#### 1. If input mat files required for edML.py exist
#inspect_input_mats(itnums)

#### 2. If detected eddied files (generated by edML.py) exist
#eddML_file_exist(itnums)

#### 2. If compiled files (that holds the eddy core information) exist
#compiled_file_exist(itnums)

#### 3. If pic files exist
#inspect_maps(itnums)






############################## Opedia Inspection  ###############################
#### 1. If the input raw files exists (data files downloaded from data sources)
inspect_raws(itnums)

#### 2. If the tile files exists (interpolated and tiled files)
inspect_tiles(itnums)


#################################################################################
