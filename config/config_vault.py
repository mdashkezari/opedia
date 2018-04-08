#!/usr/bin/env python

import os

def makedir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
	return

def leafStruc(base):
	nrt = base + 'nrt/'
	makedir(nrt)
	rep = base + 'rep/'
	makedir(rep)
	doc = base + 'doc/'
	makedir(doc)
	code = base + 'code/'
	makedir(code)
	return nrt, rep, doc, code
    	

opedia_proj = r'H:/Dropbox/projects/opedia/'
vault = r'H:/Dropbox/Apps/OpediaVault/'
makedir(vault)


################## opedia vault file structure ##################
vault_raw = vault #+ 'raw/'
makedir(vault_raw)

#########  assimilation  #########
assimilation_raw = vault_raw + 'assimilation/'
makedir(assimilation_raw)


###########  models  ##########
model_raw = vault_raw + 'model/'
makedir(model_raw)
### models/mercator_pisces ####
mercator_pisces_raw = model_raw + 'mercator_pisces/'
makedir(mercator_pisces_raw)
nrt_mercator_pisces_raw, rep_mercator_pisces_raw, doc_mercator_pisces_raw, code_mercator_pisces_raw = leafStruc(mercator_pisces_raw)
nrt_mercator_pisces_prefix = 'mercator_pisces_'
rep_mercator_pisces_prefix = 'mercator_pisces_'
######## models/darwin ########
darwin_raw = model_raw + 'darwin/'
makedir(darwin_raw)
nrt_darwin_raw, rep_darwin_raw, doc_darwin_raw, code_darwin_raw = leafStruc(darwin_raw)
nrt_darwin_prefix = 'darwin_'
rep_darwin_prefix = 'darwin_'



#########  observations  #########
obs_raw = vault_raw + 'observation/'
makedir(obs_raw)
in_situ_raw = obs_raw + 'in-situ/'
makedir(in_situ_raw)
remote_raw = obs_raw + 'remote/'
makedir(remote_raw)
#########  obs/in-situ/cruise  #########
cruise_raw = in_situ_raw + 'cruise/'
makedir(cruise_raw)
######  obs/in-situ/cruise/socat  ######
socat_raw = cruise_raw + 'socat/'
makedir(socat_raw)
nrt_socat_raw, rep_socat_raw, doc_socat_raw, code_socat_raw = leafStruc(socat_raw)
####  obs/in-situ/cruise/seaflow  #####
seaflow_raw = cruise_raw + 'seaflow/'
makedir(seaflow_raw)
nrt_seaflow_raw, rep_seaflow_raw, doc_seaflow_raw, code_seaflow_raw = leafStruc(seaflow_raw)
####  obs/in-situ/cruise/lineage  #####
lineage_raw = cruise_raw + 'lineage/'
makedir(lineage_raw)
nrt_lineage_raw, rep_lineage_raw, doc_lineage_raw, code_lineage_raw = leafStruc(lineage_raw)
####  obs/in-situ/cruise/tax16s  #####
tax16s_raw = cruise_raw + 'tax16s/'
makedir(tax16s_raw)
nrt_tax16s_raw, rep_tax16s_raw, doc_tax16s_raw, code_tax16s_raw = leafStruc(tax16s_raw)


########  obs/remote/satellite  ########
satellite_raw = remote_raw + 'satellite/'
makedir(satellite_raw)

alt_raw = satellite_raw + 'alt/'
nrt_alt_raw, rep_alt_raw, doc_alt_raw, code_alt_raw = leafStruc(alt_raw)
nrt_alt_prefix = 'nrt_alt_'
rep_alt_prefix = 'rep_alt_'

sst_raw = satellite_raw + 'sst/'
nrt_sst_raw, rep_sst_raw, doc_sst_raw, code_sst_raw = leafStruc(sst_raw)
nrt_sst_prefix = 'nrt_sst_'
rep_sst_prefix = 'rep_sst_'

chl_raw = satellite_raw +'chl/'
nrt_chl_raw, rep_chl_raw, doc_chl_raw, code_chl_raw = leafStruc(chl_raw)
nrt_chl_prefix = 'nrt_chl_'
rep_chl_prefix = 'rep_chl_'

wind_raw = satellite_raw + 'wind/'
nrt_wind_raw, rep_wind_raw, doc_wind_raw, code_wind_raw = leafStruc(wind_raw)
nrt_wind_prefix = 'nrt_wind_'
rep_wind_prefix = 'rep_wind_'

ftle_bw_sla_raw = satellite_raw + 'ftle_bw_sla/'
nrt_ftle_bw_sla_raw, rep_ftle_bw_sla_raw, doc_ftle_bw_sla_raw, code_ftle_bw_sla_raw = leafStruc(ftle_bw_sla_raw)
nrt_ftle_bw_sla_prefix = 'nrt_ftle_bw_sla_'
rep_ftle_bw_sla_prefix = 'rep_ftle_bw_sla_'

ftle_fw_sla_raw = satellite_raw + 'ftle_fw_sla/'
nrt_ftle_fw_sla_raw, rep_ftle_fw_sla_raw, doc_ftle_fw_sla_raw, code_ftle_fw_sla_raw = leafStruc(ftle_fw_sla_raw)
nrt_ftle_fw_sla_prefix = 'nrt_ftle_fw_sla_'
rep_ftle_fw_sla_prefix = 'rep_ftle_fw_sla_'

ftle_bw_adt_raw = satellite_raw + 'ftle_bw_adt/'
nrt_ftle_bw_adt_raw, rep_ftle_bw_adt_raw, doc_ftle_bw_adt_raw, code_ftle_bw_adt_raw = leafStruc(ftle_bw_adt_raw)
nrt_ftle_bw_adt_prefix = 'nrt_ftle_bw_adt_'
rep_ftle_bw_adt_prefix = 'rep_ftle_bw_adt_'

ftle_fw_adt_raw = satellite_raw + 'ftle_fw_adt/'
nrt_ftle_fw_adt_raw, rep_ftle_fw_adt_raw, doc_ftle_fw_adt_raw, code_ftle_fw_adt_raw = leafStruc(ftle_fw_adt_raw)
nrt_ftle_fw_adt_prefix = 'nrt_ftle_fw_adt_'
rep_ftle_fw_adt_prefix = 'rep_ftle_fw_adt_'

vort_sla_raw = satellite_raw + 'vort_sla/'
nrt_vort_sla_raw, rep_vort_sla_raw, doc_vort_sla_raw, code_vort_sla_raw = leafStruc(vort_sla_raw)
nrt_vort_sla_prefix = 'nrt_vort_sla_'
rep_vort_sla_prefix = 'rep_vort_sla_'

vort_adt_raw = satellite_raw + 'vort_adt/'
nrt_vort_adt_raw, rep_vort_adt_raw, doc_vort_adt_raw, code_vort_adt_raw = leafStruc(vort_adt_raw)
nrt_vort_adt_prefix = 'nrt_vort_adt_'
rep_vort_adt_prefix = 'rep_vort_adt_'

armor3d_raw = satellite_raw + 'armor3d/'
nrt_armor3d_raw, rep_armor3d_raw, doc_armor3d_raw, code_armor3d_raw = leafStruc(armor3d_raw)
nrt_armor3d_prefix = 'nrt_armor3d_'
rep_armor3d_prefix = 'rep_armor3d_'

col_raw = satellite_raw + 'col/'
nrt_col_raw, rep_col_raw, doc_col_raw, code_col_raw = leafStruc(col_raw)
nrt_col_RRS412_prefix = 'nrt_col_RRS412_'
nrt_col_RRS443_prefix = 'nrt_col_RRS443_'
nrt_col_RRS490_prefix = 'nrt_col_RRS490_'
nrt_col_RRS555_prefix = 'nrt_col_RRS555_'
nrt_col_RRS670_prefix = 'nrt_col_RRS670_'
nrt_col_CDM443_prefix = 'nrt_col_CDM443_'
nrt_col_BBP443_prefix = 'nrt_col_BBP443_'
nrt_col_KD490_prefix = 'nrt_col_KD490_'
nrt_col_ZSD_prefix = 'nrt_col_ZSD_'
nrt_col_SPM_prefix = 'nrt_col_SPM_'
rep_col_RRS412_prefix = 'rep_col_RRS412_'
rep_col_RRS443_prefix = 'rep_col_RRS443_'
rep_col_RRS490_prefix = 'rep_col_RRS490_'
rep_col_RRS555_prefix = 'rep_col_RRS555_'
rep_col_RRS670_prefix = 'rep_col_RRS670_'
rep_col_CDM443_prefix = 'rep_col_CDM443_'
rep_col_BBP443_prefix = 'rep_col_BBP443_'
rep_col_KD490_prefix = 'rep_col_KD490_'
rep_col_ZSD_prefix = 'rep_col_ZSD_'
rep_col_SPM_prefix = 'rep_col_SPM_'