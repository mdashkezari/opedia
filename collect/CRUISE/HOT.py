
import os
import sys
sys.path.append('../../config')
import config_vault as cfgv
import glob



"""Scope1, Hot268, KM1427 - https://www.rvdata.us/search/cruise/KM1427"""
def getHOT268_navigation():
    outputdir = cfgv.rep_HOT268_raw
    print(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  https://www.nodc.noaa.gov/archive/arc0128/0182287/1.1/data/0-data/KM1427_603562_r2rnav/data/KM1427_bestres.geoCSV'
    os.system(wget_str)

def getHOT268_adcp():
    outputdir = cfgv.rep_HOT268_raw
    os.chdir(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://get.rvdata.us/cruise/KM1427/fileset/115308'
    os.system('tar -zxvf 115308') #unzips data
    os.system('mv KM1427/ adcp_KM1427/') # renames folder
    os.system('rm 115308') # removes gzip archive


def getHOT268_barometer():
    outputdir = cfgv.rep_HOT268_raw
    os.chdir(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://get.rvdata.us/cruise/KM1427/fileset/115940'
    os.system(wget_str) # downloads data
    os.system('tar -zxvf 115940') #unzips data
    os.system('mv KM1427/ barometer_KM1427/') # renames folder
    os.system('rm 115940') # removes gzip archive

def getHOT268_tsv():
    outputdir = cfgv.rep_HOT268_raw
    os.chdir(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://get.rvdata.us/cruise/KM1427/fileset/116039'
    os.system(wget_str) # downloads data
    os.system('tar -zxvf 116039') #unzips data
    os.system('mv KM1427/ tsv_KM1427/') # renames folder
    os.system('rm 116039') # removes gzip archive

def getHOT268_met():
    outputdir = cfgv.rep_HOT268_raw
    os.chdir(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://get.rvdata.us/cruise/KM1427/fileset/116080'
    os.system(wget_str) # downloads data
    os.system('tar -zxvf 116080') #unzips data
    os.system('mv KM1427/ met_KM1427/') # renames folder
    os.system('rm 116080') # removes gzip archive


# getHOT268_navigation()
# getHOT268_adcp()
# getHOT268_barometer()
# getHOT268_tsv()
# getHOT268_met()
