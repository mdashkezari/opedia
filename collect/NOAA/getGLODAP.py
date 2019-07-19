

import os
import sys
sys.path.append('../../config')
import config_vault as cfgv
import glob



"""grab GLODAP data - https://www.nodc.noaa.gov/archive/arc0107/0162565/2.2/data/0-data/data_product/"""
def getGLODAP():
    outputdir = cfgv.rep_GLODAP_raw
    os.chdir(outputdir)
    print(outputdir)
    wget_str = 'wget -P ' + outputdir + ' -np -nH --cut-dirs 8 -r  https://www.nodc.noaa.gov/archive/arc0107/0162565/2.2/data/0-data/data_product/GLODAPv2%20Merged%20Master%20File.csv.zip'
    os.system(wget_str)
getGLODAP()
