import sys
sys.path.append('../../config')
import config_vault as cfgv
sys.dont_write_bytecode = True
import pandas as pd
import numpy as np




def removeBlank(cols, df):
    for col in cols:
        df[col].replace(' ', np.nan, inplace=True)
        df.dropna(subset=[col], inplace=True)
    return df


def loadArgoMerge(dataMode='all', ocean='all'):
    fname = cfgv.index_argo_raw + merge_csv
    mergeDF = pd.read_csv(fname, skiprows=8, index_col=False, dtype=object)        ### problem in column names at the original "merge" file (missing column names)
    mergeDF = removeBlank(['ocean'], mergeDF)              ## remove profiles with invalid ocean value
    ######## filters
    if dataMode.lower() != 'all':
        mergeDF = mergeDF[mergeDF['file'].str.contains("/M"+dataMode)]  
    if ocean.lower() != 'all':    
        mergeDF = mergeDF[mergeDF['ocean'].str.contains(ocean)]
    ###############

    ########## TODO: exclude the profiles in the greylist
    #indexFname = cfgv.index_argo_raw + argo.grey_csv
    #greyDF = pd.read_csv(indexFname)
    #####################################################
    return mergeDF



gdac = 'ftp://usgodae.org/pub/outgoing/argo/'
dac = gdac + 'dac/'

### original unzipped files
grey = 'ar_greylist.txt'
meta = 'ar_index_global_meta.txt.gz'
tech = 'ar_index_global_tech.txt.gz'
prof = 'ar_index_global_prof.txt.gz'
traj = 'ar_index_global_traj.txt.gz'
merge = 'argo_merge-profile_index.txt.gz'
bio_prof = 'argo_bio-profile_index.txt.gz'
bio_traj = 'argo_bio-traj_index.txt.gz'

######## csv filenames
grey_csv = grey[:-3] + 'csv'
meta_csv = meta[:-6] + 'csv'
tech_csv = tech[:-6] + 'csv'
prof_csv = prof[:-6] + 'csv'
traj_csv = traj[:-6] + 'csv'
merge_csv = merge[:-6] + 'csv'
bio_prof_csv = bio_prof[:-6] + 'csv'
bio_traj_csv = bio_traj[:-6] + 'csv'
