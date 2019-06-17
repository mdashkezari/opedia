"""
Author: Mohammad Dehghani Ashkezari <mdehghan@uw.edu>

Date: Spring 2019

Function: Generate video files from section map snapshots.
"""

from docopt import docopt
import sys
import os
sys.path.append(os.path.dirname(__file__))
import numpy as np
import pandas as pd
import warnings
import db
import subset
import common as com
import video
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.pyplot import figure
import random, string
import shutil
import jupyterInline as jup
if jup.jupytered():
    from tqdm import tqdm_notebook as tqdm
else:
    from tqdm import tqdm



def makeDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return


def sectionFrame(table, field, dt, lat, lon, depth, data, frameDirectory, frame, cmap, bounds, levels, xLabel, titleExt):
    figure(figsize=(12, 5))
    fontSize = 14
    if len(lon) > len(lat):
        X, DEPTH = np.meshgrid(lon, depth)
    else:
        X, DEPTH = np.meshgrid(lat, depth)    
    levels = np.linspace(bounds[0], bounds[1], levels)
    data = np.transpose(data)
    data = np.squeeze(data)
    cs = plt.contourf(X, DEPTH, data, levels, cmap=cmap, vmin=bounds[0], vmax=bounds[1], extend='both')
    plt.gca().invert_yaxis()
    plt.xlabel(xLabel, fontsize=fontSize)
    plt.ylabel('Depth [m]', fontsize=fontSize)
    matplotlib.rc('xtick', labelsize=fontSize)
    matplotlib.rc('ytick', labelsize=fontSize)
    unit =  ' [' + db.getVar(table, field).iloc[0]['Unit'] + ']'
    plt.title(field + unit + '\n ' + dt + '  ' + titleExt, fontsize=fontSize)
    plt.colorbar(cs, ax=plt.gca(), format='%1.1e')
    # plt.grid(linestyle = '-.', linewidth = 0.1)
    plt.tight_layout()
    plt.savefig(frameDirectory + '%5.5d.png' % (frame), dpi=300)
    plt.clf()
    plt.close()
    return


def makeFrames(table, field, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, frameDirectory, cmap, bounds, levels):
    dt1 = pd.to_datetime(startDate, format='%Y-%m-%d')
    dt2 = pd.to_datetime(endDate, format='%Y-%m-%d')
    dtRange = pd.date_range(dt1, dt2, freq='D')
    itnum = -1
    limits = [None, None]
    for frame, dtIndex in enumerate(tqdm(dtRange, desc='frames')):    
        dt = dtIndex.strftime("%Y-%m-%d")
        df = subset.section(table, field, dt, dt, lat1, lat2, lon1, lon2, depth1, depth2) 
        if len(df)<1:
            continue            
        itnum += 1
        lat = df.lat.unique()
        lon = df.lon.unique()
        depth = df.depth.unique()
        shape = (len(lat), len(lon), len(depth))
        data = df[field].values.reshape(shape)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)       
            if len(lon) > len(lat):
                data = np.mean(data, axis=0)
                xLabel = 'Longitude [$\degree$E]'
                titleExt = 'Averaged around lat: %2.2f [$\degree$N]' % np.nanmean(lat)    
            else:
                data = np.mean(data, axis=1)
                xLabel = 'Latitude [$\degree$N]'  
                titleExt = 'Averaged around lon: %2.2f [$\degree$E]' % np.nanmean(lon)
        if itnum == 0:
            bou = com.getBounds(field, data)
            if not bounds[0]: 
                limits[0] = bou[0]
            else:
                limits[0] = bounds[0]    
            if not bounds[1]: 
                limits[1] = bou[1]
            else:
                limits[1] = bounds[1] 
        sectionFrame(table, field, dt, lat, lon, depth, data, frameDirectory, itnum, cmap, tuple(limits), levels, xLabel, titleExt)
    return


def assembleFrames(frameDirectory, field, frameRate):
    vidDir = './video/' 
    makeDir(vidDir)
    vidName = vidDir + '%s_Section.mp4' % field
    echo = video.animateFrames(frameDirectory, frameRate, vidName)
    return echo, vidName


def sectionVideo(tables, variables, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, frameRate=5, cmap='viridis', bounds=[None, None], levels=21):
    for i in tqdm(range(len(tables)), desc='overall'):
        try:            
            if not com.hasField(tables[i], 'depth'):    
                com.printTQDM('\nTable %s has no depth field.' % tables[i], err=True)
                continue
            frameDirectory = './%s/' % ''.join(random.choices(string.ascii_letters, k=16))
            makeDir(frameDirectory)
            table = tables[i]
            field = variables[i]
            makeFrames(table, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, frameDirectory, cmap, bounds, levels)
            echo, vidName = assembleFrames(frameDirectory, field, frameRate)
            com.openVideo(vidName)
        finally:
            if 'frameDirectory' in locals():
                shutil.rmtree(frameDirectory)
    return





def main():
    tables = sys.argv[1]      
    variables = sys.argv[2]      
    dt1 = sys.argv[3]      
    dt2 = sys.argv[4]      
    lat1 = sys.argv[5]      
    lat2 = sys.argv[6]      
    lon1 = sys.argv[7]      
    lon2 = sys.argv[8]      
    depth1 = sys.argv[9]      
    depth2 = sys.argv[10]     
    frameRate = 5
    if len(sys.argv) > 11: 
        frameRate = int(sys.argv[11])
    cmap = 'viridis'
    if len(sys.argv) > 12:     
        cmap = sys.argv[12]
    bounds = [None, None]
    if len(sys.argv) > 13:     
        bounds = sys.argv[13]
    levels = 21
    if len(sys.argv) > 14: 
        levels = int(sys.argv[14])

    sectionVideo(tables.split(','), variables.split(','), dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, frameRate, cmap, bounds, levels)


# inline = jup.inline()   # check if jupyter is calling this script
if __name__ == '__main__':
    main()
    

