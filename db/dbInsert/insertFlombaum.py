import sys
sys.path.append('../')
import insertFunctions as iF

############################
########### OPTS ###########
tableName = 'tblFlombaum'
rawFileName = 'flombaum.csv'
############################
############################

iF.toSQLbcp(rawFileName, tableName)
