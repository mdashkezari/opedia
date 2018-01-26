import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import db
import timeSeries as TS
import itertools as itt
from datetime import datetime, timedelta
import time
from math import pi
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.models import DatetimeTickFormatter
from bokeh.palettes import all_palettes
from bokeh.models import HoverTool
from bokeh.embed import components


def embedComponents(fname, data):
    f = open(fname, 'w')
    f.write(data)
    f.close()
    return


def plotXY(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, extV, extVV, extV2, extVV2, marker='-', msize=30, clr='green'):
    p = []
    lw = 2
    w = 500
    h = 500
    TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'

    tablePairs = list(itt.combinations(tables, 2))
    variablePairs = list(itt.combinations(variables, 2))
    extVPairs = list(itt.combinations(extV, 2))
    extVVPairs = list(itt.combinations(extVV, 2))
    extV2Pairs = list(itt.combinations(extV2, 2))
    extVV2Pairs = list(itt.combinations(extVV2, 2))
    for i in range(len(tablePairs)):
        t1, y1, y_std1 = TS.timeSeries(tablePairs[i][0], variablePairs[i][0], startDate, endDate, lat1, lat2, lon1, lon2, extVPairs[i][0], extVVPairs[i][0], extV2Pairs[i][0], extVV2Pairs[i][0])
        t2, y2, y_std2 = TS.timeSeries(tablePairs[i][1], variablePairs[i][1], startDate, endDate, lat1, lat2, lon1, lon2, extVPairs[i][1], extVVPairs[i][1], extV2Pairs[i][1], extVV2Pairs[i][1])
        p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)


        p1.xaxis.axis_label = variablePairs[i][0] + ' [' + db.getVar(tablePairs[i][0], variablePairs[i][0]).iloc[0]['Unit'] + ']'
        p1.yaxis.axis_label = variablePairs[i][1] + ' [' + db.getVar(tablePairs[i][1], variablePairs[i][1]).iloc[0]['Unit'] + ']'
        leg = variablePairs[i][0] + ' / ' + variablePairs[i][1]
        if extVPairs[i][0] != None:
            leg = leg + '   ' + extVPairs[i][0] + ': ' + ( '%d' % float(extVVPairs[i][0]) ) 
            if tablePairs[i][0].find('Pisces') != -1:
                leg = leg + ' ' + 'm'

        if extVPairs[i][1] != None:
            leg = leg + '   ' + extVPairs[i][1] + ': ' + ( '%d' % float(extVVPairs[i][1]) ) 
            if tablePairs[i][1].find('Pisces') != -1:
                leg = leg + ' ' + 'm'


        fill_alpha = 0.07        
        if tablePairs[i][0].find('Pisces') != -1 or tablePairs[i][1].find('Pisces') != -1:
            fill_alpha = 0.3
        cr = p1.circle(y1, y2, fill_color="grey", hover_fill_color="firebrick", fill_alpha=fill_alpha, hover_alpha=0.3, line_color=None, hover_line_color="white", legend=leg, size=msize)
        p1.line(y1, y2, line_color=clr, line_width=lw, legend=leg)
        p1.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))    
        p.append(p1)


    output_file("embed/" + fname + ".html", title="XY")
    show(column(p))
    return


def plotXY_original(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, extV, extVV, extV2, extVV2, marker='-', msize=30, clr='green'):
    p = []
    lw = 2
    w = 500
    h = 500
    TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'

    fold1 = int(len(tables)/2)
    fold2 = fold1
    if len(tables) % 2 == 1:
        fold2 += 1 

    print fold1, fold2 
    print '>>>>>>>>>>>>'   
    tablePairs = list(itt.combinations(tables))
    variablePairs = list(itt.combinations(variables))
    extVPairs = list(itt.combinations(extV))
    extVVPairs = list(itt.combinations(extVV))
    extV2Pairs = list(itt.combinations(extV2))
    extVV2Pairs = list(itt.combinations(extVV2))
    for i in range(0, fold1):
        for j in range(fold1, fold2+1):
            print i, j
            t1, y1, y_std1 = TS.timeSeries(tables[i], variables[i], startDate, endDate, lat1, lat2, lon1, lon2, extV[i], extVV[i], extV2[i], extVV2[i])
            t2, y2, y_std2 = TS.timeSeries(tables[j], variables[j], startDate, endDate, lat1, lat2, lon1, lon2, extV[j], extVV[j], extV2[j], extVV2[j])
            p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
            p1.xaxis.axis_label = variables[i]
            p1.yaxis.axis_label = variables[j]
            leg = variables[i] + ' / ' + variables[j]
            if extV[i] != None:
                leg = leg + '   ' + extV[i] + ': ' + ( '%d' % float(extVV[i]) ) 
                if tables[i].find('Pisces') != -1:
                    leg = leg + ' ' + 'm'

            if extV[j] != None:
                leg = leg + '   ' + extV[j] + ': ' + ( '%d' % float(extVV[j]) ) 
                if tables[j].find('Pisces') != -1:
                    leg = leg + ' ' + 'm'

            cr = p1.circle(y1, y2, fill_color="grey", hover_fill_color="firebrick", fill_alpha=0.07, hover_alpha=0.3, line_color=None, hover_line_color="white", legend=leg, size=msize)
            p1.line(y1, y2, line_color=clr, line_width=lw, legend=leg)
            p1.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))
        
            '''
            p1.xaxis.formatter=DatetimeTickFormatter(
                    hours=["%d %B %Y"],
                    days=["%d %B %Y"],
                    months=["%d %B %Y"],
                    years=["%d %B %Y"],
                )
            '''    
            #p1.xaxis.major_label_orientation = pi/4
            #p1.xaxis.visible = False
            p.append(p1)


    output_file("embed/" + fname + ".html", title="XY")
    show(column(p))
    return



tables = sys.argv[1].split(',')      #tables
variables = sys.argv[2].split(',')      #variables
startDate = sys.argv[3]      #dt1
endDate = sys.argv[4]      #dt2
#startDate = sys.argv[3].split('T')[0]      #dt1
#endDate = sys.argv[4].split('T')[0]      #dt2

lat1 = float(sys.argv[5])      #lat1
lat2 = float(sys.argv[6])      #lat2
lon1 = float(sys.argv[7])      #lon1
lon2 = float(sys.argv[8])      #lon2
fname = sys.argv[9]
extV = sys.argv[10].split(',')       #extra condition: var_name
extVV = sys.argv[11].split(',')       #extra condition: var_val
extV2 = sys.argv[12].split(',')       #extra condition: var_name
extVV2 = sys.argv[13].split(',')       #extra condition: var_val



if float(lat1)>float(lat2):
    temp = lat1
    lat1 = lat2
    lat2 = temp

if float(lon1)>float(lon2):
    temp = lon1
    lon1 = lon2
    lon2 = temp

if datetime.strptime(startDate, '%Y-%m-%d')>datetime.strptime(endDate, '%Y-%m-%d'):
    temp = startDate
    startDate = endDate
    endDate = temp


for i in range(len(tables)):
    if extV[i].find('ignore') != -1:
        extV[i]=None
    if extVV[i].find('ignore') != -1:
        extVV[i]=None
    if extV2[i].find('ignore') != -1:
        extV2[i]=None
    if extVV2[i].find('ignore') != -1:
        extVV2[i]=None


tic = time.clock()
plotXY(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, extV, extVV, extV2, extVV2)
toc = time.clock()
print('Fetch time: %2.2f s' % (toc-tic))
