
import os
import sys
sys.path.append('../../config')
import config_vault as cfgv
import glob



"""grab gradients 1 seaflow data - https://github.com/armbrustlab/seaflow-sfl/blob/master/curated/SCOPE_16_751.sfl"""
def getGradients1_seaflow():
    outputdir = cfgv.rep_gradients_1_raw
    os.chdir(outputdir)
    print(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  https://raw.githubusercontent.com/armbrustlab/seaflow-sfl/master/curated/SCOPE_16_751.sfl'
    os.system(wget_str)
    os.system('mv SCOPE_16_751.sfl gradients1_seaflow.csv') # renames folder

# """grab gradients 1 cruise traj - https://www.rvdata.us/search/cruise/KOK1606 - http://scope.soest.hawaii.edu/data/gradients/data/"""
# def getGradients1_navigation():
#     outputdir = cfgv.rep_Gradients_1_raw
#     print(outputdir)
#     wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  https://www.nodc.noaa.gov/archive/arc0130/0183950/1.1/data/0-data/MGL1704_603744_r2rnav/data/MGL1704_bestres.geoCSV'
#     os.system(wget_str)
#
#
# def getGradients1_adcp(): # data not available for download
#     outputdir = cfgv.rep_Gradients1_raw
#     os.chdir(outputdir)
#     wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://get.rvdata.us/cruise/KM1427/fileset/115308'
#     os.system('tar -zxvf 115308') #unzips data
#     os.system('mv KM1427/ adcp_KM1427/') # renames folder
#     os.system('rm 115308') # removes gzip archive
#
#
# def getGradients1_barometer(): # data not available for download
#     outputdir = cfgv.rep_Gradients1_raw
#     os.chdir(outputdir)
#     wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://get.rvdata.us/cruise/KM1427/fileset/115940'
#     os.system(wget_str) # downloads data
#     os.system('tar -zxvf 115940') #unzips data
#     os.system('mv KM1427/ barometer_KM1427/') # renames folder
#     os.system('rm 115940') # removes gzip archive
#
# def getGradients1_tsv(): # data not available for download
#     outputdir = cfgv.rep_Gradients1_raw
#     os.chdir(outputdir)
#     wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://get.rvdata.us/cruise/KM1427/fileset/116039'
#     os.system(wget_str) # downloads data
#     os.system('tar -zxvf 116039') #unzips data
#     os.system('mv KM1427/ tsv_KM1427/') # renames folder
#     os.system('rm 116039') # removes gzip archive
#
# def getGradients1_met():
#     outputdir = cfgv.rep_Gradients1_raw
#     os.chdir(outputdir)
#     wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://get.rvdata.us/cruise/KM1427/fileset/116080'
#     os.system(wget_str) # downloads data
#     os.system('tar -zxvf 116080') #unzips data
#     os.system('mv KM1427/ met_KM1427/') # renames folder
#     os.system('rm 116080') # removes gzip archive


"""grab gradients 1 CTD summary data - http://scope.soest.hawaii.edu/collaborators/datainventory/data.php"""
def getGradients1_CTD_summary():
    outputdir = cfgv.rep_gradients_1_raw
    os.chdir(outputdir)
    print(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://scope.soest.hawaii.edu/data/gradients/data/kok1606.sum'
    os.system(wget_str)
    os.system('mv kok1606.sum gradients1_CTD_summary.csv') # renames folder

"""grab gradients 1 CTD data - http://scope.soest.hawaii.edu/collaborators/datainventory/data.php"""
def getGradients1_CTD():
    outputdir = cfgv.rep_gradients_1_raw
    os.chdir(outputdir)
    print(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  ftp://ftp.soest.hawaii.edu/dkarl/scope/ctd/gradients1/'
    os.system(wget_str)

def getGradients1_LICOR_PAR():
    outputdir = cfgv.rep_gradients_1_raw
    os.chdir(outputdir)
    print(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://scope.soest.hawaii.edu/data/gradients/data/gyre_edge_licorpar.txt'
    os.system(wget_str)
    os.system('mv gyre_edge_licorpar.txt gradients1_LICOPAR.csv') # renames folder


"""grab gradients 2 seaflow data - https://raw.githubusercontent.com/armbrustlab/seaflow-sfl/master/curated/MGL1704_751.sfl"""
def getGradients2_seaflow():
    outputdir = cfgv.rep_gradients_2_raw
    os.chdir(outputdir)
    print(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  https://raw.githubusercontent.com/armbrustlab/seaflow-sfl/master/curated/MGL1704_751.sfl'
    os.system(wget_str)
    os.system('mv MGL1704_751.sfl gradients2_seaflow.csv') # renames folder

"""grab gradients 2 cruise traj - https://www.rvdata.us/search/cruise/MGL1704"""
def getGradients2_navigation():
    outputdir = cfgv.rep_gradients_2_raw
    os.chdir(outputdir)
    print(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  https://www.nodc.noaa.gov/archive/arc0130/0183950/1.1/data/0-data/MGL1704_603744_r2rnav/data/MGL1704_bestres.geoCSV'
    os.system(wget_str)
    os.system('mv MGL1704_bestres.geoCSV gradients2_r2r_nav.csv') # renames folder


def getGradients2_adcp(): # data not available for download
    outputdir = cfgv.rep_Gradients2_raw
    os.chdir(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  https://www.nodc.noaa.gov/archive/arc0130/0183950/1.1/data/0-data/MGL1704_603744_r2rnav/data/MGL1704_bestres.geoCSV'
    os.system('tar -zxvf 115308') #unzips data
    os.system('mv KM1427/ adcp_KM1427/') # renames folder
    os.system('rm 115308') # removes gzip archive


def getGradients2_barometer(): # data not available for download
    outputdir = cfgv.rep_Gradients2_raw
    os.chdir(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  https://www.nodc.noaa.gov/archive/arc0130/0183950/1.1/data/0-data/MGL1704_603744_r2rnav/data/MGL1704_bestres.geoCSV'
    os.system(wget_str) # downloads data
    os.system('tar -zxvf 115940') #unzips data
    os.system('mv KM1427/ barometer_KM1427/') # renames folder
    os.system('rm 115940') # removes gzip archive

def getGradients2_tsv(): # data not available for download
    outputdir = cfgv.rep_Gradients2_raw
    os.chdir(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  https://www.nodc.noaa.gov/archive/arc0130/0183950/1.1/data/0-data/MGL1704_603744_r2rnav/data/MGL1704_bestres.geoCSV'
    os.system(wget_str) # downloads data
    os.system('tar -zxvf 116039') #unzips data
    os.system('mv KM1427/ tsv_KM1427/') # renames folder
    os.system('rm 116039') # removes gzip archive

def getGradients2_met():
    outputdir = cfgv.rep_Gradients2_raw
    os.chdir(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  https://www.nodc.noaa.gov/archive/arc0130/0183950/1.1/data/0-data/MGL1704_603744_r2rnav/data/MGL1704_bestres.geoCSV'
    os.system(wget_str) # downloads data
    os.system('tar -zxvf 116080') #unzips data
    os.system('mv KM1427/ met_KM1427/') # renames folder
    os.system('rm 116080') # removes gzip archive


"""grab gradients 2 CTD summary data - http://scope.soest.hawaii.edu/collaborators/datainventory/data.php"""
def getGradients2_CTD_summary():
    outputdir = cfgv.rep_gradients_2_raw
    os.chdir(outputdir)
    print(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://scope.soest.hawaii.edu/data/gradients/data/mgl1704.sum'
    os.system(wget_str)
    os.system('mv mgl1704.sum Gradients2_CTD_summary.csv') # renames folder

"""grab gradients 2 CTD data - http://scope.soest.hawaii.edu/collaborators/datainventory/data.php"""
def getGradients2_CTD():
    outputdir = cfgv.rep_gradients_2_raw
    os.chdir(outputdir)
    print(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  ftp://ftp.soest.hawaii.edu/dkarl/scope/ctd/gradients2/'
    os.system(wget_str)


"""grab gradients 3 seaflow data - https://raw.githubusercontent.com/armbrustlab/seaflow-sfl/master/curated/KM1906_740.sfl"""
def getGradients3_seaflow():
    outputdir = cfgv.rep_gradients_3_raw
    os.chdir(outputdir)
    print(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  https://raw.githubusercontent.com/armbrustlab/seaflow-sfl/master/curated/KM1906_740.sfl'
    os.system(wget_str)
    os.system('mv KM1906_740.sfl gradients3_seaflow.csv') # renames folder

# """grab gradients 3 cruise traj -https://www.rvdata.us/search/cruise/KM1906"""
# def getGradients3_navigation():
#     outputdir = cfgv.rep_gradients_2_raw
#     print(outputdir)
#     wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  https://www.nodc.noaa.gov/archive/arc0130/0183950/1.1/data/0-data/MGL1704_603744_r2rnav/data/MGL1704_bestres.geoCSV'
#     os.system(wget_str)
#
#
# def getGradients3_adcp(): # data not available for download
#     outputdir = cfgv.rep_Gradients3_raw
#     os.chdir(outputdir)
#     wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://get.rvdata.us/cruise/KM1427/fileset/115308'
#     os.system('tar -zxvf 115308') #unzips data
#     os.system('mv KM1427/ adcp_KM1427/') # renames folder
#     os.system('rm 115308') # removes gzip archive
#
#
# def getGradients3_barometer(): # data not available for download
#     outputdir = cfgv.rep_Gradients3_raw
#     os.chdir(outputdir)
#     wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://get.rvdata.us/cruise/KM1427/fileset/115940'
#     os.system(wget_str) # downloads data
#     os.system('tar -zxvf 115940') #unzips data
#     os.system('mv KM1427/ barometer_KM1427/') # renames folder
#     os.system('rm 115940') # removes gzip archive
#
# def getGradients3_tsv(): # data not available for download
#     outputdir = cfgv.rep_Gradients3_raw
#     os.chdir(outputdir)
#     wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://get.rvdata.us/cruise/KM1427/fileset/116039'
#     os.system(wget_str) # downloads data
#     os.system('tar -zxvf 116039') #unzips data
#     os.system('mv KM1427/ tsv_KM1427/') # renames folder
#     os.system('rm 116039') # removes gzip archive
#
# def getGradients3_met():
#     outputdir = cfgv.rep_Gradients3_raw
#     os.chdir(outputdir)
#     wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://get.rvdata.us/cruise/KM1427/fileset/116080'
#     os.system(wget_str) # downloads data
#     os.system('tar -zxvf 116080') #unzips data
#     os.system('mv KM1427/ met_KM1427/') # renames folder
#     os.system('rm 116080') # removes gzip archive

"""grab gradients 3 CTD summary data - http://scope.soest.hawaii.edu/collaborators/datainventory/data.php"""
def getGradients3_CTD_summary():
    outputdir = cfgv.rep_gradients_3_raw
    os.chdir(outputdir)
    print(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://scope.soest.hawaii.edu/data/gradients/data/gradients3.sum'
    os.system(wget_str)
    os.system('mv gradients3.sum gradients3_CTD_summary.csv') # renames folder

"""grab gradients 3 CTD data - http://scope.soest.hawaii.edu/collaborators/datainventory/data.php"""
def getGradients3_CTD():
    outputdir = cfgv.rep_gradients_3_raw
    os.chdir(outputdir)
    print(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  ftp://ftp.soest.hawaii.edu/dkarl/scope/ctd/gradients3/'
    os.system(wget_str)

def getGradients3_LICOR_PAR():
    outputdir = cfgv.rep_gradients_3_raw
    os.chdir(outputdir)
    print(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  http://scope.soest.hawaii.edu/data/gradients/data/gradients3_licorpar.txt'
    os.system(wget_str)
    os.system('mv gradients3_licorpar.txt gradients3_LICOPAR.csv') # renames folder


# getGradients1_seaflow()
# getGradients1_CTD_summary()
# getGradients1_CTD()
# getGradients1_LICOR_PAR()

# getGradients2_seaflow()
# getGradients2_navigation()
# getGradients2_CTD_summary()
# getGradients2_CTD()


# getGradients3_seaflow()
# getGradients3_CTD_summary()
# getGradients3_CTD()
# getGradients3_LICOR_PAR()
