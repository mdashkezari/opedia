




import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import config_vault as cfgv
import pandas as pd

############################
########### OPTS ###########

tableName = 'tblESV'
rawFilePath = cfgv.rep_esv_raw
rawFileName = '190419_ANT-28-5_all_fractions_deblur_eASVs.CMAP.tsv'
useCols = ['time','lat','lon','depth','ESV_ID_or_Cluster_Centroid','Relative_Abundance','Study_Max_Abund','Clustering_Level','Num_Cluster_Members','Domain','Phylum','Class','Order','Genus','Species','Temperature_celsius','Salinity_psu','Chla_ugL','Size_frac_lower_uM','Size_frac_upper_uM','Cruise_name','prok_cells_10E05_per_ml']
############################


def makeESV(rawFilePath, rawFileName, tableName):
    path = rawFilePath + rawFileName
    prefix = tableName
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df = pd.read_csv(path,  sep='\t',usecols=useCols)
    df = ip.removeMissings(['time','lat', 'lon','depth'], df)
    df = ip.NaNtoNone(df)
    df = ip.colDatatypes(df)
    df = ip.convertYYYYMMDD(df)
    df = ip.addIDcol(df)
    df = ip.removeDuplicates(df)
    df.to_csv(export_path, index=False)
    ip.sortByTimeLatLonDepth(df, export_path, 'time', 'lat', 'lon', 'depth')
    print('export path: ' ,export_path)
    return export_path


export_path= makeESV(rawFilePath, rawFileName, tableName)

iF.toSQLbcp(export_path, tableName)
