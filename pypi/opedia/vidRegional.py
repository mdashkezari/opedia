"""
Author: Mohammad Dehghani Ashkezari <mdehghan@uw.edu>

Date: Spring 2019

Function: Generate video files from regional map snapshots.
"""

from docopt import docopt
import sys
import os
sys.path.append(os.path.dirname(__file__))
import numpy as np
import pandas as pd
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


def regionalFrame(table, field, dt, lat, lon, depthLabel, data, frameDirectory, frame, cmap, bounds, levels):
    fontSize = 14
    LON, LAT = np.meshgrid(lon, lat)
    levels = np.linspace(bounds[0], bounds[1], levels)
    cs = plt.contourf(LON, LAT, data, levels, cmap=cmap, vmin=bounds[0], vmax=bounds[1], extend='both')
    plt.xlabel('Longitude [$\degree$E]', fontsize=fontSize)
    plt.ylabel('Latitude [$\degree$N]', fontsize=fontSize)
    matplotlib.rc('xtick', labelsize=fontSize)
    matplotlib.rc('ytick', labelsize=fontSize)
    unit =  ' [' + db.getVar(table, field).iloc[0]['Unit'] + ']'
    plt.title(field + unit + '\n ' + dt + ', Depth: ' + depthLabel, fontsize=fontSize)
    plt.colorbar(cs, ax=plt.gca(), format='%1.1e')   
    plt.gca().set_aspect('equal')
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
        df = subset.spaceTime(table, field, dt, dt, lat1, lat2, lon1, lon2, depth1, depth2) 
        if len(df)<1:
            continue            
        itnum += 1
        lat = df.lat.unique()
        lon = df.lon.unique()
        depth = None
        depthLabel = 'Surface'
        if 'depth' in df.columns:
            depth = df.depth.unique()
            if len(depth) > 1:
                com.printTQDM('Warning: Only pick one depth level. The first depth level is selected and the rest is ignored.', True)
                depth1, depth2 = depth[0], depth[0]
                df = df[df.depth == depth[0]]
            depthLabel = '%2.2f [m]' % depth[0]
        shape = (len(lat), len(lon))
        data = df[field].values.reshape(shape)        
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
        regionalFrame(table, field, dt, lat, lon, depthLabel, data, frameDirectory, itnum, cmap, tuple(limits), levels)
    return


def assembleFrames(frameDirectory, field, frameRate):
    vidDir = './video/' 
    makeDir(vidDir)
    vidName = vidDir + '%s_Regional.mp4' % field
    echo = video.animateFrames(frameDirectory, frameRate, vidName)
    return echo, vidName



def regionalVideo(tables, variables, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, frameRate=5, cmap='viridis', bounds=[None, None], levels=21):
    for i in tqdm(range(len(tables)), desc='overall'):
        try:
            frameDirectory = './%s/' % ''.join(random.choices(string.ascii_letters, k=16))
            makeDir(frameDirectory)
            table = tables[i]
            field = variables[i]
            makeFrames(table, field, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, frameDirectory, cmap, bounds, levels)
            echo, vidName = assembleFrames(frameDirectory, field, frameRate)
            com.openVideo(vidName)
        finally:
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

    regionalVideo(tables.split(','), variables.split(','), dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, frameRate, cmap, bounds, levels)


# inline = jup.inline()   # check if jupyter is calling this script
if __name__ == '__main__':
    main()
    