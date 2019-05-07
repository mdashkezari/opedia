import sys
sys.dont_write_bytecode = True
import os
sys.path.append(os.path.dirname(__file__))
import db
import numpy as np
from datetime import date, datetime, timedelta
from bokeh.palettes import all_palettes
import subset
import webbrowser
from tqdm import tqdm
from colorama import Fore, Back, Style, init


def normalize(vals, min_max=False):
    if min_max:
        normalized_vals=(vals-np.nanmin(vals))/(np.nanmax(vals)-np.nanmin(vals))
    else:    
        normalized_vals=(vals-np.nanmean(vals))/np.nanstd(vals)
    return normalized_vals


def openHTML(path):
    path = 'file://' + os.path.realpath(path)
    webbrowser.open(path, new=2)
    return

def PiscesDates_Offline(startDate=date(2011, 12, 31), endDate=date(2017, 12, 9)):
    delta = endDate - startDate
    dates = [(startDate + timedelta(days=x)) for x in range(0, delta.days+1, 7)]
    return dates



def nearestDate(dates, dt):
    return min(dates, key=lambda d: abs(d - dt))



def timesBetween(calTable, startDate, endDate):
    query = "SELECT [time] FROM %s WHERE " % calTable
    query += "[time] BETWEEN '%s' AND '%s' " % (startDate, endDate)
    df = db.dbFetch(query)
    return np.array(df['time'])



def temporalRes(table):
    table = table.lower()
    dt = 1                  # default temporal resolution = 1 day
    #if table.find('tblPisces'.lower()) != -1:
    #    dt = 7
    return dt


def isGrid(table, variable):
    grid = True
    query = "SELECT Spatial_Res_ID, RTRIM(LTRIM(Spatial_Resolution)) AS Spatial_Resolution FROM tblVariables "
    query = query + "JOIN tblSpatial_Resolutions ON [tblVariables].Spatial_Res_ID=[tblSpatial_Resolutions].ID "
    query = query + "WHERE Table_Name='%s' AND Short_Name='%s' " % (table, variable)
    df = db.dbFetch(query)
    if len(df) < 1:
        return None
    if df.Spatial_Resolution[0].lower().find('irregular') != -1:
        grid = False
    return grid


def getUnit(table, variable):
    return ' [' + db.getVar(table, variable).iloc[0]['Unit'] + ']'    

def canvasRect(dw, dh):
    ar = dw / dh  # aspect ratio
    h = 400 if ar > 3 else 500
    w_min = 300
    w_max = 1000
    w = int(ar * h)
    if w > w_max: w = w_max
    if w < w_min: w = w_min
    return w, h


def printTQDM(msg, err=False):
    # init()
    if err:
        tqdm.write(Fore.RED + msg)        
    else:    
        tqdm.write(msg)
    tqdm.write(Style.RESET_ALL, end='')
    return


def halt(msg):
    print(Fore.RED + msg)    
    print(Style.RESET_ALL, end='')
    sys.exit()
    return


def getBounds(varName):
    bounds = (None, None)

    if varName.find('picoeukaryote') != -1:
        bounds = (0, 0.5)
    elif varName.find('prokaryote') != -1:
        bounds = (0, 0.5)
    elif varName.find('zooplankton') != -1:
        bounds = (0, 0.5)
    elif varName.find('POC') != -1:
        bounds = (0, 0.7)
    elif varName.find('POFe') != -1:
        bounds = (0, 8e-6)
    elif varName.find('PON') != -1:
        bounds = (0, 0.15)
    elif varName.find('POSi') != -1:
        bounds = (0, 0.15)
    elif varName.find('DOFe') != -1:
        bounds = (0, 1.3e-4)
    elif varName.find('DON') != -1:
        bounds = (0, 5)
    elif varName.find('DOP') != -1:
        bounds = (0, 0.2)
    elif varName.find('SiO2') != -1:
        bounds = (0, 30)
    elif varName.find('FeT') != -1:
        bounds = (0, 2e-4)
    elif varName.find('Fe') != -1:
        bounds = (0, 1e-4)
    elif varName.find('CDOM') != -1:
        bounds = (0, 1.3e-3)
    elif (varName.find('chl0') != -1) or (varName.find('chl1') != -1) or (varName.find('chl2') != -1) or (varName.find('chl3') != -1):
        bounds = (0, 5e-2)
    elif varName.find('chl') != -1:
        bounds = (0, 5e-1)
    elif varName.find('CHL') != -1:
        bounds = (0, 5e-1)
    elif varName.find('PHYC') != -1:
        bounds = (0, 4)
    elif varName.find('PP') != -1:
        bounds = (0, 4e-2)
    elif varName.find('Si') != -1:
        bounds = (10, 30)
    elif varName.find('NO3') != -1:
        bounds = (0, 20)
    elif varName.find('NO2') != -1:
        bounds = (0, 1.5)
    elif varName.find('NH4') != -1:
        bounds = (0, 2)
    elif varName.find('PO4') != -1:
        bounds = (0, 1.5)
    elif varName.find('O2') != -1:
        bounds = (200, 320)
    elif varName.find('ALK') != -1:
        bounds = (2000, 2400)
    elif varName.find('PIC') != -1:
        bounds = (0, 0.5)
    elif varName.find('cocco') != -1:
        bounds = (0, 0.5)
    elif varName.find('DIC') != -1:
        bounds = (1700, 2200)
    elif varName.find('DOC') != -1:
        bounds = (0, 25)
    elif varName.find('diatom') != -1:
        bounds = (0, 0.5)
    elif varName.find('diazotroph') != -1:
        bounds = (0, 0.15)
    elif varName.find('dinoflagellate') != -1:
        bounds = (0, 0.25)
    elif varName.find('wind_stress') != -1:
        bounds = (0, 3e-1)
    elif varName.find('eastward_wind') != -1:
        bounds = (0, 2)
    elif varName.find('mld_nrt') != -1:
        bounds = (0, 170)          
    elif varName.find('ftle_nrt') != -1:
        bounds = (0, 0.25)          
    elif varName.find('disp_nrt') != -1:
        bounds = (0, 2.5)          
    elif varName.find('sst') != -1:
        bounds = (0, 32)          
    elif varName.find('sla') != -1:
        bounds = (-0.3, 0.3)          
    elif varName.find('sss') != -1:
        bounds = (31, 37)          
    elif varName.find('vort') != -1:
        bounds = (-4e-6, 4e-6)          
    elif varName.find('AOD') != -1:
        bounds = (0, 0.5)          
    return bounds



def getPalette(varName, nCols=256):
    paletteName = all_palettes['Viridis'][nCols]
    if varName.find('picoeukaryote') != -1:
        paletteName = all_palettes['Magma'][nCols]
    elif varName.find('prokaryote') != -1:
        paletteName = all_palettes['Inferno'][nCols]
    elif varName.find('zooplankton') != -1:
        paletteName = all_palettes['Plasma'][nCols]        
    elif varName.find('POC') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('POFe') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('PON') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('POSi') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('DOFe') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('DON') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('DOP') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('SiO2') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('FeT') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('Fe') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('CDOM') != -1:
        paletteName = all_palettes['Plasma'][nCols]
    elif varName.find('PHYC') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('PP') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('Si') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('NO3') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('NO2') != -1:
        paletteName = all_palettes['Plasma'][nCols]
    elif varName.find('NH4') != -1:
        paletteName = all_palettes['Plasma'][nCols]
    elif varName.find('PO4') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('O2') != -1:
        paletteName = all_palettes['Inferno'][nCols]
    elif varName.find('ALK') != -1:
        paletteName = all_palettes['Magma'][nCols]
    elif varName.find('PIC') != -1:
        paletteName = all_palettes['Plasma'][nCols]
    elif varName.find('chl') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('CHL') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('diazotroph') != -1:
        paletteName = all_palettes['Inferno'][nCols]
    elif varName.find('dinoflagellate') != -1:
        paletteName = all_palettes['Magma'][nCols]
    elif varName.find('diatom') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('cocco') != -1:
        paletteName = all_palettes['Plasma'][nCols]
    elif varName.find('DIC') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('DOC') != -1:
        paletteName = all_palettes['Viridis'][nCols]
    elif varName.find('wind_stress') != -1:
        paletteName = all_palettes['Plasma'][nCols]
    elif varName.find('mld_nrt') != -1:
        paletteName = all_palettes['Plasma'][nCols]        
    elif varName.find('ftle_nrt') != -1:
        paletteName = all_palettes['Inferno'][nCols]        
    elif varName.find('disp_nrt') != -1:
        paletteName = all_palettes['Inferno'][nCols]        
    elif varName.find('sst') != -1:
        paletteName = all_palettes['Inferno'][nCols]
    elif varName.find('sss') != -1:
        paletteName = all_palettes['Inferno'][11]
    elif varName.find('AOD') != -1:
        paletteName = all_palettes['Inferno'][nCols]
    elif varName.find('sla') != -1:
        paletteName = 'RdBu11'
    return paletteName
