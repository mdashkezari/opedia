"""
Author: Mohammad Dehghani Ashkezari <mdehghan@uw.edu>

Date: 2019-04-15

Function: Create a basic dashboard for sparse variables within a predefined space-time domain.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
import numpy as np
import pandas as pd
from math import pi
import db
import plotHeat
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool, DatetimeTickFormatter
from bokeh.layouts import column
import jupyterInline as jup
if jup.jupytered():
    from tqdm import tqdm_notebook as tqdm
else:
    from tqdm import tqdm


def timePanel(df, table, variable, unit, subject):
    TOOLS = "crosshair,pan,zoom_in,wheel_zoom,zoom_out,box_zoom,reset,save,"
    plotWidth, plotHeight = 800, 400
    markerSize = 9
    backgroundFillColor = None #'dimgray'
    fillColor = 'mediumslateblue'
    hoverFillColor = 'firebrick'
    hoverLineColor = 'white'
    lineColor = None
    fillAlpha = 0.5
    hoverAlpha = 0.8
    margin = 0.1    

    p2 = None
    if 'time' in df.columns:
        if isinstance(df['time'][0], str):
            df['time'] =  pd.to_datetime(df['time'], format='%Y-%m-%d')
        p2 = figure(tools=TOOLS, toolbar_location="right", title=subject, plot_width=plotWidth, plot_height=plotHeight, background_fill_color=backgroundFillColor)
        p2.yaxis.axis_label = variable + unit
        p2.xaxis.axis_label = 'Time'
        p2.xaxis.formatter = DatetimeTickFormatter(
                hours=["%Y-%m-%d"],
                days=["%Y-%m-%d"],
                months=["%Y-%m-%d"],
                years=["%Y-%m-%d"],
            )
        p2.xaxis.major_label_orientation = pi/4    
        source = ColumnDataSource({'x': df['time'], 'y': df[variable], 'Time': df['time']})      
        p2.circle('x', 'y', source = source, fill_color=fillColor, hover_fill_color=hoverFillColor, fill_alpha=fillAlpha, hover_alpha=hoverAlpha, line_color=lineColor, hover_line_color=hoverLineColor, size=markerSize)
        p2.add_tools(HoverTool(
            tooltips=[
                ('time', '@Time'),
                (variable+unit, '@y'),
            ],
            mode='mouse'
        ))
    return p2


def latPanel(df, table, variable, unit, subject):
    TOOLS = "crosshair,pan,zoom_in,wheel_zoom,zoom_out,box_zoom,reset,save,"
    plotWidth, plotHeight = 800, 400
    markerSize = 9
    backgroundFillColor = None #'dimgray'
    fillColor = 'mediumslateblue'
    hoverFillColor = 'firebrick'
    hoverLineColor = 'white'
    lineColor = None
    fillAlpha = 0.5
    hoverAlpha = 0.8
    margin = 0.1    

    p2 = None
    p2 = figure(tools=TOOLS, toolbar_location="right", title=subject, plot_width=plotWidth, plot_height=plotHeight, background_fill_color=backgroundFillColor)
    p2.yaxis.axis_label = variable + unit
    p2.xaxis.axis_label = 'Latitude'    
    p2.circle(df.lat, df[variable], fill_color=fillColor, hover_fill_color=hoverFillColor, fill_alpha=fillAlpha, hover_alpha=hoverAlpha, line_color=lineColor, hover_line_color=hoverLineColor, size=markerSize)
    p2.add_tools(HoverTool(
        tooltips=[
            ('latitude', '@x'),
            (variable+unit, '@y'),
        ],
        mode='mouse'
    ))
    return p2


def lonPanel(df, table, variable, unit, subject):
    TOOLS = "crosshair,pan,zoom_in,wheel_zoom,zoom_out,box_zoom,reset,save,"
    plotWidth, plotHeight = 800, 400
    markerSize = 9
    backgroundFillColor = None #'dimgray'
    fillColor = 'mediumslateblue'
    hoverFillColor = 'firebrick'
    hoverLineColor = 'white'
    lineColor = None
    fillAlpha = 0.5
    hoverAlpha = 0.8
    margin = 0.1    

    p2 = None
    p2 = figure(tools=TOOLS, toolbar_location="right", title=subject, plot_width=plotWidth, plot_height=plotHeight, background_fill_color=backgroundFillColor)
    p2.yaxis.axis_label = variable + unit
    p2.xaxis.axis_label = 'Longitude'
    p2.circle(df.lon, df[variable], fill_color=fillColor, hover_fill_color=hoverFillColor, fill_alpha=fillAlpha, hover_alpha=hoverAlpha, line_color=lineColor, hover_line_color=hoverLineColor, size=markerSize)
    p2.add_tools(HoverTool(
        tooltips=[
            ('longitude', '@x'),
            (variable+unit, '@y'),
        ],
        mode='mouse'
    ))
    return p2



def depthPanel(df, table, variable, unit, subject):
    TOOLS = "crosshair,pan,zoom_in,wheel_zoom,zoom_out,box_zoom,reset,save,"
    plotWidth, plotHeight = 800, 400
    markerSize = 9
    backgroundFillColor = None #'dimgray'
    fillColor = 'mediumslateblue'
    hoverFillColor = 'firebrick'
    hoverLineColor = 'white'
    lineColor = None
    fillAlpha = 0.5
    hoverAlpha = 0.8
    margin = 0.1    

    p2 = None
    if 'depth' in df.columns:
        p2 = figure(tools=TOOLS, toolbar_location="right", title=subject, plot_width=plotWidth, plot_height=plotHeight, background_fill_color=backgroundFillColor)
        p2.yaxis.axis_label = variable + unit
        p2.xaxis.axis_label = 'Depth [m]'
        p2.circle(df.depth, df[variable], fill_color=fillColor, hover_fill_color=hoverFillColor, fill_alpha=fillAlpha, hover_alpha=hoverAlpha, line_color=lineColor, hover_line_color=hoverLineColor, size=markerSize)
        p2.add_tools(HoverTool(
            tooltips=[
                ('depth', '@x'),
                (variable+unit, '@y'),
            ],
            mode='mouse'
        ))
    return p2



def dashboardPanels(df, table, variable):
    p=[]    
    time_sub = ''
    if 'depth' in df.columns:
        times = df['time'].sort_values().unique()  
        time_sub = 'time: ' + str(times[0]) + ' -- ' + str(times[-1])
    depth_sub = ''
    if 'depth' in df.columns:
        depth_sub = ', depth: %2.2f -- %2.2f' % (np.min(df.depth), np.max(df.depth)) + ' [m]'
    unit =  ' [' + db.getVar(table, variable).iloc[0]['Unit'] + ']'
    subject = time_sub + depth_sub
    unit =  ' [' + db.getVar(table, variable).iloc[0]['Unit'] + ']'

    plotHeat.heatMap(df, table, variable, unit)
    panel = timePanel(df, table, variable, unit, subject)
    if panel != None: p.append(panel)
    panel = latPanel(df, table, variable, unit, subject)    
    if panel != None: p.append(panel)        
    panel = lonPanel(df, table, variable, unit, subject)    
    if panel != None: p.append(panel)
    panel = depthPanel(df, table, variable, unit, subject)    
    if panel != None: p.append(panel)

    if len(p) > 0:
        if not jup.inline():          ## if jupyter is not the caller
            fname = 'dashboard'
            dirPath = 'embed/'
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)        
            output_file(dirPath + fname + ".html", title=variable+unit)            
        show(column(p))
    return p


