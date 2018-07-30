import sys
sys.path.append('../../config')
import config_vault as cfgv
import pandas as pd
import numpy as np
import argo
import urllib
import time


def get_argo_ftp(url):
    fname = url.split('/')[-1]
    path = cfgv.rep_merge_argo_raw + fname
    urllib.urlcleanup()
    urllib.urlretrieve(url, path)
    return


mergeDF = argo.loadArgoMerge(dataMode='D', ocean='all')
i = -1
while i<len(mergeDF):    
    url = argo.dac + mergeDF.iloc[i, 0]
    try:
        i += 1
        get_argo_ftp(url)
        print('profile %d out of %d' % (i, len(mergeDF)) )
    except:    
        print('Error at profile: %d' % i)
        i -= 1
        time.sleep(1)
    

