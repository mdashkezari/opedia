import sys
sys.path.append('../')
import insertFunctions as iF

############################
########### OPTS ###########
tableName = 'tblFlombaum_temp'
rawFileName = 'flombaum_temp.csv'
############################
############################

iF.toSQLbcp(rawFileName, tableName)
