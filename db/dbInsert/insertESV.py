
import sys
sys.path.append('../')
import insertFunctions as iF

############################
########### OPTS ###########
tableName = 'tblESV'
rawFileName = 'ANT-28-5_all_fractions_deblur_eASVs.csv'
removeCols = ['qiime2-ID', 'Cluster_Members', 'Cluster_Type', 'Run', 'Sample', 'ENA-BASE-COUNT', 'ENA-SPOT-COUNT', 'Methods_and_data']

############################
############################

iF.toSQLbcp(rawFileName, tableName, removeCols)
