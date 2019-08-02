
import os
import sys
sys.path.append('../../config')
import config_vault as cfgv
import glob



"""grab all .sfl cruises in the seaflow github - https://github.com/armbrustlab/seaflow-sfl/tree/master/curated"""
def getAllSeaFlow():
    outputdir = cfgv.rep_allSeaFlowCruises_raw
    os.chdir(outputdir)
    print(outputdir)
    git_str = 'git clone git@github.com:armbrustlab/seaflow-sfl.git'
    os.system(git_str)
    os.chdir('seaflow-sfl/curated/')
    os.system("mv *.sfl* ../../ ")
    os.chdir(outputdir)
    os.system("rm -rf seaflow-sfl")


getAllSeaFlow()
