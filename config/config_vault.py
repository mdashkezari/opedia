#!/usr/bin/env python

import os

def makedir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
	return



opedia_proj = 'H:/projects/opedia/'

vault = 'H:/opedia_vault/'
makedir(vault)


################## path to downloaded files ##################
vault_raw = vault + 'raw/'
makedir(vault_raw)


## models
model_raw = vault_raw + 'model/'
makedir(model_raw)
nrt_model_raw = model_raw + 'nrt/'
makedir(nrt_model_raw)
rep_model_raw = model_raw + 'rep/'
makedir(rep_model_raw)


## near real time/forecaste models
nrt_mercator_pisces_raw = nrt_model_raw + 'mercator_pisces/'
makedir(nrt_mercator_pisces_raw)
nrt_mercator_pisces_prefix = 'mercator_pisces_'



## observations
obs_raw = vault_raw + 'obs/'
makedir(obs_raw)
in_situ_raw = obs_raw + 'in-situ/'
makedir(in_situ_raw)
nrt_raw = obs_raw + 'nrt/'
makedir(nrt_raw)
rep_raw = obs_raw + 'rep/'
makedir(rep_raw)



## in-situ
socat_raw = in_situ_raw + 'socat/'
makedir(socat_raw)
seaflow_raw = in_situ_raw + 'seaflow/'
makedir(seaflow_raw)


## near real time observations
nrt_alt_raw = nrt_raw + 'alt/'
makedir(nrt_alt_raw)
nrt_alt_prefix = 'nrt_alt_'
'''
nrt_sla_raw = nrt_raw + 'sla/'
makedir(nrt_sla_raw)
nrt_sla_prefix = 'nrt_sla_'
nrt_uv_sla_raw = nrt_raw + 'uv_sla/'
makedir(nrt_uv_sla_raw)
nrt_uv_sla_prefix = 'nrt_uv_sla_'
nrt_adt_raw = nrt_raw + 'adt/'
makedir(nrt_adt_raw)
nrt_adt_prefix = 'nrt_adt_'
nrt_uv_adt_raw = nrt_raw + 'uv_adt/'
makedir(nrt_uv_adt_raw)
nrt_uv_adt_prefix = 'nrt_uv_adt_'
'''
nrt_sst_raw = nrt_raw + 'sst/'
makedir(nrt_sst_raw)
nrt_sst_prefix = 'nrt_sst_'
nrt_chl_raw = nrt_raw + 'chl/'
makedir(nrt_chl_raw)
nrt_chl_prefix = 'nrt_chl_'
nrt_wind_raw = nrt_raw + 'wind/'
makedir(nrt_wind_raw)
nrt_wind_prefix = 'nrt_wind_'


nrt_ftle_bw_sla_raw = nrt_raw + 'ftle_bw_sla/'
makedir(nrt_ftle_bw_sla_raw)
nrt_ftle_bw_sla_prefix = 'nrt_ftle_bw_sla_'

nrt_ftle_fw_sla_raw = nrt_raw + 'ftle_fw_sla/'
makedir(nrt_ftle_fw_sla_raw)
nrt_ftle_fw_sla_prefix = 'nrt_ftle_fw_sla_'


nrt_ftle_bw_adt_raw = nrt_raw + 'ftle_bw_adt/'
makedir(nrt_ftle_bw_adt_raw)
nrt_ftle_bw_adt_prefix = 'nrt_ftle_bw_adt_'

nrt_ftle_fw_adt_raw = nrt_raw + 'ftle_fw_adt/'
makedir(nrt_ftle_fw_adt_raw)
nrt_ftle_fw_adt_prefix = 'nrt_ftle_fw_adt_'

nrt_vort_sla_raw = nrt_raw + 'vort_sla/'
makedir(nrt_vort_sla_raw)
nrt_vort_sla_prefix = 'nrt_vort_sla_'

nrt_vort_adt_raw = nrt_raw + 'vort_adt/'
makedir(nrt_vort_adt_raw)
nrt_vort_adt_prefix = 'nrt_vort_adt_'


nrt_col_raw = nrt_raw + 'col/'
makedir(nrt_col_raw)
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
nrt_armor3d_raw = nrt_raw + 'armor3d/'
makedir(nrt_armor3d_raw)
nrt_armor3d_prefix = 'nrt_armor3d_'


## reprocessed observations
rep_alt_raw = rep_raw + 'alt/'
makedir(rep_alt_raw)
rep_alt_prefix = 'rep_alt_'
'''
rep_sla_raw = rep_raw + 'sla/'
makedir(rep_sla_raw)
rep_sla_prefix = 'rep_sla_'
rep_uv_sla_raw = rep_raw + 'uv_sla/'
makedir(rep_uv_sla_raw)
rep_uv_sla_prefix = 'rep_uv_sla_'
rep_adt_raw = rep_raw + 'adt/'
makedir(rep_adt_raw)
rep_adt_prefix = 'rep_adt_'
rep_uv_adt_raw = rep_raw + 'uv_adt/'
makedir(rep_uv_adt_raw)
rep_uv_adt_prefix = 'rep_uv_adt_'
'''
rep_chl_raw = rep_raw + 'chl/'
makedir(rep_chl_raw)
rep_chl_prefix = 'rep_chl_'
rep_wind_raw = rep_raw + 'wind/'
makedir(rep_wind_raw)
rep_wind_prefix = 'rep_wind_'



rep_ftle_bw_sla_raw = rep_raw + 'ftle_bw_sla/'
makedir(rep_ftle_bw_sla_raw)
rep_ftle_bw_sla_prefix = 'rep_ftle_bw_sla_'

rep_ftle_fw_sla_raw = rep_raw + 'ftle_fw_sla/'
makedir(rep_ftle_fw_sla_raw)
rep_ftle_fw_sla_prefix = 'rep_ftle_fw_sla_'


rep_ftle_bw_adt_raw = rep_raw + 'ftle_bw_adt/'
makedir(rep_ftle_bw_adt_raw)
rep_ftle_bw_adt_prefix = 'rep_ftle_bw_adt_'

rep_ftle_fw_adt_raw = rep_raw + 'ftle_fw_adt/'
makedir(rep_ftle_fw_adt_raw)
rep_ftle_fw_adt_prefix = 'rep_ftle_fw_adt_'

rep_vort_sla_raw = rep_raw + 'vort_sla/'
makedir(rep_vort_sla_raw)
rep_vort_sla_prefix = 'rep_vort_sla_'

rep_vort_adt_raw = rep_raw + 'vort_adt/'
makedir(rep_vort_adt_raw)
rep_vort_adt_prefix = 'rep_vort_adt_'



rep_col_raw = rep_raw + 'col/'
makedir(rep_col_raw)
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
rep_armor3d_raw = rep_raw + 'armor3d/'
makedir(rep_armor3d_raw)
rep_armor3d_prefix = 'rep_armor3d_'


##############################################################











################## path to tiled files ##################
vault_tile = vault + 'tile/'
makedir(vault_tile)


## models
model_tile = vault_tile + 'model/'
makedir(model_tile)
mercator_tile = model_tile + 'mercator/'
makedir(mercator_tile)


## observations
obs_tile = vault_tile + 'obs/'
makedir(obs_tile)
in_situ_tile = obs_tile + 'in-situ/'
makedir(in_situ_tile)
nrt_tile = obs_tile + 'nrt/'
makedir(nrt_tile)
rep_tile = obs_tile + 'rep/'
makedir(rep_tile)



## in-situ
socat_tile = in_situ_tile + 'socat/'
makedir(socat_tile)
seaflow_tile = in_situ_tile + 'seaflow/'
makedir(seaflow_tile)


## near real time observations
nrt_alt_tile = nrt_tile + 'alt/'
makedir(nrt_alt_tile)
'''
nrt_sla_tile = nrt_tile + 'sla/'
makedir(nrt_sla_tile)
nrt_uv_sla_tile = nrt_tile + 'uv_sla/'
makedir(nrt_uv_sla_tile)
nrt_adt_tile = nrt_tile + 'adt/'
makedir(nrt_adt_tile)
nrt_uv_adt_tile = nrt_tile + 'uv_adt/'
makedir(nrt_uv_adt_tile)
nrt_phase_sla_tile = nrt_tile + 'phase_sla/'
makedir(nrt_phase_sla_tile)
nrt_phase_sla_prefix = 'nrt_phase_sla_'
nrt_phase_adt_tile = nrt_tile + 'phase_adt/'
makedir(nrt_phase_adt_tile)
nrt_phase_adt_prefix = 'nrt_phase_adt_'
'''
nrt_vort_sla_tile = nrt_tile + 'vort_sla/'
makedir(nrt_vort_sla_tile)
nrt_vort_sla_prefix = 'nrt_vort_sla_' 
nrt_vort_adt_tile = nrt_tile + 'vort_adt/'
makedir(nrt_vort_adt_tile)
nrt_vort_adt_prefix = 'nrt_vort_adt_'
nrt_sst_tile = nrt_tile + 'sst/'
makedir(nrt_sst_tile)
nrt_chl_tile = nrt_tile + 'chl/'
makedir(nrt_chl_tile)
nrt_col_tile = nrt_tile + 'col/'
makedir(nrt_col_tile)
nrt_armor3d_tile = nrt_tile + 'armor3d/'
makedir(nrt_armor3d_tile)
nrt_wind_tile = nrt_tile + 'wind/'
makedir(nrt_wind_tile)


## reprocessed observations
rep_alt_tile = rep_tile + 'alt/'
makedir(rep_alt_tile)
'''
rep_sla_tile = rep_tile + 'sla/'
makedir(rep_sla_tile)
rep_uv_sla_tile = rep_tile + 'uv_sla/'
makedir(rep_uv_sla_tile)
rep_adt_tile = rep_tile + 'adt/'
makedir(rep_adt_tile)
rep_uv_adt_tile = rep_tile + 'uv_adt/'
makedir(rep_uv_adt_tile)
rep_phase_sla_tile = rep_tile + 'phase_sla/'
makedir(rep_phase_sla_tile)
rep_phase_sla_prefix = 'rep_phase_sla_'
rep_phase_adt_tile = rep_tile + 'phase_adt/'
makedir(rep_phase_adt_tile)
rep_phase_adt_prefix = 'rep_phase_adt_'
'''
rep_vort_sla_tile = rep_tile + 'vort_sla/'
makedir(rep_vort_sla_tile)
rep_vort_sla_prefix = 'rep_vort_sla_'
rep_vort_adt_tile = rep_tile + 'vort_adt/'
makedir(rep_vort_adt_tile)
rep_vort_adt_prefix = 'rep_vort_adt_'
rep_chl_tile = rep_tile + 'chl/'
makedir(rep_chl_tile)
rep_col_tile = rep_tile + 'col/'
makedir(rep_col_tile)
rep_armor3d_tile = rep_tile + 'armor3d/'
makedir(rep_armor3d_tile)
rep_wind_tile = rep_tile + 'wind/'
makedir(rep_wind_tile)


##############################################################
