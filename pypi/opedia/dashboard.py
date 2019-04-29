import os
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


def dashboardPanels(df, table, variable):
    p=[]    
    TOOLS = "crosshair,pan,zoom_in,wheel_zoom,zoom_out,box_zoom,reset,save,"
    w2, h2 = 800, 400
    msize = 9
    backgroundFillColor = None #'dimgray'
    fillColor = 'mediumslateblue'
    hoverFillColor = 'firebrick'
    hoverLineColor = 'white'
    lineColor = None
    fillAlpha = 0.5
    hoverAlpha = 0.8
    margin = 0.1    


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


    #### heatmap #####
    plotHeat.heatMap(df, table, variable, unit)


    if 'time' in df.columns:
        #### time-val #####
        if isinstance(df['time'][0], str):
            df['time'] =  pd.to_datetime(df['time'], format='%Y-%m-%d')

        # dy = np.nanmax(df[variable]) - np.nanmin(df[variable])
        # xRange = (np.nanmin(df['time']), np.nanmax(df['time']))
        # yRange = (np.nanmin(df[variable])-margin*dy, np.nanmax(df[variable])+margin*dy)
        # p2 = figure(tools=TOOLS, toolbar_location="right", title=subject, plot_width=w2, plot_height=h2, x_range=xRange, y_range=yRange, background_fill_color=backgroundFillColor)
        p2 = figure(tools=TOOLS, toolbar_location="right", title=subject, plot_width=w2, plot_height=h2, background_fill_color=backgroundFillColor)
        p2.yaxis.axis_label = variable + unit
        p2.xaxis.axis_label = 'Time'
        p2.xaxis.formatter = DatetimeTickFormatter(
                hours=["%Y-%m-%d"],
                days=["%Y-%m-%d"],
                months=["%Y-%m-%d"],
                years=["%Y-%m-%d"],
            )
        p2.xaxis.major_label_orientation = pi/4    
        # p2.circle(df['time'], df[variable], fill_color=fillColor, hover_fill_color=hoverFillColor, fill_alpha=fillAlpha, hover_alpha=hoverAlpha, line_color=lineColor, hover_line_color=hoverLineColor, size=msize)       
        source = ColumnDataSource({'x': df['time'], 'y': df[variable], 'Time': df['time'].dt.strftime('%Y-%m-%d') })      
        p2.circle('x', 'y', source = source, fill_color=fillColor, hover_fill_color=hoverFillColor, fill_alpha=fillAlpha, hover_alpha=hoverAlpha, line_color=lineColor, hover_line_color=hoverLineColor, size=msize)
        p2.add_tools(HoverTool(
            tooltips=[
                ('time', '@Time'),
                (variable+unit, '@y'),
            ],
            mode='mouse'
        ))
        p.append(p2)


    #### lat-val #####
    p2 = figure(tools=TOOLS, toolbar_location="right", title=subject, plot_width=w2, plot_height=h2, background_fill_color=backgroundFillColor)
    p2.yaxis.axis_label = variable + unit
    p2.xaxis.axis_label = 'Latitude'    
    p2.circle(df.lat, df[variable], fill_color=fillColor, hover_fill_color=hoverFillColor, fill_alpha=fillAlpha, hover_alpha=hoverAlpha, line_color=lineColor, hover_line_color=hoverLineColor, size=msize)
    p2.add_tools(HoverTool(
        tooltips=[
            ('latitude', '@x'),
            (variable+unit, '@y'),
        ],
        mode='mouse'
    ))
    p.append(p2)


    #### lon-val #####
    p2 = figure(tools=TOOLS, toolbar_location="right", title=subject, plot_width=w2, plot_height=h2, background_fill_color=backgroundFillColor)
    p2.yaxis.axis_label = variable + unit
    p2.xaxis.axis_label = 'Longitude'
    p2.circle(df.lon, df[variable], fill_color=fillColor, hover_fill_color=hoverFillColor, fill_alpha=fillAlpha, hover_alpha=hoverAlpha, line_color=lineColor, hover_line_color=hoverLineColor, size=msize)
    p2.add_tools(HoverTool(
        tooltips=[
            ('longitude', '@x'),
            (variable+unit, '@y'),
        ],
        mode='mouse'
    ))
    p.append(p2)


    #### depth-val #####
    if 'depth' in df.columns:
        p2 = figure(tools=TOOLS, toolbar_location="right", title=subject, plot_width=w2, plot_height=h2, background_fill_color=backgroundFillColor)
        p2.yaxis.axis_label = variable + unit
        p2.xaxis.axis_label = 'Depth [m]'
        p2.circle(df.depth, df[variable], fill_color=fillColor, hover_fill_color=hoverFillColor, fill_alpha=fillAlpha, hover_alpha=hoverAlpha, line_color=lineColor, hover_line_color=hoverLineColor, size=msize)
        p2.add_tools(HoverTool(
            tooltips=[
                ('depth', '@x'),
                (variable+unit, '@y'),
            ],
            mode='mouse'
        ))
        p.append(p2)


    if len(p) > 0:
        inline = jup.inline()   # check if jupyter is calling this script
        if not inline:          ## if jupyter is not the caller
            fname = 'dashboard'
            dirPath = 'embed/'
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)        
            output_file(dirPath + fname + ".html", title=variable+unit)            
        show(column(p))
    return p


    inline = jup.inline()   # check if jupyter is calling this script