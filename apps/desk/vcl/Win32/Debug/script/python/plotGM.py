import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import db
from datetime import datetime, timedelta
import time
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.palettes import all_palettes
from bokeh.models import LinearColorMapper, BasicTicker, ColorBar
from bokeh.embed import components


def embedComponents(fname, data):
    f = open(fname, 'w')
    f.write(data)
    f.close()
    return


def prepareGMQuery(table, dt):
    query = "SELECT * FROM %s WHERE "
    query = query + "[time]='%s' ORDER BY lat, lon"
    query = query % (table, dt)
    return query



def GM_org(table, dt, fname):
    ############# App-Level Query #############
    #query = prepareGMQuery(table, dt)
    #df = db.dbFetch(query)
    ###########################################

    ######### Stored Procedure Query ##########
    query = 'EXEC uspGlobalMap ?, ?, ?'
    fields = ['sla', 'adt', 'ugosa', 'vgosa']
    args = [table, ', '.join(fields), dt]
    args = [table, 'sla', dt]
    df = db.dbFetchStoredProc(query, args)
    df = pd.DataFrame.from_records(df, columns=fields)
    ###########################################

    shape = (720, 1440)   # global -- quarter degree
    #shape = (200,200)     # NPG
    sla = df['sla'].reshape(shape)
    sst = df['sst'].reshape(shape)
    u = df['u']
    v = df['v']
    vel = np.power(u, 2) + np.power(v, 2)
    vel = np.power(vel, 0.5)
    vel = vel.reshape(shape)

    bokehGM(data=[sla, sst, vel], subject=['SLA (m) '+dt, 'SST (C) '+dt, 'Velocity (m/s) '+dt])
    return


def bokehGM_org(data, subject, fname):
    TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
    w = 1000
    h = 500



    ind = 0
    p1 = figure(tools=TOOLS, toolbar_location="above", title=subject[ind], plot_width=w, plot_height=h, x_range=(-180, 180), y_range=(-90, 90))
    p1.xaxis.axis_label = 'Longitude'
    p1.yaxis.axis_label = 'Latitude'
    #p1.image(image=[data[ind]], x=-180, y=-90, dw=360, dh=180, palette=all_palettes['RdBu'][11])
    color_mapper = LinearColorMapper(palette="RdBu11", low=-0.3, high=0.3)
    p1.image(image=[data[ind]], color_mapper=color_mapper, x=-180, y=-90, dw=360, dh=180)
    color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                     label_standoff=12, border_line_color=None, location=(0,0))
    p1.add_layout(color_bar, 'right')



    ind = 1
    p2 = figure(tools=TOOLS, toolbar_location="above", title=subject[ind], plot_width=w, plot_height=h, x_range=(-180, 180), y_range=(-90, 90))
    p2.xaxis.axis_label = 'Longitude'
    p2.yaxis.axis_label = 'Latitude'
    #p2.image(image=[data[ind]], x=-180, y=-90, dw=360, dh=180, palette=all_palettes['Inferno'][256])
    color_mapper = LinearColorMapper(palette="Inferno256", low=0, high=30)
    p2.image(image=[data[ind]], color_mapper=color_mapper, x=-180, y=-90, dw=360, dh=180)
    color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                     label_standoff=12, border_line_color=None, location=(0,0))
    p2.add_layout(color_bar, 'right')


    ind = 2
    p3 = figure(tools=TOOLS, toolbar_location="above", title=subject[ind], plot_width=w, plot_height=h, x_range=(-180, 180), y_range=(-90, 90))
    p3.xaxis.axis_label = 'Longitude'
    p3.yaxis.axis_label = 'Latitude'
    #p3.image(image=[data[ind]], x=-180, y=-90, dw=360, dh=180, palette=all_palettes['Viridis'][11])
    color_mapper = LinearColorMapper(palette="Inferno256", low=0, high=0.7)
    p3.image(image=[data[ind]], color_mapper=color_mapper, x=-180, y=-90, dw=360, dh=180)
    color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                     label_standoff=12, border_line_color=None, location=(0,0))
    p3.add_layout(color_bar, 'right')


    output_file("embed/" + fname + ".html", title="Global Map")
    show(column(p1, p2, p3))

    p1_script, p1_div = components(p1)
    embedComponents('embed/scriptGM1.js', p1_script)
    embedComponents('embed/divGM1.js', p1_div)

    p2_script, p2_div = components(p2)
    embedComponents('embed/scriptGM2.js', p1_script)
    embedComponents('embed/divGM2.js', p1_div)

    p3_script, p3_div = components(p3)
    embedComponents('embed/scriptGM3.js', p1_script)
    embedComponents('embed/divGM3.js', p1_div)

    return
































def GM(tables, variabels, dt, arg4, fname):
    '''
    ############# App-Level Query #############
    query = prepareGMQuery(table, dt)
    df = db.dbFetch(query)
    ###########################################
    '''

    ######### Stored Procedure Query ##########
    shape = (720, 1440)   # global -- quarter degree
    data = []
    subs = [] 
    for i in range(len(tables)):
        args = [tables[i], variabels[i], dt]
        query = 'EXEC uspGlobalMap ?, ?, ?'
        if tables[i].find('Wind') != -1:
            args = [tables[i], variabels[i], dt, arg4]
            query = 'EXEC uspGlobalWind ?, ?, ?, ?'
        if tables[i].find('Pisces') != -1:
            args = [tables[i], variabels[i], dt, arg4]
            query = 'EXEC uspGlobalPisces ?, ?, ?, ?'
        df = db.dbFetchStoredProc(query, args)        
        #df = pd.DataFrame.from_records(df, columns=variabels[i])
        df = pd.DataFrame.from_records(df)

        x = np.sqrt((len(df)/2))
        x = int(x)
        shape = (x, 2*x)
        if tables[i].find('Vort') != -1:
            shape = (2*x, x)
        if tables[i].find('Wind') != -1:
            shape = (641, 1440)
        if tables[i].find('Pisces') != -1:
            shape = (359, 720)
        
        if tables[i].find('Vort') != -1: 
            data.append(np.transpose(df.values.reshape(shape)))
        else:    
            data.append(df.values.reshape(shape))

        if len(arg4)>0:
            if tables[i].find('Wind') != -1:
                sub = variabels[i] + ' ' + dt + ' ' + arg4 + 'H'
            if tables[i].find('Pisces') != -1:
                sub = variabels[i] + ' ' + dt + ' Depth: ' + arg4 + ' m'
        else:
            sub = variabels[i] + ' ' + dt    
        subs.append(sub)
    ###########################################
    bokehGM(data=data, subject=subs, fname=fname)
    return


def bokehGM(data, subject, fname):
    TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
    w = 1000
    h = 500

    p = []
    for ind in range(len(data)):
        p1 = figure(tools=TOOLS, toolbar_location="above", title=subject[ind], plot_width=w, plot_height=h, x_range=(-180, 180), y_range=(-90, 90))
        p1.xaxis.axis_label = 'Longitude'
        p1.yaxis.axis_label = 'Latitude'
        #p1.image(image=[data[ind]], x=-180, y=-90, dw=360, dh=180, palette=all_palettes['RdBu'][11])
        ##color_mapper = LinearColorMapper(palette="RdBu11", low=-0.3, high=0.3)
        color_mapper = LinearColorMapper(palette="RdBu11", low=-1e-5, high=1e-5)
        p1.image(image=[data[ind]], color_mapper=color_mapper, x=-180, y=-90, dw=360, dh=180)
        color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                        label_standoff=12, border_line_color=None, location=(0,0))
        p1.add_layout(color_bar, 'right')
        p.append(p1)



    output_file("embed/" + fname + ".html", title="Global Map")
    show(column(p))
    '''
    p1_script, p1_div = components(p1)
    embedComponents('embed/scriptGM1.js', p1_script)
    embedComponents('embed/divGM1.js', p1_div)
    '''
    return




arg1 = sys.argv[1]      #tables
arg2 = sys.argv[2]      #variables
arg3 = sys.argv[3]      #dt
fname = sys.argv[4]
arg4 = ''
if len(sys.argv)==6:
    arg4 = sys.argv[5]

GM(arg1.split(','), arg2.split(','), arg3, arg4, fname)