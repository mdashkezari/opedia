"""
Author: Mohammad Dehghani Ashkezari <mdehghan@uw.edu>

Date: Spring 2019

Function: Generate video outputs using ffmpeg library.
"""

from docopt import docopt
import sys
import os
sys.path.append(os.path.dirname(__file__))


def animateFrames(frameDirectory, frameRate, vidName):
    cmd = 'ffmpeg ' 
    cmd += ' -y -hide_banner -loglevel panic'
    cmd += ' -r ' + str(frameRate) 
    cmd += ' -i '+ frameDirectory + '%5d.png'
    cmd += ' -pix_fmt yuv420p'
    cmd += ' -vcodec libx264 ' + vidName
    echo = os.system(cmd)
    return echo

