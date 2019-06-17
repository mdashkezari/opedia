"""
Author: Mohammad Dehghani Ashkezari <mdehghan@uw.edu>

Date: 2019-04-15

Function: Create a geospatial heatmap of sparse variables within a predefined space-time domain.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
import common as com
import numpy as np
import folium
from folium.plugins import HeatMap, MarkerCluster, Fullscreen, MousePosition



colors = {'darkOrange': '#FF8C00', 'cyan': '#0A8A9F'}


def addLayers(m):
    tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
    folium.TileLayer(tiles=tiles, attr=(' '), name='Blue Marble').add_to(m)
    folium.TileLayer(tiles='cartoDBdark_matter', name='Black Diamond').add_to(m)
    return m


def addMousePosition(m):
    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
    MousePosition(
        position='bottomright',
        separator=' | ',
        empty_string='NaN',
        lng_first=True,
        num_digits=20,
        prefix='Coordinates:',
        lat_formatter=formatter,
        lng_formatter=formatter
    ).add_to(m)
    return m


def addMarkers(m, df, variable, unit):
    normalized = com.normalize(df[variable])
    mc = MarkerCluster(name=variable+unit, options={'spiderfyOnMaxZoom':'False', 'disableClusteringAtZoom' : '4'})
    for i in range(len(df)):
        folium.CircleMarker(location=[df.lat[i], df.lon[i]], radius=(normalized[i] * 10), tooltip='%s: %f%s <br> date: %s' % (variable, df[variable][i], unit, df['time'][i]), color=colors['darkOrange'], fill=True).add_to(mc)
    mc.add_to(m)
    return m


def addFullScreen(m):
    Fullscreen(
        position='topright',
        title='Full Screen',
        title_cancel='Exit',
        force_separate_button=True
    ).add_to(m)
    return m





def heatMap(df, table, variable, unit):
    df.dropna(subset=[variable], inplace=True)
    df.reset_index(drop=True, inplace=True)
    normalized = com.normalize(df[variable])
    data = list(zip(df.lat, df.lon, normalized))

    m = folium.Map([df.lat.mean(), df.lon.mean()], tiles=None, zoom_start=3, control_scale=True, prefer_canvas=True)
    m.get_root().title = 'Map: ' + variable + unit
    m = addLayers(m)
    HeatMap(data, name='Data Density (%s)' % variable).add_to(m)
    m = addMarkers(m, df, variable, unit)
    m = addMousePosition(m)
    folium.LayerControl(collapsed=True).add_to(m)
    # m = addFullScreen(m)

    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    fname = dirPath + 'heatMap.html'
    if os.path.exists(fname):
        os.remove(fname)
    m.save(fname)
    com.openHTML(fname)
    return
