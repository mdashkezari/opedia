import os
import sys
import urllib
import gzip
sys.path.append('../../config')
import config_vault as cfgv
import argo_config as argo


def unzip(path):
    inF = gzip.open(path, 'rb')
    uncompPath = path[:-3]
    outF = open(uncompPath, 'wb')    
    outF.write(inF.read())
    inF.close()
    outF.close()
    return uncompPath

def get_index_ftp(baseURL, fname, unzipFlag=True):
    url = baseURL + fname
    path = cfgv.index_argo_raw + fname
    print ('Downloading Argo index: ' + url)
    urllib.urlcleanup()
    urllib.urlretrieve(url, path)
    if unzipFlag:
        unzipPath = unzip(path)
        os.remove(path)
        path = unzipPath     
    rePath = path.replace('.txt', '.csv')
    if os.path.isfile(rePath):
        os.remove(rePath)
    os.rename(path, rePath)
    return



index_baseURL = argo.gdac
grey = argo.grey
meta = argo.meta
tech = argo.tech
prof = argo.prof
traj = argo.traj
merge = argo.merge
bio_prof = argo.bio_prof
bio_traj = argo.bio_traj


get_index_ftp(index_baseURL, grey, False)
get_index_ftp(index_baseURL, prof)
get_index_ftp(index_baseURL, traj)
get_index_ftp(index_baseURL, merge)
get_index_ftp(index_baseURL, bio_prof)
get_index_ftp(index_baseURL, bio_traj)
get_index_ftp(index_baseURL, meta)
get_index_ftp(index_baseURL, tech)