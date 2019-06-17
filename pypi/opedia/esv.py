"""
Author: Mohammad Dehghani Ashkezari <mdehghan@uw.edu>

Date: Winter 2018

Function: Retrieve 16s amplicon within a predefined space-time domain. 
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
import db
import export
import numpy as np
import pandas as pd
from math import pi
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.models import DatetimeTickFormatter
from bokeh.palettes import all_palettes
from bokeh.models import HoverTool
from bokeh.embed import components
from bokeh.models import Legend
import jupyterInline as jup
if jup.jupytered():
    from tqdm import tqdm_notebook as tqdm
else:
    from tqdm import tqdm




def exportData(df):
    # dirPath = 'data/'
    # path = dirPath + 'esv.csv'
    # if not os.path.exists(dirPath):
    #     os.makedirs(dirPath)    
    # df.to_csv(path, index=False)    
    #     
    export.dump(df, table='tblESV', variable='relative_abundance', prefix='ESV', fmt='.csv')
    return


def aggQuery(depth1, depth2, cruise_name, cluster_level, size_frac_lower, size_frac_upper, domain, kingdom, phylum, class_tax, order, genus, species):
    query = "SELECT [time], lat, lon, AVG(depth) AS depth, SUM(relative_abundance) AS abund FROM tblESV WHERE "
    query += "depth BETWEEN %f AND %f AND " % (depth1, depth2)
    query += "cruise_name='%s' AND " % cruise_name
    query += "cluster_level=%d AND " % cluster_level  
    query += "size_frac_lower=%f AND " % size_frac_lower  
    if size_frac_upper is not None:
        query += "size_frac_upper=%f AND " % size_frac_upper 
    else:
        query += "size_frac_upper IS NULL AND " 

    if domain is not None:
        if domain == nullPlaceholder:
            query = query + "RTRIM(LTRIM(domain)) IS NULL AND "
        else:    
            query = query + "RTRIM(LTRIM(domain))='%s' AND " % domain
    if kingdom is not None:
        if kingdom == nullPlaceholder:
            query = query + "RTRIM(LTRIM(kingdom)) IS NULL AND "
        else:    
            query = query + "RTRIM(LTRIM(kingdom)) = '%s' AND " % kingdom 
    if phylum is not None:
        if phylum == nullPlaceholder:
            query = query + "RTRIM(LTRIM(phylum)) IS NULL AND "
        else:    
            query = query + "RTRIM(LTRIM(phylum)) = '%s' AND " % phylum
    if class_tax is not None:
        if class_tax == nullPlaceholder:
            query = query + "RTRIM(LTRIM([class])) IS NULL AND "
        else:    
            query = query + "RTRIM(LTRIM([class])) = '%s' AND " % class_tax
    if order is not None:
        if order == nullPlaceholder:
            query = query + "RTRIM(LTRIM([order])) IS NULL AND "
        else:    
            query = query + "RTRIM(LTRIM([order])) = '%s' AND " % order
    if genus is not None:
        if genus == nullPlaceholder:
            query = query + "RTRIM(LTRIM([genus])) IS NULL AND "
        else:    
            query = query + "RTRIM(LTRIM([genus])) = '%s' AND " % genus
    if species is not None:
        if genus == nullPlaceholder:
            query = query + "RTRIM(LTRIM([species])) IS NULL AND "
        else:    
            query = query + "RTRIM(LTRIM([species])) = '%s' AND " % species
    query = query[:-4]
    query = query + "GROUP BY [time], [lat], [lon] "
    query = query + "ORDER BY [time], [lat], [lon] "
    df = db.dbFetch(query)
    return df


def organismsList(tax, depth1, depth2, cruise_name, cluster_level, size_frac_lower, size_frac_upper, table='tblESV'):
    query = "SELECT [%s], SUM(relative_abundance) AS total FROM %s WHERE " % (tax, table)
    query += "depth BETWEEN %f AND %f AND " % (depth1, depth2)
    query += "cruise_name='%s' AND " % cruise_name
    # removing null, ambiguous, and uncultured taxa labels
    query += "[%s] IS NOT NULL AND " % tax
    query += "[%s] NOT LIKE '%s' AND " % (tax, '%uncultured%')
    query += "[%s] NOT LIKE '%s' AND " % (tax, '%ambiguous%')
    query += "[%s] NOT LIKE '%s' AND " % (tax, '%unidentified%')
    query += "[%s] NOT LIKE '%s' AND " % (tax, '%metagenome%')

    query += "cluster_level=%d AND " % cluster_level  
    query += "size_frac_lower=%f AND " % size_frac_lower  
    if size_frac_upper is not None:
        query += "size_frac_upper=%f " % size_frac_upper 
    else:
        query += "size_frac_upper IS NULL " 
    query += "GROUP BY [%s] ORDER BY total DESC " % tax
    df = db.dbFetch(query)
    df[tax] = df[tax].str.strip()
    return df





def plotESVs(topN, tax, depth1, depth2, cruise_name, cluster_level, size_frac_lower, size_frac_upper):
    def spectrum(ind):
        colList = ['grey', 'purple', 'darkturquoise', 'black', 'red', 'blue', 'pink', 'lime', 'green', 'orange']
        ind = ind % len(colList)
        col = colList[ind]
        return col

    
    # get the list of organisms at the specified taxonomy level, "tax", sorted by their abundance 
    orgs = organismsList(tax, depth1, depth2, cruise_name, cluster_level, size_frac_lower, size_frac_upper)
    if topN < len(orgs):
        orgs = orgs[:topN]
        
    orgs = np.array(orgs[tax])  

    msize=10
    p = []
    lw = 2
    w = 800
    h = 400
    TOOLS = 'pan,wheel_zoom,zoom_in,zoom_out,box_zoom, undo,redo,reset,tap,save,box_select,poly_select,lasso_select'
    p1 = figure(tools=TOOLS, toolbar_location="above", plot_width=w, plot_height=h)
    p1.xaxis.axis_label = 'Latitude'
    p1.yaxis.axis_label = 'Relative Abundance'
    fill_alpha = 0.7

    df = pd.DataFrame()
    for i in tqdm(range(len(orgs)), desc='overall'):
        if orgs[i] is None:
            orgs[i] = nullPlaceholder
        domain, kingdom, phylum, class_tax, order, genus, species = None, None, None, None, None, None, None
        if tax.lower().find('domain') != -1:
            domain = orgs[i]
        elif tax.lower().find('kingdom') != -1:    
            kingdom = orgs[i]
        elif tax.lower().find('phylum') != -1:    
            phylum = orgs[i]
        elif tax.lower().find('class') != -1:    
            class_tax = orgs[i]
        elif tax.lower().find('order') != -1:    
            order = orgs[i]
        elif tax.lower().find('genus') != -1:    
            genus = orgs[i]
        elif tax.lower().find('species') != -1:    
            species = orgs[i]


        dfOrg = aggQuery(depth1, depth2, cruise_name, cluster_level, size_frac_lower, size_frac_upper, domain, kingdom, phylum, class_tax, order, genus, species)
        
        dfOrg.sort_values(by=['lat'], inplace=True)

        x, y = dfOrg['lat'], dfOrg['abund']        
        leg = orgs[i]
        filCol = spectrum(i)
        cr = p1.circle(x, y, fill_color=filCol, hover_fill_color="firebrick", fill_alpha=fill_alpha, hover_alpha=0.3, line_color=None, hover_line_color="white", legend=leg , size=msize)
        p1.line(x, y, line_color=filCol, line_width=lw, legend=leg )          

        if i == 0:
            df = dfOrg.copy()
            df.drop(['abund'], axis=1, inplace=True)
        df[orgs[i]+'_abund'] = dfOrg['abund']


    p.append(p1)
    
    if exportDataFlag:
        exportData(df)   

    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)    
    if not inline:      ## if jupyter is not the caller
        output_file(dirPath + fname + ".html", title="ESV")
    show(column(p))
    print('')   
    
    return





inline = jup.inline()   # check if jupyter is calling this script
nullPlaceholder = 'NULL'
exportDataFlag = True
fname = 'esv'


