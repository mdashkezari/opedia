import sys
import numpy as np

from mpl_toolkits.basemap import Basemap

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pyodbc
import pandas.io.sql as sql
import pandas as pd
import matplotlib.ticker as mtick
import ML
from scipy.stats import pearsonr 
import math
import cmocean
import seaborn as sns



def db_connect():
    try:
        #print('Connecting to Database ...')
        
        
        ## Local Database
        server = 'THEBEAST'
        db = 'Eddy2003_2015'
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')
        
        '''
        ## Cloud (Azure) Databe
        server = 'oceanatlas.database.windows.net'
        db = 'Eddy2003_2015'
        Uid = 'AdminAtlas@oceanatlas'
        psw = 'Ocean@2016@'
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Uid=' + Uid + ';Pwd='+ psw +';Encrypt=yes')
        '''

        #print('Successful Database Connection')
    except Exception as e:
        print('Error in Database Connectio. Error message: '+str(e))
        
    return conn


def get_query_file():
    q = open('query.txt', 'r')
    lines = q.readlines()
    return lines


def corr_coef(data1, data2, cleanup=False):
    
    if cleanup:
        x = np.array([])
        y = np.array([])
        for i in range(0, len(data1)):
            if data1[i] <> None and data2[i] <> None:
                if (not math.isnan(data1[i])) and (not math.isnan(data2[i])):
                    x = np.append(x, data1[i])
                    y = np.append(y, data2[i])
        data1 = x
        data2 = y                
    
    if len(data1)>0 and len(data2)>0:
        corr, p_val = pearsonr(data1, data2)
        n = len(data1)            
        if np.abs(corr) >= 2/math.sqrt(n):
            sig = 1
        else:
            sig = 0    
    else:
        corr = None
        sig = None            
    return corr, sig

def plot_single_hist(data, clr='m', labelx='', labely='', leg='', yscale='linear', store_path='', bincount=200):   

    if len(filter(None, data)) < 1:
        return
    if np.isnan(np.nansum(data)):   # if all values are nans
        return
    plt.clf()	
    bins = np.linspace(np.nanmin(data), np.nanmax(data), bincount)
    lw = 1

    ss = len(data)
    data=np.nan_to_num(data)

    plt.hist(data, bins=bins, color=clr, histtype='step', linewidth=lw, alpha=1)
    plt.hist(data, bins=bins, color=clr, label=[leg + str(', Sample Size: ') + str(ss)], histtype='stepfilled', alpha=0.25)
    if len(labelx) > 0:
        plt.xlabel(labelx)
    if len(labely) > 0:
        plt.ylabel(labely)
    if len(leg) > 0:
        le = plt.legend()
        le.set_frame_on(False)
    plt.gca().set_yscale(yscale)    
    plt.axis([None, None, 0, None])
    plt.tight_layout()
    plt.show(block=False)
    if len(store_path) > 0:
        plt.savefig(store_path, format='png', dpi=300, transparent=plot_transparency)
    return


def plot_double_hist(data1, data2, clr1='m', clr2='b', labelx='', labely='', leg1='', leg2='', yscale='linear', store_path='', bincount=200):
    if len(filter(None, data1)) < 1 or len(filter(None, data2)) < 1:
        return
    if np.isnan(np.nansum(data1)) or np.isnan(np.nansum(data2)):   # if all values are nans
        return
    plt.clf()   

    ss1 = len(data1)
    ss2 = len(data2)
    mmin = np.array([np.nanmin(data1), np.nanmin(data2)])
    mmax = np.array([np.nanmax(data1), np.nanmax(data2)])
    bins = np.linspace(np.nanmin(mmin), np.nanmax(mmax), bincount)

    lw = 1        

    data1=np.nan_to_num(data1)
    data2=np.nan_to_num(data2)

    plt.hist(data1, bins=bins, color=clr1, histtype='step', linewidth=lw, alpha=1)
    plt.hist(data1, bins=bins, color=clr1, label=[leg1 + str(', Sample Size: ') + str(ss1)], histtype='stepfilled', alpha=0.15)
    plt.hist(data2, bins=bins, color=clr2, histtype='step', linewidth=lw, alpha=1)
    plt.hist(data2, bins=bins, color=clr2, label=[leg2 + str(', Sample Size: ') + str(ss2)], histtype='stepfilled', alpha=0.15)

    if len(labelx) > 0:
        plt.xlabel(labelx)
    if len(labely) > 0:
        plt.ylabel(labely)
    if len(leg1) > 0 and len(leg2) > 0:
        le = plt.legend()
        le.set_frame_on(False)
    if len(leg1) > 0 and len(leg2) > 0:
        plt.title('%s: %2.2e$\pm$%2.2e\n%s: %2.2e$\pm$%2.2e' % (leg1, np.nanmean(data1), np.nanstd(data1), leg2, np.nanmean(data2), np.nanstd(data2)), fontsize=11 )
    plt.gca().set_yscale(yscale)    
    plt.axis([None, None, 0, None])
    plt.tight_layout()
    plt.show(block=False)
    if len(store_path) > 0:
        plt.savefig(store_path, format='png', dpi=300, transparent=plot_transparency)
    return
    

def plot_double_hist_xlim(data1, data2, bincount, bins, ylim=-1, clr1='m', clr2='b', labelx='', labely='', leg1='', leg2='', yscale='linear', store_path=''):
    if len(filter(None, data1)) < 1 or len(filter(None, data2)) < 1:
        return
    plt.clf()   

    lw = 1        

    data1=np.nan_to_num(data1)
    data2=np.nan_to_num(data2)

    plt.hist(data1, bins=bins, color=clr1, histtype='step', linewidth=lw, alpha=1)
    plt.hist(data1, bins=bins, color=clr1, label=[leg1], histtype='stepfilled', alpha=0.25)
    plt.hist(data2, bins=bins, color=clr2, histtype='step', linewidth=lw, alpha=1)
    plt.hist(data2, bins=bins, color=clr2, label=[leg2], histtype='stepfilled', alpha=0.25)

    if ylim != -1:
        plt.ylim(0, ylim)
    if len(labelx) > 0:
        plt.xlabel(labelx)
    if len(labely) > 0:
        plt.ylabel(labely)
    if len(leg1) > 0 and len(leg2) > 0:
        le = plt.legend()
        le.set_frame_on(False)
    if len(leg1) > 0 and len(leg2) > 0:
        plt.title('%s: %2.2e$\pm$%2.2e\n%s: %2.2e$\pm$%2.2e' % (leg1, np.nanmean(data1), np.nanstd(data1), leg2, np.nanmean(data2), np.nanstd(data2)), fontsize=11 )
    plt.gca().set_yscale(yscale)    
    plt.tight_layout()
    plt.show(block=False)
    if len(store_path) > 0:
        plt.savefig(store_path, format='png', dpi=300, transparent=plot_transparency)
    return

    
def plot_hex_trend(data1, data2, marker='o', msize=1, clr=[0.4, 0.1, 0.8], labelx='', labely='', leg='', store_path='', hexbins=20):   
    if len(filter(None, data1)) < 1 or len(filter(None, data2)) < 1:
        return
    plt.clf()       
    ##################### hexbin #####################    
    l = len(data1)
    data = np.hstack((data1, data2))
    data = data.reshape(2, l)
    data = np.transpose(data)
    df1 = pd.DataFrame(data)
    
    ax = df1.plot(kind='hexbin', x=0, y=1, gridsize=hexbins)
    fig = ax.get_figure()
    if len(labelx) > 0:
        ax.set_xlabel(labelx)
    if len(labely) > 0:
        ax.set_ylabel(labely)
    
    if len(store_path) > 0:
        fig.savefig(store_path, format='png', dpi=300, transparent=plot_transparency)

    plt.figure()
    ##################################################    
    return
    
    
def plot_trend(data1, data2, marker='o', msize=1, clr=[0.4, 0.1, 0.8], labelx='', labely='', leg='', store_path=''):
    #marker='o--'
    plt.clf()
    plt.plot(data1, data2, marker, markersize=msize, markerfacecolor=clr, markeredgecolor=clr, alpha=0.25, label=leg)
    if len(labelx) > 0:
        plt.xlabel(labelx)
    if len(labely) > 0:
        plt.ylabel(labely)
    if len(leg) > 0:
        le = plt.legend()
        le.set_frame_on(False)

    '''
    x = np.array([])
    y = np.array([])
    for i in range(0, len(data1)):
        if data1[i] <> None and data2[i] <> None:
            if (not math.isnan(data1[i])) and (not math.isnan(data2[i])):
                x = np.append(x, data1[i])
                y = np.append(y, data2[i])
    corr, p_val = pearsonr(x, y)
    plt.title( 'Pearsonr: %.3f, p-value: %.2e' % (corr, p_val) )
    '''


    #plt.gca().xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))    
    plt.show(block=False)
    plt.tight_layout()
    if len(store_path) > 0:
        plt.savefig(store_path, format='png', dpi=300, transparent=plot_transparency)    
    return


def plot_double_trend(data1, data2, data2_up, data2_down, data3, data4, data4_up, data4_down, error_band=True, marker='o--', msize=1, clr1=[0.4, 0.1, 0.8], clr2='cyan', labelx='', labely='', leg1='', leg2='', store_path=''):

    clr1 = 'b'
    clr2 = 'r'
    marker='--'

    d1, d2, d2_u, d2_d, d3, d4, d4_u, d4_d = np.array([]), np.array([]), np.array([]), np.array([]), np.array([]), np.array([]), np.array([]), np.array([])

    for i in range(0, len(data1)):
        if ~np.isnan(data2[i]):
            d1 = np.append(d1, data1[i])
            d2 = np.append(d2, data2[i])
            d2_u = np.append(d2_u, data2_up[i])
            d2_d = np.append(d2_d, data2_down[i])
    for i in range(0, len(data3)):
        if ~np.isnan(data4[i]):
            d3 = np.append(d3, data3[i])
            d4 = np.append(d4, data4[i])
            d4_u = np.append(d4_u, data4_up[i])
            d4_d = np.append(d4_d, data4_down[i])
    data1, data2, data2_up, data2_down, data3, data4, data4_up, data4_down = d1, d2, d2_u, d2_d, d3, d4, d4_u, d4_d        
    z1 = np.polyfit(data1, data2, 1)
    p1 = np.poly1d(z1)
    z2 = np.polyfit(data3, data4, 1)
    p2 = np.poly1d(z2)

    #count1 = np.count_nonzero(~np.isnan(data2))
    #count2 = np.count_nonzero(~np.isnan(data4))
    m1 = np.nanmean(data2)
    m2 = np.nanmean(data4)
    std1 = np.nanstd(data2)
    std2 = np.nanstd(data4)
    stat1 = '%2.2f $\pm$ %2.2f \n Slope: %.2E' % (m1, std1, z1[0])
    stat2 = '%2.2f $\pm$ %2.2f \n Slope: %.2E' % (m2, std2, z2[0])
    leg1 = leg1 + ': ' + stat1
    leg2 = leg2 + ': ' + stat2

    plt.clf()
    plt.plot(data1, data2, marker, color=clr1, markersize=msize, markerfacecolor=clr1, markeredgecolor=clr1, alpha=0.7, label=leg1)
    plt.plot(data3, data4, marker, color=clr2, markersize=msize, markerfacecolor=clr2, markeredgecolor=clr2, alpha=0.7, label=leg2)
    if error_band:
        #plt.fill_between(data1, data2_up, data2_down, color=clr1, alpha=0.3)
        #plt.fill_between(data3, data4_up, data4_down, color=clr2, alpha=0.3)
        plt.fill_between(data1, data2_up, data2_down, color=[0.3,0.3,0.3], alpha=0.3)
        plt.fill_between(data3, data4_up, data4_down, color=[0.3,0.3,0.3], alpha=0.3)
        
    ##############  linear fits  ################    
    plt.plot(data1, p1(data1), '-', color='k')
    plt.plot(data3, p2(data3), '-', color='orange')
    ##############################################
        
    if len(labelx) > 0:
        plt.xlabel(labelx)
    if len(labely) > 0:
        plt.ylabel(labely)
    if len(leg1) > 0 and len(leg2) > 0:
        le = plt.legend()
        le.set_frame_on(False)

    diff = 100 * (abs(m1) - abs(m2)) / np.nanmean([abs(m1), abs(m2)])
    ti = 'Average Anomaly: %2.2f' % diff 
    plt.title(ti+'%')

    plt.gca().xaxis.set_major_formatter(mtick.FormatStrFormatter('%d'))    
    plt.show(block=False)
    plt.tight_layout()
    if len(store_path) > 0:
        plt.savefig(store_path, format='png', dpi=300, transparent=plot_transparency)
        
    ############### Saving the data file    
    try:
        if len(store_path) > 0:
            np.savez(store_path.split('.png')[0]+'.npz', x1=data1, y1=data2, y1_up=data2_up, y1_down=data2_down, x2=data3, y2=data4, y2_up=data4_up, y2_down=data4_down, z1=z1, z2=z2)
    except Exception as e:
        print('Error in plot_double_trend (saving npz file). Error message: '+str(e))

    return


def plot_triple_trend(data1, data2, data2_up, data2_down, data3, data4, data4_up, data4_down, data5, data6, data6_up, data6_down, error_band=True, marker='o--', msize=1, clr1=[0.4, 0.1, 0.8], clr2='cyan', clr3='k', labelx='', labely='', leg1='', leg2='', leg3='', store_path=''):
    #marker='o--'
    plt.clf()
    plt.plot(data1, data2, marker, markersize=msize, markerfacecolor=clr1, markeredgecolor=clr1, alpha=0.7, label=leg1)
    plt.plot(data3, data4, marker, markersize=msize, markerfacecolor=clr2, markeredgecolor=clr2, alpha=0.7, label=leg2)
    plt.plot(data5, data6, marker, markersize=msize, markerfacecolor=clr3, markeredgecolor=clr3, alpha=0.7, label=leg3)
    if error_band:
        plt.fill_between(data1, data2_up, data2_down, color=clr1, alpha=0.3)
        plt.fill_between(data3, data4_up, data4_down, color=clr2, alpha=0.3)
        plt.fill_between(data5, data6_up, data6_down, color=clr3, alpha=0.3)
    if len(labelx) > 0:
        plt.xlabel(labelx)
    if len(labely) > 0:
        plt.ylabel(labely)
    if len(leg1) > 0 and len(leg2) > 0:
        le = plt.legend()
        le.set_frame_on(False)
    plt.gca().xaxis.set_major_formatter(mtick.FormatStrFormatter('%d'))    
    plt.show(block=False)
    plt.tight_layout()
    if len(store_path) > 0:
        plt.savefig(store_path, format='png', dpi=300, transparent=plot_transparency)
    return
    
def zero_to_nan(nparr):
     #nparr[nparr == 0] = np.nan
     return nparr

     
def core_single_hists(df):
    plot_single_hist(np.array(df.mld_mean_fixed), 'm', 'MLD (m)', 'Density', 'Mixed Layer Depth', 'linear', 'gallery/mld_mean_fixed.png')
    plot_single_hist(zero_to_nan(np.array(df.chl_mean_fixed)), 'm', 'CHL (mg.m$^{-3}$)', 'Density', 'Chlorophyll', 'linear', 'gallery/chl_mean_fixed.png')
    
    plot_single_hist(np.array(df.eddy_radius), 'm', 'Radius (km)', 'Density', 'Eddy Radius', 'linear', 'gallery/eddy_radius.png', 50)
    plot_single_hist(np.array(df.eddy_lat), 'm', 'Latitude ($\degree$)', 'Density', 'Eddy Latitude', 'linear', 'gallery/eddy_lat.png')
    plot_single_hist(np.array(df.eddy_lon), 'm', 'Longitude ($\degree$)', 'Density', 'Eddy Longitude', 'linear', 'gallery/eddy_lon.png')

    plot_single_hist(np.array(df.phase_integ_fixed), 'm', 'Phase Integral ($\degree$)', 'Density', 'Phase Integral', 'linear', 'gallery/phase_integ_fixed.png')
    plot_single_hist(np.array(df.sla_mean_fixed), 'm', 'SLA (m)', 'Density', 'SLA', 'linear', 'gallery/sla_mean_fixed.png')
    plot_single_hist(np.array(df.vort_mean_fixed), 'm', 'Vorticity (s$^{-1}$)', 'Density', 'Relative Vorticity', 'linear', 'gallery/vort_mean_fixed.png')
    plot_single_hist(np.array(df.displacement_mean_fixed), 'm', 'Displacement ($\delta\degree$)', 'Density', 'Lagrangian Displacemet', 'linear', 'gallery/displacement_mean_fixed.png')
    plot_single_hist(np.array(df.ftle_mean_fixed), 'm', 'FTLE (day$^{-1}$)', 'Density', 'FTLE', 'linear', 'gallery/ftle_mean_fixed.png')
    plot_single_hist(np.array(df.sst_mean_fixed), 'm', 'SST (c$\degree$)', 'Density', 'SST', 'linear', 'gallery/sst_mean_fixed.png')
    return

    
def track_single_hists(df):
    plot_single_hist(np.array(df.lifetime), 'm', 'Lifetime (day)', 'Density', 'Eddy Lifetime', 'log', 'gallery/lifetime.png')
    plot_single_hist(np.array(df.propagation), 'm', 'Propagation (km)', 'Density', 'Total Propagation', 'log', 'gallery/propagation.png')
    plot_single_hist(np.array(df.mean_velocity), 'm', 'Mean Velocity (km/day)', 'Density', 'Eddy Mean Velocity', 'linear', 'gallery/mean_velocity.png')
    return
    
def attribute_single_hists(df):
    plot_single_hist(np.array(df.radius), 'm', 'Radius (km)', 'Density', 'Eddy Radius', 'linear', 'gallery/eddy_radius.png', 50)
    plot_single_hist(np.array(df.lat), 'm', 'Latitude ($\degree$)', 'Density', 'Eddy Latitude', 'linear', 'gallery/eddy_lat.png')
    plot_single_hist(np.array(df.lon), 'm', 'Longitude ($\degree$)', 'Density', 'Eddy Longitude', 'linear', 'gallery/eddy_lon.png')

    plot_single_hist(np.array(df.phase_integ_fixed), 'm', 'Phase Integral ($\degree$)', 'Density', 'Phase Integral', 'linear', 'gallery/phase_integ_fixed.png')
    plot_single_hist(np.array(df.sla_mean_fixed), 'm', 'SLA (m)', 'Density', 'SLA', 'linear', 'gallery/sla_mean_fixed.png')
    plot_single_hist(np.array(df.vort_mean_fixed), 'm', 'Vorticity (s$^{-1}$)', 'Density', 'Relative Vorticity', 'linear', 'gallery/vort_mean_fixed.png')
    plot_single_hist(np.array(df.displacement_mean_fixed), 'm', 'Displacement ($\delta\degree$)', 'Density', 'Lagrangian Displacemet', 'linear', 'gallery/displacement_mean_fixed.png')
    plot_single_hist(np.array(df.ftle_mean_fixed), 'm', 'FTLE (day$^{-1}$)', 'Density', 'FTLE', 'linear', 'gallery/ftle_mean_fixed.png')
    plot_single_hist(np.array(df.sst_mean_fixed), 'm', 'SST (c$\degree$)', 'Density', 'SST', 'linear', 'gallery/sst_mean_fixed.png')
    plot_single_hist(np.array(df.chl_mean_fixed), 'm', 'CHL (mg.m$^{-3}$)', 'Density', 'Chlorophyll', 'linear', 'gallery/chl_mean_fixed.png')
    return


def single_hists(df, dataset):
    if dataset == 'Cores':
        core_single_hists(df)
    if dataset == 'Tracks':
        track_single_hists(df)
    return


def anomally_core_hists(df):
    try:
        plot_single_hist(np.array(df.mld_mean_fixed - df.mld_mean_bkg), 'm', 'MLD Anomaly(m)', 'Density', 'Mixed Layer Depth Anomaly', 'linear', 'gallery/mld_ano.png')
        plot_single_hist(np.array(df.sla_mean_fixed)-np.array(df.sla_mean_bkg), 'm', 'SLA Anomally (m)', 'Density', 'SLA Anomally', 'linear', 'gallery/anomally_sla_mean_fixed.png')
        plot_single_hist(np.array(df.vort_mean_fixed)-np.array(df.vort_mean_bkg), 'm', 'Vorticity Anomally(s$^{-1}$)', 'Density', 'Relative Vorticity Anomally', 'linear', 'gallery/anomally_vort_mean_fixed.png')
        plot_single_hist(np.array(df.displacement_mean_fixed)-np.array(df.displacement_mean_bkg), 'm', 'Displacement Anomally ($\delta\degree$)', 'Density', 'Lagrangian Displacemet Anomally', 'linear', 'gallery/anomally_displacement_mean_fixed.png')
        plot_single_hist(np.array(df.ftle_mean_fixed)-np.array(df.ftle_mean_bkg), 'm', 'FTLE Anomally (day$^{-1}$)', 'Density', 'FTLE Anomally', 'linear', 'gallery/anomally_ftle_mean_fixed.png')
        plot_single_hist(np.array(df.sst_mean_fixed)-np.array(df.sst_mean_bkg), 'm', 'SST Anomally (c$\degree$)', 'Density', 'SST Anomally', 'linear', 'gallery/anomally_sst_mean_fixed.png')
        plot_single_hist(np.array(df.chl_mean_fixed)-np.array(df.chl_mean_bkg), 'm', 'CHL Anomally (mg.m$^{-3}$)', 'Density', 'Chlorophyll Anomally', 'linear', 'gallery/anomally_chl_mean_fixed.png')
        plot_single_hist(np.array(df.CO2_mean_surface)-np.array(df.CO2_mean_surface_bkg), 'm', 'CO$_2$ Anomally (uatm)', 'Density', 'CO$_2$ Anomally', 'linear', 'gallery/anomally_co2_surface.png')        
    except:
        print('Function error:  anomally_core_hists')        
    return

def eddy_bkg_core_hists(df):
    plot_double_hist(np.array(df.sla_mean_fixed), np.array(df.sla_mean_bkg), 'b', 'm', 'SLA (m)', 'Density', 'Eddy', 'Background', 'linear', 'gallery/double_eddy_bkg_sla.png')
    plot_double_hist(np.array(df.vort_mean_fixed), np.array(df.vort_mean_bkg), 'b', 'm', 'Vorticity (s$^{-1}$)', 'Density', 'Eddy', 'Background', 'linear', 'gallery/double_eddy_bkg_vort.png')
    plot_double_hist(np.array(df.displacement_mean_fixed), np.array(df.displacement_mean_bkg), 'b', 'm', 'Displacement ($\delta\degree$)', 'Density', 'Eddy', 'Background', 'linear', 'gallery/double_eddy_bkg_displacement.png')
    plot_double_hist(np.array(df.ftle_mean_fixed), np.array(df.ftle_mean_bkg), 'b', 'm', 'FTLE (day$^{-1}$)', 'Density', 'Eddy', 'Background', 'linear', 'gallery/double_eddy_bkg_ftle.png')
    plot_double_hist(np.array(df.sst_mean_fixed), np.array(df.sst_mean_bkg), 'b', 'm', 'SST (c$\degree$)', 'Density', 'Eddy', 'Background', 'linear', 'gallery/double_eddy_bkg_sst.png')
    plot_double_hist(zero_to_nan(np.array(df.chl_mean_fixed)), zero_to_nan(np.array(df.chl_mean_bkg)), 'b', 'm', 'CHL (mg.m$^{-3}$)', 'Density', 'Eddy', 'Background', 'linear', 'gallery/double_eddy_bkg_chl.png')
    plot_double_hist(np.array(df.CO2_mean_surface), np.array(df.CO2_mean_surface_bkg), 'b', 'm', 'CO$_2$ (uatm)', 'Density', 'Eddy', 'Background', 'linear', 'gallery/double_eddy_bkg_co2.png', 30)        
    return


def core_trend(df):

    ########################## hex trends ##########################
    plot_hex_trend(np.array(df.CO2_mean_surface), np.array(df.sst_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'fCO$_2$ ($\mu$atm)', 'SST (c$\degree$)', '', 'gallery/trend_co2_sst_hex.png', 50)
    #plot_hex_trend(np.array(df.CO2_mean_surface), np.array(df.eddy_lat), 'o', 6, [0.4, 0.1, 0.8], 'fCO$_2$ ($\mu$atm)', 'Latitude ($\degree$)', '', 'gallery/trend_co2_lat.png', 20)
    #plot_hex_trend(np.array(df.CO2_mean_surface), np.array(df.eddy_lon), 'o', 6, [0.4, 0.1, 0.8], 'fCO$_2$ ($\mu$atm)', 'Longitude ($\degree$)', '', 'gallery/trend_co2_lon.png', 20)

    plot_hex_trend(np.array(df.vort_mean_fixed), np.array(df.eddy_lat), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'Latitude ($\degree$)', '', 'gallery/trend_vort_lat_hex.png', 100)
    plot_hex_trend(np.array(df.vort_mean_fixed), np.array(df.sla_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'SLA (m)', '', 'gallery/trend_vort_sla_hex.png', 100)
    plot_hex_trend(np.array(df.vort_mean_fixed), np.array(df.sst_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'SST (c$\degree$)', '', 'gallery/trend_vort_sst_hex.png', 100)

    ##################### characteristic trends #####################
 #   plot_trend(np.array(df.eddy_lat), np.array(df.eddy_radius), 'o', 6, [0.4, 0.1, 0.8], 'Latitude ($\degree$)', 'Radius (km)', '', 'gallery/trend_lat_radius.png')
    
    ########################## co2 trends ##########################
    #plot_trend(np.array(df.CO2_mean_surface), np.array(df.phase_integ_fixed), 'o', 6, [0.4, 0.1, 0.8], 'fCO$_2$ ($\mu$atm)', 'Phase Integral ($\degree$)', '', 'gallery/trend_co2_phase.png')
    plot_trend(np.array(df.CO2_mean_surface), np.array(df.sla_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'fCO$_2$ ($\mu$atm)', 'SLA (m)', '', 'gallery/trend_co2_sla.png')
    plot_trend(np.array(df.CO2_mean_surface), np.array(df.displacement_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'fCO$_2$ ($\mu$atm)', 'Displacement ($\delta\degree$)', '', 'gallery/trend_co2_displacement.png')
    plot_trend(np.array(df.CO2_mean_surface), np.array(df.ftle_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'fCO$_2$ ($\mu$atm)', 'FTLE (day$^{-1}$)', '', 'gallery/trend_co2_ftle.png')
    plot_trend(np.array(df.CO2_mean_surface), np.array(df.chl_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'fCO$_2$ ($\mu$atm)', 'CHL (mg.m$^{-3}$)', '', 'gallery/trend_co2_chl.png')
    plot_trend(np.array(df.CO2_mean_surface), np.array(df.vort_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'fCO$_2$ ($\mu$atm)', 'Vorticity (s$^{-1}$)', '', 'gallery/trend_co2_vort.png')
    plot_trend(np.array(df.CO2_mean_surface), np.array(df.eddy_lat), 'o', 6, [0.4, 0.1, 0.8], 'fCO$_2$ ($\mu$atm)', 'Latitude ($\degree$)', '', 'gallery/trend_co2_lat.png')
    plot_trend(np.array(df.CO2_mean_surface), np.array(df.eddy_lon), 'o', 6, [0.4, 0.1, 0.8], 'fCO$_2$ ($\mu$atm)', 'Longitude ($\degree$)', '', 'gallery/trend_co2_lon.png')

    ########################## vort trends ##########################
    plot_trend(np.array(df.vort_mean_fixed), np.array(df.eddy_lat), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'Latitude ($\degree$)', '', 'gallery/trend_vort_lat.png')
    plot_trend(np.array(df.vort_mean_fixed), np.array(df.eddy_lon), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'Longitude ($\degree$)', '', 'gallery/trend_vort_lon.png')
    plot_trend(np.array(df.vort_mean_fixed), np.array(df.phase_integ_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'Phase Integral ($\degree$)', '', 'gallery/trend_vort_phase.png')
    plot_trend(np.array(df.vort_mean_fixed), np.array(df.sla_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'SLA (m)', '', 'gallery/trend_vort_sla.png')
    plot_trend(np.array(df.vort_mean_fixed), np.array(df.displacement_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'Displacement ($\delta\degree$)', '', 'gallery/trend_vort_displacement.png')
    plot_trend(np.array(df.vort_mean_fixed), np.array(df.ftle_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'FTLE (day$^{-1}$)', '', 'gallery/trend_vort_ftle.png')
    plot_trend(np.array(df.vort_mean_fixed), np.array(df.sst_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'SST (c$\degree$)', '', 'gallery/trend_vort_sst.png')
    plot_trend(np.array(df.vort_mean_fixed), np.array(df.chl_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'CHL (mg.m$^{-3}$)', '', 'gallery/trend_vort_chl.png')
    
    
    ########################## CHL trends ##########################
    plot_trend(np.array(df.chl_mean_fixed), np.array(df.eddy_lat), 'o', 6, [0.4, 0.1, 0.8], 'CHL (mg.m$^{-3}$)', 'Latitude ($\degree$)', '', 'gallery/trend_chl_lat.png')
    plot_trend(np.array(df.chl_mean_fixed), np.array(df.eddy_lon), 'o', 6, [0.4, 0.1, 0.8], 'CHL (mg.m$^{-3}$)', 'Longitude ($\degree$)', '', 'gallery/trend_chl_lon.png')
    #plot_trend(np.array(df.chl_mean_fixed), np.array(df.phase_integ_fixed), 'o', 6, [0.4, 0.1, 0.8], 'CHL (mg.m$^{-3}$)', 'Phase Integral ($\degree$)', '', 'gallery/trend_chl_phase.png')
    plot_trend(np.array(df.chl_mean_fixed), np.array(df.sla_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'CHL (mg.m$^{-3}$)', 'SLA (m)', '', 'gallery/trend_chl_sla.png')
    plot_trend(np.array(df.chl_mean_fixed), np.array(df.vort_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'CHL (mg.m$^{-3}$)', 'Vorticity (s$^{-1}$)', '', 'gallery/trend_chl_vort.png')
    #plot_trend(np.array(df.chl_mean_fixed), np.array(df.displacement_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'CHL (mg.m$^{-3}$)', 'Displacement ($\delta\degree$)', '', 'gallery/trend_chl_displacement.png')
    #plot_trend(np.array(df.chl_mean_fixed), np.array(df.ftle_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'CHL (mg.m$^{-3}$)', 'FTLE (day$^{-1}$)', '', 'gallery/trend_chl_ftle.png')
    plot_trend(np.array(df.chl_mean_fixed), np.array(df.sst_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'CHL (mg.m$^{-3}$)', 'SST (c$\degree$)', '', 'gallery/trend_chl_sst.png')

    
    ########################## SST trends ##########################
    plot_trend(np.array(df.sst_mean_fixed), np.array(df.eddy_lat), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'Latitude ($\degree$)', '', 'gallery/trend_sst_lat.png')
    plot_trend(np.array(df.sst_mean_fixed), np.array(df.eddy_lon), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'Longitude ($\degree$)', '', 'gallery/trend_sst_lon.png')
    #plot_trend(np.array(df.sst_mean_fixed), np.array(df.phase_integ_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'Phase Integral ($\degree$)', '', 'gallery/trend_sst_phase.png')
    plot_trend(np.array(df.sst_mean_fixed), np.array(df.sla_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'SLA (m)', '', 'gallery/trend_sst_sla.png')
    plot_trend(np.array(df.sst_mean_fixed), np.array(df.vort_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'Vorticity (s$^{-1}$)', '', 'gallery/trend_sst_vort.png')
    #plot_trend(np.array(df.sst_mean_fixed), np.array(df.displacement_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'Displacement ($\delta\degree$)', '', 'gallery/trend_sst_displacement.png')
    #plot_trend(np.array(df.sst_mean_fixed), np.array(df.ftle_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'FTLE (day$^{-1}$)', '', 'gallery/trend_sst_ftle.png')
    #plot_trend(np.array(df.sst_mean_fixed), np.array(df.chl_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'CHL (mg.m$^{-3}$)', '', 'gallery/trend_sst_chl.png')


    '''
    ########################## SLA trends ##########################
    plot_trend(np.array(df.sla_mean_fixed), np.array(df.phase_integ_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SLA (m)', 'Phase Integral ($\degree$)', '', 'gallery/trend_sla_phase.png')
    plot_trend(np.array(df.sla_mean_fixed), np.array(df.vort_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SLA (m)', 'Vorticity (s$^{-1}$)', '', 'gallery/trend_sla_vort.png')
    plot_trend(np.array(df.sla_mean_fixed), np.array(df.displacement_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SLA (m)', 'Displacement ($\delta\degree$)', '', 'gallery/trend_sla_displacement.png')
    plot_trend(np.array(df.sla_mean_fixed), np.array(df.ftle_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SLA (m)', 'FTLE (day$^{-1}$)', '', 'gallery/trend_sla_ftle.png')
    plot_trend(np.array(df.sla_mean_fixed), np.array(df.sst_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SLA (m)', 'SST (c$\degree$)', '', 'gallery/trend_sla_sst.png')
    plot_trend(np.array(df.sla_mean_fixed), np.array(df.chl_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SLA (m)', 'CHL (mg.m$^{-3}$)', '', 'gallery/trend_sla_chl.png')

    '''
    plot_trend(np.array(df.sst_mean_fixed), np.array(df.CO2_mean_surface), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'CO$_2$ (uatm)', '', 'gallery/trend_sst_co2.png')

    return

def track_trend(df):
    ########################## Lifetime trends ##########################
    plot_trend(np.array(df.lifetime), np.array(df.mean_velocity), 'o', 6, [0.4, 0.1, 0.8], 'Lifetime (day)', 'Mean Velocity (km/day)', '', 'gallery/trend_lifetime_mean_velocity.png')
    plot_trend(np.array(df.lifetime), np.array(df.propagation), 'o', 6, [0.4, 0.1, 0.8], 'Lifetime (day)', 'Propagation (km)', '', 'gallery/trend_lifetime_propagation.png')
    return


def attribute_trend(df):
    ##################### characteristic trends #####################
    plot_trend(np.array(df.lat), np.array(df.radius), 'o', 6, [0.4, 0.1, 0.8], 'Latitude ($\degree$)', 'Radius (km)', '', 'gallery/trend_lat_radius.png')
    plot_trend(np.array(df.velocity), np.array(df.lat), 'o', 6, [0.4, 0.1, 0.8], 'Velocity (km/day)', 'Latitude ($\degree$)', '', 'gallery/trend_velocity_lat.png')
    plot_trend(np.array(df.velocity), np.array(df.radius), 'o', 6, [0.4, 0.1, 0.8], 'Velocity (km/day)', 'Radius (km)', '', 'gallery/trend_velocity_radius.png')
    plot_trend(np.array(df.acceleration), np.array(df.radius), 'o', 6, [0.4, 0.1, 0.8], 'acceleration (km.day$^{-2}$)', 'Radius (km)', '', 'gallery/trend_acceleration_radius.png')

    plot_trend(np.array(df.days_to_go), np.array(df.velocity), 'o', 6, [0.4, 0.1, 0.8], 'Remaining Life (day)', 'Velocity (km/day)', '', 'gallery/trend_remaining_days_velocity.png')
    plot_trend(np.array(df.days_to_go), np.array(df.acceleration), 'o', 6, [0.4, 0.1, 0.8], 'Remaining Life (day)', 'Acceleration (km.day$^{-2}$)', '', 'gallery/trend_remaining_days_acceleration.png')
    plot_trend(np.array(df.age_percentile), np.array(df.velocity), 'o', 6, [0.4, 0.1, 0.8], 'Age Percentile', 'Velocity (km/day)', '', 'gallery/trend_age_percentile_velocity.png')
    plot_trend(np.array(df.age_percentile), np.array(df.acceleration), 'o', 6, [0.4, 0.1, 0.8], 'Age Percentile', 'Acceleration (km.day$^{-2}$)', '', 'gallery/trend_age_percentile_acceleration.png')

    
    ########################## vort trends ##########################
    plot_hex_trend(np.array(df.vort_mean_fixed), np.array(df.sst_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'SST (c$\degree$)', '', 'gallery/trend_vort_sst_hex.png', 50)

    plot_trend(np.array(df.vort_mean_fixed), np.array(df.phase_integ_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'Phase Integral ($\degree$)', '', 'gallery/trend_vort_phase.png')
    plot_trend(np.array(df.vort_mean_fixed), np.array(df.sla_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'SLA (m)', '', 'gallery/trend_vort_sla.png')
    plot_trend(np.array(df.vort_mean_fixed), np.array(df.displacement_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'Displacement ($\delta\degree$)', '', 'gallery/trend_vort_displacement.png')
    plot_trend(np.array(df.vort_mean_fixed), np.array(df.ftle_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'FTLE (day$^{-1}$)', '', 'gallery/trend_vort_ftle.png')
    plot_trend(np.array(df.vort_mean_fixed), np.array(df.sst_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'SST (c$\degree$)', '', 'gallery/trend_vort_sst.png')
    plot_trend(np.array(df.vort_mean_fixed), np.array(df.chl_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'Vorticity (s$^{-1}$)', 'CHL (mg.m$^{-3}$)', '', 'gallery/trend_vort_chl.png')
    
    '''
    ########################## SLA trends ##########################
    plot_trend(np.array(df.sla_mean_fixed), np.array(df.phase_integ_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SLA (m)', 'Phase Integral ($\degree$)', '', 'gallery/trend_sla_phase.png')
    plot_trend(np.array(df.sla_mean_fixed), np.array(df.vort_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SLA (m)', 'Vorticity (s$^{-1}$)', '', 'gallery/trend_sla_vort.png')
    plot_trend(np.array(df.sla_mean_fixed), np.array(df.displacement_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SLA (m)', 'Displacement ($\delta\degree$)', '', 'gallery/trend_sla_displacement.png')
    plot_trend(np.array(df.sla_mean_fixed), np.array(df.ftle_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SLA (m)', 'FTLE (day$^{-1}$)', '', 'gallery/trend_sla_ftle.png')
    plot_trend(np.array(df.sla_mean_fixed), np.array(df.sst_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SLA (m)', 'SST (c$\degree$)', '', 'gallery/trend_sla_sst.png')
    plot_trend(np.array(df.sla_mean_fixed), np.array(df.chl_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SLA (m)', 'CHL (mg.m$^{-3}$)', '', 'gallery/trend_sla_chl.png')

    ########################## CHL trends ##########################
    plot_trend(chl, np.array(df.phase_integ_fixed), 'o', 6, [0.4, 0.1, 0.8], 'CHL (mg.m$^{-3}$)', 'Phase Integral ($\degree$)', '', 'gallery/trend_chl_phase.png')
    plot_trend(chl, np.array(df.sla_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'CHL (mg.m$^{-3}$)', 'SLA (m)', '', 'gallery/trend_chl_sla.png')
    plot_trend(chl, np.array(df.vort_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'CHL (mg.m$^{-3}$)', 'Vorticity (s$^{-1}$)', '', 'gallery/trend_chl_vort.png')
    plot_trend(chl, np.array(df.displacement_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'CHL (mg.m$^{-3}$)', 'Displacement ($\delta\degree$)', '', 'gallery/trend_chl_displacement.png')
    plot_trend(chl, np.array(df.ftle_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'CHL (mg.m$^{-3}$)', 'FTLE (day$^{-1}$)', '', 'gallery/trend_chl_ftle.png')
    plot_trend(chl, np.array(df.sst_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'CHL (mg.m$^{-3}$)', 'SST (c$\degree$)', '', 'gallery/trend_chl_sst.png')

    ########################## SST trends ##########################
    plot_trend(np.array(df.sst_mean_fixed), np.array(df.phase_integ_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'Phase Integral ($\degree$)', '', 'gallery/trend_sst_phase.png')
    plot_trend(np.array(df.sst_mean_fixed), np.array(df.sla_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'SLA (m)', '', 'gallery/trend_sst_sla.png')
    plot_trend(np.array(df.sst_mean_fixed), np.array(df.vort_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'Vorticity (s$^{-1}$)', '', 'gallery/trend_sst_vort.png')
    plot_trend(np.array(df.sst_mean_fixed), np.array(df.displacement_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'Displacement ($\delta\degree$)', '', 'gallery/trend_sst_displacement.png')
    plot_trend(np.array(df.sst_mean_fixed), np.array(df.ftle_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'FTLE (day$^{-1}$)', '', 'gallery/trend_sst_ftle.png')
    plot_trend(np.array(df.sst_mean_fixed), np.array(df.chl_mean_fixed), 'o', 6, [0.4, 0.1, 0.8], 'SST (c$\degree$)', 'CHL (mg.m$^{-3}$)', '', 'gallery/trend_sst_chl.png')
    '''
    return

    

def trend(df, dataset):
    if dataset == 'Cores':
        core_trend(df)
    if dataset == 'Tracks':
        track_trend(df)
    return
    


def core_double_hist(df1, df2):

    plot_double_hist(np.array(df1.eddy_radius), np.array(df2.eddy_radius), 'b', 'm', 'Eddy Radius (km)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_radius.png', 50)
    plot_double_hist(np.array(df1.sst_mean_fixed) - np.array(df1.sst_mean_full), np.array(df2.sst_mean_fixed) - np.array(df2.sst_mean_full), 'b', 'm', 'sst_mean_fixed - sst_mean_full (c$\degree$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_sst_mean_fixed_sst_mean_full.png', 50)

    plot_double_hist(np.array(df1.phase_integ_fixed), np.array(df2.phase_integ_fixed), 'b', 'm', 'Phase Integral ($\degree$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_phase.png')
    plot_double_hist(np.array(df1.sla_mean_fixed), np.array(df2.sla_mean_fixed), 'b', 'm', 'SLA (m)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_sla.png')

    plot_double_hist(np.array(df1.sla_mean_fixed - df1.sla_mean_bkg), np.array(df2.sla_mean_fixed - df2.sla_mean_bkg), 'b', 'm', 'SLA Anomally (m)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_sla_anomally.png')

    plot_double_hist(np.array(df1.vort_mean_fixed), np.array(df2.vort_mean_fixed), 'b', 'm', 'Vorticity (s$^{-1}$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_vort.png')
    plot_double_hist(np.array(df1.displacement_mean_fixed), np.array(df2.displacement_mean_fixed), 'b', 'm', 'Displacement ($\delta\degree$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_displacement.png')
    plot_double_hist(np.array(df1.ftle_mean_fixed), np.array(df2.ftle_mean_fixed), 'b', 'm', 'FTLE (day$^{-1}$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_ftle.png')
    plot_double_hist(np.array(df1.sst_mean_fixed), np.array(df2.sst_mean_fixed), 'b', 'm', 'SST (c$\degree$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_sst.png')
    plot_double_hist(zero_to_nan(np.array(df1.chl_mean_fixed)), zero_to_nan(np.array(df2.chl_mean_fixed)), 'b', 'm', 'CHL (mg.m$^{-3}$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_chl.png')

    plot_double_hist(np.array(df1.CO2_mean_surface), np.array(df2.CO2_mean_surface), 'b', 'm', 'CO$_2$ (uatm)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_co2.png', 30)
    plot_double_hist(np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), 'b', 'm', 'CO$_2$ Anomally (uatm)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_co2_anomally.png', 30)

    chl1 = np.array(df1.chl_mean_fixed)
    chl1 = chl1[np.where(chl1 < 0.5)]
    chl2 = np.array(df2.chl_mean_fixed)
    chl2 = chl2[np.where(chl2 < 0.5)]
    plot_double_hist(chl1, chl2, 'b', 'm', 'Filtered CHL (mg.m$^{-3}$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_filtered_chl.png', 100)
    return


def core_double_hist_xlim(df1, df2):
    #plot_double_hist(np.array(df1.mld_mean_fixed-df1.mld_mean_bkg), np.array(df2.mld_mean_fixed-df2.mld_mean_bkg), 'b', 'm', 'Mixed-Layaer Anomally (m)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_mld_ano.png', 50)
    plot_double_hist_xlim(np.array(df1.mld_mean_fixed-df1.mld_mean_bkg), np.array(df2.mld_mean_fixed-df2.mld_mean_bkg), 100, np.linspace(-200, 200, 100), -1, 'b', 'm', 'Mixed-Layaer Anomally (m)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_mld_ano.png')

    chl1 = zero_to_nan(np.array(df1.chl_mean_fixed))
    chl2 = zero_to_nan(np.array(df2.chl_mean_fixed))
    plot_double_hist_xlim((chl1 - np.array(df1.chl_mean_bkg)) / np.array(df1.chl_std_bkg), (chl2 - np.array(df2.chl_mean_bkg)) / np.array(df2.chl_std_bkg), 100, np.linspace(-.75, .75, 100), -1, 'b', 'm', '(chl_mean_fixed - chl_mean_bkg) / chl_std_bkg ($\sigma$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_chl_sig.png')
    plot_double_hist_xlim((np.array(df1.sst_mean_fixed) - np.array(df1.sst_mean_bkg)) / np.array(df1.sst_std_bkg), (np.array(df2.sst_mean_fixed) - np.array(df2.sst_mean_bkg)) / np.array(df2.sst_std_bkg), 100, np.linspace(-.4, .4, 100), -1, 'b', 'm', '(sst_mean_fixed - sst_mean_bkg) / sst_std_bkg ($\sigma$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_sst_sig.png')
    plot_double_hist_xlim((np.array(df1.ftle_mean_fixed) - np.array(df1.ftle_mean_bkg)) / np.array(df1.ftle_std_bkg), (np.array(df2.ftle_mean_fixed) - np.array(df2.ftle_mean_bkg)) / np.array(df2.ftle_std_bkg), 100, np.linspace(-2, 2, 100), -1, 'b', 'm', '(ftle_mean_fixed - ftle_mean_bkg) / ftle_std_bkg ($\sigma$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_ftle_sig.png')
    plot_double_hist_xlim((np.array(df1.displacement_mean_fixed) - np.array(df1.displacement_mean_bkg)) / np.array(df1.displacement_std_bkg), (np.array(df2.displacement_mean_fixed) - np.array(df2.displacement_mean_bkg)) / np.array(df2.displacement_std_bkg), 100, np.linspace(-2, 2, 100), -1, 'b', 'm', '(displacement_mean_fixed - displacement_mean_bkg) / displacement_std_bkg ($\sigma$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_displacement_sig.png')
    plot_double_hist_xlim((np.array(df1.vort_mean_fixed) - np.array(df1.vort_mean_bkg)) / np.array(df1.vort_std_bkg), (np.array(df2.vort_mean_fixed) - np.array(df2.vort_mean_bkg)) / np.array(df2.vort_std_bkg), 200, np.linspace(-100, 100, 200), -1, 'b', 'm', '(vort_mean_fixed - vort_mean_bkg) / vort_std_bkg ($\sigma$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_vort_sig.png')
    plot_double_hist_xlim((np.array(df1.sla_mean_fixed) - np.array(df1.sla_mean_bkg)) / np.array(df1.sla_std_bkg), (np.array(df2.sla_mean_fixed) - np.array(df2.sla_mean_bkg)) / np.array(df2.sla_std_bkg), 100, np.linspace(-5, 5, 100), -1, 'b', 'm', '(sla_mean_fixed - sla_mean_bkg) / sla_std_bkg ($\sigma$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_sla_sig.png')
    plot_double_hist_xlim((np.array(df1.phase_integ_fixed) - np.array(df1.phase_mean_bkg)) / np.array(df1.phase_std_bkg), (np.array(df2.phase_integ_fixed) - np.array(df2.phase_mean_bkg)) / np.array(df2.phase_std_bkg), 100, np.linspace(-3, 3, 100), -1, 'b', 'm', '(phase_integ_fixed - phase_mean_bkg) / phase_std_bkg ($\sigma$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_phase_sig.png')

    #plot_double_hist_xlim(np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), 400, np.linspace(-3, 3, 400), -1, 'b', 'm', 'CO$_2$ Anomally (uatm)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_co2_anomally.png')
    
    return
   
def track_double_hist(df1, df2):
    plot_double_hist(np.array(df1.lifetime), np.array(df2.lifetime), 'b', 'm', 'Lifetime (day)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'log', 'gallery/double_lifetime.png')
    plot_double_hist(np.array(df1.propagation), np.array(df2.propagation), 'b', 'm', 'Propagation (km)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'log', 'gallery/double_propagation.png')
    plot_double_hist(np.array(df1.mean_velocity), np.array(df2.mean_velocity), 'b', 'm', 'Mean Velocity (km/day)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_mean_velocity.png')
    return


def attribute_double_hist(df1, df2):
    plot_double_hist(np.array(df1.radius), np.array(df2.radius), 'b', 'm', 'Eddy Radius (km)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_radius.png', 50)

    plot_double_hist(np.array(df1.phase_integ_fixed), np.array(df2.phase_integ_fixed), 'b', 'm', 'Phase Integral ($\degree$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_phase.png')
    plot_double_hist(np.array(df1.sla_mean_fixed), np.array(df2.sla_mean_fixed), 'b', 'm', 'SLA (m)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_sla.png')
    plot_double_hist(np.array(df1.vort_mean_fixed), np.array(df2.vort_mean_fixed), 'b', 'm', 'Vorticity (s$^{-1}$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_vort.png')
    plot_double_hist(np.array(df1.displacement_mean_fixed), np.array(df2.displacement_mean_fixed), 'b', 'm', 'Displacement ($\delta\degree$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_displacement.png')
    plot_double_hist(np.array(df1.ftle_mean_fixed), np.array(df2.ftle_mean_fixed), 'b', 'm', 'FTLE (day$^{-1}$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_ftle.png')
    plot_double_hist(np.array(df1.sst_mean_fixed), np.array(df2.sst_mean_fixed), 'b', 'm', 'SST (c$\degree$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_sst.png')
    plot_double_hist(np.array(df1.chl_mean_fixed), np.array(df2.chl_mean_fixed), 'b', 'm', 'CHL (mg.m$^{-3}$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_chl.png')

    chl1 = np.array(df1.chl_mean_fixed)
    chl1 = chl1[np.where(chl1 < 0.5)]
    chl2 = np.array(df2.chl_mean_fixed)
    chl2 = chl2[np.where(chl2 < 0.5)]
    plot_double_hist(chl1, chl2, 'b', 'm', 'Filtered CHL (mg.m$^{-3}$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_filtered_chl.png', 30)
    return


def double_hist(df1, df2, dataset):
    if dataset == 'Cores':
      core_double_hist_xlim(df1, df2)       # Significance plots (against background)
      core_double_hist(df1, df2)  
    if dataset == 'Tracks':
      track_double_hist(df1, df2)  
    return


def join_attribute(query):
    sp = query.split()
    index = sp.index('tblTracks') + 1
    sp.insert(index, 'JOIN tblAttributes ON track_id=track_id_attributes')
    result = ' '.join(sp)
    return result


def mid_range(dist, mid_method):
    dist = np.array(dist)

    try:
        n = len(dist[~np.isnan(dist)])
    except:
        n = np.nan
        
    try:
        if mid_method == 0:
            std = 2 * np.nanstd(dist)   ## 2sigma effect (95%)
            mid = np.nanmean(dist)            
            up = mid + std / math.sqrt(n)
            down = mid - std / math.sqrt(n)
        elif mid_method == 1:
            mid = np.nanmedian(dist)        
            up = np.nanpercentile(dist, 75)
            down = np.nanpercentile(dist, 25)
    except:
        mid = np.nan
        up = np.nan
        down = np.nan        
    return mid, up, down



def append_range(vals, vals_up, vals_down, dist, mid_method=1):
    mid_method = 0
    mid, up, down = mid_range(dist, mid_method)
    vals = np.append(vals, mid)
    vals_up = np.append(vals_up, up)
    vals_down = np.append(vals_down, down)
    return vals, vals_up, vals_down


def monthly_series(query, error_band):
    if query.find('WHERE') >= 0:
        query1 = query + ' AND eddy_polarity=1'
        query2 = query + ' AND eddy_polarity=-1'
    else:
        query1 = query + ' WHERE eddy_polarity=1'
        query2 = query + ' WHERE eddy_polarity=-1'

    cyc_n = np.array([])
    cyc_n_up = np.array([])
    cyc_n_down = np.array([])
    lat = np.array([])
    lat_up = np.array([])
    lat_down = np.array([])
    lon = np.array([])
    lon_up = np.array([])
    lon_down = np.array([])
    radius = np.array([])
    radius_up = np.array([])
    radius_down = np.array([])
    phase = np.array([])
    phase_up = np.array([])
    phase_down = np.array([])
    sla = np.array([])
    sla_up = np.array([])
    sla_down = np.array([])
    vort = np.array([])
    vort_up = np.array([])
    vort_down = np.array([])
    disp = np.array([])
    disp_up = np.array([])
    disp_down = np.array([])
    ftle = np.array([])
    ftle_up = np.array([])
    ftle_down = np.array([])
    sst = np.array([])
    sst_up = np.array([])
    sst_down = np.array([])
    chl = np.array([])
    chl_up = np.array([])
    chl_down = np.array([])
    co2 = np.array([])
    co2_up = np.array([])
    co2_down = np.array([])
    mld = np.array([])
    mld_up = np.array([])
    mld_down = np.array([])
    sss = np.array([])
    sss_up = np.array([])
    sss_down = np.array([])

    ano_phase = np.array([])
    ano_phase_up = np.array([])
    ano_phase_down = np.array([])
    ano_sla = np.array([])
    ano_sla_up = np.array([])
    ano_sla_down = np.array([])
    ano_vort = np.array([])
    ano_vort_up = np.array([])
    ano_vort_down = np.array([])
    ano_disp = np.array([])
    ano_disp_up = np.array([])
    ano_disp_down = np.array([])
    ano_ftle = np.array([])
    ano_ftle_up = np.array([])
    ano_ftle_down = np.array([])
    ano_sst = np.array([])
    ano_sst_up = np.array([])
    ano_sst_down = np.array([])
    ano_chl = np.array([])
    ano_chl_up = np.array([])
    ano_chl_down = np.array([])
    ano_co2 = np.array([])
    ano_co2_up = np.array([])
    ano_co2_down = np.array([])
    ano_mld = np.array([])
    ano_mld_up = np.array([])
    ano_mld_down = np.array([])
    ano_sss = np.array([])
    ano_sss_up = np.array([])
    ano_sss_down = np.array([])


    anti_cyc_n = np.array([])
    anti_cyc_n_up = np.array([])
    anti_cyc_n_down = np.array([])
    anti_lat = np.array([])
    anti_lat_up = np.array([])
    anti_lat_down = np.array([])
    anti_lon = np.array([])
    anti_lon_up = np.array([])
    anti_lon_down = np.array([])
    anti_radius = np.array([])
    anti_radius_up = np.array([])
    anti_radius_down = np.array([])
    anti_phase = np.array([])
    anti_phase_up = np.array([])
    anti_phase_down = np.array([])
    anti_sla = np.array([])
    anti_sla_up = np.array([])
    anti_sla_down = np.array([])
    anti_vort = np.array([])
    anti_vort_up = np.array([])
    anti_vort_down = np.array([])
    anti_disp = np.array([])
    anti_disp_up = np.array([])
    anti_disp_down = np.array([])
    anti_ftle = np.array([])
    anti_ftle_up = np.array([])
    anti_ftle_down = np.array([])
    anti_sst = np.array([])
    anti_sst_up = np.array([])
    anti_sst_down = np.array([])
    anti_chl = np.array([])
    anti_chl_up = np.array([])
    anti_chl_down = np.array([])
    anti_co2 = np.array([])
    anti_co2_up = np.array([])
    anti_co2_down = np.array([])
    anti_mld = np.array([])
    anti_mld_up = np.array([])
    anti_mld_down = np.array([])
    anti_sss = np.array([])
    anti_sss_up = np.array([])
    anti_sss_down = np.array([])

    anti_ano_phase = np.array([])
    anti_ano_phase_up = np.array([])
    anti_ano_phase_down = np.array([])
    anti_ano_sla = np.array([])
    anti_ano_sla_up = np.array([])
    anti_ano_sla_down = np.array([])
    anti_ano_vort = np.array([])
    anti_ano_vort_up = np.array([])
    anti_ano_vort_down = np.array([])
    anti_ano_disp = np.array([])
    anti_ano_disp_up = np.array([])
    anti_ano_disp_down = np.array([])
    anti_ano_ftle = np.array([])
    anti_ano_ftle_up = np.array([])
    anti_ano_ftle_down = np.array([])
    anti_ano_sst = np.array([])
    anti_ano_sst_up = np.array([])
    anti_ano_sst_down = np.array([])
    anti_ano_chl = np.array([])
    anti_ano_chl_up = np.array([])
    anti_ano_chl_down = np.array([])
    anti_ano_co2 = np.array([])
    anti_ano_co2_up = np.array([])
    anti_ano_co2_down = np.array([])
    anti_ano_mld = np.array([])
    anti_ano_mld_up = np.array([])
    anti_ano_mld_down = np.array([])
    anti_ano_sss = np.array([])
    anti_ano_sss_up = np.array([])
    anti_ano_sss_down = np.array([])

    query11 = str(query1)
    query22 = str(query2)
    month1 = 1
    month2 = 12
    
    for month in range(month1, month2+1):

        #m = [7,8,9,10,11,12,1,2,3,4,5,6]
        #month = m[month-1]        
        
        query1 = query11 + ' AND month=' + str(month)
        query2 = query22 + ' AND month=' + str(month)
        
        conn = db_connect()
        df1 = sql.read_sql(query1, conn)
        conn.close()
        conn = db_connect()
        df2 = sql.read_sql(query2, conn)
        conn.close()
        
        df1 = df1.fillna(float('NaN'))
        df2 = df2.fillna(float('NaN'))
                
        '''
        #############  fixed radius
        cyc_n, cyc_n_up, cyc_n_down = append_range(cyc_n, cyc_n_up, cyc_n_down, len(np.array(df1.year)))
        lat, lat_up, lat_down = append_range(lat, lat_up, lat_down, df1.eddy_lat)
        lon, lon_up, lon_down = append_range(lon, lon_up, lon_down, df1.eddy_lon)
        radius, radius_up, radius_down = append_range(radius, radius_up, radius_down, df1.eddy_radius)
        phase, phase_up, phase_down = append_range(phase, phase_up, phase_down, df1.phase_integ_fixed)
        sla, sla_up, sla_down = append_range(sla, sla_up, sla_down, df1.sla_mean_fixed)
        vort, vort_up, vort_down = append_range(vort, vort_up, vort_down, df1.vort_mean_fixed)
        disp, disp_up, disp_down = append_range(disp, disp_up, disp_down, df1.displacement_mean_fixed)
        ftle, ftle_up, ftle_down = append_range(ftle, ftle_up, ftle_down, df1.ftle_mean_fixed)
        sst, sst_up, sst_down = append_range(sst, sst_up, sst_down, df1.sst_mean_fixed)
        chl, chl_up, chl_down = append_range(chl, chl_up, chl_down, df1.chl_mean_fixed)
        co2, co2_up, co2_down = append_range(co2, co2_up, co2_down, df1.CO2_mean_surface)
        mld, mld_up, mld_down = append_range(mld, mld_up, mld_down, df1.mld_mean_fixed)
        sss, sss_up, sss_down = append_range(sss, sss_up, sss_down, df1.sss_mean_fixed)
        
        ano_phase, ano_phase_up, ano_phase_down = append_range(ano_phase, ano_phase_up, ano_phase_down, df1.phase_integ_fixed - df1.phase_mean_bkg)
        ano_sla, ano_sla_up, ano_sla_down = append_range(ano_sla, ano_sla_up, ano_sla_down, df1.sla_mean_fixed - df1.sla_mean_bkg)
        ano_vort, ano_vort_up, ano_vort_down = append_range(ano_vort, ano_vort_up, ano_vort_down, df1.vort_mean_fixed - df1.vort_mean_bkg)
        ano_disp, ano_disp_up, ano_disp_down = append_range(ano_disp, ano_disp_up, ano_disp_down, df1.displacement_mean_fixed - df1.displacement_mean_bkg)
        ano_ftle, ano_ftle_up, ano_ftle_down = append_range(ano_ftle, ano_ftle_up, ano_ftle_down, df1.ftle_mean_fixed - df1.ftle_mean_bkg)
        ano_sst, ano_sst_up, ano_sst_down = append_range(ano_sst, ano_sst_up, ano_sst_down, df1.sst_mean_fixed - df1.sst_mean_bkg)
        ano_chl, ano_chl_up, ano_chl_down = append_range(ano_chl, ano_chl_up, ano_chl_down, df1.chl_mean_fixed - df1.chl_mean_bkg)
        ano_co2, ano_co2_up, ano_co2_down = append_range(ano_co2, ano_co2_up, ano_co2_down, df1.CO2_mean_surface - df1.CO2_mean_surface_bkg)
        ano_mld, ano_mld_up, ano_mld_down = append_range(ano_mld, ano_mld_up, ano_mld_down, df1.mld_mean_fixed - df1.mld_mean_bkg)
        ano_sss, ano_sss_up, ano_sss_down = append_range(ano_sss, ano_sss_up, ano_sss_down, df1.sss_mean_fixed - df1.sss_mean_bkg)
        
        
        anti_cyc_n, anti_cyc_n_up, anti_cyc_n_down = append_range(anti_cyc_n, anti_cyc_n_up, anti_cyc_n_down, len(np.array(df2.year)))
        anti_lat, anti_lat_up, anti_lat_down = append_range(anti_lat, anti_lat_up, anti_lat_down, df2.eddy_lat)
        anti_lon, anti_lon_up, anti_lon_down = append_range(anti_lon, anti_lon_up, anti_lon_down, df2.eddy_lon)
        anti_radius, anti_radius_up, anti_radius_down = append_range(anti_radius, anti_radius_up, anti_radius_down, df2.eddy_radius)
        anti_phase, anti_phase_up, anti_phase_down = append_range(anti_phase, anti_phase_up, anti_phase_down, df2.phase_integ_fixed)
        anti_sla, anti_sla_up, anti_sla_down = append_range(anti_sla, anti_sla_up, anti_sla_down, df2.sla_mean_fixed)
        anti_vort, anti_vort_up, anti_vort_down = append_range(anti_vort, anti_vort_up, anti_vort_down, df2.vort_mean_fixed)
        anti_disp, anti_disp_up, anti_disp_down = append_range(anti_disp, anti_disp_up, anti_disp_down, df2.displacement_mean_fixed)
        anti_ftle, anti_ftle_up, anti_ftle_down = append_range(anti_ftle, anti_ftle_up, anti_ftle_down, df2.ftle_mean_fixed)
        anti_sst, anti_sst_up, anti_sst_down = append_range(anti_sst, anti_sst_up, anti_sst_down, df2.sst_mean_fixed)
        anti_chl, anti_chl_up, anti_chl_down = append_range(anti_chl, anti_chl_up, anti_chl_down, df2.chl_mean_fixed)
        anti_co2, anti_co2_up, anti_co2_down = append_range(anti_co2, anti_co2_up, anti_co2_down, df2.CO2_mean_surface)
        anti_mld, anti_mld_up, anti_mld_down = append_range(anti_mld, anti_mld_up, anti_mld_down, df2.mld_mean_fixed)
        anti_sss, anti_sss_up, anti_sss_down = append_range(anti_sss, anti_sss_up, anti_sss_down, df2.sss_mean_fixed)


        anti_ano_phase, anti_ano_phase_up, anti_ano_phase_down = append_range(anti_ano_phase, anti_ano_phase_up, anti_ano_phase_down, df2.phase_integ_fixed - df2.phase_mean_bkg)
        anti_ano_sla, anti_ano_sla_up, anti_ano_sla_down = append_range(anti_ano_sla, anti_ano_sla_up, anti_ano_sla_down, df2.sla_mean_fixed - df2.sla_mean_bkg)
        anti_ano_vort, anti_ano_vort_up, anti_ano_vort_down = append_range(anti_ano_vort, anti_ano_vort_up, anti_ano_vort_down, df2.vort_mean_fixed - df2.vort_mean_bkg)
        anti_ano_disp, anti_ano_disp_up, anti_ano_disp_down = append_range(anti_ano_disp, anti_ano_disp_up, anti_ano_disp_down, df2.displacement_mean_fixed - df2.displacement_mean_bkg)
        anti_ano_ftle, anti_ano_ftle_up, anti_ano_ftle_down = append_range(anti_ano_ftle, anti_ano_ftle_up, anti_ano_ftle_down, df2.ftle_mean_fixed - df2.ftle_mean_bkg)
        anti_ano_sst, anti_ano_sst_up, anti_ano_sst_down = append_range(anti_ano_sst, anti_ano_sst_up, anti_ano_sst_down, df2.sst_mean_fixed - df2.sst_mean_bkg)
        anti_ano_chl, anti_ano_chl_up, anti_ano_chl_down = append_range(anti_ano_chl, anti_ano_chl_up, anti_ano_chl_down, df2.chl_mean_fixed - df2.chl_mean_bkg)
        anti_ano_co2, anti_ano_co2_up, anti_ano_co2_down = append_range(anti_ano_co2, anti_ano_co2_up, anti_ano_co2_down, df2.CO2_mean_surface - df2.CO2_mean_surface_bkg)
        anti_ano_mld, anti_ano_mld_up, anti_ano_mld_down = append_range(anti_ano_mld, anti_ano_mld_up, anti_ano_mld_down, df2.mld_mean_fixed - df2.mld_mean_bkg)
        anti_ano_sss, anti_ano_sss_up, anti_ano_sss_down = append_range(anti_ano_sss, anti_ano_sss_up, anti_ano_sss_down, df2.sss_mean_fixed - df2.sss_mean_bkg)
        '''    
        


        #############  full radius
        cyc_n, cyc_n_up, cyc_n_down = append_range(cyc_n, cyc_n_up, cyc_n_down, len(np.array(df1.year)))
        lat, lat_up, lat_down = append_range(lat, lat_up, lat_down, df1.eddy_lat)
        lon, lon_up, lon_down = append_range(lon, lon_up, lon_down, df1.eddy_lon)
        radius, radius_up, radius_down = append_range(radius, radius_up, radius_down, df1.eddy_radius)
        phase, phase_up, phase_down = append_range(phase, phase_up, phase_down, df1.phase_integ_full)
        sla, sla_up, sla_down = append_range(sla, sla_up, sla_down, df1.sla_mean_full)
        vort, vort_up, vort_down = append_range(vort, vort_up, vort_down, df1.vort_mean_full)
        disp, disp_up, disp_down = append_range(disp, disp_up, disp_down, df1.displacement_mean_full)
        ftle, ftle_up, ftle_down = append_range(ftle, ftle_up, ftle_down, df1.ftle_mean_full)
        sst, sst_up, sst_down = append_range(sst, sst_up, sst_down, df1.sst_mean_full)
        chl, chl_up, chl_down = append_range(chl, chl_up, chl_down, df1.chl_mean_full)
        co2, co2_up, co2_down = append_range(co2, co2_up, co2_down, df1.CO2_mean_surface)
        mld, mld_up, mld_down = append_range(mld, mld_up, mld_down, df1.mld_mean_full)
        sss, sss_up, sss_down = append_range(sss, sss_up, sss_down, df1.sss_mean_full)
        
        ano_phase, ano_phase_up, ano_phase_down = append_range(ano_phase, ano_phase_up, ano_phase_down, df1.phase_integ_full - df1.phase_mean_bkg)
        ano_sla, ano_sla_up, ano_sla_down = append_range(ano_sla, ano_sla_up, ano_sla_down, df1.sla_mean_full - df1.sla_mean_bkg)
        ano_vort, ano_vort_up, ano_vort_down = append_range(ano_vort, ano_vort_up, ano_vort_down, df1.vort_mean_full - df1.vort_mean_bkg)
        ano_disp, ano_disp_up, ano_disp_down = append_range(ano_disp, ano_disp_up, ano_disp_down, df1.displacement_mean_full - df1.displacement_mean_bkg)
        ano_ftle, ano_ftle_up, ano_ftle_down = append_range(ano_ftle, ano_ftle_up, ano_ftle_down, df1.ftle_mean_full - df1.ftle_mean_bkg)
        ano_sst, ano_sst_up, ano_sst_down = append_range(ano_sst, ano_sst_up, ano_sst_down, df1.sst_mean_full - df1.sst_mean_bkg)
        ano_chl, ano_chl_up, ano_chl_down = append_range(ano_chl, ano_chl_up, ano_chl_down, df1.chl_mean_full - df1.chl_mean_bkg)
        ano_co2, ano_co2_up, ano_co2_down = append_range(ano_co2, ano_co2_up, ano_co2_down, df1.CO2_mean_surface - df1.CO2_mean_surface_bkg)
        ano_mld, ano_mld_up, ano_mld_down = append_range(ano_mld, ano_mld_up, ano_mld_down, df1.mld_mean_full - df1.mld_mean_bkg)
        ano_sss, ano_sss_up, ano_sss_down = append_range(ano_sss, ano_sss_up, ano_sss_down, df1.sss_mean_full - df1.sss_mean_bkg)
        
        
        anti_cyc_n, anti_cyc_n_up, anti_cyc_n_down = append_range(anti_cyc_n, anti_cyc_n_up, anti_cyc_n_down, len(np.array(df2.year)))
        anti_lat, anti_lat_up, anti_lat_down = append_range(anti_lat, anti_lat_up, anti_lat_down, df2.eddy_lat)
        anti_lon, anti_lon_up, anti_lon_down = append_range(anti_lon, anti_lon_up, anti_lon_down, df2.eddy_lon)
        anti_radius, anti_radius_up, anti_radius_down = append_range(anti_radius, anti_radius_up, anti_radius_down, df2.eddy_radius)
        anti_phase, anti_phase_up, anti_phase_down = append_range(anti_phase, anti_phase_up, anti_phase_down, df2.phase_integ_full)
        anti_sla, anti_sla_up, anti_sla_down = append_range(anti_sla, anti_sla_up, anti_sla_down, df2.sla_mean_full)
        anti_vort, anti_vort_up, anti_vort_down = append_range(anti_vort, anti_vort_up, anti_vort_down, df2.vort_mean_full)
        anti_disp, anti_disp_up, anti_disp_down = append_range(anti_disp, anti_disp_up, anti_disp_down, df2.displacement_mean_full)
        anti_ftle, anti_ftle_up, anti_ftle_down = append_range(anti_ftle, anti_ftle_up, anti_ftle_down, df2.ftle_mean_full)
        anti_sst, anti_sst_up, anti_sst_down = append_range(anti_sst, anti_sst_up, anti_sst_down, df2.sst_mean_full)
        anti_chl, anti_chl_up, anti_chl_down = append_range(anti_chl, anti_chl_up, anti_chl_down, df2.chl_mean_full)
        anti_co2, anti_co2_up, anti_co2_down = append_range(anti_co2, anti_co2_up, anti_co2_down, df2.CO2_mean_surface)
        anti_mld, anti_mld_up, anti_mld_down = append_range(anti_mld, anti_mld_up, anti_mld_down, df2.mld_mean_full)
        anti_sss, anti_sss_up, anti_sss_down = append_range(anti_sss, anti_sss_up, anti_sss_down, df2.sss_mean_full)


        anti_ano_phase, anti_ano_phase_up, anti_ano_phase_down = append_range(anti_ano_phase, anti_ano_phase_up, anti_ano_phase_down, df2.phase_integ_full - df2.phase_mean_bkg)
        anti_ano_sla, anti_ano_sla_up, anti_ano_sla_down = append_range(anti_ano_sla, anti_ano_sla_up, anti_ano_sla_down, df2.sla_mean_full - df2.sla_mean_bkg)
        anti_ano_vort, anti_ano_vort_up, anti_ano_vort_down = append_range(anti_ano_vort, anti_ano_vort_up, anti_ano_vort_down, df2.vort_mean_full - df2.vort_mean_bkg)
        anti_ano_disp, anti_ano_disp_up, anti_ano_disp_down = append_range(anti_ano_disp, anti_ano_disp_up, anti_ano_disp_down, df2.displacement_mean_full - df2.displacement_mean_bkg)
        anti_ano_ftle, anti_ano_ftle_up, anti_ano_ftle_down = append_range(anti_ano_ftle, anti_ano_ftle_up, anti_ano_ftle_down, df2.ftle_mean_full - df2.ftle_mean_bkg)
        anti_ano_sst, anti_ano_sst_up, anti_ano_sst_down = append_range(anti_ano_sst, anti_ano_sst_up, anti_ano_sst_down, df2.sst_mean_full - df2.sst_mean_bkg)
        anti_ano_chl, anti_ano_chl_up, anti_ano_chl_down = append_range(anti_ano_chl, anti_ano_chl_up, anti_ano_chl_down, df2.chl_mean_full - df2.chl_mean_bkg)
        anti_ano_co2, anti_ano_co2_up, anti_ano_co2_down = append_range(anti_ano_co2, anti_ano_co2_up, anti_ano_co2_down, df2.CO2_mean_surface - df2.CO2_mean_surface_bkg)
        anti_ano_mld, anti_ano_mld_up, anti_ano_mld_down = append_range(anti_ano_mld, anti_ano_mld_up, anti_ano_mld_down, df2.mld_mean_full - df2.mld_mean_bkg)
        anti_ano_sss, anti_ano_sss_up, anti_ano_sss_down = append_range(anti_ano_sss, anti_ano_sss_up, anti_ano_sss_down, df2.sss_mean_full - df2.sss_mean_bkg)
        
        
    month = range(month1, month2+1)    
    plot_double_trend(month, cyc_n, cyc_n_up, cyc_n_down, month, anti_cyc_n, anti_cyc_n_up, anti_cyc_n_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'Count', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_count.png')
    plot_double_trend(month, lat, lat_up, lat_down, month, anti_lat, anti_lat_up, anti_lat_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'Latitude ($\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_lat.png')
    plot_double_trend(month, lon, lon_up, lon_down, month, anti_lon, anti_lon_up, anti_lon_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'Longitude ($\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_lon.png')
    plot_double_trend(month, radius, radius_up, radius_down, month, anti_radius, anti_radius_up, anti_radius_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'Radius (km)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_radius.png')
    plot_double_trend(month, phase, phase_up, phase_down, month, anti_phase, anti_phase_up, anti_phase_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'Phase Integral ($\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_phase.png')
    plot_double_trend(month, sla, sla_up, sla_down, month, anti_sla, anti_sla_up, anti_sla_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'SLA (m)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_sla.png')
    plot_double_trend(month, vort, vort_up, vort_down, month, anti_vort, anti_vort_up, anti_vort_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'Relative Vorticity ($s^{-1}$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_vort.png')
    plot_double_trend(month, disp, disp_up, disp_down, month, anti_disp, anti_disp_up, anti_disp_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'Lag. Displacement ($\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_disp.png')
    plot_double_trend(month, ftle, ftle_up, ftle_down, month, anti_ftle, anti_ftle_up, anti_ftle_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'FTLE (day$^{-1}$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ftle.png')
    plot_double_trend(month, sst, sst_up, sst_down, month, anti_sst, anti_sst_up, anti_sst_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'SST (c$\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_sst.png')
    plot_double_trend(month, chl, chl_up, chl_down, month, anti_chl, anti_chl_up, anti_chl_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'CHL (mg.m$^{-3}$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_chl.png')
    plot_double_trend(month, co2, co2_up, co2_down, month, anti_co2, anti_co2_up, anti_co2_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'fCO$_2$ ($\mu$atm)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_co2.png')
    plot_double_trend(month, mld, mld_up, mld_down, month, anti_mld, anti_mld_up, anti_mld_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'MLD (m)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_mld.png')
    plot_double_trend(month, sss, sss_up, sss_down, month, anti_sss, anti_sss_up, anti_sss_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'Salinity (PSU)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_sss.png')


    plot_double_trend(month, ano_phase, ano_phase_up, ano_phase_down, month, anti_ano_phase, anti_ano_phase_up, anti_ano_phase_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'Phase Integral Anamolly ($\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_phase.png')
    plot_double_trend(month, ano_sla, ano_sla_up, ano_sla_down, month, anti_ano_sla, anti_ano_sla_up, anti_ano_sla_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'SLA Anomally (m)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_sla.png')
    plot_double_trend(month, ano_vort, ano_vort_up, ano_vort_down, month, anti_ano_vort, anti_ano_vort_up, anti_ano_vort_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'Relative Vorticity Anomally ($s^{-1}$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_vort.png')
    plot_double_trend(month, ano_disp, ano_disp_up, ano_disp_down, month, anti_ano_disp, anti_ano_disp_up, anti_ano_disp_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'Lag. Displacement Anomally ($\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_disp.png')
    plot_double_trend(month, ano_ftle, ano_ftle_up, ano_ftle_down, month, anti_ano_ftle, anti_ano_ftle_up, anti_ano_ftle_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'FTLE Anomally (day$^{-1}$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_ftle.png')
    plot_double_trend(month, ano_sst, ano_sst_up, ano_sst_down, month, anti_ano_sst, anti_ano_sst_up, anti_ano_sst_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'SST Anomally ($\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_sst.png')
    plot_double_trend(month, ano_chl, ano_chl_up, ano_chl_down, month, anti_ano_chl, anti_ano_chl_up, anti_ano_chl_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'CHL Anomally (mg.m$^{-3}$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_chl.png')
    plot_double_trend(month, ano_co2, ano_co2_up, ano_co2_down, month, anti_ano_co2, anti_ano_co2_up, anti_ano_co2_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'CO2 Anomally ($\mu$atm)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_co2.png')
    plot_double_trend(month, ano_mld, ano_mld_up, ano_mld_down, month, anti_ano_mld, anti_ano_mld_up, anti_ano_mld_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'MLD Anomally (m)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_mld.png')
    plot_double_trend(month, ano_sss, ano_sss_up, ano_sss_down, month, anti_ano_sss, anti_ano_sss_up, anti_ano_sss_down, error_band, 'o--', 6, 'c', 'm', 'Month', 'Salinity Anomally (PSU)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_sss.png')

    return    



def yearly_series(query, error_band):
    if query.find('WHERE') >= 0:
        query1 = query + ' AND eddy_polarity=1'
        query2 = query + ' AND eddy_polarity=-1'
    else:
        query1 = query + ' WHERE eddy_polarity=1'
        query2 = query + ' WHERE eddy_polarity=-1'

    cyc_n = np.array([])
    cyc_n_up = np.array([])
    cyc_n_down = np.array([])
    lat = np.array([])
    lat_up = np.array([])
    lat_down = np.array([])
    lon = np.array([])
    lon_up = np.array([])
    lon_down = np.array([])
    radius = np.array([])
    radius_up = np.array([])
    radius_down = np.array([])
    phase = np.array([])
    phase_up = np.array([])
    phase_down = np.array([])
    sla = np.array([])
    sla_up = np.array([])
    sla_down = np.array([])
    vort = np.array([])
    vort_up = np.array([])
    vort_down = np.array([])
    disp = np.array([])
    disp_up = np.array([])
    disp_down = np.array([])
    ftle = np.array([])
    ftle_up = np.array([])
    ftle_down = np.array([])
    sst = np.array([])
    sst_up = np.array([])
    sst_down = np.array([])
    chl = np.array([])
    chl_up = np.array([])
    chl_down = np.array([])
    co2 = np.array([])
    co2_up = np.array([])
    co2_down = np.array([])
    mld = np.array([])
    mld_up = np.array([])
    mld_down = np.array([])
    sss = np.array([])
    sss_up = np.array([])
    sss_down = np.array([])

    ano_phase = np.array([])
    ano_phase_up = np.array([])
    ano_phase_down = np.array([])
    ano_sla = np.array([])
    ano_sla_up = np.array([])
    ano_sla_down = np.array([])
    ano_vort = np.array([])
    ano_vort_up = np.array([])
    ano_vort_down = np.array([])
    ano_disp = np.array([])
    ano_disp_up = np.array([])
    ano_disp_down = np.array([])
    ano_ftle = np.array([])
    ano_ftle_up = np.array([])
    ano_ftle_down = np.array([])
    ano_sst = np.array([])
    ano_sst_up = np.array([])
    ano_sst_down = np.array([])
    ano_chl = np.array([])
    ano_chl_up = np.array([])
    ano_chl_down = np.array([])
    ano_co2 = np.array([])
    ano_co2_up = np.array([])
    ano_co2_down = np.array([])
    ano_mld = np.array([])
    ano_mld_up = np.array([])
    ano_mld_down = np.array([])
    ano_sss = np.array([])
    ano_sss_up = np.array([])
    ano_sss_down = np.array([])


    anti_cyc_n = np.array([])
    anti_cyc_n_up = np.array([])
    anti_cyc_n_down = np.array([])
    anti_lat = np.array([])
    anti_lat_up = np.array([])
    anti_lat_down = np.array([])
    anti_lon = np.array([])
    anti_lon_up = np.array([])
    anti_lon_down = np.array([])
    anti_radius = np.array([])
    anti_radius_up = np.array([])
    anti_radius_down = np.array([])
    anti_phase = np.array([])
    anti_phase_up = np.array([])
    anti_phase_down = np.array([])
    anti_sla = np.array([])
    anti_sla_up = np.array([])
    anti_sla_down = np.array([])
    anti_vort = np.array([])
    anti_vort_up = np.array([])
    anti_vort_down = np.array([])
    anti_disp = np.array([])
    anti_disp_up = np.array([])
    anti_disp_down = np.array([])
    anti_ftle = np.array([])
    anti_ftle_up = np.array([])
    anti_ftle_down = np.array([])
    anti_sst = np.array([])
    anti_sst_up = np.array([])
    anti_sst_down = np.array([])
    anti_chl = np.array([])
    anti_chl_up = np.array([])
    anti_chl_down = np.array([])
    anti_co2 = np.array([])
    anti_co2_up = np.array([])
    anti_co2_down = np.array([])
    anti_mld = np.array([])
    anti_mld_up = np.array([])
    anti_mld_down = np.array([])
    anti_sss = np.array([])
    anti_sss_up = np.array([])
    anti_sss_down = np.array([])

    anti_ano_phase = np.array([])
    anti_ano_phase_up = np.array([])
    anti_ano_phase_down = np.array([])
    anti_ano_sla = np.array([])
    anti_ano_sla_up = np.array([])
    anti_ano_sla_down = np.array([])
    anti_ano_vort = np.array([])
    anti_ano_vort_up = np.array([])
    anti_ano_vort_down = np.array([])
    anti_ano_disp = np.array([])
    anti_ano_disp_up = np.array([])
    anti_ano_disp_down = np.array([])
    anti_ano_ftle = np.array([])
    anti_ano_ftle_up = np.array([])
    anti_ano_ftle_down = np.array([])
    anti_ano_sst = np.array([])
    anti_ano_sst_up = np.array([])
    anti_ano_sst_down = np.array([])
    anti_ano_chl = np.array([])
    anti_ano_chl_up = np.array([])
    anti_ano_chl_down = np.array([])
    anti_ano_co2 = np.array([])
    anti_ano_co2_up = np.array([])
    anti_ano_co2_down = np.array([])
    anti_ano_mld = np.array([])
    anti_ano_mld_up = np.array([])
    anti_ano_mld_down = np.array([])
    anti_ano_sss = np.array([])
    anti_ano_sss_up = np.array([])
    anti_ano_sss_down = np.array([])


    query11 = str(query1)
    query22 = str(query2)
    year1 = 2003
    year2 = 2015
    
    for year in range(year1, year2+1):
        query1 = query11 + ' AND year=' + str(year)
        query2 = query22 + ' AND year=' + str(year)
        
        conn = db_connect()
        df1 = sql.read_sql(query1, conn)
        conn.close()
        conn = db_connect()
        df2 = sql.read_sql(query2, conn)
        conn.close()
        
        df1 = df1.fillna(float('NaN'))
        df2 = df2.fillna(float('NaN'))
        
        '''
        #################################################
        # This should only be used to reverse the vorticity signs of the NH eddies in order to calculate the global vorticity mean
        for i in range(0, len(df1)):
            if df1.eddy_lat[i] > 0:
                df1.vort_mean_full[i] = -1 * df1.vort_mean_fixed[i]
                df1.vort_mean_full[i] = -1 * df1.vort_mean_full[i]
                df1.vort_mean_bkg[i] = -1 * df1.vort_mean_bkg[i]
        for i in range(0, len(df2)):
            if df2.eddy_lat[i] > 0:
                df2.vort_mean_full[i] = -1 * df2.vort_mean_fixed[i]
                df2.vort_mean_full[i] = -1 * df2.vort_mean_full[i]
                df2.vort_mean_bkg[i] = -1 * df2.vort_mean_bkg[i]
        #################################################
        '''                
                

        '''
        #############  fixed radius
        cyc_n, cyc_n_up, cyc_n_down = append_range(cyc_n, cyc_n_up, cyc_n_down, len(np.array(df1.year)))
        lat, lat_up, lat_down = append_range(lat, lat_up, lat_down, df1.eddy_lat)
        lon, lon_up, lon_down = append_range(lon, lon_up, lon_down, df1.eddy_lon)
        radius, radius_up, radius_down = append_range(radius, radius_up, radius_down, df1.eddy_radius)
        phase, phase_up, phase_down = append_range(phase, phase_up, phase_down, df1.phase_integ_fixed)
        sla, sla_up, sla_down = append_range(sla, sla_up, sla_down, df1.sla_mean_fixed)
        vort, vort_up, vort_down = append_range(vort, vort_up, vort_down, df1.vort_mean_fixed)
        disp, disp_up, disp_down = append_range(disp, disp_up, disp_down, df1.displacement_mean_fixed)
        ftle, ftle_up, ftle_down = append_range(ftle, ftle_up, ftle_down, df1.ftle_mean_fixed)
        sst, sst_up, sst_down = append_range(sst, sst_up, sst_down, df1.sst_mean_fixed)
        chl, chl_up, chl_down = append_range(chl, chl_up, chl_down, df1.chl_mean_fixed)
        co2, co2_up, co2_down = append_range(co2, co2_up, co2_down, df1.CO2_mean_surface)
        mld, mld_up, mld_down = append_range(mld, mld_up, mld_down, df1.mld_mean_fixed)
        sss, sss_up, sss_down = append_range(sss, sss_up, sss_down, df1.sss_mean_fixed)
        
        ano_phase, ano_phase_up, ano_phase_down = append_range(ano_phase, ano_phase_up, ano_phase_down, df1.phase_integ_fixed - df1.phase_mean_bkg)
        ano_sla, ano_sla_up, ano_sla_down = append_range(ano_sla, ano_sla_up, ano_sla_down, df1.sla_mean_fixed - df1.sla_mean_bkg)
        ano_vort, ano_vort_up, ano_vort_down = append_range(ano_vort, ano_vort_up, ano_vort_down, df1.vort_mean_fixed - df1.vort_mean_bkg)
        ano_disp, ano_disp_up, ano_disp_down = append_range(ano_disp, ano_disp_up, ano_disp_down, df1.displacement_mean_fixed - df1.displacement_mean_bkg)
        ano_ftle, ano_ftle_up, ano_ftle_down = append_range(ano_ftle, ano_ftle_up, ano_ftle_down, df1.ftle_mean_fixed - df1.ftle_mean_bkg)
        ano_sst, ano_sst_up, ano_sst_down = append_range(ano_sst, ano_sst_up, ano_sst_down, df1.sst_mean_fixed - df1.sst_mean_bkg)
        ano_chl, ano_chl_up, ano_chl_down = append_range(ano_chl, ano_chl_up, ano_chl_down, df1.chl_mean_fixed - df1.chl_mean_bkg)
        ano_co2, ano_co2_up, ano_co2_down = append_range(ano_co2, ano_co2_up, ano_co2_down, df1.CO2_mean_surface - df1.CO2_mean_surface_bkg)
        ano_mld, ano_mld_up, ano_mld_down = append_range(ano_mld, ano_mld_up, ano_mld_down, df1.mld_mean_fixed - df1.mld_mean_bkg)
        ano_sss, ano_sss_up, ano_sss_down = append_range(ano_sss, ano_sss_up, ano_sss_down, df1.sss_mean_fixed - df1.sss_mean_bkg)
        
        
        anti_cyc_n, anti_cyc_n_up, anti_cyc_n_down = append_range(anti_cyc_n, anti_cyc_n_up, anti_cyc_n_down, len(np.array(df2.year)))
        anti_lat, anti_lat_up, anti_lat_down = append_range(anti_lat, anti_lat_up, anti_lat_down, df2.eddy_lat)
        anti_lon, anti_lon_up, anti_lon_down = append_range(anti_lon, anti_lon_up, anti_lon_down, df2.eddy_lon)
        anti_radius, anti_radius_up, anti_radius_down = append_range(anti_radius, anti_radius_up, anti_radius_down, df2.eddy_radius)
        anti_phase, anti_phase_up, anti_phase_down = append_range(anti_phase, anti_phase_up, anti_phase_down, df2.phase_integ_fixed)
        anti_sla, anti_sla_up, anti_sla_down = append_range(anti_sla, anti_sla_up, anti_sla_down, df2.sla_mean_fixed)
        anti_vort, anti_vort_up, anti_vort_down = append_range(anti_vort, anti_vort_up, anti_vort_down, df2.vort_mean_fixed)
        anti_disp, anti_disp_up, anti_disp_down = append_range(anti_disp, anti_disp_up, anti_disp_down, df2.displacement_mean_fixed)
        anti_ftle, anti_ftle_up, anti_ftle_down = append_range(anti_ftle, anti_ftle_up, anti_ftle_down, df2.ftle_mean_fixed)
        anti_sst, anti_sst_up, anti_sst_down = append_range(anti_sst, anti_sst_up, anti_sst_down, df2.sst_mean_fixed)
        anti_chl, anti_chl_up, anti_chl_down = append_range(anti_chl, anti_chl_up, anti_chl_down, df2.chl_mean_fixed)
        anti_co2, anti_co2_up, anti_co2_down = append_range(anti_co2, anti_co2_up, anti_co2_down, df2.CO2_mean_surface)
        anti_mld, anti_mld_up, anti_mld_down = append_range(anti_mld, anti_mld_up, anti_mld_down, df2.mld_mean_fixed)
        anti_sss, anti_sss_up, anti_sss_down = append_range(anti_sss, anti_sss_up, anti_sss_down, df2.sss_mean_fixed)


        anti_ano_phase, anti_ano_phase_up, anti_ano_phase_down = append_range(anti_ano_phase, anti_ano_phase_up, anti_ano_phase_down, df2.phase_integ_fixed - df2.phase_mean_bkg)
        anti_ano_sla, anti_ano_sla_up, anti_ano_sla_down = append_range(anti_ano_sla, anti_ano_sla_up, anti_ano_sla_down, df2.sla_mean_fixed - df2.sla_mean_bkg)
        anti_ano_vort, anti_ano_vort_up, anti_ano_vort_down = append_range(anti_ano_vort, anti_ano_vort_up, anti_ano_vort_down, df2.vort_mean_fixed - df2.vort_mean_bkg)
        anti_ano_disp, anti_ano_disp_up, anti_ano_disp_down = append_range(anti_ano_disp, anti_ano_disp_up, anti_ano_disp_down, df2.displacement_mean_fixed - df2.displacement_mean_bkg)
        anti_ano_ftle, anti_ano_ftle_up, anti_ano_ftle_down = append_range(anti_ano_ftle, anti_ano_ftle_up, anti_ano_ftle_down, df2.ftle_mean_fixed - df2.ftle_mean_bkg)
        anti_ano_sst, anti_ano_sst_up, anti_ano_sst_down = append_range(anti_ano_sst, anti_ano_sst_up, anti_ano_sst_down, df2.sst_mean_fixed - df2.sst_mean_bkg)
        anti_ano_chl, anti_ano_chl_up, anti_ano_chl_down = append_range(anti_ano_chl, anti_ano_chl_up, anti_ano_chl_down, df2.chl_mean_fixed - df2.chl_mean_bkg)
        anti_ano_co2, anti_ano_co2_up, anti_ano_co2_down = append_range(anti_ano_co2, anti_ano_co2_up, anti_ano_co2_down, df2.CO2_mean_surface - df2.CO2_mean_surface_bkg)
        anti_ano_mld, anti_ano_mld_up, anti_ano_mld_down = append_range(anti_ano_mld, anti_ano_mld_up, anti_ano_mld_down, df2.mld_mean_fixed - df2.mld_mean_bkg)
        anti_ano_sss, anti_ano_sss_up, anti_ano_sss_down = append_range(anti_ano_sss, anti_ano_sss_up, anti_ano_sss_down, df2.sss_mean_fixed - df2.sss_mean_bkg)
        '''    
        


        #############  full radius
        cyc_n, cyc_n_up, cyc_n_down = append_range(cyc_n, cyc_n_up, cyc_n_down, len(np.array(df1.year)))
        lat, lat_up, lat_down = append_range(lat, lat_up, lat_down, df1.eddy_lat)
        lon, lon_up, lon_down = append_range(lon, lon_up, lon_down, df1.eddy_lon)
        radius, radius_up, radius_down = append_range(radius, radius_up, radius_down, df1.eddy_radius)
        phase, phase_up, phase_down = append_range(phase, phase_up, phase_down, df1.phase_integ_full)
        sla, sla_up, sla_down = append_range(sla, sla_up, sla_down, df1.sla_mean_full)
        vort, vort_up, vort_down = append_range(vort, vort_up, vort_down, df1.vort_mean_full)
        disp, disp_up, disp_down = append_range(disp, disp_up, disp_down, df1.displacement_mean_full)
        ftle, ftle_up, ftle_down = append_range(ftle, ftle_up, ftle_down, df1.ftle_mean_full)
        sst, sst_up, sst_down = append_range(sst, sst_up, sst_down, df1.sst_mean_full)
        chl, chl_up, chl_down = append_range(chl, chl_up, chl_down, df1.chl_mean_full)
        co2, co2_up, co2_down = append_range(co2, co2_up, co2_down, df1.CO2_mean_surface)
        mld, mld_up, mld_down = append_range(mld, mld_up, mld_down, df1.mld_mean_full)
        sss, sss_up, sss_down = append_range(sss, sss_up, sss_down, df1.sss_mean_full)
        
        ano_phase, ano_phase_up, ano_phase_down = append_range(ano_phase, ano_phase_up, ano_phase_down, df1.phase_integ_full - df1.phase_mean_bkg)
        ano_sla, ano_sla_up, ano_sla_down = append_range(ano_sla, ano_sla_up, ano_sla_down, df1.sla_mean_full - df1.sla_mean_bkg)
        ano_vort, ano_vort_up, ano_vort_down = append_range(ano_vort, ano_vort_up, ano_vort_down, df1.vort_mean_full - df1.vort_mean_bkg)
        ano_disp, ano_disp_up, ano_disp_down = append_range(ano_disp, ano_disp_up, ano_disp_down, df1.displacement_mean_full - df1.displacement_mean_bkg)
        ano_ftle, ano_ftle_up, ano_ftle_down = append_range(ano_ftle, ano_ftle_up, ano_ftle_down, df1.ftle_mean_full - df1.ftle_mean_bkg)
        ano_sst, ano_sst_up, ano_sst_down = append_range(ano_sst, ano_sst_up, ano_sst_down, df1.sst_mean_full - df1.sst_mean_bkg)
        ano_chl, ano_chl_up, ano_chl_down = append_range(ano_chl, ano_chl_up, ano_chl_down, df1.chl_mean_full - df1.chl_mean_bkg)
        ano_co2, ano_co2_up, ano_co2_down = append_range(ano_co2, ano_co2_up, ano_co2_down, df1.CO2_mean_surface - df1.CO2_mean_surface_bkg)
        ano_mld, ano_mld_up, ano_mld_down = append_range(ano_mld, ano_mld_up, ano_mld_down, df1.mld_mean_full - df1.mld_mean_bkg)
        ano_sss, ano_sss_up, ano_sss_down = append_range(ano_sss, ano_sss_up, ano_sss_down, df1.sss_mean_full - df1.sss_mean_bkg)
        
        
        anti_cyc_n, anti_cyc_n_up, anti_cyc_n_down = append_range(anti_cyc_n, anti_cyc_n_up, anti_cyc_n_down, len(np.array(df2.year)))
        anti_lat, anti_lat_up, anti_lat_down = append_range(anti_lat, anti_lat_up, anti_lat_down, df2.eddy_lat)
        anti_lon, anti_lon_up, anti_lon_down = append_range(anti_lon, anti_lon_up, anti_lon_down, df2.eddy_lon)
        anti_radius, anti_radius_up, anti_radius_down = append_range(anti_radius, anti_radius_up, anti_radius_down, df2.eddy_radius)
        anti_phase, anti_phase_up, anti_phase_down = append_range(anti_phase, anti_phase_up, anti_phase_down, df2.phase_integ_full)
        anti_sla, anti_sla_up, anti_sla_down = append_range(anti_sla, anti_sla_up, anti_sla_down, df2.sla_mean_full)
        anti_vort, anti_vort_up, anti_vort_down = append_range(anti_vort, anti_vort_up, anti_vort_down, df2.vort_mean_full)
        anti_disp, anti_disp_up, anti_disp_down = append_range(anti_disp, anti_disp_up, anti_disp_down, df2.displacement_mean_full)
        anti_ftle, anti_ftle_up, anti_ftle_down = append_range(anti_ftle, anti_ftle_up, anti_ftle_down, df2.ftle_mean_full)
        anti_sst, anti_sst_up, anti_sst_down = append_range(anti_sst, anti_sst_up, anti_sst_down, df2.sst_mean_full)
        anti_chl, anti_chl_up, anti_chl_down = append_range(anti_chl, anti_chl_up, anti_chl_down, df2.chl_mean_full)
        anti_co2, anti_co2_up, anti_co2_down = append_range(anti_co2, anti_co2_up, anti_co2_down, df2.CO2_mean_surface)
        anti_mld, anti_mld_up, anti_mld_down = append_range(anti_mld, anti_mld_up, anti_mld_down, df2.mld_mean_full)
        anti_sss, anti_sss_up, anti_sss_down = append_range(anti_sss, anti_sss_up, anti_sss_down, df2.sss_mean_full)


        anti_ano_phase, anti_ano_phase_up, anti_ano_phase_down = append_range(anti_ano_phase, anti_ano_phase_up, anti_ano_phase_down, df2.phase_integ_full - df2.phase_mean_bkg)
        anti_ano_sla, anti_ano_sla_up, anti_ano_sla_down = append_range(anti_ano_sla, anti_ano_sla_up, anti_ano_sla_down, df2.sla_mean_full - df2.sla_mean_bkg)
        anti_ano_vort, anti_ano_vort_up, anti_ano_vort_down = append_range(anti_ano_vort, anti_ano_vort_up, anti_ano_vort_down, df2.vort_mean_full - df2.vort_mean_bkg)
        anti_ano_disp, anti_ano_disp_up, anti_ano_disp_down = append_range(anti_ano_disp, anti_ano_disp_up, anti_ano_disp_down, df2.displacement_mean_full - df2.displacement_mean_bkg)
        anti_ano_ftle, anti_ano_ftle_up, anti_ano_ftle_down = append_range(anti_ano_ftle, anti_ano_ftle_up, anti_ano_ftle_down, df2.ftle_mean_full - df2.ftle_mean_bkg)
        anti_ano_sst, anti_ano_sst_up, anti_ano_sst_down = append_range(anti_ano_sst, anti_ano_sst_up, anti_ano_sst_down, df2.sst_mean_full - df2.sst_mean_bkg)
        anti_ano_chl, anti_ano_chl_up, anti_ano_chl_down = append_range(anti_ano_chl, anti_ano_chl_up, anti_ano_chl_down, df2.chl_mean_full - df2.chl_mean_bkg)
        anti_ano_co2, anti_ano_co2_up, anti_ano_co2_down = append_range(anti_ano_co2, anti_ano_co2_up, anti_ano_co2_down, df2.CO2_mean_surface - df2.CO2_mean_surface_bkg)
        anti_ano_mld, anti_ano_mld_up, anti_ano_mld_down = append_range(anti_ano_mld, anti_ano_mld_up, anti_ano_mld_down, df2.mld_mean_full - df2.mld_mean_bkg)
        anti_ano_sss, anti_ano_sss_up, anti_ano_sss_down = append_range(anti_ano_sss, anti_ano_sss_up, anti_ano_sss_down, df2.sss_mean_full - df2.sss_mean_bkg)



    year = range(year1, year2+1) 
    plot_double_trend(year, cyc_n, cyc_n_up, cyc_n_down, year, anti_cyc_n, anti_cyc_n_up, anti_cyc_n_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'Count', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_count.png')
    plot_double_trend(year, lat, lat_up, lat_down, year, anti_lat, anti_lat_up, anti_lat_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'Latitude ($\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_lat.png')
    plot_double_trend(year, lon, lon_up, lon_down, year, anti_lon, anti_lon_up, anti_lon_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'Longitude ($\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_lon.png')
    plot_double_trend(year, radius, radius_up, radius_down, year, anti_radius, anti_radius_up, anti_radius_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'Radius (km)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_radius.png')
    plot_double_trend(year, phase, phase_up, phase_down, year, anti_phase, anti_phase_up, anti_phase_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'Phase Integral ($\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_phase.png')
    plot_double_trend(year, sla, sla_up, sla_down, year, anti_sla, anti_sla_up, anti_sla_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'SLA (m)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_sla.png')
    plot_double_trend(year, vort, vort_up, vort_down, year, anti_vort, anti_vort_up, anti_vort_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'Relative Vorticity ($s^{-1}$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_vort.png')
    plot_double_trend(year, disp, disp_up, disp_down, year, anti_disp, anti_disp_up, anti_disp_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'Lag. Displacement ($\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_disp.png')
    plot_double_trend(year, ftle, ftle_up, ftle_down, year, anti_ftle, anti_ftle_up, anti_ftle_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'FTLE (day$^{-1}$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ftle.png')
    plot_double_trend(year, sst, sst_up, sst_down, year, anti_sst, anti_sst_up, anti_sst_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'SST (c$\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_sst.png')
    plot_double_trend(year, chl, chl_up, chl_down, year, anti_chl, anti_chl_up, anti_chl_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'CHL (mg.m$^{-3}$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_chl.png')
    plot_double_trend(year, co2, co2_up, co2_down, year, anti_co2, anti_co2_up, anti_co2_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'fCO$_2$ ($\mu$atm)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_co2.png')
    plot_double_trend(year, mld, mld_up, mld_down, year, anti_mld, anti_mld_up, anti_mld_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'MLD (m)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_mld.png')
    plot_double_trend(year, sss, sss_up, sss_down, year, anti_sss, anti_sss_up, anti_sss_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'Salinity (PSU)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_sss.png')



    plot_double_trend(year, ano_phase, ano_phase_up, ano_phase_down, year, anti_ano_phase, anti_ano_phase_up, anti_ano_phase_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'Phase Integral Anamolly ($\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_phase.png')
    plot_double_trend(year, ano_sla, ano_sla_up, ano_sla_down, year, anti_ano_sla, anti_ano_sla_up, anti_ano_sla_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'SLA Anomally (m)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_sla.png')
    plot_double_trend(year, ano_vort, ano_vort_up, ano_vort_down, year, anti_ano_vort, anti_ano_vort_up, anti_ano_vort_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'Relative Vorticity Anomally ($s^{-1}$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_vort.png')
    plot_double_trend(year, ano_disp, ano_disp_up, ano_disp_down, year, anti_ano_disp, anti_ano_disp_up, anti_ano_disp_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'Lag. Displacement Anomally ($\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_disp.png')
    plot_double_trend(year, ano_ftle, ano_ftle_up, ano_ftle_down, year, anti_ano_ftle, anti_ano_ftle_up, anti_ano_ftle_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'FTLE Anomally (day$^{-1}$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_ftle.png')
    plot_double_trend(year, ano_sst, ano_sst_up, ano_sst_down, year, anti_ano_sst, anti_ano_sst_up, anti_ano_sst_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'SST Anomally ($\degree$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_sst.png')
    plot_double_trend(year, ano_chl, ano_chl_up, ano_chl_down, year, anti_ano_chl, anti_ano_chl_up, anti_ano_chl_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'CHL Anomally (mg.m$^{-3}$)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_chl.png')
    plot_double_trend(year, ano_co2, ano_co2_up, ano_co2_down, year, anti_ano_co2, anti_ano_co2_up, anti_ano_co2_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'CO2 Anomally ($\mu$atm)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_co2.png')
    plot_double_trend(year, ano_mld, ano_mld_up, ano_mld_down, year, anti_ano_mld, anti_ano_mld_up, anti_ano_mld_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'MLD Anomally (m)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_mld.png')
    plot_double_trend(year, ano_sss, ano_sss_up, ano_sss_down, year, anti_ano_sss, anti_ano_sss_up, anti_ano_sss_down, error_band, 'o--', 6, 'c', 'm', 'Year', 'Salinity Anomally (PSU)', 'Cyclonic', 'Anti-Cyclonic', 'gallery/double_trend_ano_sss.png')

    return    


def monthly_correlations(query, error_band):
    if query.find('WHERE') >= 0:
        query1 = query + ' AND eddy_polarity=1'
        query2 = query + ' AND eddy_polarity=-1'
    else:
        query1 = query + ' WHERE eddy_polarity=1'
        query2 = query + ' WHERE eddy_polarity=-1'


    corr_lat_sst = np.array([])
    corr_lon_sst = np.array([])
    corr_radius_sst = np.array([])
    corr_phase_sst = np.array([])
    corr_sla_sst = np.array([])
    corr_vort_sst = np.array([])
    corr_disp_sst = np.array([])
    corr_ftle_sst = np.array([])
    corr_chl_sst = np.array([])
    corr_co2_sst = np.array([])

    corr_lat_chl = np.array([])
    corr_lon_chl = np.array([])
    corr_radius_chl = np.array([])
    corr_phase_chl = np.array([])
    corr_sla_chl = np.array([])
    corr_vort_chl = np.array([])
    corr_disp_chl = np.array([])
    corr_ftle_chl = np.array([])
    corr_sst_chl = np.array([])
    corr_co2_chl = np.array([])

    corr_lat_co2 = np.array([])
    corr_lon_co2 = np.array([])
    corr_radius_co2 = np.array([])
    corr_phase_co2 = np.array([])
    corr_sla_co2 = np.array([])
    corr_vort_co2 = np.array([])
    corr_disp_co2 = np.array([])
    corr_ftle_co2 = np.array([])
    corr_sst_co2 = np.array([])
    corr_chl_co2 = np.array([])

    ######## anomally correlations ######
    corr_chl_sst_ano = np.array([]) 
    corr_co2_sst_ano = np.array([])
    corr_sla_sst_ano = np.array([])
    corr_co2_chl_ano = np.array([])
    corr_sla_chl_ano = np.array([])
    corr_sla_co2_ano = np.array([])        
    #####################################


    anti_corr_lat_sst = np.array([])
    anti_corr_lon_sst = np.array([])
    anti_corr_radius_sst = np.array([])
    anti_corr_phase_sst = np.array([])
    anti_corr_sla_sst = np.array([])
    anti_corr_vort_sst = np.array([])
    anti_corr_disp_sst = np.array([])
    anti_corr_ftle_sst = np.array([])
    anti_corr_chl_sst = np.array([])
    anti_corr_co2_sst = np.array([])

    anti_corr_lat_chl = np.array([])
    anti_corr_lon_chl = np.array([])
    anti_corr_radius_chl = np.array([])
    anti_corr_phase_chl = np.array([])
    anti_corr_sla_chl = np.array([])
    anti_corr_vort_chl = np.array([])
    anti_corr_disp_chl = np.array([])
    anti_corr_ftle_chl = np.array([])
    anti_corr_sst_chl = np.array([])
    anti_corr_co2_chl = np.array([])

    anti_corr_lat_co2 = np.array([])
    anti_corr_lon_co2 = np.array([])
    anti_corr_radius_co2 = np.array([])
    anti_corr_phase_co2 = np.array([])
    anti_corr_sla_co2 = np.array([])
    anti_corr_vort_co2 = np.array([])
    anti_corr_disp_co2 = np.array([])
    anti_corr_ftle_co2 = np.array([])
    anti_corr_sst_co2 = np.array([])
    anti_corr_chl_co2 = np.array([])

    ######## anomally correlations ######
    anti_corr_chl_sst_ano = np.array([]) 
    anti_corr_co2_sst_ano = np.array([])
    anti_corr_sla_sst_ano = np.array([])
    anti_corr_co2_chl_ano = np.array([])
    anti_corr_sla_chl_ano = np.array([])
    anti_corr_sla_co2_ano = np.array([])        
    #####################################


    query11 = str(query1)
    query22 = str(query2)
    month1 = 1
    month2 = 12
    
    for month in range(month1, month2+1):
        query1 = query11 + ' AND month=' + str(month)
        query2 = query22 + ' AND month=' + str(month)
        
        conn = db_connect()
        df1 = sql.read_sql(query1, conn)
        conn.close()
        conn = db_connect()
        df2 = sql.read_sql(query2, conn)
        conn.close()
        
        df1 = df1.fillna(float('NaN'))
        df2 = df2.fillna(float('NaN'))
                
        corr, pv = corr_coef(np.array(df1.eddy_lat), np.array(df1.sst_mean_fixed), False)
        corr_lat_sst = np.append(corr_lat_sst, corr) 
        corr, pv = corr_coef(np.array(df1.eddy_lon), np.array(df1.sst_mean_fixed), False)
        corr_lon_sst = np.append(corr_lon_sst, corr) 
        corr, pv = corr_coef(np.array(df1.eddy_radius), np.array(df1.sst_mean_fixed), False)
        corr_radius_sst = np.append(corr_radius_sst, corr) 
        corr, pv = corr_coef(np.array(df1.phase_integ_fixed), np.array(df1.sst_mean_fixed), False)
        corr_phase_sst = np.append(corr_phase_sst, corr) 
        corr, pv = corr_coef(np.array(df1.sla_mean_fixed), np.array(df1.sst_mean_fixed), False)
        corr_sla_sst = np.append(corr_sla_sst, corr) 
        corr, pv = corr_coef(np.array(df1.vort_mean_fixed), np.array(df1.sst_mean_fixed), False)
        corr_vort_sst = np.append(corr_vort_sst, corr) 
        corr, pv = corr_coef(np.array(df1.displacement_mean_fixed), np.array(df1.sst_mean_fixed), False)
        corr_disp_sst = np.append(corr_disp_sst, corr) 
        corr, pv = corr_coef(np.array(df1.ftle_mean_fixed), np.array(df1.sst_mean_fixed), False)
        corr_ftle_sst = np.append(corr_ftle_sst, corr) 
        corr, pv = corr_coef(np.array(df1.chl_mean_fixed), np.array(df1.sst_mean_fixed), True)
        corr_chl_sst = np.append(corr_chl_sst, corr) 
        corr, pv = corr_coef(np.array(df1.CO2_mean_surface), np.array(df1.sst_mean_fixed), True)
        corr_co2_sst = np.append(corr_co2_sst, corr) 

        corr, pv = corr_coef(np.array(df1.eddy_lat), np.array(df1.chl_mean_fixed), True)
        corr_lat_chl = np.append(corr_lat_chl, corr) 
        corr, pv = corr_coef(np.array(df1.eddy_lon), np.array(df1.chl_mean_fixed), True)
        corr_lon_chl = np.append(corr_lon_chl, corr) 
        corr, pv = corr_coef(np.array(df1.eddy_radius), np.array(df1.chl_mean_fixed), True)
        corr_radius_chl = np.append(corr_radius_chl, corr) 
        corr, pv = corr_coef(np.array(df1.phase_integ_fixed), np.array(df1.chl_mean_fixed), True)
        corr_phase_chl = np.append(corr_phase_chl, corr) 
        corr, pv = corr_coef(np.array(df1.sla_mean_fixed), np.array(df1.chl_mean_fixed), True)
        corr_sla_chl = np.append(corr_sla_chl, corr) 
        corr, pv = corr_coef(np.array(df1.vort_mean_fixed), np.array(df1.chl_mean_fixed), True)
        corr_vort_chl = np.append(corr_vort_chl, corr) 
        corr, pv = corr_coef(np.array(df1.displacement_mean_fixed), np.array(df1.chl_mean_fixed), True)
        corr_disp_chl = np.append(corr_disp_chl, corr) 
        corr, pv = corr_coef(np.array(df1.ftle_mean_fixed), np.array(df1.chl_mean_fixed), True)
        corr_ftle_chl = np.append(corr_ftle_chl, corr) 
        corr, pv = corr_coef(np.array(df1.sst_mean_fixed), np.array(df1.chl_mean_fixed), True)
        corr_sst_chl = np.append(corr_sst_chl, corr) 
        corr, pv = corr_coef(np.array(df1.CO2_mean_surface), np.array(df1.chl_mean_fixed), True)
        corr_co2_chl = np.append(corr_co2_chl, corr) 

        corr, pv = corr_coef(np.array(df1.eddy_lat), np.array(df1.CO2_mean_surface), True)
        corr_lat_co2 = np.append(corr_lat_co2, corr) 
        corr, pv = corr_coef(np.array(df1.eddy_lon), np.array(df1.CO2_mean_surface), True)
        corr_lon_co2 = np.append(corr_lon_co2, corr) 
        corr, pv = corr_coef(np.array(df1.eddy_radius), np.array(df1.CO2_mean_surface), True)
        corr_radius_co2 = np.append(corr_radius_co2, corr) 
        corr, pv = corr_coef(np.array(df1.phase_integ_fixed), np.array(df1.CO2_mean_surface), True)
        corr_phase_co2 = np.append(corr_phase_co2, corr) 
        corr, pv = corr_coef(np.array(df1.sla_mean_fixed), np.array(df1.CO2_mean_surface), True)
        corr_sla_co2 = np.append(corr_sla_co2, corr) 
        corr, pv = corr_coef(np.array(df1.vort_mean_fixed), np.array(df1.CO2_mean_surface), True)
        corr_vort_co2 = np.append(corr_vort_co2, corr) 
        corr, pv = corr_coef(np.array(df1.displacement_mean_fixed), np.array(df1.CO2_mean_surface), True)
        corr_disp_co2 = np.append(corr_disp_co2, corr) 
        corr, pv = corr_coef(np.array(df1.ftle_mean_fixed), np.array(df1.CO2_mean_surface), True)
        corr_ftle_co2 = np.append(corr_ftle_co2, corr) 
        corr, pv = corr_coef(np.array(df1.sst_mean_fixed), np.array(df1.CO2_mean_surface), True)
        corr_sst_co2 = np.append(corr_sst_co2, corr) 
        corr, pv = corr_coef(np.array(df1.chl_mean_fixed), np.array(df1.CO2_mean_surface), True)
        corr_chl_co2 = np.append(corr_chl_co2, corr) 
        

        ############### anomally correlations  ####################
        corr, pv = corr_coef(np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), np.array(df1.sst_mean_fixed)-np.array(df1.sst_mean_bkg), True)
        corr_chl_sst_ano = np.append(corr_chl_sst_ano, corr) 
        corr, pv = corr_coef(np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), np.array(df1.sst_mean_fixed)-np.array(df1.sst_mean_bkg), True)
        corr_co2_sst_ano = np.append(corr_co2_sst_ano, corr) 
        corr, pv = corr_coef(np.array(df1.sla_mean_fixed)-np.array(df1.sla_mean_bkg), np.array(df1.sst_mean_fixed)-np.array(df1.sst_mean_bkg), False)
        corr_sla_sst_ano = np.append(corr_sla_sst_ano, corr) 
        corr, pv = corr_coef(np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
        corr_co2_chl_ano = np.append(corr_co2_chl_ano, corr) 
        corr, pv = corr_coef(np.array(df1.sla_mean_fixed)-np.array(df1.sla_mean_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
        corr_sla_chl_ano = np.append(corr_sla_chl_ano, corr) 
        corr, pv = corr_coef(np.array(df1.sla_mean_fixed)-np.array(df1.sla_mean_bkg), np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), True)
        corr_sla_co2_ano = np.append(corr_sla_co2_ano, corr) 
        ###########################################################





        corr, pv = corr_coef(np.array(df2.eddy_lat), np.array(df2.sst_mean_fixed), False)
        anti_corr_lat_sst = np.append(anti_corr_lat_sst, corr) 
        corr, pv = corr_coef(np.array(df2.eddy_lon), np.array(df2.sst_mean_fixed), False)
        anti_corr_lon_sst = np.append(anti_corr_lon_sst, corr) 
        corr, pv = corr_coef(np.array(df2.eddy_radius), np.array(df2.sst_mean_fixed), False)
        anti_corr_radius_sst = np.append(anti_corr_radius_sst, corr) 
        corr, pv = corr_coef(np.array(df2.phase_integ_fixed), np.array(df2.sst_mean_fixed), False)
        anti_corr_phase_sst = np.append(anti_corr_phase_sst, corr) 
        corr, pv = corr_coef(np.array(df2.sla_mean_fixed), np.array(df2.sst_mean_fixed), False)
        anti_corr_sla_sst = np.append(anti_corr_sla_sst, corr) 
        corr, pv = corr_coef(np.array(df2.vort_mean_fixed), np.array(df2.sst_mean_fixed), False)
        anti_corr_vort_sst = np.append(anti_corr_vort_sst, corr) 
        corr, pv = corr_coef(np.array(df2.displacement_mean_fixed), np.array(df2.sst_mean_fixed), False)
        anti_corr_disp_sst = np.append(anti_corr_disp_sst, corr) 
        corr, pv = corr_coef(np.array(df2.ftle_mean_fixed), np.array(df2.sst_mean_fixed), False)
        anti_corr_ftle_sst = np.append(anti_corr_ftle_sst, corr) 
        corr, pv = corr_coef(np.array(df2.chl_mean_fixed), np.array(df2.sst_mean_fixed), True)
        anti_corr_chl_sst = np.append(anti_corr_chl_sst, corr) 
        corr, pv = corr_coef(np.array(df2.CO2_mean_surface), np.array(df2.sst_mean_fixed), True)
        anti_corr_co2_sst = np.append(anti_corr_co2_sst, corr) 

        corr, pv = corr_coef(np.array(df2.eddy_lat), np.array(df2.chl_mean_fixed), True)
        anti_corr_lat_chl = np.append(anti_corr_lat_chl, corr) 
        corr, pv = corr_coef(np.array(df2.eddy_lon), np.array(df2.chl_mean_fixed), True)
        anti_corr_lon_chl = np.append(anti_corr_lon_chl, corr) 
        corr, pv = corr_coef(np.array(df2.eddy_radius), np.array(df2.chl_mean_fixed), True)
        anti_corr_radius_chl = np.append(anti_corr_radius_chl, corr) 
        corr, pv = corr_coef(np.array(df2.phase_integ_fixed), np.array(df2.chl_mean_fixed), True)
        anti_corr_phase_chl = np.append(anti_corr_phase_chl, corr) 
        corr, pv = corr_coef(np.array(df2.sla_mean_fixed), np.array(df2.chl_mean_fixed), True)
        anti_corr_sla_chl = np.append(anti_corr_sla_chl, corr) 
        corr, pv = corr_coef(np.array(df2.vort_mean_fixed), np.array(df2.chl_mean_fixed), True)
        anti_corr_vort_chl = np.append(anti_corr_vort_chl, corr) 
        corr, pv = corr_coef(np.array(df2.displacement_mean_fixed), np.array(df2.chl_mean_fixed), True)
        anti_corr_disp_chl = np.append(anti_corr_disp_chl, corr) 
        corr, pv = corr_coef(np.array(df2.ftle_mean_fixed), np.array(df2.chl_mean_fixed), True)
        anti_corr_ftle_chl = np.append(anti_corr_ftle_chl, corr) 
        corr, pv = corr_coef(np.array(df2.sst_mean_fixed), np.array(df2.chl_mean_fixed), True)
        anti_corr_sst_chl = np.append(anti_corr_sst_chl, corr) 
        corr, pv = corr_coef(np.array(df2.CO2_mean_surface), np.array(df2.chl_mean_fixed), True)
        anti_corr_co2_chl = np.append(anti_corr_co2_chl, corr) 

        corr, pv = corr_coef(np.array(df2.eddy_lat), np.array(df2.CO2_mean_surface), True)
        anti_corr_lat_co2 = np.append(anti_corr_lat_co2, corr) 
        corr, pv = corr_coef(np.array(df2.eddy_lon), np.array(df2.CO2_mean_surface), True)
        anti_corr_lon_co2 = np.append(anti_corr_lon_co2, corr) 
        corr, pv = corr_coef(np.array(df2.eddy_radius), np.array(df2.CO2_mean_surface), True)
        anti_corr_radius_co2 = np.append(anti_corr_radius_co2, corr) 
        corr, pv = corr_coef(np.array(df2.phase_integ_fixed), np.array(df2.CO2_mean_surface), True)
        anti_corr_phase_co2 = np.append(anti_corr_phase_co2, corr) 
        corr, pv = corr_coef(np.array(df2.sla_mean_fixed), np.array(df2.CO2_mean_surface), True)
        anti_corr_sla_co2 = np.append(anti_corr_sla_co2, corr) 
        corr, pv = corr_coef(np.array(df2.vort_mean_fixed), np.array(df2.CO2_mean_surface), True)
        anti_corr_vort_co2 = np.append(anti_corr_vort_co2, corr) 
        corr, pv = corr_coef(np.array(df2.displacement_mean_fixed), np.array(df2.CO2_mean_surface), True)
        anti_corr_disp_co2 = np.append(anti_corr_disp_co2, corr) 
        corr, pv = corr_coef(np.array(df2.ftle_mean_fixed), np.array(df2.CO2_mean_surface), True)
        anti_corr_ftle_co2 = np.append(anti_corr_ftle_co2, corr) 
        corr, pv = corr_coef(np.array(df2.sst_mean_fixed), np.array(df2.CO2_mean_surface), True)
        anti_corr_sst_co2 = np.append(anti_corr_sst_co2, corr) 
        corr, pv = corr_coef(np.array(df2.chl_mean_fixed), np.array(df2.CO2_mean_surface), True)
        anti_corr_chl_co2 = np.append(anti_corr_chl_co2, corr) 
        
        
        ############### anomally correlations  ####################
        corr, pv = corr_coef(np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), np.array(df2.sst_mean_fixed)-np.array(df2.sst_mean_bkg), True)
        anti_corr_chl_sst_ano = np.append(anti_corr_chl_sst_ano, corr) 
        corr, pv = corr_coef(np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), np.array(df2.sst_mean_fixed)-np.array(df2.sst_mean_bkg), True)
        anti_corr_co2_sst_ano = np.append(anti_corr_co2_sst_ano, corr) 
        corr, pv = corr_coef(np.array(df2.sla_mean_fixed)-np.array(df2.sla_mean_bkg), np.array(df2.sst_mean_fixed)-np.array(df2.sst_mean_bkg), False)
        anti_corr_sla_sst_ano = np.append(anti_corr_sla_sst_ano, corr) 
        corr, pv = corr_coef(np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
        anti_corr_co2_chl_ano = np.append(anti_corr_co2_chl_ano, corr) 
        corr, pv = corr_coef(np.array(df2.sla_mean_fixed)-np.array(df2.sla_mean_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
        anti_corr_sla_chl_ano = np.append(anti_corr_sla_chl_ano, corr) 
        corr, pv = corr_coef(np.array(df2.sla_mean_fixed)-np.array(df2.sla_mean_bkg), np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), True)
        anti_corr_sla_co2_ano = np.append(anti_corr_sla_co2_ano, corr) 
        ###########################################################

        
        
    month = range(month1, month2+1)    
    plot_double_trend(month, corr_lat_sst, corr_lat_sst, corr_lat_sst, month, anti_corr_lat_sst, anti_corr_lat_sst, anti_corr_lat_sst, error_band, 'o--', 6, 'c', 'm', 'Month', 'lat-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_lat_sst.png')
    plot_double_trend(month, corr_lon_sst, corr_lon_sst, corr_lon_sst, month, anti_corr_lon_sst, anti_corr_lon_sst, anti_corr_lon_sst, error_band, 'o--', 6, 'c', 'm', 'Month', 'lon-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_lon_sst.png')
    plot_double_trend(month, corr_radius_sst, corr_radius_sst, corr_radius_sst, month, anti_corr_radius_sst, anti_corr_radius_sst, anti_corr_radius_sst, error_band, 'o--', 6, 'c', 'm', 'Month', 'radius-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_radius_sst.png')
    plot_double_trend(month, corr_phase_sst, corr_phase_sst, corr_phase_sst, month, anti_corr_phase_sst, anti_corr_phase_sst, anti_corr_phase_sst, error_band, 'o--', 6, 'c', 'm', 'Month', 'radius-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_phase_sst.png')
    plot_double_trend(month, corr_sla_sst, corr_sla_sst, corr_sla_sst, month, anti_corr_sla_sst, anti_corr_sla_sst, anti_corr_sla_sst, error_band, 'o--', 6, 'c', 'm', 'Month', 'sla-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sla_sst.png')
    plot_double_trend(month, corr_vort_sst, corr_vort_sst, corr_vort_sst, month, anti_corr_vort_sst, anti_corr_vort_sst, anti_corr_vort_sst, error_band, 'o--', 6, 'c', 'm', 'Month', 'vort-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_vort_sst.png')
    plot_double_trend(month, corr_disp_sst, corr_disp_sst, corr_disp_sst, month, anti_corr_disp_sst, anti_corr_disp_sst, anti_corr_disp_sst, error_band, 'o--', 6, 'c', 'm', 'Month', 'disp-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_disp_sst.png')
    plot_double_trend(month, corr_ftle_sst, corr_ftle_sst, corr_ftle_sst, month, anti_corr_ftle_sst, anti_corr_ftle_sst, anti_corr_ftle_sst, error_band, 'o--', 6, 'c', 'm', 'Month', 'ftle-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_ftle_sst.png')
    plot_double_trend(month, corr_chl_sst, corr_chl_sst, corr_chl_sst, month, anti_corr_chl_sst, anti_corr_chl_sst, anti_corr_chl_sst, error_band, 'o--', 6, 'c', 'm', 'Month', 'chl-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_chl_sst.png')
    plot_double_trend(month, corr_co2_sst, corr_co2_sst, corr_co2_sst, month, anti_corr_co2_sst, anti_corr_co2_sst, anti_corr_co2_sst, error_band, 'o--', 6, 'c', 'm', 'Month', 'fCO$_2$-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_co2_sst.png')

    plot_double_trend(month, corr_lat_chl, corr_lat_chl, corr_lat_chl, month, anti_corr_lat_chl, anti_corr_lat_chl, anti_corr_lat_chl, error_band, 'o--', 6, 'c', 'm', 'Month', 'lat-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_lat_chl.png')
    plot_double_trend(month, corr_lon_chl, corr_lon_chl, corr_lon_chl, month, anti_corr_lon_chl, anti_corr_lon_chl, anti_corr_lon_chl, error_band, 'o--', 6, 'c', 'm', 'Month', 'lon-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_lon_chl.png')
    plot_double_trend(month, corr_radius_chl, corr_radius_chl, corr_radius_chl, month, anti_corr_radius_chl, anti_corr_radius_chl, anti_corr_radius_chl, error_band, 'o--', 6, 'c', 'm', 'Month', 'radius-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_radius_chl.png')
    plot_double_trend(month, corr_phase_chl, corr_phase_chl, corr_phase_chl, month, anti_corr_phase_chl, anti_corr_phase_chl, anti_corr_phase_chl, error_band, 'o--', 6, 'c', 'm', 'Month', 'radius-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_phase_chl.png')
    plot_double_trend(month, corr_sla_chl, corr_sla_chl, corr_sla_chl, month, anti_corr_sla_chl, anti_corr_sla_chl, anti_corr_sla_chl, error_band, 'o--', 6, 'c', 'm', 'Month', 'sla-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sla_chl.png')
    plot_double_trend(month, corr_vort_chl, corr_vort_chl, corr_vort_chl, month, anti_corr_vort_chl, anti_corr_vort_chl, anti_corr_vort_chl, error_band, 'o--', 6, 'c', 'm', 'Month', 'vort-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_vort_chl.png')
    plot_double_trend(month, corr_disp_chl, corr_disp_chl, corr_disp_chl, month, anti_corr_disp_chl, anti_corr_disp_chl, anti_corr_disp_chl, error_band, 'o--', 6, 'c', 'm', 'Month', 'disp-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_disp_chl.png')
    plot_double_trend(month, corr_ftle_chl, corr_ftle_chl, corr_ftle_chl, month, anti_corr_ftle_chl, anti_corr_ftle_chl, anti_corr_ftle_chl, error_band, 'o--', 6, 'c', 'm', 'Month', 'ftle-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_ftle_chl.png')
    plot_double_trend(month, corr_sst_chl, corr_sst_chl, corr_sst_chl, month, anti_corr_sst_chl, anti_corr_sst_chl, anti_corr_sst_chl, error_band, 'o--', 6, 'c', 'm', 'Month', 'sst-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sst_chl.png')
    plot_double_trend(month, corr_co2_chl, corr_co2_chl, corr_co2_chl, month, anti_corr_co2_chl, anti_corr_co2_chl, anti_corr_co2_chl, error_band, 'o--', 6, 'c', 'm', 'Month', 'fCO$_2$-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_co2_chl.png')

    plot_double_trend(month, corr_lat_co2, corr_lat_co2, corr_lat_co2, month, anti_corr_lat_co2, anti_corr_lat_co2, anti_corr_lat_co2, error_band, 'o--', 6, 'c', 'm', 'Month', 'lat-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_lat_co2.png')
    plot_double_trend(month, corr_lon_co2, corr_lon_co2, corr_lon_co2, month, anti_corr_lon_co2, anti_corr_lon_co2, anti_corr_lon_co2, error_band, 'o--', 6, 'c', 'm', 'Month', 'lon-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_lon_co2.png')
    plot_double_trend(month, corr_radius_co2, corr_radius_co2, corr_radius_co2, month, anti_corr_radius_co2, anti_corr_radius_co2, anti_corr_radius_co2, error_band, 'o--', 6, 'c', 'm', 'Month', 'radius-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_radius_co2.png')
    plot_double_trend(month, corr_phase_co2, corr_phase_co2, corr_phase_co2, month, anti_corr_phase_co2, anti_corr_phase_co2, anti_corr_phase_co2, error_band, 'o--', 6, 'c', 'm', 'Month', 'radius-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_phase_co2.png')
    plot_double_trend(month, corr_sla_co2, corr_sla_co2, corr_sla_co2, month, anti_corr_sla_co2, anti_corr_sla_co2, anti_corr_sla_co2, error_band, 'o--', 6, 'c', 'm', 'Month', 'sla-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sla_co2.png')
    plot_double_trend(month, corr_vort_co2, corr_vort_co2, corr_vort_co2, month, anti_corr_vort_co2, anti_corr_vort_co2, anti_corr_vort_co2, error_band, 'o--', 6, 'c', 'm', 'Month', 'vort-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_vort_co2.png')
    plot_double_trend(month, corr_disp_co2, corr_disp_co2, corr_disp_co2, month, anti_corr_disp_co2, anti_corr_disp_co2, anti_corr_disp_co2, error_band, 'o--', 6, 'c', 'm', 'Month', 'disp-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_disp_co2.png')
    plot_double_trend(month, corr_ftle_co2, corr_ftle_co2, corr_ftle_co2, month, anti_corr_ftle_co2, anti_corr_ftle_co2, anti_corr_ftle_co2, error_band, 'o--', 6, 'c', 'm', 'Month', 'ftle-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_ftle_co2.png')
    plot_double_trend(month, corr_sst_co2, corr_sst_co2, corr_sst_co2, month, anti_corr_sst_co2, anti_corr_sst_co2, anti_corr_sst_co2, error_band, 'o--', 6, 'c', 'm', 'Month', 'sst-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sst_co2.png')
    plot_double_trend(month, corr_chl_co2, corr_chl_co2, corr_chl_co2, month, anti_corr_chl_co2, anti_corr_chl_co2, anti_corr_chl_co2, error_band, 'o--', 6, 'c', 'm', 'Month', 'chl-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_chl_co2.png')


    ############### anomally correlations  ####################
    plot_double_trend(month, corr_sla_sst_ano, corr_sla_sst_ano, corr_sla_sst_ano, month, anti_corr_sla_sst_ano, anti_corr_sla_sst_ano, anti_corr_sla_sst_ano, error_band, 'o--', 6, 'c', 'm', 'Month', 'sla-sst anomally corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sla_sst_ano.png')
    plot_double_trend(month, corr_chl_sst_ano, corr_chl_sst_ano, corr_chl_sst_ano, month, anti_corr_chl_sst_ano, anti_corr_chl_sst_ano, anti_corr_chl_sst_ano, error_band, 'o--', 6, 'c', 'm', 'Month', 'chl-sst anomally corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_chl_sst_ano.png')
    plot_double_trend(month, corr_co2_sst_ano, corr_co2_sst_ano, corr_co2_sst_ano, month, anti_corr_co2_sst_ano, anti_corr_co2_sst_ano, anti_corr_co2_sst_ano, error_band, 'o--', 6, 'c', 'm', 'Month', 'fCO$_2$-sst anomally corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_co2_sst_ano.png')
    plot_double_trend(month, corr_sla_chl_ano, corr_sla_chl_ano, corr_sla_chl_ano, month, anti_corr_sla_chl_ano, anti_corr_sla_chl_ano, anti_corr_sla_chl_ano, error_band, 'o--', 6, 'c', 'm', 'Month', 'sla-chl anomally corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sla_chl_ano.png')
    plot_double_trend(month, corr_co2_chl_ano, corr_co2_chl_ano, corr_co2_chl_ano, month, anti_corr_co2_chl_ano, anti_corr_co2_chl_ano, anti_corr_co2_chl_ano, error_band, 'o--', 6, 'c', 'm', 'Month', 'fCO$_2$-chl anomally corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_co2_chl_ano.png')
    plot_double_trend(month, corr_sla_co2_ano, corr_sla_co2_ano, corr_sla_co2_ano, month, anti_corr_sla_co2_ano, anti_corr_sla_co2_ano, anti_corr_sla_co2_ano, error_band, 'o--', 6, 'c', 'm', 'Month', 'sla-fCO$_2$ anomally corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sla_co2_ano.png')
    ###########################################################
    return    



def yearly_correlations(query, error_band):
    if query.find('WHERE') >= 0:
        query1 = query + ' AND eddy_polarity=1'
        query2 = query + ' AND eddy_polarity=-1'
    else:
        query1 = query + ' WHERE eddy_polarity=1'
        query2 = query + ' WHERE eddy_polarity=-1'

    corr_lat_sst = np.array([])
    corr_lon_sst = np.array([])
    corr_radius_sst = np.array([])
    corr_phase_sst = np.array([])
    corr_sla_sst = np.array([])
    corr_vort_sst = np.array([])
    corr_disp_sst = np.array([])
    corr_ftle_sst = np.array([])
    corr_chl_sst = np.array([])
    corr_co2_sst = np.array([])

    corr_lat_chl = np.array([])
    corr_lon_chl = np.array([])
    corr_radius_chl = np.array([])
    corr_phase_chl = np.array([])
    corr_sla_chl = np.array([])
    corr_vort_chl = np.array([])
    corr_disp_chl = np.array([])
    corr_ftle_chl = np.array([])
    corr_sst_chl = np.array([])
    corr_co2_chl = np.array([])

    corr_lat_co2 = np.array([])
    corr_lon_co2 = np.array([])
    corr_radius_co2 = np.array([])
    corr_phase_co2 = np.array([])
    corr_sla_co2 = np.array([])
    corr_vort_co2 = np.array([])
    corr_disp_co2 = np.array([])
    corr_ftle_co2 = np.array([])
    corr_sst_co2 = np.array([])
    corr_chl_co2 = np.array([])

    
    ######## anomally correlations ######
    corr_chl_sst_ano = np.array([]) 
    corr_co2_sst_ano = np.array([])
    corr_sla_sst_ano = np.array([])
    corr_co2_chl_ano = np.array([])
    corr_sla_chl_ano = np.array([])
    corr_sla_co2_ano = np.array([])        
    #####################################


    anti_corr_lat_sst = np.array([])
    anti_corr_lon_sst = np.array([])
    anti_corr_radius_sst = np.array([])
    anti_corr_phase_sst = np.array([])
    anti_corr_sla_sst = np.array([])
    anti_corr_vort_sst = np.array([])
    anti_corr_disp_sst = np.array([])
    anti_corr_ftle_sst = np.array([])
    anti_corr_chl_sst = np.array([])
    anti_corr_co2_sst = np.array([])

    anti_corr_lat_chl = np.array([])
    anti_corr_lon_chl = np.array([])
    anti_corr_radius_chl = np.array([])
    anti_corr_phase_chl = np.array([])
    anti_corr_sla_chl = np.array([])
    anti_corr_vort_chl = np.array([])
    anti_corr_disp_chl = np.array([])
    anti_corr_ftle_chl = np.array([])
    anti_corr_sst_chl = np.array([])
    anti_corr_co2_chl = np.array([])

    anti_corr_lat_co2 = np.array([])
    anti_corr_lon_co2 = np.array([])
    anti_corr_radius_co2 = np.array([])
    anti_corr_phase_co2 = np.array([])
    anti_corr_sla_co2 = np.array([])
    anti_corr_vort_co2 = np.array([])
    anti_corr_disp_co2 = np.array([])
    anti_corr_ftle_co2 = np.array([])
    anti_corr_sst_co2 = np.array([])
    anti_corr_chl_co2 = np.array([])

    ######## anomally correlations ######
    anti_corr_chl_sst_ano = np.array([]) 
    anti_corr_co2_sst_ano = np.array([])
    anti_corr_sla_sst_ano = np.array([])
    anti_corr_co2_chl_ano = np.array([])
    anti_corr_sla_chl_ano = np.array([])
    anti_corr_sla_co2_ano = np.array([])        
    #####################################



    query11 = str(query1)
    query22 = str(query2)
    year1 = 2003
    year2 = 2015
    
    for year in range(year1, year2+1):
        query1 = query11 + ' AND year=' + str(year)
        query2 = query22 + ' AND year=' + str(year)
        
        conn = db_connect()
        df1 = sql.read_sql(query1, conn)
        conn.close()
        conn = db_connect()
        df2 = sql.read_sql(query2, conn)
        conn.close()
        
        df1 = df1.fillna(float('NaN'))
        df2 = df2.fillna(float('NaN'))


        corr, pv = corr_coef(np.array(df1.eddy_lat), np.array(df1.sst_mean_fixed), False)
        corr_lat_sst = np.append(corr_lat_sst, corr) 
        corr, pv = corr_coef(np.array(df1.eddy_lon), np.array(df1.sst_mean_fixed), False)
        corr_lon_sst = np.append(corr_lon_sst, corr) 
        corr, pv = corr_coef(np.array(df1.eddy_radius), np.array(df1.sst_mean_fixed), False)
        corr_radius_sst = np.append(corr_radius_sst, corr) 
        corr, pv = corr_coef(np.array(df1.phase_integ_fixed), np.array(df1.sst_mean_fixed), False)
        corr_phase_sst = np.append(corr_phase_sst, corr) 
        corr, pv = corr_coef(np.array(df1.sla_mean_fixed), np.array(df1.sst_mean_fixed), False)
        corr_sla_sst = np.append(corr_sla_sst, corr) 
        corr, pv = corr_coef(np.array(df1.vort_mean_fixed), np.array(df1.sst_mean_fixed), False)
        corr_vort_sst = np.append(corr_vort_sst, corr) 
        corr, pv = corr_coef(np.array(df1.displacement_mean_fixed), np.array(df1.sst_mean_fixed), False)
        corr_disp_sst = np.append(corr_disp_sst, corr) 
        corr, pv = corr_coef(np.array(df1.ftle_mean_fixed), np.array(df1.sst_mean_fixed), False)
        corr_ftle_sst = np.append(corr_ftle_sst, corr) 
        corr, pv = corr_coef(np.array(df1.chl_mean_fixed), np.array(df1.sst_mean_fixed), True)
        corr_chl_sst = np.append(corr_chl_sst, corr) 
        corr, pv = corr_coef(np.array(df1.CO2_mean_surface), np.array(df1.sst_mean_fixed), True)
        corr_co2_sst = np.append(corr_co2_sst, corr) 

        corr, pv = corr_coef(np.array(df1.eddy_lat), np.array(df1.chl_mean_fixed), True)
        corr_lat_chl = np.append(corr_lat_chl, corr) 
        corr, pv = corr_coef(np.array(df1.eddy_lon), np.array(df1.chl_mean_fixed), True)
        corr_lon_chl = np.append(corr_lon_chl, corr) 
        corr, pv = corr_coef(np.array(df1.eddy_radius), np.array(df1.chl_mean_fixed), True)
        corr_radius_chl = np.append(corr_radius_chl, corr) 
        corr, pv = corr_coef(np.array(df1.phase_integ_fixed), np.array(df1.chl_mean_fixed), True)
        corr_phase_chl = np.append(corr_phase_chl, corr) 
        corr, pv = corr_coef(np.array(df1.sla_mean_fixed), np.array(df1.chl_mean_fixed), True)
        corr_sla_chl = np.append(corr_sla_chl, corr) 
        corr, pv = corr_coef(np.array(df1.vort_mean_fixed), np.array(df1.chl_mean_fixed), True)
        corr_vort_chl = np.append(corr_vort_chl, corr) 
        corr, pv = corr_coef(np.array(df1.displacement_mean_fixed), np.array(df1.chl_mean_fixed), True)
        corr_disp_chl = np.append(corr_disp_chl, corr) 
        corr, pv = corr_coef(np.array(df1.ftle_mean_fixed), np.array(df1.chl_mean_fixed), True)
        corr_ftle_chl = np.append(corr_ftle_chl, corr) 
        corr, pv = corr_coef(np.array(df1.sst_mean_fixed), np.array(df1.chl_mean_fixed), True)
        corr_sst_chl = np.append(corr_sst_chl, corr) 
        corr, pv = corr_coef(np.array(df1.CO2_mean_surface), np.array(df1.chl_mean_fixed), True)
        corr_co2_chl = np.append(corr_co2_chl, corr) 

        corr, pv = corr_coef(np.array(df1.eddy_lat), np.array(df1.CO2_mean_surface), True)
        corr_lat_co2 = np.append(corr_lat_co2, corr) 
        corr, pv = corr_coef(np.array(df1.eddy_lon), np.array(df1.CO2_mean_surface), True)
        corr_lon_co2 = np.append(corr_lon_co2, corr) 
        corr, pv = corr_coef(np.array(df1.eddy_radius), np.array(df1.CO2_mean_surface), True)
        corr_radius_co2 = np.append(corr_radius_co2, corr) 
        corr, pv = corr_coef(np.array(df1.phase_integ_fixed), np.array(df1.CO2_mean_surface), True)
        corr_phase_co2 = np.append(corr_phase_co2, corr) 
        corr, pv = corr_coef(np.array(df1.sla_mean_fixed), np.array(df1.CO2_mean_surface), True)
        corr_sla_co2 = np.append(corr_sla_co2, corr) 
        corr, pv = corr_coef(np.array(df1.vort_mean_fixed), np.array(df1.CO2_mean_surface), True)
        corr_vort_co2 = np.append(corr_vort_co2, corr) 
        corr, pv = corr_coef(np.array(df1.displacement_mean_fixed), np.array(df1.CO2_mean_surface), True)
        corr_disp_co2 = np.append(corr_disp_co2, corr) 
        corr, pv = corr_coef(np.array(df1.ftle_mean_fixed), np.array(df1.CO2_mean_surface), True)
        corr_ftle_co2 = np.append(corr_ftle_co2, corr) 
        corr, pv = corr_coef(np.array(df1.sst_mean_fixed), np.array(df1.CO2_mean_surface), True)
        corr_sst_co2 = np.append(corr_sst_co2, corr) 
        corr, pv = corr_coef(np.array(df1.chl_mean_fixed), np.array(df1.CO2_mean_surface), True)
        corr_chl_co2 = np.append(corr_chl_co2, corr) 

         ############### anomally correlations  ####################
        corr, pv = corr_coef(np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), np.array(df1.sst_mean_fixed)-np.array(df1.sst_mean_bkg), True)
        corr_chl_sst_ano = np.append(corr_chl_sst_ano, corr) 
        corr, pv = corr_coef(np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), np.array(df1.sst_mean_fixed)-np.array(df1.sst_mean_bkg), True)
        corr_co2_sst_ano = np.append(corr_co2_sst_ano, corr) 
        corr, pv = corr_coef(np.array(df1.sla_mean_fixed)-np.array(df1.sla_mean_bkg), np.array(df1.sst_mean_fixed)-np.array(df1.sst_mean_bkg), False)
        corr_sla_sst_ano = np.append(corr_sla_sst_ano, corr) 
        corr, pv = corr_coef(np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
        corr_co2_chl_ano = np.append(corr_co2_chl_ano, corr) 
        corr, pv = corr_coef(np.array(df1.sla_mean_fixed)-np.array(df1.sla_mean_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
        corr_sla_chl_ano = np.append(corr_sla_chl_ano, corr) 
        corr, pv = corr_coef(np.array(df1.sla_mean_fixed)-np.array(df1.sla_mean_bkg), np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), True)
        corr_sla_co2_ano = np.append(corr_sla_co2_ano, corr) 
        ###########################################################


       

        corr, pv = corr_coef(np.array(df2.eddy_lat), np.array(df2.sst_mean_fixed), False)
        anti_corr_lat_sst = np.append(anti_corr_lat_sst, corr) 
        corr, pv = corr_coef(np.array(df2.eddy_lon), np.array(df2.sst_mean_fixed), False)
        anti_corr_lon_sst = np.append(anti_corr_lon_sst, corr) 
        corr, pv = corr_coef(np.array(df2.eddy_radius), np.array(df2.sst_mean_fixed), False)
        anti_corr_radius_sst = np.append(anti_corr_radius_sst, corr) 
        corr, pv = corr_coef(np.array(df2.phase_integ_fixed), np.array(df2.sst_mean_fixed), False)
        anti_corr_phase_sst = np.append(anti_corr_phase_sst, corr) 
        corr, pv = corr_coef(np.array(df2.sla_mean_fixed), np.array(df2.sst_mean_fixed), False)
        anti_corr_sla_sst = np.append(anti_corr_sla_sst, corr) 
        corr, pv = corr_coef(np.array(df2.vort_mean_fixed), np.array(df2.sst_mean_fixed), False)
        anti_corr_vort_sst = np.append(anti_corr_vort_sst, corr) 
        corr, pv = corr_coef(np.array(df2.displacement_mean_fixed), np.array(df2.sst_mean_fixed), False)
        anti_corr_disp_sst = np.append(anti_corr_disp_sst, corr) 
        corr, pv = corr_coef(np.array(df2.ftle_mean_fixed), np.array(df2.sst_mean_fixed), False)
        anti_corr_ftle_sst = np.append(anti_corr_ftle_sst, corr) 
        corr, pv = corr_coef(np.array(df2.chl_mean_fixed), np.array(df2.sst_mean_fixed), True)
        anti_corr_chl_sst = np.append(anti_corr_chl_sst, corr) 
        corr, pv = corr_coef(np.array(df2.CO2_mean_surface), np.array(df2.sst_mean_fixed), True)
        anti_corr_co2_sst = np.append(anti_corr_co2_sst, corr) 

        corr, pv = corr_coef(np.array(df2.eddy_lat), np.array(df2.chl_mean_fixed), True)
        anti_corr_lat_chl = np.append(anti_corr_lat_chl, corr) 
        corr, pv = corr_coef(np.array(df2.eddy_lon), np.array(df2.chl_mean_fixed), True)
        anti_corr_lon_chl = np.append(anti_corr_lon_chl, corr) 
        corr, pv = corr_coef(np.array(df2.eddy_radius), np.array(df2.chl_mean_fixed), True)
        anti_corr_radius_chl = np.append(anti_corr_radius_chl, corr) 
        corr, pv = corr_coef(np.array(df2.phase_integ_fixed), np.array(df2.chl_mean_fixed), True)
        anti_corr_phase_chl = np.append(anti_corr_phase_chl, corr) 
        corr, pv = corr_coef(np.array(df2.sla_mean_fixed), np.array(df2.chl_mean_fixed), True)
        anti_corr_sla_chl = np.append(anti_corr_sla_chl, corr) 
        corr, pv = corr_coef(np.array(df2.vort_mean_fixed), np.array(df2.chl_mean_fixed), True)
        anti_corr_vort_chl = np.append(anti_corr_vort_chl, corr) 
        corr, pv = corr_coef(np.array(df2.displacement_mean_fixed), np.array(df2.chl_mean_fixed), True)
        anti_corr_disp_chl = np.append(anti_corr_disp_chl, corr) 
        corr, pv = corr_coef(np.array(df2.ftle_mean_fixed), np.array(df2.chl_mean_fixed), True)
        anti_corr_ftle_chl = np.append(anti_corr_ftle_chl, corr) 
        corr, pv = corr_coef(np.array(df2.sst_mean_fixed), np.array(df2.chl_mean_fixed), True)
        anti_corr_sst_chl = np.append(anti_corr_sst_chl, corr) 
        corr, pv = corr_coef(np.array(df2.CO2_mean_surface), np.array(df2.chl_mean_fixed), True)
        anti_corr_co2_chl = np.append(anti_corr_co2_chl, corr) 

        corr, pv = corr_coef(np.array(df2.eddy_lat), np.array(df2.CO2_mean_surface), True)
        anti_corr_lat_co2 = np.append(anti_corr_lat_co2, corr) 
        corr, pv = corr_coef(np.array(df2.eddy_lon), np.array(df2.CO2_mean_surface), True)
        anti_corr_lon_co2 = np.append(anti_corr_lon_co2, corr) 
        corr, pv = corr_coef(np.array(df2.eddy_radius), np.array(df2.CO2_mean_surface), True)
        anti_corr_radius_co2 = np.append(anti_corr_radius_co2, corr) 
        corr, pv = corr_coef(np.array(df2.phase_integ_fixed), np.array(df2.CO2_mean_surface), True)
        anti_corr_phase_co2 = np.append(anti_corr_phase_co2, corr) 
        corr, pv = corr_coef(np.array(df2.sla_mean_fixed), np.array(df2.CO2_mean_surface), True)
        anti_corr_sla_co2 = np.append(anti_corr_sla_co2, corr) 
        corr, pv = corr_coef(np.array(df2.vort_mean_fixed), np.array(df2.CO2_mean_surface), True)
        anti_corr_vort_co2 = np.append(anti_corr_vort_co2, corr) 
        corr, pv = corr_coef(np.array(df2.displacement_mean_fixed), np.array(df2.CO2_mean_surface), True)
        anti_corr_disp_co2 = np.append(anti_corr_disp_co2, corr) 
        corr, pv = corr_coef(np.array(df2.ftle_mean_fixed), np.array(df2.CO2_mean_surface), True)
        anti_corr_ftle_co2 = np.append(anti_corr_ftle_co2, corr) 
        corr, pv = corr_coef(np.array(df2.sst_mean_fixed), np.array(df2.CO2_mean_surface), True)
        anti_corr_sst_co2 = np.append(anti_corr_sst_co2, corr) 
        corr, pv = corr_coef(np.array(df2.chl_mean_fixed), np.array(df2.CO2_mean_surface), True)
        anti_corr_chl_co2 = np.append(anti_corr_chl_co2, corr) 


        ############### anomally correlations  ####################
        corr, pv = corr_coef(np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), np.array(df2.sst_mean_fixed)-np.array(df2.sst_mean_bkg), True)
        anti_corr_chl_sst_ano = np.append(anti_corr_chl_sst_ano, corr) 
        corr, pv = corr_coef(np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), np.array(df2.sst_mean_fixed)-np.array(df2.sst_mean_bkg), True)
        anti_corr_co2_sst_ano = np.append(anti_corr_co2_sst_ano, corr) 
        corr, pv = corr_coef(np.array(df2.sla_mean_fixed)-np.array(df2.sla_mean_bkg), np.array(df2.sst_mean_fixed)-np.array(df2.sst_mean_bkg), False)
        anti_corr_sla_sst_ano = np.append(anti_corr_sla_sst_ano, corr) 
        corr, pv = corr_coef(np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
        anti_corr_co2_chl_ano = np.append(anti_corr_co2_chl_ano, corr) 
        corr, pv = corr_coef(np.array(df2.sla_mean_fixed)-np.array(df2.sla_mean_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
        anti_corr_sla_chl_ano = np.append(anti_corr_sla_chl_ano, corr) 
        corr, pv = corr_coef(np.array(df2.sla_mean_fixed)-np.array(df2.sla_mean_bkg), np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), True)
        anti_corr_sla_co2_ano = np.append(anti_corr_sla_co2_ano, corr) 
        ###########################################################

        
        
    year = range(year1, year2+1) 
    plot_double_trend(year, corr_lat_sst, corr_lat_sst, corr_lat_sst, year, anti_corr_lat_sst, anti_corr_lat_sst, anti_corr_lat_sst, error_band, 'o--', 6, 'c', 'm', 'Year', 'lat-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_lat_sst.png')
    plot_double_trend(year, corr_lon_sst, corr_lon_sst, corr_lon_sst, year, anti_corr_lon_sst, anti_corr_lon_sst, anti_corr_lon_sst, error_band, 'o--', 6, 'c', 'm', 'Year', 'lon-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_lon_sst.png')
    plot_double_trend(year, corr_radius_sst, corr_radius_sst, corr_radius_sst, year, anti_corr_radius_sst, anti_corr_radius_sst, anti_corr_radius_sst, error_band, 'o--', 6, 'c', 'm', 'Year', 'radius-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_radius_sst.png')
    plot_double_trend(year, corr_phase_sst, corr_phase_sst, corr_phase_sst, year, anti_corr_phase_sst, anti_corr_phase_sst, anti_corr_phase_sst, error_band, 'o--', 6, 'c', 'm', 'Year', 'radius-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_phase_sst.png')
    plot_double_trend(year, corr_sla_sst, corr_sla_sst, corr_sla_sst, year, anti_corr_sla_sst, anti_corr_sla_sst, anti_corr_sla_sst, error_band, 'o--', 6, 'c', 'm', 'Year', 'sla-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sla_sst.png')
    plot_double_trend(year, corr_vort_sst, corr_vort_sst, corr_vort_sst, year, anti_corr_vort_sst, anti_corr_vort_sst, anti_corr_vort_sst, error_band, 'o--', 6, 'c', 'm', 'Year', 'vort-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_vort_sst.png')
    plot_double_trend(year, corr_disp_sst, corr_disp_sst, corr_disp_sst, year, anti_corr_disp_sst, anti_corr_disp_sst, anti_corr_disp_sst, error_band, 'o--', 6, 'c', 'm', 'Year', 'disp-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_disp_sst.png')
    plot_double_trend(year, corr_ftle_sst, corr_ftle_sst, corr_ftle_sst, year, anti_corr_ftle_sst, anti_corr_ftle_sst, anti_corr_ftle_sst, error_band, 'o--', 6, 'c', 'm', 'Year', 'ftle-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_ftle_sst.png')
    plot_double_trend(year, corr_chl_sst, corr_chl_sst, corr_chl_sst, year, anti_corr_chl_sst, anti_corr_chl_sst, anti_corr_chl_sst, error_band, 'o--', 6, 'c', 'm', 'Year', 'chl-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_chl_sst.png')
    plot_double_trend(year, corr_co2_sst, corr_co2_sst, corr_co2_sst, year, anti_corr_co2_sst, anti_corr_co2_sst, anti_corr_co2_sst, error_band, 'o--', 6, 'c', 'm', 'Year', 'fCO$_2$-sst corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_co2_sst.png')

    plot_double_trend(year, corr_lat_chl, corr_lat_chl, corr_lat_chl, year, anti_corr_lat_chl, anti_corr_lat_chl, anti_corr_lat_chl, error_band, 'o--', 6, 'c', 'm', 'Year', 'lat-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_lat_chl.png')
    plot_double_trend(year, corr_lon_chl, corr_lon_chl, corr_lon_chl, year, anti_corr_lon_chl, anti_corr_lon_chl, anti_corr_lon_chl, error_band, 'o--', 6, 'c', 'm', 'Year', 'lon-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_lon_chl.png')
    plot_double_trend(year, corr_radius_chl, corr_radius_chl, corr_radius_chl, year, anti_corr_radius_chl, anti_corr_radius_chl, anti_corr_radius_chl, error_band, 'o--', 6, 'c', 'm', 'Year', 'radius-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_radius_chl.png')
    plot_double_trend(year, corr_phase_chl, corr_phase_chl, corr_phase_chl, year, anti_corr_phase_chl, anti_corr_phase_chl, anti_corr_phase_chl, error_band, 'o--', 6, 'c', 'm', 'Year', 'radius-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_phase_chl.png')
    plot_double_trend(year, corr_sla_chl, corr_sla_chl, corr_sla_chl, year, anti_corr_sla_chl, anti_corr_sla_chl, anti_corr_sla_chl, error_band, 'o--', 6, 'c', 'm', 'Year', 'sla-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sla_chl.png')
    plot_double_trend(year, corr_vort_chl, corr_vort_chl, corr_vort_chl, year, anti_corr_vort_chl, anti_corr_vort_chl, anti_corr_vort_chl, error_band, 'o--', 6, 'c', 'm', 'Year', 'vort-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_vort_chl.png')
    plot_double_trend(year, corr_disp_chl, corr_disp_chl, corr_disp_chl, year, anti_corr_disp_chl, anti_corr_disp_chl, anti_corr_disp_chl, error_band, 'o--', 6, 'c', 'm', 'Year', 'disp-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_disp_chl.png')
    plot_double_trend(year, corr_ftle_chl, corr_ftle_chl, corr_ftle_chl, year, anti_corr_ftle_chl, anti_corr_ftle_chl, anti_corr_ftle_chl, error_band, 'o--', 6, 'c', 'm', 'Year', 'ftle-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_ftle_chl.png')
    plot_double_trend(year, corr_sst_chl, corr_sst_chl, corr_sst_chl, year, anti_corr_sst_chl, anti_corr_sst_chl, anti_corr_sst_chl, error_band, 'o--', 6, 'c', 'm', 'Year', 'sst-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sst_chl.png')
    plot_double_trend(year, corr_co2_chl, corr_co2_chl, corr_co2_chl, year, anti_corr_co2_chl, anti_corr_co2_chl, anti_corr_co2_chl, error_band, 'o--', 6, 'c', 'm', 'Year', 'fCO$_2$-chl corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_co2_chl.png')

    plot_double_trend(year, corr_lat_co2, corr_lat_co2, corr_lat_co2, year, anti_corr_lat_co2, anti_corr_lat_co2, anti_corr_lat_co2, error_band, 'o--', 6, 'c', 'm', 'Year', 'lat-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_lat_co2.png')
    plot_double_trend(year, corr_lon_co2, corr_lon_co2, corr_lon_co2, year, anti_corr_lon_co2, anti_corr_lon_co2, anti_corr_lon_co2, error_band, 'o--', 6, 'c', 'm', 'Year', 'lon-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_lon_co2.png')
    plot_double_trend(year, corr_radius_co2, corr_radius_co2, corr_radius_co2, year, anti_corr_radius_co2, anti_corr_radius_co2, anti_corr_radius_co2, error_band, 'o--', 6, 'c', 'm', 'Year', 'radius-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_radius_co2.png')
    plot_double_trend(year, corr_phase_co2, corr_phase_co2, corr_phase_co2, year, anti_corr_phase_co2, anti_corr_phase_co2, anti_corr_phase_co2, error_band, 'o--', 6, 'c', 'm', 'Year', 'radius-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_phase_co2.png')
    plot_double_trend(year, corr_sla_co2, corr_sla_co2, corr_sla_co2, year, anti_corr_sla_co2, anti_corr_sla_co2, anti_corr_sla_co2, error_band, 'o--', 6, 'c', 'm', 'Year', 'sla-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sla_co2.png')
    plot_double_trend(year, corr_vort_co2, corr_vort_co2, corr_vort_co2, year, anti_corr_vort_co2, anti_corr_vort_co2, anti_corr_vort_co2, error_band, 'o--', 6, 'c', 'm', 'Year', 'vort-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_vort_co2.png')
    plot_double_trend(year, corr_disp_co2, corr_disp_co2, corr_disp_co2, year, anti_corr_disp_co2, anti_corr_disp_co2, anti_corr_disp_co2, error_band, 'o--', 6, 'c', 'm', 'Year', 'disp-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_disp_co2.png')
    plot_double_trend(year, corr_ftle_co2, corr_ftle_co2, corr_ftle_co2, year, anti_corr_ftle_co2, anti_corr_ftle_co2, anti_corr_ftle_co2, error_band, 'o--', 6, 'c', 'm', 'Year', 'ftle-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_ftle_co2.png')
    plot_double_trend(year, corr_sst_co2, corr_sst_co2, corr_sst_co2, year, anti_corr_sst_co2, anti_corr_sst_co2, anti_corr_sst_co2, error_band, 'o--', 6, 'c', 'm', 'Year', 'sst-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sst_co2.png')
    plot_double_trend(year, corr_chl_co2, corr_chl_co2, corr_chl_co2, year, anti_corr_chl_co2, anti_corr_chl_co2, anti_corr_chl_co2, error_band, 'o--', 6, 'c', 'm', 'Year', 'chl-fCO$_2$ corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_chl_co2.png')



    ############### anomally correlations  ####################
    plot_double_trend(year, corr_sla_sst_ano, corr_sla_sst_ano, corr_sla_sst_ano, year, anti_corr_sla_sst_ano, anti_corr_sla_sst_ano, anti_corr_sla_sst_ano, error_band, 'o--', 6, 'c', 'm', 'Year', 'sla-sst anomally corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sla_sst_ano.png')
    plot_double_trend(year, corr_chl_sst_ano, corr_chl_sst_ano, corr_chl_sst_ano, year, anti_corr_chl_sst_ano, anti_corr_chl_sst_ano, anti_corr_chl_sst_ano, error_band, 'o--', 6, 'c', 'm', 'Year', 'chl-sst anomally corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_chl_sst_ano.png')
    plot_double_trend(year, corr_co2_sst_ano, corr_co2_sst_ano, corr_co2_sst_ano, year, anti_corr_co2_sst_ano, anti_corr_co2_sst_ano, anti_corr_co2_sst_ano, error_band, 'o--', 6, 'c', 'm', 'Year', 'fCO$_2$-sst anomally corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_co2_sst_ano.png')
    plot_double_trend(year, corr_sla_chl_ano, corr_sla_chl_ano, corr_sla_chl_ano, year, anti_corr_sla_chl_ano, anti_corr_sla_chl_ano, anti_corr_sla_chl_ano, error_band, 'o--', 6, 'c', 'm', 'Year', 'sla-chl anomally corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sla_chl_ano.png')
    plot_double_trend(year, corr_co2_chl_ano, corr_co2_chl_ano, corr_co2_chl_ano, year, anti_corr_co2_chl_ano, anti_corr_co2_chl_ano, anti_corr_co2_chl_ano, error_band, 'o--', 6, 'c', 'm', 'Year', 'fCO$_2$-chl anomally corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_co2_chl_ano.png')
    plot_double_trend(year, corr_sla_co2_ano, corr_sla_co2_ano, corr_sla_co2_ano, year, anti_corr_sla_co2_ano, anti_corr_sla_co2_ano, anti_corr_sla_co2_ano, error_band, 'o--', 6, 'c', 'm', 'Year', 'sla-fCO$_2$ anomally corr. coef.', 'Cyclonic', 'Anti-Cyclonic', 'gallery/cc_sla_co2_ano.png')
    ###########################################################
    return    


def spatial_map_ex(eddy_lon, eddy_lat, vals, minlat, maxlat, minlon, maxlon, spacing, store_path='', title='', bounds=None, cleanup=False, col_map='jet'):
    '''
    try:
        spacing = 20
        minlat = -90
        maxlat = 90
        minlon = -180
        maxlon = 180
    
        if cleanup:
            x = np.array([])
            y = np.array([])
            z = np.array([])
            for i in range(0, len(eddy_lon)):
                if eddy_lon[i] <> None and eddy_lat[i] <> None and vals[i] <> None:
                    if (not math.isnan(eddy_lon[i])) and (not math.isnan(eddy_lat[i])) and (not math.isnan(vals[i])):
                        x = np.append(x, eddy_lon[i])
                        y = np.append(y, eddy_lat[i])
                        z = np.append(z, vals[i])
            eddy_lon = x
            eddy_lat = y                
            vals = z                
    
    
        plt.clf()
    
        eddy_lon[np.where(eddy_lon>180)] = eddy_lon[np.where(eddy_lon>180)] - 360        
        if minlon>180:
            minlon = minlon - 360
        if maxlon>180:
            maxlon = maxlon - 360
    
        ################ Projection  #################
        #map = Basemap(projection='kav7', lon_0=0, resolution='l')
        #map = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='l')
    
    
        #if minlon * maxlon < 0:
        #    map = Basemap(projection='mill', llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=minlon, urcrnrlon=maxlon, resolution='l')
        #else:    
        #    map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=minlon, urcrnrlon=maxlon,\
        #        rsphere=(6378137.00,6356752.3142),\
        #        resolution='l',area_thresh=1000.,projection='lcc',\
        #        lat_1=maxlat,lon_0=(maxlon+minlon)/2)
       
        map = Basemap(projection='mill', llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=minlon, urcrnrlon=maxlon, resolution='l')
    
        ##############################################
        
        
        #map.drawcoastlines(linewidth=0.5)
        map.fillcontinents(color='#333333', lake_color='#333333')
        
        #map.drawparallels(np.arange(-90.,90.,30.), linewidth=.5, color=[.2,.2,.2], labels=[1,1,0,0], fontsize=5)
        #map.drawmeridians(np.arange(-180.,180.,60.), linewidth=.5, color=[.2,.2,.2], labels=[0,0,0,1], fontsize=5)
    
        map.drawparallels(np.arange(minlat,maxlat, spacing ), linewidth=.5, color=[.2,.2,.2], labels=[1,1,0,0], fontsize=5)
        map.drawmeridians(np.arange(minlon,maxlon, spacing ), linewidth=.5, color=[.2,.2,.2], labels=[0,0,0,1], fontsize=5)
    
        ##############   Map Background  ##############
        #map.bluemarble()
        #map.shadedrelief()
        #map.etopo()
        ##############################################
        if bounds == None:
            bounds = [np.nanpercentile(vals, 5), np.nanpercentile(vals, 95)]
            
        #eddy_lon[np.where(eddy_lon>180)] = eddy_lon[np.where(eddy_lon>180)] - 360
        x_map, y_map = map(eddy_lon, eddy_lat)
    
    
        cm = plt.cm.get_cmap(col_map)    
        sc = map.scatter(x_map, y_map, c=vals, vmin=bounds[0], vmax=bounds[1], cmap=cm, lw=0, marker='s', s=1.5) #, s=5
        map.colorbar(sc, 'bottom', size='5%', pad='7%')
        if len(title) > 0:
            plt.title(title)
        
        if len(store_path) > 0:
            plt.savefig(store_path, bbox_inches='tight' , dpi=300, transparent=plot_transparency)
    except Exception as e:
        print('Error in spatial_map_ex. Error message: '+str(e))

    '''
    try:
        if len(store_path) > 0:
            np.savez(store_path.split('.png')[0]+'.npz', eddy_lon=eddy_lon, eddy_lat=eddy_lat, vals=vals)
    except Exception as e:
        print('Error in spatial_map_ex (saving npz file). Error message: '+str(e))
        

    return



def hovmoller_plot(X, Y, V, store_path='', title='', col_map='jet'):
    plt.clf()        
    cp = plt.contourf(X, Y, V, cmap=col_map)
    plt.colorbar(cp)
    
    plt.xlabel('Year')
    plt.ylabel('Latitude')
    if len(title) > 0:
        plt.title(title)


    if len(store_path) > 0:
        plt.savefig(store_path, bbox_inches='tight' , dpi=300, transparent=plot_transparency)

    try:
        if len(store_path) > 0:
            np.savez(store_path.split('.png')[0]+'.npz', X=X, Y=Y, V=V)
    except Exception as e:
        print('Error in hovmoller_plot (saving npz file). Error message: '+str(e))
        

    return


def remove_spatial_conditions(query):
    res = []
    sp = query.split()
    for i in range(0, len(sp)):
        if sp[i].lower().find('eddy_lon')<0 and sp[i].lower().find('eddy_lat')<0:
            if sp[i].upper().find('AND')>=0 and (sp[i+1].lower().find('eddy_lon')>=0 or sp[i+1].lower().find('eddy_lat')>=0):
                continue
            if sp[i].upper().find('AND')>=0 and res[-1].upper().find('WHERE')>=0:
                continue
            res.append(sp[i])
    res = ' '.join(res)            
    return res
    

def diff_percent(val1, val2):    
    diffper = 100 * (np.nanmedian(val1) - np.nanmedian(val2))
    m = (np.nanmedian(val1) + np.nanmedian(val2)) / 2
    try:
        diffper = diffper / m
    except:
        diffper = np.nan
    return diffper


def spatially_averaged_monthly_series(query):
    '''
    ######## hawaii
    minlat = 19
    maxlat = 49
    minlon = 190
    maxlon = 220
    ################
    '''

    minlat = -80
    maxlat = 70
    minlon = 0
    maxlon = 360
    
    spacing = 5.
    query = remove_spatial_conditions(query)
    lats = np.arange(minlat+spacing/2., maxlat, spacing)
    lons = np.arange(minlon+spacing/2., maxlon, spacing)
    base_query = query
    
    month1 = 1
    month2 = 12
    month_name = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    for temporal in range(month1, month2+1):
    #for temporal in np.array([1,7,2,8,3,9,4,10,5,11,6,12]):
        query = base_query
        if query.find('WHERE') >= 0:
            query = query + ' AND month=' + str(temporal)
        else:        
            query = query + ' WHERE month=' + str(temporal)

        query_temporal = query 
        tile_lats = np.array([])
        tile_lons = np.array([])


        cyc_n = np.array([])
        cyc_n_up = np.array([])
        cyc_n_down = np.array([])
        lat = np.array([])
        lat_up = np.array([])
        lat_down = np.array([])
        lon = np.array([])
        lon_up = np.array([])
        lon_down = np.array([])
        radius = np.array([])
        radius_up = np.array([])
        radius_down = np.array([])
        phase = np.array([])
        phase_up = np.array([])
        phase_down = np.array([])
        sla = np.array([])
        sla_up = np.array([])
        sla_down = np.array([])
        vort = np.array([])
        vort_up = np.array([])
        vort_down = np.array([])
        disp = np.array([])
        disp_up = np.array([])
        disp_down = np.array([])
        ftle = np.array([])
        ftle_up = np.array([])
        ftle_down = np.array([])
        sst = np.array([])
        sst_up = np.array([])
        sst_down = np.array([])
        chl = np.array([])
        chl_up = np.array([])
        chl_down = np.array([])
        co2 = np.array([])
        co2_up = np.array([])
        co2_down = np.array([])
        mld = np.array([])
        mld_up = np.array([])
        mld_down = np.array([])
        sss = np.array([])
        sss_up = np.array([])
        sss_down = np.array([])
        
    
        ano_phase = np.array([])
        ano_phase_up = np.array([])
        ano_phase_down = np.array([])
        ano_sla = np.array([])
        ano_sla_up = np.array([])
        ano_sla_down = np.array([])
        ano_vort = np.array([])
        ano_vort_up = np.array([])
        ano_vort_down = np.array([])
        ano_disp = np.array([])
        ano_disp_up = np.array([])
        ano_disp_down = np.array([])
        ano_ftle = np.array([])
        ano_ftle_up = np.array([])
        ano_ftle_down = np.array([])
        ano_sst = np.array([])
        ano_sst_up = np.array([])
        ano_sst_down = np.array([])
        ano_chl = np.array([])
        ano_chl_up = np.array([])
        ano_chl_down = np.array([])
        ano_co2 = np.array([])
        ano_co2_up = np.array([])
        ano_co2_down = np.array([])
        ano_mld = np.array([])
        ano_mld_up = np.array([])
        ano_mld_down = np.array([])
        ano_sss = np.array([])
        ano_sss_up = np.array([])
        ano_sss_down = np.array([])
    
        ######## anomally correlations ######
        corr_chl_sst_ano = np.array([]) 
        corr_co2_sst_ano = np.array([])
        corr_sla_sst_ano = np.array([])
        corr_co2_chl_ano = np.array([])
        corr_sla_chl_ano = np.array([])
        corr_sla_co2_ano = np.array([])        
        corr_sla_chl_ano2 = np.array([])        
        corr_vort_chl_ano = np.array([])
        corr_disp_chl_ano = np.array([])
        corr_ftle_chl_ano = np.array([])

        corr_mld_sla_ano = np.array([])
        corr_mld_sst_ano = np.array([])
        corr_mld_sss_ano = np.array([])
        corr_mld_chl_ano = np.array([])
        corr_mld_co2_ano = np.array([])        


        corr_chl_sst_ano_sig = np.array([]) 
        corr_co2_sst_ano_sig = np.array([])
        corr_sla_sst_ano_sig = np.array([])
        corr_co2_chl_ano_sig = np.array([])
        corr_sla_chl_ano_sig = np.array([])
        corr_sla_co2_ano_sig = np.array([])        
        corr_sla_chl_ano2_sig = np.array([])
        corr_vort_chl_ano_sig = np.array([])
        corr_disp_chl_ano_sig = np.array([])
        corr_ftle_chl_ano_sig = np.array([])

        corr_mld_sla_ano_sig = np.array([])
        corr_mld_sst_ano_sig = np.array([])
        corr_mld_sss_ano_sig = np.array([])
        corr_mld_chl_ano_sig = np.array([])
        corr_mld_co2_ano_sig = np.array([])        
        #####################################
    

        anti_cyc_n = np.array([])
        anti_cyc_n_up = np.array([])
        anti_cyc_n_down = np.array([])
        anti_lat = np.array([])
        anti_lat_up = np.array([])
        anti_lat_down = np.array([])
        anti_lon = np.array([])
        anti_lon_up = np.array([])
        anti_lon_down = np.array([])
        anti_radius = np.array([])
        anti_radius_up = np.array([])
        anti_radius_down = np.array([])
        anti_phase = np.array([])
        anti_phase_up = np.array([])
        anti_phase_down = np.array([])
        anti_sla = np.array([])
        anti_sla_up = np.array([])
        anti_sla_down = np.array([])
        anti_vort = np.array([])
        anti_vort_up = np.array([])
        anti_vort_down = np.array([])
        anti_disp = np.array([])
        anti_disp_up = np.array([])
        anti_disp_down = np.array([])
        anti_ftle = np.array([])
        anti_ftle_up = np.array([])
        anti_ftle_down = np.array([])
        anti_sst = np.array([])
        anti_sst_up = np.array([])
        anti_sst_down = np.array([])
        anti_chl = np.array([])
        anti_chl_up = np.array([])
        anti_chl_down = np.array([])
        anti_co2 = np.array([])
        anti_co2_up = np.array([])
        anti_co2_down = np.array([])
        anti_mld = np.array([])
        anti_mld_up = np.array([])
        anti_mld_down = np.array([])
        anti_sss = np.array([])
        anti_sss_up = np.array([])
        anti_sss_down = np.array([])
    
        anti_ano_phase = np.array([])
        anti_ano_phase_up = np.array([])
        anti_ano_phase_down = np.array([])
        anti_ano_sla = np.array([])
        anti_ano_sla_up = np.array([])
        anti_ano_sla_down = np.array([])
        anti_ano_vort = np.array([])
        anti_ano_vort_up = np.array([])
        anti_ano_vort_down = np.array([])
        anti_ano_disp = np.array([])
        anti_ano_disp_up = np.array([])
        anti_ano_disp_down = np.array([])
        anti_ano_ftle = np.array([])
        anti_ano_ftle_up = np.array([])
        anti_ano_ftle_down = np.array([])
        anti_ano_sst = np.array([])
        anti_ano_sst_up = np.array([])
        anti_ano_sst_down = np.array([])
        anti_ano_chl = np.array([])
        anti_ano_chl_up = np.array([])
        anti_ano_chl_down = np.array([])
        anti_ano_co2 = np.array([])
        anti_ano_co2_up = np.array([])
        anti_ano_co2_down = np.array([])
        anti_ano_mld = np.array([])
        anti_ano_mld_up = np.array([])
        anti_ano_mld_down = np.array([])
        anti_ano_sss = np.array([])
        anti_ano_sss_up = np.array([])
        anti_ano_sss_down = np.array([])


        ######## anomally correlations ######
        anti_corr_chl_sst_ano = np.array([]) 
        anti_corr_co2_sst_ano = np.array([])
        anti_corr_sla_sst_ano = np.array([])
        anti_corr_co2_chl_ano = np.array([])
        anti_corr_sla_chl_ano = np.array([])
        anti_corr_sla_co2_ano = np.array([])        
        anti_corr_sla_chl_ano2 = np.array([])
        anti_corr_vort_chl_ano = np.array([])
        anti_corr_disp_chl_ano = np.array([])
        anti_corr_ftle_chl_ano = np.array([])

        anti_corr_mld_sla_ano = np.array([])
        anti_corr_mld_sst_ano = np.array([])
        anti_corr_mld_sss_ano = np.array([])
        anti_corr_mld_chl_ano = np.array([])
        anti_corr_mld_co2_ano = np.array([])        


        anti_corr_chl_sst_ano_sig = np.array([]) 
        anti_corr_co2_sst_ano_sig = np.array([])
        anti_corr_sla_sst_ano_sig = np.array([])
        anti_corr_co2_chl_ano_sig = np.array([])
        anti_corr_sla_chl_ano_sig = np.array([])
        anti_corr_sla_co2_ano_sig = np.array([])        
        anti_corr_sla_chl_ano2_sig = np.array([])
        anti_corr_vort_chl_ano_sig = np.array([])
        anti_corr_disp_chl_ano_sig = np.array([])
        anti_corr_ftle_chl_ano_sig = np.array([])

        anti_corr_mld_sla_ano_sig = np.array([])
        anti_corr_mld_sst_ano_sig = np.array([])
        anti_corr_mld_sss_ano_sig = np.array([])
        anti_corr_mld_chl_ano_sig = np.array([])
        anti_corr_mld_co2_ano_sig = np.array([])        
        #####################################


        diff_disp = np.array([])
        diff_ftle = np.array([])
        diff_sst = np.array([])
        diff_chl = np.array([])
        diff_chl_full = np.array([])
        diff_co2 = np.array([])

        diff_mld = np.array([])
        diff_sss = np.array([])

        diff_disp_ano = np.array([])
        diff_ftle_ano = np.array([])
        diff_sst_ano = np.array([])
        diff_chl_ano = np.array([])
        diff_chl_full_ano = np.array([])
        diff_co2_ano = np.array([])

        diff_mld_ano = np.array([])
        diff_sss_ano = np.array([])

        counter = 0
        for midlat in lats:
            for midlon in lons:
                counter += 1
                print('Cycle: %d, Progress: %2.2f%s ' % (temporal, 100.*counter/(len(lats)*len(lons)), '%'))
                
                ulat = midlat + spacing/2.
                llat = midlat - spacing/2.
                ulon = midlon + spacing/2.
                llon = midlon - spacing/2.
                query = query_temporal + ' AND eddy_lat>='+str(llat) + ' AND eddy_lat<='+str(ulat)+ ' AND eddy_lon>='+str(llon) + ' AND eddy_lon<='+str(ulon)            
                query1 = query + ' AND eddy_polarity=1'
                query2 = query + ' AND eddy_polarity=-1'
                conn = db_connect()
                df1 = sql.read_sql(query1, conn)
                conn.close()
                conn = db_connect()
                df2 = sql.read_sql(query2, conn)
                conn.close()
                if len(df1)<1 or len(df2)<1:
                    #print('No match found. len(df1): '+str(len(df1))+' len(df2): '+str(len(df2)))
                    continue                
                df1 = df1.fillna(float('NaN'))
                df2 = df2.fillna(float('NaN'))                    

                tile_lats = np.append(tile_lats, midlat)
                tile_lons = np.append(tile_lons, midlon)

                cyc_n, cyc_n_up, cyc_n_down = append_range(cyc_n, cyc_n_up, cyc_n_down, len(np.array(df1.year)))
                lat, lat_up, lat_down = append_range(lat, lat_up, lat_down, df1.eddy_lat)
                lon, lon_up, lon_down = append_range(lon, lon_up, lon_down, df1.eddy_lon)
                radius, radius_up, radius_down = append_range(radius, radius_up, radius_down, df1.eddy_radius)
                phase, phase_up, phase_down = append_range(phase, phase_up, phase_down, df1.phase_integ_fixed)
                sla, sla_up, sla_down = append_range(sla, sla_up, sla_down, df1.sla_mean_fixed)
                vort, vort_up, vort_down = append_range(vort, vort_up, vort_down, df1.vort_mean_fixed)
                disp, disp_up, disp_down = append_range(disp, disp_up, disp_down, df1.displacement_mean_fixed)
                ftle, ftle_up, ftle_down = append_range(ftle, ftle_up, ftle_down, df1.ftle_mean_fixed)
                sst, sst_up, sst_down = append_range(sst, sst_up, sst_down, df1.sst_mean_fixed)
                chl, chl_up, chl_down = append_range(chl, chl_up, chl_down, df1.chl_mean_fixed)
                co2, co2_up, co2_down = append_range(co2, co2_up, co2_down, df1.CO2_mean_surface)
                mld, mld_up, mld_down = append_range(mld, mld_up, mld_down, df1.mld_mean_fixed)
                sss, sss_up, sss_down = append_range(sss, sss_up, sss_down, df1.sss_mean_fixed)
                                
                ano_phase, ano_phase_up, ano_phase_down = append_range(ano_phase, ano_phase_up, ano_phase_down, 100 * (df1.phase_integ_fixed - df1.phase_mean_bkg) / df1.phase_mean_bkg)
                ano_sla, ano_sla_up, ano_sla_down = append_range(ano_sla, ano_sla_up, ano_sla_down, 100 * (df1.sla_mean_fixed - df1.sla_mean_bkg) / df1.sla_mean_bkg)
                ano_vort, ano_vort_up, ano_vort_down = append_range(ano_vort, ano_vort_up, ano_vort_down, 100 * (df1.vort_mean_fixed - df1.vort_mean_bkg) / df1.vort_mean_bkg)
                ano_disp, ano_disp_up, ano_disp_down = append_range(ano_disp, ano_disp_up, ano_disp_down, 100 * (df1.displacement_mean_fixed - df1.displacement_mean_bkg) / df1.displacement_mean_bkg)
                ano_ftle, ano_ftle_up, ano_ftle_down = append_range(ano_ftle, ano_ftle_up, ano_ftle_down, 100 * (df1.ftle_mean_fixed - df1.ftle_mean_bkg) / df1.ftle_mean_bkg)
                ano_sst, ano_sst_up, ano_sst_down = append_range(ano_sst, ano_sst_up, ano_sst_down, 100 * (df1.sst_mean_fixed - df1.sst_mean_bkg) / df1.sst_mean_bkg)
                ano_chl, ano_chl_up, ano_chl_down = append_range(ano_chl, ano_chl_up, ano_chl_down, 100 * (df1.chl_mean_fixed - df1.chl_mean_bkg) / df1.chl_mean_bkg)
                ano_co2, ano_co2_up, ano_co2_down = append_range(ano_co2, ano_co2_up, ano_co2_down, 100 * (df1.CO2_mean_surface - df1.CO2_mean_surface_bkg) / df1.CO2_mean_surface_bkg)
                ano_mld, ano_mld_up, ano_mld_down = append_range(ano_mld, ano_mld_up, ano_mld_down, 100 * (df1.mld_mean_fixed - df1.mld_mean_bkg) / df1.mld_mean_bkg)
                ano_sss, ano_sss_up, ano_sss_down = append_range(ano_sss, ano_sss_up, ano_sss_down, 100 * (df1.sss_mean_fixed - df1.sss_mean_bkg) / df1.sss_mean_bkg)
                

                ############### anomally correlations  ####################
                corr, sig = corr_coef(np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), np.array(df1.sst_mean_fixed)-np.array(df1.sst_mean_bkg), True)
                corr_chl_sst_ano = np.append(corr_chl_sst_ano, corr) 
                corr_chl_sst_ano_sig = np.append(corr_chl_sst_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), np.array(df1.sst_mean_fixed)-np.array(df1.sst_mean_bkg), True)
                corr_co2_sst_ano = np.append(corr_co2_sst_ano, corr) 
                corr_co2_sst_ano_sig = np.append(corr_co2_sst_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.sla_mean_fixed)-np.array(df1.sla_mean_bkg), np.array(df1.sst_mean_fixed)-np.array(df1.sst_mean_bkg), False)
                corr_sla_sst_ano = np.append(corr_sla_sst_ano, corr) 
                corr_sla_sst_ano_sig = np.append(corr_sla_sst_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
                corr_co2_chl_ano = np.append(corr_co2_chl_ano, corr) 
                corr_co2_chl_ano_sig = np.append(corr_co2_chl_ano, sig) 
                corr, sig = corr_coef(np.array(df1.sla_mean_fixed)-np.array(df1.sla_mean_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
                corr_sla_chl_ano = np.append(corr_sla_chl_ano, corr) 
                corr_sla_chl_ano_sig = np.append(corr_sla_chl_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.sla_mean_fixed)-np.array(df1.sla_mean_bkg), np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), True)
                corr_sla_co2_ano = np.append(corr_sla_co2_ano, corr) 
                corr_sla_co2_ano_sig = np.append(corr_sla_co2_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.sla_mean_fixed), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
                corr_sla_chl_ano2 = np.append(corr_sla_chl_ano2, corr) 
                corr_sla_chl_ano2_sig = np.append(corr_sla_chl_ano2_sig, sig) 
                corr, sig = corr_coef(np.array(df1.vort_mean_fixed)-np.array(df1.vort_mean_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
                corr_vort_chl_ano = np.append(corr_vort_chl_ano, corr) 
                corr_vort_chl_ano_sig = np.append(corr_vort_chl_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.displacement_mean_fixed)-np.array(df1.displacement_mean_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
                corr_disp_chl_ano = np.append(corr_disp_chl_ano, corr) 
                corr_disp_chl_ano_sig = np.append(corr_disp_chl_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.ftle_mean_fixed)-np.array(df1.ftle_mean_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
                corr_ftle_chl_ano = np.append(corr_ftle_chl_ano, corr) 
                corr_ftle_chl_ano_sig = np.append(corr_ftle_chl_ano_sig, sig) 


                corr, sig = corr_coef(np.array(df1.mld_mean_fixed)-np.array(df1.mld_mean_bkg), np.array(df1.sla_mean_fixed)-np.array(df1.sla_mean_bkg), True)
                corr_mld_sla_ano = np.append(corr_mld_sla_ano, corr) 
                corr_mld_sla_ano_sig = np.append(corr_mld_sla_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.mld_mean_fixed)-np.array(df1.mld_mean_bkg), np.array(df1.sst_mean_fixed)-np.array(df1.sst_mean_bkg), True)
                corr_mld_sst_ano = np.append(corr_mld_sst_ano, corr) 
                corr_mld_sst_ano_sig = np.append(corr_mld_sst_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.mld_mean_fixed)-np.array(df1.mld_mean_bkg), np.array(df1.sss_mean_fixed)-np.array(df1.sss_mean_bkg), True)
                corr_mld_sss_ano = np.append(corr_mld_sss_ano, corr) 
                corr_mld_sss_ano_sig = np.append(corr_mld_sss_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.mld_mean_fixed)-np.array(df1.mld_mean_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
                corr_mld_chl_ano = np.append(corr_mld_chl_ano, corr) 
                corr_mld_chl_ano_sig = np.append(corr_mld_chl_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.mld_mean_fixed)-np.array(df1.mld_mean_bkg), np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), True)
                corr_mld_co2_ano = np.append(corr_mld_co2_ano, corr) 
                corr_mld_co2_ano_sig = np.append(corr_mld_co2_ano_sig, sig) 
                ###########################################################


                anti_cyc_n, anti_cyc_n_up, anti_cyc_n_down = append_range(anti_cyc_n, anti_cyc_n_up, anti_cyc_n_down, len(np.array(df2.year)))
                anti_lat, anti_lat_up, anti_lat_down = append_range(anti_lat, anti_lat_up, anti_lat_down, df2.eddy_lat)
                anti_lon, anti_lon_up, anti_lon_down = append_range(anti_lon, anti_lon_up, anti_lon_down, df2.eddy_lon)
                anti_radius, anti_radius_up, anti_radius_down = append_range(anti_radius, anti_radius_up, anti_radius_down, df2.eddy_radius)
                anti_phase, anti_phase_up, anti_phase_down = append_range(anti_phase, anti_phase_up, anti_phase_down, df2.phase_integ_fixed)
                anti_sla, anti_sla_up, anti_sla_down = append_range(anti_sla, anti_sla_up, anti_sla_down, df2.sla_mean_fixed)
                anti_vort, anti_vort_up, anti_vort_down = append_range(anti_vort, anti_vort_up, anti_vort_down, df2.vort_mean_fixed)
                anti_disp, anti_disp_up, anti_disp_down = append_range(anti_disp, anti_disp_up, anti_disp_down, df2.displacement_mean_fixed)
                anti_ftle, anti_ftle_up, anti_ftle_down = append_range(anti_ftle, anti_ftle_up, anti_ftle_down, df2.ftle_mean_fixed)
                anti_sst, anti_sst_up, anti_sst_down = append_range(anti_sst, anti_sst_up, anti_sst_down, df2.sst_mean_fixed)
                anti_chl, anti_chl_up, anti_chl_down = append_range(anti_chl, anti_chl_up, anti_chl_down, df2.chl_mean_fixed)
                anti_co2, anti_co2_up, anti_co2_down = append_range(anti_co2, anti_co2_up, anti_co2_down, df2.CO2_mean_surface)                
                anti_mld, anti_mld_up, anti_mld_down = append_range(anti_mld, anti_mld_up, anti_mld_down, df2.mld_mean_fixed)
                anti_sss, anti_sss_up, anti_sss_down = append_range(anti_sss, anti_sss_up, anti_sss_down, df2.sss_mean_fixed)

                anti_ano_phase, anti_ano_phase_up, anti_ano_phase_down = append_range(anti_ano_phase, anti_ano_phase_up, anti_ano_phase_down, 100 * (df2.phase_integ_fixed - df2.phase_mean_bkg) / df2.phase_mean_bkg)
                anti_ano_sla, anti_ano_sla_up, anti_ano_sla_down = append_range(anti_ano_sla, anti_ano_sla_up, anti_ano_sla_down, 100 * (df2.sla_mean_fixed - df2.sla_mean_bkg) / df2.sla_mean_bkg)
                anti_ano_vort, anti_ano_vort_up, anti_ano_vort_down = append_range(anti_ano_vort, anti_ano_vort_up, anti_ano_vort_down, 100 * (df2.vort_mean_fixed - df2.vort_mean_bkg) / df2.vort_mean_bkg)
                anti_ano_disp, anti_ano_disp_up, anti_ano_disp_down = append_range(anti_ano_disp, anti_ano_disp_up, anti_ano_disp_down, 100 * (df2.displacement_mean_fixed - df2.displacement_mean_bkg) / df2.displacement_mean_bkg)
                anti_ano_ftle, anti_ano_ftle_up, anti_ano_ftle_down = append_range(anti_ano_ftle, anti_ano_ftle_up, anti_ano_ftle_down, 100 * (df2.ftle_mean_fixed - df2.ftle_mean_bkg) / df2.ftle_mean_bkg)
                anti_ano_sst, anti_ano_sst_up, anti_ano_sst_down = append_range(anti_ano_sst, anti_ano_sst_up, anti_ano_sst_down, 100 * (df2.sst_mean_fixed - df2.sst_mean_bkg) / df2.sst_mean_bkg)
                anti_ano_chl, anti_ano_chl_up, anti_ano_chl_down = append_range(anti_ano_chl, anti_ano_chl_up, anti_ano_chl_down, 100 * (df2.chl_mean_fixed - df2.chl_mean_bkg) / df2.chl_mean_bkg)
                anti_ano_co2, anti_ano_co2_up, anti_ano_co2_down = append_range(anti_ano_co2, anti_ano_co2_up, anti_ano_co2_down, 100 * (df2.CO2_mean_surface - df2.CO2_mean_surface_bkg) / df2.CO2_mean_surface_bkg)                
                anti_ano_mld, anti_ano_mld_up, anti_ano_mld_down = append_range(anti_ano_mld, anti_ano_mld_up, anti_ano_mld_down, 100 * (df2.mld_mean_fixed - df2.mld_mean_bkg) / df2.mld_mean_bkg)
                anti_ano_sss, anti_ano_sss_up, anti_ano_sss_down = append_range(anti_ano_sss, anti_ano_sss_up, anti_ano_sss_down, 100 * (df2.sss_mean_fixed - df2.sss_mean_bkg) / df2.sss_mean_bkg)

                ############### anomally correlations  ####################
                corr, sig = corr_coef(np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), np.array(df2.sst_mean_fixed)-np.array(df2.sst_mean_bkg), True)
                anti_corr_chl_sst_ano = np.append(anti_corr_chl_sst_ano, corr) 
                anti_corr_chl_sst_ano_sig = np.append(anti_corr_chl_sst_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), np.array(df2.sst_mean_fixed)-np.array(df2.sst_mean_bkg), True)
                anti_corr_co2_sst_ano = np.append(anti_corr_co2_sst_ano, corr) 
                anti_corr_co2_sst_ano_sig = np.append(anti_corr_co2_sst_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.sla_mean_fixed)-np.array(df2.sla_mean_bkg), np.array(df2.sst_mean_fixed)-np.array(df2.sst_mean_bkg), False)
                anti_corr_sla_sst_ano = np.append(anti_corr_sla_sst_ano, corr) 
                anti_corr_sla_sst_ano_sig = np.append(anti_corr_sla_sst_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
                anti_corr_co2_chl_ano = np.append(anti_corr_co2_chl_ano, corr) 
                anti_corr_co2_chl_ano_sig = np.append(anti_corr_co2_chl_ano_sig, corr) 
                corr, sig = corr_coef(np.array(df2.sla_mean_fixed)-np.array(df2.sla_mean_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
                anti_corr_sla_chl_ano = np.append(anti_corr_sla_chl_ano, corr) 
                anti_corr_sla_chl_ano_sig = np.append(anti_corr_sla_chl_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.sla_mean_fixed)-np.array(df2.sla_mean_bkg), np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), True)
                anti_corr_sla_co2_ano = np.append(anti_corr_sla_co2_ano, corr) 
                anti_corr_sla_co2_ano_sig = np.append(anti_corr_sla_co2_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.sla_mean_fixed), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
                anti_corr_sla_chl_ano2 = np.append(anti_corr_sla_chl_ano2, corr) 
                anti_corr_sla_chl_ano2_sig = np.append(anti_corr_sla_chl_ano2_sig, sig) 
                corr, sig = corr_coef(np.array(df2.vort_mean_fixed)-np.array(df2.vort_mean_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
                anti_corr_vort_chl_ano = np.append(anti_corr_vort_chl_ano, corr) 
                anti_corr_vort_chl_ano_sig = np.append(anti_corr_vort_chl_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.displacement_mean_fixed)-np.array(df2.displacement_mean_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
                anti_corr_disp_chl_ano = np.append(anti_corr_disp_chl_ano, corr) 
                anti_corr_disp_chl_ano_sig = np.append(anti_corr_disp_chl_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.ftle_mean_fixed)-np.array(df2.ftle_mean_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
                anti_corr_ftle_chl_ano = np.append(anti_corr_ftle_chl_ano, corr) 
                anti_corr_ftle_chl_ano_sig = np.append(anti_corr_ftle_chl_ano_sig, sig) 


                corr, sig = corr_coef(np.array(df2.mld_mean_fixed)-np.array(df2.mld_mean_bkg), np.array(df2.sla_mean_fixed)-np.array(df2.sla_mean_bkg), True)
                anti_corr_mld_sla_ano = np.append(anti_corr_mld_sla_ano, corr) 
                anti_corr_mld_sla_ano_sig = np.append(anti_corr_mld_sla_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.mld_mean_fixed)-np.array(df2.mld_mean_bkg), np.array(df2.sst_mean_fixed)-np.array(df2.sst_mean_bkg), True)
                anti_corr_mld_sst_ano = np.append(anti_corr_mld_sst_ano, corr) 
                anti_corr_mld_sst_ano_sig = np.append(anti_corr_mld_sst_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.mld_mean_fixed)-np.array(df2.mld_mean_bkg), np.array(df2.sss_mean_fixed)-np.array(df2.sss_mean_bkg), True)
                anti_corr_mld_sss_ano = np.append(anti_corr_mld_sss_ano, corr) 
                anti_corr_mld_sss_ano_sig = np.append(anti_corr_mld_sss_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.mld_mean_fixed)-np.array(df2.mld_mean_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
                anti_corr_mld_chl_ano = np.append(anti_corr_mld_chl_ano, corr) 
                anti_corr_mld_chl_ano_sig = np.append(anti_corr_mld_chl_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.mld_mean_fixed)-np.array(df2.mld_mean_bkg), np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), True)
                anti_corr_mld_co2_ano = np.append(anti_corr_mld_co2_ano, corr) 
                anti_corr_mld_co2_ano_sig = np.append(anti_corr_mld_co2_ano_sig, sig) 
                ###########################################################

                
                diff_disp = np.append(diff_disp, diff_percent(df2.displacement_mean_fixed, df1.displacement_mean_fixed))
                diff_ftle = np.append(diff_ftle, diff_percent(df2.ftle_mean_fixed, df1.ftle_mean_fixed))
                diff_sst = np.append(diff_sst, diff_percent(df2.sst_mean_fixed, df1.sst_mean_fixed))
                diff_chl = np.append(diff_chl, diff_percent(df2.chl_mean_fixed, df1.chl_mean_fixed))
                diff_chl_full = np.append(diff_chl_full, diff_percent(df2.chl_mean_full, df1.chl_mean_full))
                diff_co2 = np.append(diff_co2, diff_percent(df2.CO2_mean_surface, df1.CO2_mean_surface))                
                diff_mld = np.append(diff_mld, diff_percent(df2.mld_mean_fixed, df1.mld_mean_fixed))
                diff_sss = np.append(diff_sss, diff_percent(df2.sss_mean_fixed, df1.sss_mean_fixed))

                diff_disp_ano = np.append(diff_disp_ano, diff_percent(df2.displacement_mean_fixed-df2.displacement_mean_bkg, df1.displacement_mean_fixed-df1.displacement_mean_bkg))
                diff_ftle_ano = np.append(diff_ftle_ano, diff_percent(df2.ftle_mean_fixed-df2.ftle_mean_bkg, df1.ftle_mean_fixed-df1.ftle_mean_bkg))
                diff_sst_ano = np.append(diff_sst_ano, diff_percent(df2.sst_mean_fixed-df2.sst_mean_bkg, df1.sst_mean_fixed-df1.sst_mean_bkg))
                diff_chl_ano = np.append(diff_chl_ano, diff_percent(df2.chl_mean_fixed-df2.chl_mean_bkg, df1.chl_mean_fixed-df1.chl_mean_bkg))
                diff_chl_full_ano = np.append(diff_chl_full_ano, diff_percent(df2.chl_mean_full-df2.chl_mean_bkg, df1.chl_mean_full-df1.chl_mean_bkg))
                diff_co2_ano = np.append(diff_co2_ano, diff_percent(df2.CO2_mean_surface-df2.CO2_mean_surface_bkg, df1.CO2_mean_surface-df1.CO2_mean_surface_bkg))
                diff_mld_ano = np.append(diff_mld_ano, diff_percent(df2.mld_mean_fixed-df2.mld_mean_bkg, df1.mld_mean_fixed-df1.mld_mean_bkg))
                diff_sss_ano = np.append(diff_sss_ano, diff_percent(df2.sss_mean_fixed-df2.sss_mean_bkg, df1.sss_mean_fixed-df1.sss_mean_bkg))


        bound_ano = [-50, 50]
        bound_corr = [-.5, .5]
        bound_signi = [0, 1]
        corr_ano_cm = 'bwr'
        ########################### cyclonic ###########################
        spatial_map_ex(tile_lons, tile_lats, radius, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_radius_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric Radius ($km$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, phase, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_phase_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric Phase ($\degree$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, cyc_n, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_count_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Counts' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, lat, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_lat_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric Latitude ($\degree$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, lon, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_lon_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric Longitude ($\degree$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, sla, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_sla_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric SLA (m)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, vort, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_vort_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric Vorticity (s$^{-1}$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, disp, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_disp_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric Displacement ($\degree$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, ftle, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_ftle_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric FTLE ($\degree$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, sst, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_sst_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric SST ($\degree$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, chl, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_chl_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric CHL (mg.m$^{-3}$)' + '\n ' + month_name[temporal], [0, 0.4])
        spatial_map_ex(tile_lons, tile_lats, co2, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_co2_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric fCO2 ($\mu$atm)' + '\n ' + month_name[temporal], None, True)    
        spatial_map_ex(tile_lons, tile_lats, mld, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_mld_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric MLD (m)' + '\n ' + month_name[temporal], [0, 250])
        spatial_map_ex(tile_lons, tile_lats, sss, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_sss_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric SSS (psu)' + '\n ' + month_name[temporal], [31, 39])

    
        spatial_map_ex(tile_lons, tile_lats, ano_phase, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_phase_ano_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric Phase Anomally (%)' + '\n ' + month_name[temporal], bound_ano)
        spatial_map_ex(tile_lons, tile_lats, ano_sla, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_sla_ano_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric SLA Anomally (%)' + '\n ' + month_name[temporal], bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, ano_vort, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_vort_ano_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric Vorticity Anomally (%)' + '\n ' + month_name[temporal], bound_ano)
        spatial_map_ex(tile_lons, tile_lats, ano_disp, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_disp_ano_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric Displacement Anomally (%)' + '\n ' + month_name[temporal], bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, ano_ftle, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_ftle_ano_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric FTLE Anomally (%)' + '\n ' + month_name[temporal], bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, ano_sst, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_sst_ano_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric SST Anomally (%)' + '\n ' + month_name[temporal], bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, ano_chl, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_chl_ano_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric CHL Anomally (%)' + '\n ' + month_name[temporal], bound_ano, False, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, ano_co2, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_co2_ano_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric fCO2 Anomally (%)' + '\n ' + month_name[temporal], bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, ano_mld, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_mld_ano_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric MLD Anomally (%)' + '\n ' + month_name[temporal], bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, ano_sss, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_sss_ano_'+str(temporal)+'.png', 'Monthly STA Cyclonic Eddy Centric SSS Anomally (%)' + '\n ' + month_name[temporal], bound_ano, True, 'bwr')

        ######## anomally correlations ######
        spatial_map_ex(tile_lons, tile_lats, corr_chl_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_chl_sst_ano_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric CHL-SST Anomally' + '\n ' + month_name[temporal], bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_co2_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_co2_sst_ano_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric CO2-SST Anomally' + '\n ' + month_name[temporal], bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_sst_ano_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric SLA-SST Anomally' + '\n ' + month_name[temporal], bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_co2_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_co2_chl_ano_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric CO2-CHL Anomally' + '\n ' + month_name[temporal], bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_chl_ano_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric SLA-CHL Anomally' + '\n ' + month_name[temporal], bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_co2_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_co2_ano_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric SLA-CO2 Anomally' + '\n ' + month_name[temporal], bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_chl_ano2, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_chl_ano2_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric SLA-CHL2 Anomally' + '\n ' + month_name[temporal], bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_vort_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_vort_chl_ano_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric Vort-CHL Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_disp_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_disp_chl_ano_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric disp-CHL Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_ftle_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_ftle_chl_ano_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric ftle-CHL Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)

        spatial_map_ex(tile_lons, tile_lats, corr_mld_sla_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_mld_sla_ano_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric MLD-SLA Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_mld_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_mld_sst_ano_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric MLD-SST Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_mld_sss_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_mld_sss_ano_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric MLD-SSS Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_mld_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_mld_chl_ano_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric MLD-CHL Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_mld_co2_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_mld_co2_ano_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric MLD-CO2 Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)


        spatial_map_ex(tile_lons, tile_lats, corr_chl_sst_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_chl_sst_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric CHL-SST Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_co2_sst_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_co2_sst_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric CO2-SST Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_sst_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_sst_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric SLA-SST Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_co2_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_co2_chl_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric CO2-CHL Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_chl_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric SLA-CHL Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_co2_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_co2_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric SLA-CO2 Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_chl_ano2_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_chl_ano2_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric SLA-CHL2 Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_vort_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_vort_chl_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric Vort-CHL Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_disp_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_disp_chl_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric disp-CHL Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_ftle_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_ftle_chl_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric ftle-CHL Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)

        spatial_map_ex(tile_lons, tile_lats, corr_mld_sla_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_mld_sla_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric MLD-SLA Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_mld_sst_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_mld_sst_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric MLD-SST Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_mld_sss_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_mld_sss_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric MLD-SSS Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_mld_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_mld_chl_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric MLD-CHL Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_mld_co2_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_mld_co2_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. Cyclonic Eddy Centric MLD-CO2 Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        #####################################

        #################################################################            




        ########################### anticyclonic ###########################
        spatial_map_ex(tile_lons, tile_lats, anti_radius, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_radius_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric Radius ($km$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, anti_phase, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_phase_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric Phase ($\degree$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, anti_cyc_n, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_count_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Counts' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, anti_lat, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_lat_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric Latitude ($\degree$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, anti_lon, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_lon_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric Longitude ($\degree$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, anti_sla, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_sla_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric SLA (m)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, anti_vort, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_vort_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric Vorticity (s$^{-1}$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, anti_disp, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_disp_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric Displacement ($\degree$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, anti_ftle, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_ftle_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric FTLE ($\degree$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, anti_sst, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_sst_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric SST ($\degree$)' + '\n ' + month_name[temporal])
        spatial_map_ex(tile_lons, tile_lats, anti_chl, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_chl_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric CHL (mg.m$^{-3}$)' + '\n ' + month_name[temporal], [0, 0.4])
        spatial_map_ex(tile_lons, tile_lats, anti_co2, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_co2_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric fCO2 ($\mu$atm)' + '\n ' + month_name[temporal], None, True)    
        spatial_map_ex(tile_lons, tile_lats, anti_mld, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_mld_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric MLD (m)' + '\n ' + month_name[temporal], [0, 250])
        spatial_map_ex(tile_lons, tile_lats, anti_sss, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_sss_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric SSS (psu)' + '\n ' + month_name[temporal], [31, 39])

    
        spatial_map_ex(tile_lons, tile_lats, anti_ano_phase, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_phase_ano_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric Phase Anomally (%)' + '\n ' + month_name[temporal], bound_ano)
        spatial_map_ex(tile_lons, tile_lats, anti_ano_sla, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_sla_ano_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric SLA Anomally (%)' + '\n ' + month_name[temporal], bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, anti_ano_vort, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_vort_ano_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric Vorticity Anomally (%)' + '\n ' + month_name[temporal], bound_ano)
        spatial_map_ex(tile_lons, tile_lats, anti_ano_disp, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_disp_ano_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric Displacement Anomally (%)' + '\n ' + month_name[temporal], bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, anti_ano_ftle, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_ftle_ano_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric FTLE Anomally (%)' + '\n ' + month_name[temporal], bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, anti_ano_sst, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_sst_ano_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric SST Anomally (%)' + '\n ' + month_name[temporal], bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, anti_ano_chl, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_chl_ano_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric CHL Anomally (%)' + '\n ' + month_name[temporal], bound_ano, False, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, anti_ano_co2, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_co2_ano_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric fCO2 Anomally (%)' + '\n ' + month_name[temporal], bound_ano, True, 'bwr')        
        spatial_map_ex(tile_lons, tile_lats, anti_ano_mld, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_mld_ano_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric MLD Anomally (%)' + '\n ' + month_name[temporal], bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, anti_ano_sss, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_sss_ano_'+str(temporal)+'.png', 'Monthly STA AntiCyclonic Eddy Centric SSS Anomally (%)' + '\n ' + month_name[temporal], bound_ano, True, 'bwr')

        ######## anomally correlations ######
        spatial_map_ex(tile_lons, tile_lats, anti_corr_chl_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_chl_sst_ano_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric CHL-SST Anomally' + '\n ' + month_name[temporal], bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_co2_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_co2_sst_ano_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric CO2-SST Anomally' + '\n ' + month_name[temporal], bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_sst_ano_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric SLA-SST Anomally' + '\n ' + month_name[temporal], bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_co2_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_co2_chl_ano_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric CO2-CHL Anomally' + '\n ' + month_name[temporal], bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_chl_ano_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric SLA-CHL Anomally' + '\n ' + month_name[temporal], bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_co2_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_co2_ano_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric SLA-CO2 Anomally' + '\n ' + month_name[temporal], bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_chl_ano2, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_chl_ano2_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric SLA-CHL2 Anomally' + '\n ' + month_name[temporal], bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_vort_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_vort_chl_ano_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric Vort-CHL Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_disp_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_disp_chl_ano_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric disp-CHL Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_ftle_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_ftle_chl_ano_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric ftle-CHL Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)

        spatial_map_ex(tile_lons, tile_lats, anti_corr_mld_sla_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_mld_sla_ano_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric MLD-SLA Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_mld_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_mld_sst_ano_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric MLD-SST Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_mld_sss_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_mld_sss_ano_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric MLD-SSS Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_mld_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_mld_chl_ano_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric MLD-CHL Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_mld_co2_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_mld_co2_ano_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric MLD-CO2 Anomally' + '\n ' + month_name[temporal], bound_corr, True, corr_ano_cm)

        spatial_map_ex(tile_lons, tile_lats, anti_corr_chl_sst_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_chl_sst_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric CHL-SST Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_co2_sst_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_co2_sst_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric CO2-SST Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_sst_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_sst_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric SLA-SST Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_co2_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_co2_chl_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric CO2-CHL Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_chl_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric SLA-CHL Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_co2_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_co2_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric SLA-CO2 Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_chl_ano2_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_chl_ano2_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric SLA-CHL2 Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_vort_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_vort_chl_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric Vort-CHL Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_disp_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_disp_chl_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric disp-CHL Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_ftle_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_ftle_chl_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric ftle-CHL Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)

        spatial_map_ex(tile_lons, tile_lats, anti_corr_mld_sla_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_mld_sla_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric MLD-SLA Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_mld_sst_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_mld_sst_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric MLD-SST Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_mld_sss_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_mld_sss_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric MLD-SSS Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_mld_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_mld_chl_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric MLD-CHL Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_mld_co2_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_mld_co2_ano_sig_'+str(temporal)+'.png', 'Monthly STA Corr. AntiCyclonic Eddy Centric MLD-CO2 Anomally Signi.' + '\n ' + month_name[temporal], bound_signi)
        #####################################
        
        #################################################################
        




        ########################### differential ###########################

        diff_bounds = [-50, 50]
        colmap = 'bwr'
        colmap = 'seismic'
        colmap = cmocean.cm.balance 
        
        spatial_map_ex(tile_lons, tile_lats, diff_disp_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_disp_ano_'+str(temporal)+'.png', 'Monthly Differential STA Displacement Anomally (%)' + '\n ' + month_name[temporal], diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_ftle_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_ftle_ano_'+str(temporal)+'.png', 'Monthly Differential STA FTLE Anomally (%)' + '\n ' + month_name[temporal], diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_sst_ano_'+str(temporal)+'.png', 'Monthly Differential STA SST Anomally (%)' + '\n ' + month_name[temporal], diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_chl_ano_'+str(temporal)+'.png', 'Monthly Differential STA CHL Anomally (%)' + '\n ' + month_name[temporal], diff_bounds, False, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_chl_full_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_chl_full_ano_'+str(temporal)+'.png', 'Monthly Differential STA CHL(full) Anomally (%)' + '\n ' + month_name[temporal], diff_bounds, False, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_co2_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_co2_ano_'+str(temporal)+'.png', 'Monthly Differential STA $fCO_{2}$ Anomally (%)' + '\n ' + month_name[temporal], diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_mld_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_mld_ano_'+str(temporal)+'.png', 'Monthly Differential STA MLD Anomally (%)' + '\n ' + month_name[temporal], diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_sss_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_sss_ano_'+str(temporal)+'.png', 'Monthly Differential STA SSS Anomally (%)' + '\n ' + month_name[temporal], diff_bounds, True, colmap)

        spatial_map_ex(tile_lons, tile_lats, diff_disp, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_disp_'+str(temporal)+'.png', 'Monthly Differential STA Displacement (%)' + '\n ' + month_name[temporal], diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_ftle, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_ftle_'+str(temporal)+'.png', 'Monthly Differential STA FTLE (%)' + '\n ' + month_name[temporal], diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_sst, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_sst_'+str(temporal)+'.png', 'Monthly Differential STA SST (%)' + '\n ' + month_name[temporal], diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_chl, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_chl_'+str(temporal)+'.png', 'Monthly Differential STA CHL (%)' + '\n ' + month_name[temporal], diff_bounds, False, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_chl_full, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_chl_full_'+str(temporal)+'.png', 'Monthly Differential STA CHL(full) (%)' + '\n ' + month_name[temporal], diff_bounds, False, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_co2, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_co2_'+str(temporal)+'.png', 'Monthly Differential STA $fCO_{2}$ (%)' + '\n ' + month_name[temporal], diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_mld, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_mld_'+str(temporal)+'.png', 'Monthly Differential STA MLD (%)' + '\n ' + month_name[temporal], diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_sss, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_sss_'+str(temporal)+'.png', 'Monthly Differential STA SSS (%)' + '\n ' + month_name[temporal], diff_bounds, True, colmap)
        #################################################################
    return    




def spatially_averaged_yearly_series(query):
    '''
    ######## hawaii
    minlat = 19
    maxlat = 49
    minlon = 190
    maxlon = 220
    ################
    '''

    minlat = -80
    maxlat = 70
    minlon = 0
    maxlon = 360
    
    spacing = 5.
    query = remove_spatial_conditions(query)
    lats = np.arange(minlat+spacing/2., maxlat, spacing)
    lons = np.arange(minlon+spacing/2., maxlon, spacing)
    base_query = query
    
    temporal1 = 2003
    temporal2 = 2015

    for temporal in range(temporal1, temporal2+1):
        query = base_query
        if query.find('WHERE') >= 0:
            query = query + ' AND year=' + str(temporal)
        else:        
            query = query + ' WHERE year=' + str(temporal)

        query_temporal = query 
        tile_lats = np.array([])
        tile_lons = np.array([])


        cyc_n = np.array([])
        cyc_n_up = np.array([])
        cyc_n_down = np.array([])
        lat = np.array([])
        lat_up = np.array([])
        lat_down = np.array([])
        lon = np.array([])
        lon_up = np.array([])
        lon_down = np.array([])
        radius = np.array([])
        radius_up = np.array([])
        radius_down = np.array([])
        phase = np.array([])
        phase_up = np.array([])
        phase_down = np.array([])
        sla = np.array([])
        sla_up = np.array([])
        sla_down = np.array([])
        vort = np.array([])
        vort_up = np.array([])
        vort_down = np.array([])
        disp = np.array([])
        disp_up = np.array([])
        disp_down = np.array([])
        ftle = np.array([])
        ftle_up = np.array([])
        ftle_down = np.array([])
        sst = np.array([])
        sst_up = np.array([])
        sst_down = np.array([])
        chl = np.array([])
        chl_up = np.array([])
        chl_down = np.array([])
        co2 = np.array([])
        co2_up = np.array([])
        co2_down = np.array([])
    
        ano_phase = np.array([])
        ano_phase_up = np.array([])
        ano_phase_down = np.array([])
        ano_sla = np.array([])
        ano_sla_up = np.array([])
        ano_sla_down = np.array([])
        ano_vort = np.array([])
        ano_vort_up = np.array([])
        ano_vort_down = np.array([])
        ano_disp = np.array([])
        ano_disp_up = np.array([])
        ano_disp_down = np.array([])
        ano_ftle = np.array([])
        ano_ftle_up = np.array([])
        ano_ftle_down = np.array([])
        ano_sst = np.array([])
        ano_sst_up = np.array([])
        ano_sst_down = np.array([])
        ano_chl = np.array([])
        ano_chl_up = np.array([])
        ano_chl_down = np.array([])
        ano_co2 = np.array([])
        ano_co2_up = np.array([])
        ano_co2_down = np.array([])
    
        ######## anomally correlations ######
        corr_chl_sst_ano = np.array([]) 
        corr_co2_sst_ano = np.array([])
        corr_sla_sst_ano = np.array([])
        corr_co2_chl_ano = np.array([])
        corr_sla_chl_ano = np.array([])
        corr_sla_co2_ano = np.array([])        
        corr_sla_chl_ano2 = np.array([])        
        corr_vort_chl_ano = np.array([])
        corr_disp_chl_ano = np.array([])
        corr_ftle_chl_ano = np.array([])

        corr_chl_sst_ano_sig = np.array([]) 
        corr_co2_sst_ano_sig = np.array([])
        corr_sla_sst_ano_sig = np.array([])
        corr_co2_chl_ano_sig = np.array([])
        corr_sla_chl_ano_sig = np.array([])
        corr_sla_co2_ano_sig = np.array([])        
        corr_sla_chl_ano2_sig = np.array([])
        corr_vort_chl_ano_sig = np.array([])
        corr_disp_chl_ano_sig = np.array([])
        corr_ftle_chl_ano_sig = np.array([])
        #####################################
    

        anti_cyc_n = np.array([])
        anti_cyc_n_up = np.array([])
        anti_cyc_n_down = np.array([])
        anti_lat = np.array([])
        anti_lat_up = np.array([])
        anti_lat_down = np.array([])
        anti_lon = np.array([])
        anti_lon_up = np.array([])
        anti_lon_down = np.array([])
        anti_radius = np.array([])
        anti_radius_up = np.array([])
        anti_radius_down = np.array([])
        anti_phase = np.array([])
        anti_phase_up = np.array([])
        anti_phase_down = np.array([])
        anti_sla = np.array([])
        anti_sla_up = np.array([])
        anti_sla_down = np.array([])
        anti_vort = np.array([])
        anti_vort_up = np.array([])
        anti_vort_down = np.array([])
        anti_disp = np.array([])
        anti_disp_up = np.array([])
        anti_disp_down = np.array([])
        anti_ftle = np.array([])
        anti_ftle_up = np.array([])
        anti_ftle_down = np.array([])
        anti_sst = np.array([])
        anti_sst_up = np.array([])
        anti_sst_down = np.array([])
        anti_chl = np.array([])
        anti_chl_up = np.array([])
        anti_chl_down = np.array([])
        anti_co2 = np.array([])
        anti_co2_up = np.array([])
        anti_co2_down = np.array([])
    
        anti_ano_phase = np.array([])
        anti_ano_phase_up = np.array([])
        anti_ano_phase_down = np.array([])
        anti_ano_sla = np.array([])
        anti_ano_sla_up = np.array([])
        anti_ano_sla_down = np.array([])
        anti_ano_vort = np.array([])
        anti_ano_vort_up = np.array([])
        anti_ano_vort_down = np.array([])
        anti_ano_disp = np.array([])
        anti_ano_disp_up = np.array([])
        anti_ano_disp_down = np.array([])
        anti_ano_ftle = np.array([])
        anti_ano_ftle_up = np.array([])
        anti_ano_ftle_down = np.array([])
        anti_ano_sst = np.array([])
        anti_ano_sst_up = np.array([])
        anti_ano_sst_down = np.array([])
        anti_ano_chl = np.array([])
        anti_ano_chl_up = np.array([])
        anti_ano_chl_down = np.array([])
        anti_ano_co2 = np.array([])
        anti_ano_co2_up = np.array([])
        anti_ano_co2_down = np.array([])


        ######## anomally correlations ######
        anti_corr_chl_sst_ano = np.array([]) 
        anti_corr_co2_sst_ano = np.array([])
        anti_corr_sla_sst_ano = np.array([])
        anti_corr_co2_chl_ano = np.array([])
        anti_corr_sla_chl_ano = np.array([])
        anti_corr_sla_co2_ano = np.array([])        
        anti_corr_sla_chl_ano2 = np.array([])
        anti_corr_vort_chl_ano = np.array([])
        anti_corr_disp_chl_ano = np.array([])
        anti_corr_ftle_chl_ano = np.array([])


        anti_corr_chl_sst_ano_sig = np.array([]) 
        anti_corr_co2_sst_ano_sig = np.array([])
        anti_corr_sla_sst_ano_sig = np.array([])
        anti_corr_co2_chl_ano_sig = np.array([])
        anti_corr_sla_chl_ano_sig = np.array([])
        anti_corr_sla_co2_ano_sig = np.array([])        
        anti_corr_sla_chl_ano2_sig = np.array([])
        anti_corr_vort_chl_ano_sig = np.array([])
        anti_corr_disp_chl_ano_sig = np.array([])
        anti_corr_ftle_chl_ano_sig = np.array([])
        #####################################


        diff_disp = np.array([])
        diff_ftle = np.array([])
        diff_sst = np.array([])
        diff_chl = np.array([])
        diff_chl_full = np.array([])
        diff_co2 = np.array([])

        diff_disp_ano = np.array([])
        diff_ftle_ano = np.array([])
        diff_sst_ano = np.array([])
        diff_chl_ano = np.array([])
        diff_chl_full_ano = np.array([])
        diff_co2_ano = np.array([])

        counter = 0
        for midlat in lats:
            for midlon in lons:
                counter += 1
                print('Cycle: %d, Progress: %2.2f%s ' % (temporal, 100.*counter/(len(lats)*len(lons)), '%'))
                
                ulat = midlat + spacing/2.
                llat = midlat - spacing/2.
                ulon = midlon + spacing/2.
                llon = midlon - spacing/2.
                query = query_temporal + ' AND eddy_lat>='+str(llat) + ' AND eddy_lat<='+str(ulat)+ ' AND eddy_lon>='+str(llon) + ' AND eddy_lon<='+str(ulon)            
                query1 = query + ' AND eddy_polarity=1'
                query2 = query + ' AND eddy_polarity=-1'
                conn = db_connect()
                df1 = sql.read_sql(query1, conn)
                conn.close()
                conn = db_connect()
                df2 = sql.read_sql(query2, conn)
                conn.close()
                if len(df1)<1 or len(df2)<1:
                    #print('No match found. len(df1): '+str(len(df1))+' len(df2): '+str(len(df2)))
                    continue                
                df1 = df1.fillna(float('NaN'))
                df2 = df2.fillna(float('NaN'))                    

                tile_lats = np.append(tile_lats, midlat)
                tile_lons = np.append(tile_lons, midlon)

                cyc_n, cyc_n_up, cyc_n_down = append_range(cyc_n, cyc_n_up, cyc_n_down, len(np.array(df1.year)))
                lat, lat_up, lat_down = append_range(lat, lat_up, lat_down, df1.eddy_lat)
                lon, lon_up, lon_down = append_range(lon, lon_up, lon_down, df1.eddy_lon)
                radius, radius_up, radius_down = append_range(radius, radius_up, radius_down, df1.eddy_radius)
                phase, phase_up, phase_down = append_range(phase, phase_up, phase_down, df1.phase_integ_fixed)
                sla, sla_up, sla_down = append_range(sla, sla_up, sla_down, df1.sla_mean_fixed)
                vort, vort_up, vort_down = append_range(vort, vort_up, vort_down, df1.vort_mean_fixed)
                disp, disp_up, disp_down = append_range(disp, disp_up, disp_down, df1.displacement_mean_fixed)
                ftle, ftle_up, ftle_down = append_range(ftle, ftle_up, ftle_down, df1.ftle_mean_fixed)
                sst, sst_up, sst_down = append_range(sst, sst_up, sst_down, df1.sst_mean_fixed)
                chl, chl_up, chl_down = append_range(chl, chl_up, chl_down, df1.chl_mean_fixed)
                co2, co2_up, co2_down = append_range(co2, co2_up, co2_down, df1.CO2_mean_surface)
                                
                ano_phase, ano_phase_up, ano_phase_down = append_range(ano_phase, ano_phase_up, ano_phase_down, 100 * (df1.phase_integ_fixed - df1.phase_mean_bkg) / df1.phase_mean_bkg)
                ano_sla, ano_sla_up, ano_sla_down = append_range(ano_sla, ano_sla_up, ano_sla_down, 100 * (df1.sla_mean_fixed - df1.sla_mean_bkg) / df1.sla_mean_bkg)
                ano_vort, ano_vort_up, ano_vort_down = append_range(ano_vort, ano_vort_up, ano_vort_down, 100 * (df1.vort_mean_fixed - df1.vort_mean_bkg) / df1.vort_mean_bkg)
                ano_disp, ano_disp_up, ano_disp_down = append_range(ano_disp, ano_disp_up, ano_disp_down, 100 * (df1.displacement_mean_fixed - df1.displacement_mean_bkg) / df1.displacement_mean_bkg)
                ano_ftle, ano_ftle_up, ano_ftle_down = append_range(ano_ftle, ano_ftle_up, ano_ftle_down, 100 * (df1.ftle_mean_fixed - df1.ftle_mean_bkg) / df1.ftle_mean_bkg)
                ano_sst, ano_sst_up, ano_sst_down = append_range(ano_sst, ano_sst_up, ano_sst_down, 100 * (df1.sst_mean_fixed - df1.sst_mean_bkg) / df1.sst_mean_bkg)
                ano_chl, ano_chl_up, ano_chl_down = append_range(ano_chl, ano_chl_up, ano_chl_down, 100 * (df1.chl_mean_fixed - df1.chl_mean_bkg) / df1.chl_mean_bkg)
                ano_co2, ano_co2_up, ano_co2_down = append_range(ano_co2, ano_co2_up, ano_co2_down, 100 * (df1.CO2_mean_surface - df1.CO2_mean_surface_bkg) / df1.CO2_mean_surface_bkg)
                
                

                ############### anomally correlations  ####################
                corr, sig = corr_coef(np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), np.array(df1.sst_mean_fixed)-np.array(df1.sst_mean_bkg), True)
                corr_chl_sst_ano = np.append(corr_chl_sst_ano, corr) 
                corr_chl_sst_ano_sig = np.append(corr_chl_sst_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), np.array(df1.sst_mean_fixed)-np.array(df1.sst_mean_bkg), True)
                corr_co2_sst_ano = np.append(corr_co2_sst_ano, corr) 
                corr_co2_sst_ano_sig = np.append(corr_co2_sst_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.sla_mean_fixed)-np.array(df1.sla_mean_bkg), np.array(df1.sst_mean_fixed)-np.array(df1.sst_mean_bkg), False)
                corr_sla_sst_ano = np.append(corr_sla_sst_ano, corr) 
                corr_sla_sst_ano_sig = np.append(corr_sla_sst_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
                corr_co2_chl_ano = np.append(corr_co2_chl_ano, corr) 
                corr_co2_chl_ano_sig = np.append(corr_co2_chl_ano, sig) 
                corr, sig = corr_coef(np.array(df1.sla_mean_fixed)-np.array(df1.sla_mean_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
                corr_sla_chl_ano = np.append(corr_sla_chl_ano, corr) 
                corr_sla_chl_ano_sig = np.append(corr_sla_chl_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.sla_mean_fixed)-np.array(df1.sla_mean_bkg), np.array(df1.CO2_mean_surface)-np.array(df1.CO2_mean_surface_bkg), True)
                corr_sla_co2_ano = np.append(corr_sla_co2_ano, corr) 
                corr_sla_co2_ano_sig = np.append(corr_sla_co2_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.sla_mean_fixed), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
                corr_sla_chl_ano2 = np.append(corr_sla_chl_ano2, corr) 
                corr_sla_chl_ano2_sig = np.append(corr_sla_chl_ano2_sig, sig) 
                corr, sig = corr_coef(np.array(df1.vort_mean_fixed)-np.array(df1.vort_mean_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
                corr_vort_chl_ano = np.append(corr_vort_chl_ano, corr) 
                corr_vort_chl_ano_sig = np.append(corr_vort_chl_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.displacement_mean_fixed)-np.array(df1.displacement_mean_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
                corr_disp_chl_ano = np.append(corr_disp_chl_ano, corr) 
                corr_disp_chl_ano_sig = np.append(corr_disp_chl_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df1.ftle_mean_fixed)-np.array(df1.ftle_mean_bkg), np.array(df1.chl_mean_fixed)-np.array(df1.chl_mean_bkg), True)
                corr_ftle_chl_ano = np.append(corr_ftle_chl_ano, corr) 
                corr_ftle_chl_ano_sig = np.append(corr_ftle_chl_ano_sig, sig) 
                ###########################################################


                anti_cyc_n, anti_cyc_n_up, anti_cyc_n_down = append_range(anti_cyc_n, anti_cyc_n_up, anti_cyc_n_down, len(np.array(df2.year)))
                anti_lat, anti_lat_up, anti_lat_down = append_range(anti_lat, anti_lat_up, anti_lat_down, df2.eddy_lat)
                anti_lon, anti_lon_up, anti_lon_down = append_range(anti_lon, anti_lon_up, anti_lon_down, df2.eddy_lon)
                anti_radius, anti_radius_up, anti_radius_down = append_range(anti_radius, anti_radius_up, anti_radius_down, df2.eddy_radius)
                anti_phase, anti_phase_up, anti_phase_down = append_range(anti_phase, anti_phase_up, anti_phase_down, df2.phase_integ_fixed)
                anti_sla, anti_sla_up, anti_sla_down = append_range(anti_sla, anti_sla_up, anti_sla_down, df2.sla_mean_fixed)
                anti_vort, anti_vort_up, anti_vort_down = append_range(anti_vort, anti_vort_up, anti_vort_down, df2.vort_mean_fixed)
                anti_disp, anti_disp_up, anti_disp_down = append_range(anti_disp, anti_disp_up, anti_disp_down, df2.displacement_mean_fixed)
                anti_ftle, anti_ftle_up, anti_ftle_down = append_range(anti_ftle, anti_ftle_up, anti_ftle_down, df2.ftle_mean_fixed)
                anti_sst, anti_sst_up, anti_sst_down = append_range(anti_sst, anti_sst_up, anti_sst_down, df2.sst_mean_fixed)
                anti_chl, anti_chl_up, anti_chl_down = append_range(anti_chl, anti_chl_up, anti_chl_down, df2.chl_mean_fixed)
                anti_co2, anti_co2_up, anti_co2_down = append_range(anti_co2, anti_co2_up, anti_co2_down, df2.CO2_mean_surface)
                
                anti_ano_phase, anti_ano_phase_up, anti_ano_phase_down = append_range(anti_ano_phase, anti_ano_phase_up, anti_ano_phase_down, 100 * (df2.phase_integ_fixed - df2.phase_mean_bkg) / df2.phase_mean_bkg)
                anti_ano_sla, anti_ano_sla_up, anti_ano_sla_down = append_range(anti_ano_sla, anti_ano_sla_up, anti_ano_sla_down, 100 * (df2.sla_mean_fixed - df2.sla_mean_bkg) / df2.sla_mean_bkg)
                anti_ano_vort, anti_ano_vort_up, anti_ano_vort_down = append_range(anti_ano_vort, anti_ano_vort_up, anti_ano_vort_down, 100 * (df2.vort_mean_fixed - df2.vort_mean_bkg) / df2.vort_mean_bkg)
                anti_ano_disp, anti_ano_disp_up, anti_ano_disp_down = append_range(anti_ano_disp, anti_ano_disp_up, anti_ano_disp_down, 100 * (df2.displacement_mean_fixed - df2.displacement_mean_bkg) / df2.displacement_mean_bkg)
                anti_ano_ftle, anti_ano_ftle_up, anti_ano_ftle_down = append_range(anti_ano_ftle, anti_ano_ftle_up, anti_ano_ftle_down, 100 * (df2.ftle_mean_fixed - df2.ftle_mean_bkg) / df2.ftle_mean_bkg)
                anti_ano_sst, anti_ano_sst_up, anti_ano_sst_down = append_range(anti_ano_sst, anti_ano_sst_up, anti_ano_sst_down, 100 * (df2.sst_mean_fixed - df2.sst_mean_bkg) / df2.sst_mean_bkg)
                anti_ano_chl, anti_ano_chl_up, anti_ano_chl_down = append_range(anti_ano_chl, anti_ano_chl_up, anti_ano_chl_down, 100 * (df2.chl_mean_fixed - df2.chl_mean_bkg) / df2.chl_mean_bkg)
                anti_ano_co2, anti_ano_co2_up, anti_ano_co2_down = append_range(anti_ano_co2, anti_ano_co2_up, anti_ano_co2_down, 100 * (df2.CO2_mean_surface - df2.CO2_mean_surface_bkg) / df2.CO2_mean_surface_bkg)
                

                ############### anomally correlations  ####################
                corr, sig = corr_coef(np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), np.array(df2.sst_mean_fixed)-np.array(df2.sst_mean_bkg), True)
                anti_corr_chl_sst_ano = np.append(anti_corr_chl_sst_ano, corr) 
                anti_corr_chl_sst_ano_sig = np.append(anti_corr_chl_sst_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), np.array(df2.sst_mean_fixed)-np.array(df2.sst_mean_bkg), True)
                anti_corr_co2_sst_ano = np.append(anti_corr_co2_sst_ano, corr) 
                anti_corr_co2_sst_ano_sig = np.append(anti_corr_co2_sst_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.sla_mean_fixed)-np.array(df2.sla_mean_bkg), np.array(df2.sst_mean_fixed)-np.array(df2.sst_mean_bkg), False)
                anti_corr_sla_sst_ano = np.append(anti_corr_sla_sst_ano, corr) 
                anti_corr_sla_sst_ano_sig = np.append(anti_corr_sla_sst_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
                anti_corr_co2_chl_ano = np.append(anti_corr_co2_chl_ano, corr) 
                anti_corr_co2_chl_ano_sig = np.append(anti_corr_co2_chl_ano_sig, corr) 
                corr, sig = corr_coef(np.array(df2.sla_mean_fixed)-np.array(df2.sla_mean_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
                anti_corr_sla_chl_ano = np.append(anti_corr_sla_chl_ano, corr) 
                anti_corr_sla_chl_ano_sig = np.append(anti_corr_sla_chl_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.sla_mean_fixed)-np.array(df2.sla_mean_bkg), np.array(df2.CO2_mean_surface)-np.array(df2.CO2_mean_surface_bkg), True)
                anti_corr_sla_co2_ano = np.append(anti_corr_sla_co2_ano, corr) 
                anti_corr_sla_co2_ano_sig = np.append(anti_corr_sla_co2_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.sla_mean_fixed), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
                anti_corr_sla_chl_ano2 = np.append(anti_corr_sla_chl_ano2, corr) 
                anti_corr_sla_chl_ano2_sig = np.append(anti_corr_sla_chl_ano2_sig, sig) 
                corr, sig = corr_coef(np.array(df2.vort_mean_fixed)-np.array(df2.vort_mean_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
                anti_corr_vort_chl_ano = np.append(anti_corr_vort_chl_ano, corr) 
                anti_corr_vort_chl_ano_sig = np.append(anti_corr_vort_chl_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.displacement_mean_fixed)-np.array(df2.displacement_mean_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
                anti_corr_disp_chl_ano = np.append(anti_corr_disp_chl_ano, corr) 
                anti_corr_disp_chl_ano_sig = np.append(anti_corr_disp_chl_ano_sig, sig) 
                corr, sig = corr_coef(np.array(df2.ftle_mean_fixed)-np.array(df2.ftle_mean_bkg), np.array(df2.chl_mean_fixed)-np.array(df2.chl_mean_bkg), True)
                anti_corr_ftle_chl_ano = np.append(anti_corr_ftle_chl_ano, corr) 
                anti_corr_ftle_chl_ano_sig = np.append(anti_corr_ftle_chl_ano_sig, sig) 
                ###########################################################

                
                diff_disp = np.append(diff_disp, diff_percent(df2.displacement_mean_fixed, df1.displacement_mean_fixed))
                diff_ftle = np.append(diff_ftle, diff_percent(df2.ftle_mean_fixed, df1.ftle_mean_fixed))
                diff_sst = np.append(diff_sst, diff_percent(df2.sst_mean_fixed, df1.sst_mean_fixed))
                diff_chl = np.append(diff_chl, diff_percent(df2.chl_mean_fixed, df1.chl_mean_fixed))
                diff_chl_full = np.append(diff_chl_full, diff_percent(df2.chl_mean_full, df1.chl_mean_full))
                diff_co2 = np.append(diff_co2, diff_percent(df2.CO2_mean_surface, df1.CO2_mean_surface))
                
                diff_disp_ano = np.append(diff_disp_ano, diff_percent(df2.displacement_mean_fixed-df2.displacement_mean_bkg, df1.displacement_mean_fixed-df1.displacement_mean_bkg))
                diff_ftle_ano = np.append(diff_ftle_ano, diff_percent(df2.ftle_mean_fixed-df2.ftle_mean_bkg, df1.ftle_mean_fixed-df1.ftle_mean_bkg))
                diff_sst_ano = np.append(diff_sst_ano, diff_percent(df2.sst_mean_fixed-df2.sst_mean_bkg, df1.sst_mean_fixed-df1.sst_mean_bkg))
                diff_chl_ano = np.append(diff_chl_ano, diff_percent(df2.chl_mean_fixed-df2.chl_mean_bkg, df1.chl_mean_fixed-df1.chl_mean_bkg))
                diff_chl_full_ano = np.append(diff_chl_full_ano, diff_percent(df2.chl_mean_full-df2.chl_mean_bkg, df1.chl_mean_full-df1.chl_mean_bkg))
                diff_co2_ano = np.append(diff_co2_ano, diff_percent(df2.CO2_mean_surface-df2.CO2_mean_surface_bkg, df1.CO2_mean_surface-df1.CO2_mean_surface_bkg))



        bound_ano = [-50, 50]
        bound_corr = [-.5, .5]
        bound_signi = [0, 1]
        corr_ano_cm = 'bwr'
        ########################### cyclonic ###########################
        spatial_map_ex(tile_lons, tile_lats, radius, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_radius_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric Radius ($km$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, phase, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_phase_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric Phase ($\degree$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, cyc_n, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_count_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Counts' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, lat, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_lat_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric Latitude ($\degree$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, lon, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_lon_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric Longitude ($\degree$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, sla, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_sla_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric SLA (m)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, vort, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_vort_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric Vorticity (s$^{-1}$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, disp, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_disp_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric Displacement ($\degree$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, ftle, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_ftle_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric FTLE ($\degree$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, sst, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_sst_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric SST ($\degree$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, chl, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_chl_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric CHL (mg.m$^{-3}$)' + '\n ' + str(temporal), [0, 0.4])
        spatial_map_ex(tile_lons, tile_lats, co2, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_co2_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric fCO2 ($\mu$atm)' + '\n ' + str(temporal), None, True)
    
    
        spatial_map_ex(tile_lons, tile_lats, ano_phase, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_phase_ano_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric Phase Anomally (%)' + '\n ' + str(temporal), bound_ano)
        spatial_map_ex(tile_lons, tile_lats, ano_sla, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_sla_ano_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric SLA Anomally (%)' + '\n ' + str(temporal), bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, ano_vort, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_vort_ano_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric Vorticity Anomally (%)' + '\n ' + str(temporal), bound_ano)
        spatial_map_ex(tile_lons, tile_lats, ano_disp, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_disp_ano_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric Displacement Anomally (%)' + '\n ' + str(temporal), bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, ano_ftle, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_ftle_ano_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric FTLE Anomally (%)' + '\n ' + str(temporal), bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, ano_sst, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_sst_ano_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric SST Anomally (%)' + '\n ' + str(temporal), bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, ano_chl, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_chl_ano_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric CHL Anomally (%)' + '\n ' + str(temporal), bound_ano, False, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, ano_co2, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_co2_ano_'+str(temporal)+'.png', 'Yearly STA Cyclonic Eddy Centric fCO2 Anomally (%)' + '\n ' + str(temporal), bound_ano, True, 'bwr')

        ######## anomally correlations ######
        spatial_map_ex(tile_lons, tile_lats, corr_chl_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_chl_sst_ano_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric CHL-SST Anomally' + '\n ' + str(temporal), bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_co2_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_co2_sst_ano_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric CO2-SST Anomally' + '\n ' + str(temporal), bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_sst_ano_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric SLA-SST Anomally' + '\n ' + str(temporal), bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_co2_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_co2_chl_ano_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric CO2-CHL Anomally' + '\n ' + str(temporal), bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_chl_ano_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric SLA-CHL Anomally' + '\n ' + str(temporal), bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_co2_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_co2_ano_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric SLA-CO2 Anomally' + '\n ' + str(temporal), bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_chl_ano2, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_chl_ano2_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric SLA-CHL2 Anomally' + '\n ' + str(temporal), bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_vort_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_vort_chl_ano_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric Vort-CHL Anomally' + '\n ' + str(temporal), bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_disp_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_disp_chl_ano_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric disp-CHL Anomally' + '\n ' + str(temporal), bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, corr_ftle_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_ftle_chl_ano_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric ftle-CHL Anomally' + '\n ' + str(temporal), bound_corr, True, corr_ano_cm)

        spatial_map_ex(tile_lons, tile_lats, corr_chl_sst_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_chl_sst_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric CHL-SST Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_co2_sst_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_co2_sst_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric CO2-SST Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_sst_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_sst_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric SLA-SST Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_co2_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_co2_chl_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric CO2-CHL Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_chl_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric SLA-CHL Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_co2_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_co2_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric SLA-CO2 Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_sla_chl_ano2_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_sla_chl_ano2_sig_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric SLA-CHL2 Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_vort_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_vort_chl_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric Vort-CHL Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_disp_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_disp_chl_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric disp-CHL Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, corr_ftle_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_cyc_corr_ftle_chl_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. Cyclonic Eddy Centric ftle-CHL Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        #####################################

        #################################################################            




        ########################### anticyclonic ###########################
        spatial_map_ex(tile_lons, tile_lats, anti_radius, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_radius_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric Radius ($km$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, anti_phase, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_phase_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric Phase ($\degree$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, anti_cyc_n, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_count_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Counts' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, anti_lat, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_lat_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric Latitude ($\degree$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, anti_lon, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_lon_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric Longitude ($\degree$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, anti_sla, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_sla_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric SLA (m)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, anti_vort, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_vort_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric Vorticity (s$^{-1}$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, anti_disp, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_disp_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric Displacement ($\degree$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, anti_ftle, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_ftle_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric FTLE ($\degree$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, anti_sst, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_sst_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric SST ($\degree$)' + '\n ' + str(temporal))
        spatial_map_ex(tile_lons, tile_lats, anti_chl, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_chl_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric CHL (mg.m$^{-3}$)' + '\n ' + str(temporal), [0, 0.4])
        spatial_map_ex(tile_lons, tile_lats, anti_co2, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_co2_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric fCO2 ($\mu$atm)' + '\n ' + str(temporal), None, True)
    
    
        spatial_map_ex(tile_lons, tile_lats, anti_ano_phase, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_phase_ano_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric Phase Anomally (%)' + '\n ' + str(temporal), bound_ano)
        spatial_map_ex(tile_lons, tile_lats, anti_ano_sla, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_sla_ano_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric SLA Anomally (%)' + '\n ' + str(temporal), bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, anti_ano_vort, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_vort_ano_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric Vorticity Anomally (%)' + '\n ' + str(temporal), bound_ano)
        spatial_map_ex(tile_lons, tile_lats, anti_ano_disp, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_disp_ano_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric Displacement Anomally (%)' + '\n ' + str(temporal), bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, anti_ano_ftle, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_ftle_ano_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric FTLE Anomally (%)' + '\n ' + str(temporal), bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, anti_ano_sst, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_sst_ano_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric SST Anomally (%)' + '\n ' + str(temporal), bound_ano, True, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, anti_ano_chl, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_chl_ano_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric CHL Anomally (%)' + '\n ' + str(temporal), bound_ano, False, 'bwr')
        spatial_map_ex(tile_lons, tile_lats, anti_ano_co2, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_co2_ano_'+str(temporal)+'.png', 'Yearly STA AntiCyclonic Eddy Centric fCO2 Anomally (%)' + '\n ' + str(temporal), bound_ano, True, 'bwr')
        
        ######## anomally correlations ######
        spatial_map_ex(tile_lons, tile_lats, anti_corr_chl_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_chl_sst_ano_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric CHL-SST Anomally' + '\n ' + str(temporal), bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_co2_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_co2_sst_ano_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric CO2-SST Anomally' + '\n ' + str(temporal), bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_sst_ano_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric SLA-SST Anomally' + '\n ' + str(temporal), bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_co2_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_co2_chl_ano_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric CO2-CHL Anomally' + '\n ' + str(temporal), bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_chl_ano_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric SLA-CHL Anomally' + '\n ' + str(temporal), bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_co2_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_co2_ano_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric SLA-CO2 Anomally' + '\n ' + str(temporal), bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_chl_ano2, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_chl_ano2_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric SLA-CHL2 Anomally' + '\n ' + str(temporal), bound_corr, False, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_vort_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_vort_chl_ano_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric Vort-CHL Anomally' + '\n ' + str(temporal), bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_disp_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_disp_chl_ano_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric disp-CHL Anomally' + '\n ' + str(temporal), bound_corr, True, corr_ano_cm)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_ftle_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_ftle_chl_ano_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric ftle-CHL Anomally' + '\n ' + str(temporal), bound_corr, True, corr_ano_cm)

        spatial_map_ex(tile_lons, tile_lats, anti_corr_chl_sst_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_chl_sst_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric CHL-SST Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_co2_sst_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_co2_sst_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric CO2-SST Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_sst_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_sst_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric SLA-SST Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_co2_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_co2_chl_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric CO2-CHL Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_chl_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric SLA-CHL Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_co2_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_co2_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric SLA-CO2 Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_sla_chl_ano2_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_sla_chl_ano2_sig_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric SLA-CHL2 Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_vort_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_vort_chl_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric Vort-CHL Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_disp_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_disp_chl_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric disp-CHL Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        spatial_map_ex(tile_lons, tile_lats, anti_corr_ftle_chl_ano_sig, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_anticyc_corr_ftle_chl_ano_sig_'+str(temporal)+'.png', 'Yearly STA Corr. AntiCyclonic Eddy Centric ftle-CHL Anomally Signi.' + '\n ' + str(temporal), bound_signi)
        #####################################
        
        #################################################################
        




        ########################### differential ###########################

        diff_bounds = [-50, 50]
        colmap = 'bwr'
        colmap = 'seismic'
        colmap = cmocean.cm.balance 
        
        spatial_map_ex(tile_lons, tile_lats, diff_disp_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_disp_ano_'+str(temporal)+'.png', 'Yearly Differential STA Displacement Anomally (%)' + '\n ' + str(temporal), diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_ftle_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_ftle_ano_'+str(temporal)+'.png', 'Yearly Differential STA FTLE Anomally (%)' + '\n ' + str(temporal), diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_sst_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_sst_ano_'+str(temporal)+'.png', 'Yearly Differential STA SST Anomally (%)' + '\n ' + str(temporal), diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_chl_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_chl_ano_'+str(temporal)+'.png', 'Yearly Differential STA CHL Anomally (%)' + '\n ' + str(temporal), diff_bounds, False, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_chl_full_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_chl_full_ano_'+str(temporal)+'.png', 'Monthly Differential STA CHL(full) Anomally (%)' + '\n ' + str(temporal), diff_bounds, False, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_co2_ano, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_co2_ano_'+str(temporal)+'.png', 'Yearly Differential STA $fCO_{2}$ Anomally (%)' + '\n ' + str(temporal), diff_bounds, True, colmap)

        spatial_map_ex(tile_lons, tile_lats, diff_disp, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_disp_'+str(temporal)+'.png', 'Yearly Differential STA Displacement (%)' + '\n ' + str(temporal), diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_ftle, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_ftle_'+str(temporal)+'.png', 'Yearly Differential STA FTLE (%)' + '\n ' + str(temporal), diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_sst, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_sst_'+str(temporal)+'.png', 'Yearly Differential STA SST (%)' + '\n ' + str(temporal), diff_bounds, True, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_chl, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_chl_'+str(temporal)+'.png', 'Yearly Differential STA CHL (%)' + '\n ' + str(temporal), diff_bounds, False, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_chl_full, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_chl_full_'+str(temporal)+'.png', 'Yearly Differential STA CHL(full) (%)' + '\n ' + str(temporal), diff_bounds, False, colmap)
        spatial_map_ex(tile_lons, tile_lats, diff_co2, minlat, maxlat, minlon, maxlon, spacing, 'gallery/sta_diff_co2_'+str(temporal)+'.png', 'Yearly Differential STA $fCO_{2}$ (%)' + '\n ' + str(temporal), diff_bounds, True, colmap)
        #################################################################
    return    




def hovmoller(query):
    temporal1 = 2003
    temporal2 = 2015

    minlat = -80
    maxlat = 80    
    spacing = 4.
    
    query = remove_spatial_conditions(query)
    x = range(temporal1, temporal2+1)
    y = np.arange(minlat+spacing/2., maxlat, spacing)
    base_query = query
    
    X, Y = np.meshgrid(x, y)


    cyc_n = X * np.nan
    radius = X * np.nan
    sla = X * np.nan
    vort = X * np.nan
    disp = X * np.nan
    ftle = X * np.nan
    sst = X * np.nan
    chl = X * np.nan
    co2 = X * np.nan
    mld = X * np.nan
    sss = X * np.nan
    
    ano_sla = X * np.nan
    ano_vort = X * np.nan
    ano_disp = X * np.nan
    ano_ftle = X * np.nan
    ano_sst = X * np.nan
    ano_chl = X * np.nan
    ano_co2 = X * np.nan
    ano_mld = X * np.nan
    ano_sss = X * np.nan


    anti_cyc_n = X * np.nan
    anti_radius = X * np.nan
    anti_sla = X * np.nan
    anti_vort = X * np.nan
    anti_disp = X * np.nan
    anti_ftle = X * np.nan
    anti_sst = X * np.nan
    anti_chl = X * np.nan
    anti_co2 = X * np.nan
    anti_mld = X * np.nan
    anti_sss = X * np.nan
    
    anti_ano_sla = X * np.nan
    anti_ano_vort = X * np.nan
    anti_ano_disp = X * np.nan
    anti_ano_ftle = X * np.nan
    anti_ano_sst = X * np.nan
    anti_ano_chl = X * np.nan
    anti_ano_co2 = X * np.nan
    anti_ano_mld = X * np.nan
    anti_ano_sss = X * np.nan



    diff_disp = X * np.nan
    diff_ftle = X * np.nan
    diff_sst = X * np.nan
    diff_chl = X * np.nan
    diff_co2 = X * np.nan
    diff_mld = X * np.nan
    diff_sss = X * np.nan

    counter = 0
    for dim0 in range(0, X.shape[0]):        
        for dim1 in range(0, X.shape[1]):
                temporal = X[dim0, dim1]
                midlat = Y[dim0, dim1]
                counter += 1
                print('Cycle: %d, Progress: %2.2f%s ' % (temporal, 100.*counter/(X.shape[0]*X.shape[1]), '%'))

                
        
                query = base_query
                if query.find('WHERE') >= 0:
                    query = query + ' AND year=' + str(temporal)
                else:        
                    query = query + ' WHERE year=' + str(temporal)
        
                query_temporal = query 


                ulat = midlat + spacing/2.
                llat = midlat - spacing/2.
                query = query_temporal + ' AND eddy_lat>='+str(llat) + ' AND eddy_lat<='+str(ulat)          
                query1 = query + ' AND eddy_polarity=1'
                query2 = query + ' AND eddy_polarity=-1'
                conn = db_connect()
                df1 = sql.read_sql(query1, conn)
                conn.close()
                conn = db_connect()
                df2 = sql.read_sql(query2, conn)
                conn.close()
                if len(df1)<1 or len(df2)<1:
                    #print('No match found. len(df1): '+str(len(df1))+' len(df2): '+str(len(df2)))
                    continue                
                df1 = df1.fillna(float('NaN'))
                df2 = df2.fillna(float('NaN'))                    

                
                cyc_n[dim0, dim1] = len(np.array(df1.year))
                radius[dim0, dim1] = np.nanmean(df1.eddy_radius)
                sla[dim0, dim1] = np.nanmean(df1.sla_mean_fixed)
                vort[dim0, dim1] = np.nanmean(df1.vort_mean_fixed)
                disp[dim0, dim1] = np.nanmean(df1.displacement_mean_fixed)
                ftle[dim0, dim1] = np.nanmean(df1.ftle_mean_fixed)
                sst[dim0, dim1] = np.nanmean(df1.sst_mean_fixed)
                chl[dim0, dim1] = np.nanmean(df1.chl_mean_fixed)
                co2[dim0, dim1] = np.nanmean(df1.CO2_mean_surface)
                mld[dim0, dim1] = np.nanmean(df1.mld_mean_fixed)
                sss[dim0, dim1] = np.nanmean(df1.sss_mean_fixed)
                
                ano_sla[dim0, dim1] = np.nanmean(df1.sla_mean_fixed-df1.sla_mean_bkg)
                ano_vort[dim0, dim1] = np.nanmean(df1.vort_mean_fixed-df1.vort_mean_bkg)
                ano_disp[dim0, dim1] = np.nanmean(df1.displacement_mean_fixed-df1.displacement_mean_bkg)
                ano_ftle[dim0, dim1] = np.nanmean(df1.ftle_mean_fixed-df1.ftle_mean_bkg)
                ano_sst[dim0, dim1] = np.nanmean(df1.sst_mean_fixed-df1.sst_mean_bkg)
                ano_chl[dim0, dim1] = np.nanmean(df1.chl_mean_fixed-df1.chl_mean_bkg)
                ano_co2[dim0, dim1] = np.nanmean(df1.CO2_mean_surface-df1.CO2_mean_surface_bkg)
                ano_mld[dim0, dim1] = np.nanmean(df1.mld_mean_fixed-df1.mld_mean_bkg)
                ano_sss[dim0, dim1] = np.nanmean(df1.sss_mean_fixed-df1.sss_mean_bkg)
                





                anti_cyc_n[dim0, dim1] = len(np.array(df2.year))
                anti_radius[dim0, dim1] = np.nanmean(df2.eddy_radius)
                anti_sla[dim0, dim1] = np.nanmean(df2.sla_mean_fixed)
                anti_vort[dim0, dim1] = np.nanmean(df2.vort_mean_fixed)
                anti_disp[dim0, dim1] = np.nanmean(df2.displacement_mean_fixed)
                anti_ftle[dim0, dim1] = np.nanmean(df2.ftle_mean_fixed)
                anti_sst[dim0, dim1] = np.nanmean(df2.sst_mean_fixed)
                anti_chl[dim0, dim1] = np.nanmean(df2.chl_mean_fixed)
                anti_co2[dim0, dim1] = np.nanmean(df2.CO2_mean_surface)
                anti_mld[dim0, dim1] = np.nanmean(df2.mld_mean_fixed)
                anti_sss[dim0, dim1] = np.nanmean(df2.sss_mean_fixed)
                
                anti_ano_sla[dim0, dim1] = np.nanmean(df2.sla_mean_fixed-df2.sla_mean_bkg)
                anti_ano_vort[dim0, dim1] = np.nanmean(df2.vort_mean_fixed-df2.vort_mean_bkg)
                anti_ano_disp[dim0, dim1] = np.nanmean(df2.displacement_mean_fixed-df2.displacement_mean_bkg)
                anti_ano_ftle[dim0, dim1] = np.nanmean(df2.ftle_mean_fixed-df2.ftle_mean_bkg)
                anti_ano_sst[dim0, dim1] = np.nanmean(df2.sst_mean_fixed-df2.sst_mean_bkg)
                anti_ano_chl[dim0, dim1] = np.nanmean(df2.chl_mean_fixed-df2.chl_mean_bkg)
                anti_ano_co2[dim0, dim1] = np.nanmean(df2.CO2_mean_surface-df2.CO2_mean_surface_bkg)
                anti_ano_mld[dim0, dim1] = np.nanmean(df2.mld_mean_fixed-df2.mld_mean_bkg)
                anti_ano_sss[dim0, dim1] = np.nanmean(df2.sss_mean_fixed-df2.sss_mean_bkg)



                diff_disp[dim0, dim1] = diff_percent(df2.displacement_mean_fixed, df1.displacement_mean_fixed)
                diff_ftle[dim0, dim1] = diff_percent(df2.ftle_mean_fixed, df1.ftle_mean_fixed)
                diff_sst[dim0, dim1] = diff_percent(df2.sst_mean_fixed, df1.sst_mean_fixed)
                diff_chl[dim0, dim1] = diff_percent(df2.chl_mean_fixed, df1.chl_mean_fixed)
                diff_co2[dim0, dim1] = diff_percent(df2.CO2_mean_surface, df1.CO2_mean_surface)
                diff_mld[dim0, dim1] = diff_percent(df2.mld_mean_fixed, df1.mld_mean_fixed)
                diff_sss[dim0, dim1] = diff_percent(df2.sss_mean_fixed, df1.sss_mean_fixed)
                    

    diff_cm = 'bwr'
    ########################### cyclonic ###########################
    hovmoller_plot(X, Y, cyc_n, 'gallery/hovmoller_cyc_count.png', title='Cyclonic Eddy Counts', col_map='jet') 
    hovmoller_plot(X, Y, radius, 'gallery/hovmoller_cyc_radius.png', title='Cyclonic Eddy Radius (km)', col_map='jet') 
    hovmoller_plot(X, Y, sla, 'gallery/hovmoller_cyc_sla.png', title='Cyclonic Eddy SLA (m)', col_map='jet') 
    hovmoller_plot(X, Y, vort, 'gallery/hovmoller_cyc_vort.png', title='Cyclonic Eddy Vorticity (s$^{-1}$)', col_map='jet') 
    hovmoller_plot(X, Y, disp, 'gallery/hovmoller_cyc_disp.png', title='Cyclonic Eddy Displacement ($\degree$)', col_map='jet') 
    hovmoller_plot(X, Y, ftle, 'gallery/hovmoller_cyc_ftle.png', title='Cyclonic Eddy FTLE (day$^{-1}$)', col_map='jet') 
    hovmoller_plot(X, Y, co2, 'gallery/hovmoller_cyc_co2.png', title='Cyclonic Eddy fCO$_2$ ($\mu$atm)', col_map='jet') 
    hovmoller_plot(X, Y, sst, 'gallery/hovmoller_cyc_sst.png', title='Cyclonic Eddy SST (C$\degree$)', col_map='jet') 
    hovmoller_plot(X, Y, mld, 'gallery/hovmoller_cyc_mld.png', title='Cyclonic Eddy MLD (m)', col_map='jet') 
    hovmoller_plot(X, Y, sss, 'gallery/hovmoller_cyc_sss.png', title='Cyclonic Eddy SSS (psu)', col_map='jet') 

    hovmoller_plot(X, Y, ano_sla, 'gallery/hovmoller_cyc_sla_ano.png', title='Cyclonic Eddy SLA Anomally (m)', col_map='jet') 
    hovmoller_plot(X, Y, ano_vort, 'gallery/hovmoller_cyc_vort_ano.png', title='Cyclonic Eddy Vorticity Anomally (s$^{-1}$)', col_map='jet') 
    hovmoller_plot(X, Y, ano_disp, 'gallery/hovmoller_cyc_disp_ano.png', title='Cyclonic Eddy Displacement Anomally ($\degree$)', col_map='jet') 
    hovmoller_plot(X, Y, ano_ftle, 'gallery/hovmoller_cyc_ftle_ano.png', title='Cyclonic Eddy FTLE Anomally (day$^{-1}$)', col_map='jet') 
    hovmoller_plot(X, Y, ano_co2, 'gallery/hovmoller_cyc_co2_ano.png', title='Cyclonic Eddy fCO$_2$ Anomally ($\mu$atm)', col_map='jet') 
    hovmoller_plot(X, Y, ano_sst, 'gallery/hovmoller_cyc_sst_ano.png', title='Cyclonic Eddy SST Anomally (C$\degree$)', col_map='jet') 
    hovmoller_plot(X, Y, ano_mld, 'gallery/hovmoller_cyc_mld_ano.png', title='Cyclonic Eddy MLD Anomally (m)', col_map='jet') 
    hovmoller_plot(X, Y, ano_sss, 'gallery/hovmoller_cyc_sss_ano.png', title='Cyclonic Eddy SSS Anomally (psu)', col_map='jet') 




    hovmoller_plot(X, Y, anti_cyc_n, 'gallery/hovmoller_anticyc_count.png', title='AntiCyclonic Eddy Counts', col_map='jet') 
    hovmoller_plot(X, Y, anti_radius, 'gallery/hovmoller_anticyc_radius.png', title='AntiCyclonic Eddy Radius (km)', col_map='jet') 
    hovmoller_plot(X, Y, anti_sla, 'gallery/hovmoller_anticyc_sla.png', title='AntiCyclonic Eddy SLA (m)', col_map='jet') 
    hovmoller_plot(X, Y, anti_vort, 'gallery/hovmoller_anticyc_vort.png', title='AntiCyclonic Eddy Vorticity (s$^{-1}$)', col_map='jet') 
    hovmoller_plot(X, Y, anti_disp, 'gallery/hovmoller_anticyc_disp.png', title='AntiCyclonic Eddy Displacement ($\degree$)', col_map='jet') 
    hovmoller_plot(X, Y, anti_ftle, 'gallery/hovmoller_anticyc_ftle.png', title='AntiCyclonic Eddy FTLE (day$^{-1}$)', col_map='jet') 
    hovmoller_plot(X, Y, anti_co2, 'gallery/hovmoller_anticyc_co2.png', title='AntiCyclonic Eddy fCO$_2$ ($\mu$atm)', col_map='jet') 
    hovmoller_plot(X, Y, anti_sst, 'gallery/hovmoller_anticyc_sst.png', title='AntiCyclonic Eddy SST (C$\degree$)', col_map='jet') 
    hovmoller_plot(X, Y, anti_mld, 'gallery/hovmoller_anticyc_mld.png', title='AntiCyclonic Eddy MLD (m)', col_map='jet') 
    hovmoller_plot(X, Y, anti_sss, 'gallery/hovmoller_anticyc_sss.png', title='AntiCyclonic Eddy SSS (psu)', col_map='jet') 

    hovmoller_plot(X, Y, anti_ano_sla, 'gallery/hovmoller_anticyc_sla_ano.png', title='AntiCyclonic Eddy SLA Anomally (m)', col_map='jet') 
    hovmoller_plot(X, Y, anti_ano_vort, 'gallery/hovmoller_anticyc_vort_ano.png', title='AntiCyclonic Eddy Vorticity Anomally (s$^{-1}$)', col_map='jet') 
    hovmoller_plot(X, Y, anti_ano_disp, 'gallery/hovmoller_anticyc_disp_ano.png', title='AntiCyclonic Eddy Displacement Anomally ($\degree$)', col_map='jet') 
    hovmoller_plot(X, Y, anti_ano_ftle, 'gallery/hovmoller_anticyc_ftle_ano.png', title='AntiCyclonic Eddy FTLE Anomally (day$^{-1}$)', col_map='jet') 
    hovmoller_plot(X, Y, anti_ano_co2, 'gallery/hovmoller_anticyc_co2_ano.png', title='AntiCyclonic Eddy fCO$_2$ Anomally ($\mu$atm)', col_map='jet') 
    hovmoller_plot(X, Y, anti_ano_sst, 'gallery/hovmoller_anticyc_sst_ano.png', title='AntiCyclonic Eddy SST Anomally (C$\degree$)', col_map='jet') 
    hovmoller_plot(X, Y, anti_ano_mld, 'gallery/hovmoller_anticyc_mld_ano.png', title='AntiCyclonic Eddy MLD Anomally (m)', col_map='jet') 
    hovmoller_plot(X, Y, anti_ano_sss, 'gallery/hovmoller_anticyc_sss_ano.png', title='AntiCyclonic Eddy SSS Anomally (psu)', col_map='jet') 
    
    

    hovmoller_plot(X, Y, diff_disp, 'gallery/hovmoller_diff_disp.png', title='Differential Displacement (%)', col_map=diff_cm) 
    hovmoller_plot(X, Y, diff_ftle, 'gallery/hovmoller_diff_ftle.png', title='Differential FTLE (%)', col_map=diff_cm) 
    hovmoller_plot(X, Y, diff_sst, 'gallery/hovmoller_diff_sst.png', title='Differential SST (%)', col_map=diff_cm) 
    hovmoller_plot(X, Y, diff_chl, 'gallery/hovmoller_diff_chl.png', title='Differential CHL (%)', col_map=diff_cm) 
    hovmoller_plot(X, Y, diff_co2, 'gallery/hovmoller_diff_co2.png', title='Differential $fCO_{2}$ (%)', col_map=diff_cm) 
    hovmoller_plot(X, Y, diff_mld, 'gallery/hovmoller_diff_mld.png', title='Differential MLD (%)', col_map=diff_cm) 
    hovmoller_plot(X, Y, diff_sss, 'gallery/hovmoller_diff_sss.png', title='Differential SSS (%)', col_map=diff_cm) 
    return    





def pairplot(df, cols, store_path=''):
    plt.clf()
    df = df.fillna(method='ffill')
    df = df.fillna(method='bfill')
    df = df.fillna(0)
    #sns.set(style='ticks', context='notebook')
    sns.pairplot(df[cols], size=2.5)

    plt.tight_layout()
    if len(store_path) > 0:
        plt.savefig(store_path, format='png', dpi=300, transparent=plot_transparency)
    return


def cores_sns_pairplot(df):
    cols = ['year', 'month', 'eddy_lat', 'eddy_lon', 'chl_mean_fixed', 'sst_mean_fixed', 'displacement_mean_fixed', 'vort_mean_fixed', 'sla_mean_fixed']
    cols = ['eddy_lat', 'eddy_lon', 'chl_mean_fixed', 'sst_mean_fixed', 'sla_mean_fixed', 'CO2_mean_surface']
    pairplot(df, cols, 'gallery/cores_pp1.png')
    
    return


def sns_pairplot(df, dataset):
    if dataset == 'Cores':
        cores_sns_pairplot(df)
    #if dataset == 'Tracks':
        #tracks_sns_pairplot(df)
    return


def cores_map(eddy_lon, eddy_lat):
    plt.clf()
    	
    map = Basemap(projection='kav7', lon_0=0, resolution='l')
    #map.drawcoastlines(linewidth=0.1)
    #map.fillcontinents(color='#333333', lake_color='#333333')
    #map.drawparallels(np.arange(-90.,99.,30.), linewidth=.2, color='w', labels=[1,1,0,0], fontsize=5)
    #map.drawmeridians(np.arange(-180.,180.,60.), linewidth=.2, color='w', labels=[0,0,0,1], fontsize=5)
    map.bluemarble()
    
    eddy_lon[np.where(eddy_lon>180)] = eddy_lon[np.where(eddy_lon>180)] - 360
    x_map, y_map = map(eddy_lon, eddy_lat)
    map.plot(x_map, y_map, 'ro', markersize=1, markeredgewidth=0.0, alpha=1)
    
    plt.savefig('gallery/map.png', bbox_inches='tight' , dpi=300, transparent=plot_transparency)

    return



def spatial_map(eddy_lon, eddy_lat, vals, store_path='', title='', bounds=None, cleanup=False, col_map='jet'):

    try:
        if cleanup:
            x = np.array([])
            y = np.array([])
            z = np.array([])
            for i in range(0, len(eddy_lon)):
                if eddy_lon[i] <> None and eddy_lat[i] <> None and vals[i] <> None:
                    if (not math.isnan(eddy_lon[i])) and (not math.isnan(eddy_lat[i])) and (not math.isnan(vals[i])):
                        x = np.append(x, eddy_lon[i])
                        y = np.append(y, eddy_lat[i])
                        z = np.append(z, vals[i])
            eddy_lon = x
            eddy_lat = y                
            vals = z                
            
        plt.clf()
    
        eddy_lon[np.where(eddy_lon>180)] = eddy_lon[np.where(eddy_lon>180)] - 360
        minlat = np.nanmin(eddy_lat)
        maxlat = np.nanmax(eddy_lat)
        minlon = np.nanmin(eddy_lon)
        maxlon = np.nanmax(eddy_lon)
        
        minlat = -90
        maxlat = 90
    
        ################ Projection  #################
        #map = Basemap(projection='kav7', lon_0=0, resolution='l')
        #map = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='l')
    
    
        if minlon * maxlon < 0:
            map = Basemap(projection='mill', llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=minlon, urcrnrlon=maxlon, resolution='l')
        else:    
            map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=minlon, urcrnrlon=maxlon,\
                rsphere=(6378137.00,6356752.3142),\
                resolution='l',area_thresh=1000.,projection='lcc',\
                lat_1=maxlat,lon_0=(maxlon+minlon)/2)
    
        ##############################################
        
        
        #map.drawcoastlines(linewidth=0.5)
        map.fillcontinents(color='#333333', lake_color='#333333')
        
        #map.drawparallels(np.arange(-90.,90.,30.), linewidth=.5, color=[.2,.2,.2], labels=[1,1,0,0], fontsize=5)
        #map.drawmeridians(np.arange(-180.,180.,60.), linewidth=.5, color=[.2,.2,.2], labels=[0,0,0,1], fontsize=5)
    
        map.drawparallels(np.arange(minlat,maxlat, (maxlat-minlat)/10 ), linewidth=.5, color=[.2,.2,.2], labels=[1,1,0,0], fontsize=5)
        map.drawmeridians(np.arange(minlon,maxlon, (maxlon-minlon)/10 ), linewidth=.5, color=[.2,.2,.2], labels=[0,0,0,1], fontsize=5)
    
        ##############   Map Background  ##############
        #map.bluemarble()
        #map.shadedrelief()
        #map.etopo()
        ##############################################
        if bounds == None:
            bounds = [np.nanpercentile(vals, 5), np.nanpercentile(vals, 95)]
            
        #eddy_lon[np.where(eddy_lon>180)] = eddy_lon[np.where(eddy_lon>180)] - 360
        x_map, y_map = map(eddy_lon, eddy_lat)
    
        cm = plt.cm.get_cmap(col_map)    
        sc = map.scatter(x_map, y_map, c=vals, vmin=bounds[0], vmax=bounds[1], cmap=cm, lw=0) #, s=5
        map.colorbar(sc, 'bottom', size='5%', pad='7%')
        if len(title) > 0:
            plt.title(title + '\n Sample Size: ' + str(len(eddy_lon)))
        
        if len(store_path) > 0:
            plt.savefig(store_path, bbox_inches='tight' , dpi=300, transparent=plot_transparency)
            
    except Exception as e:
        print('Error in spatial_map. Error message: '+str(e))
    return


def core_spatial_maps(df):
    #spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.eddy_radius), 'gallery/map_radius.png', 'Eddy Centric Radius ($km$)')
    #spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.phase_integ_fixed), 'gallery/map_phase.png', 'Eddy Centric Phase ($\degree$)')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.sla_mean_fixed), 'gallery/map_sla.png', 'Eddy Centric SLA (m)')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.vort_mean_fixed), 'gallery/map_vort.png', 'Eddy Centric Vorticity (s$^{-1}$)')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.displacement_mean_fixed), 'gallery/map_disp.png', 'Eddy Centric Displacement ($\degree$)')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.ftle_mean_fixed), 'gallery/map_ftle.png', 'Eddy Centric FTLE ($\degree$)')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.sst_mean_fixed), 'gallery/map_sst.png', 'Eddy Centric SST ($\degree$)')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.chl_mean_fixed), 'gallery/map_chl.png', 'Eddy Centric CHL (mg.m$^{-3}$)', [0, 0.4], True, cmocean.cm.algae)
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.mld_mean_fixed), 'gallery/map_mld.png', 'Eddy Centric MLD (m)')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.sss_mean_fixed), 'gallery/map_sss.png', 'Eddy Centric SSS (psu)')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.CO2_mean_surface), 'gallery/map_co2.png', 'Eddy Centric fCO2 ($\mu$atm)', None, True)


    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.phase_integ_fixed - df.phase_mean_bkg), 'gallery/map_ano_phase.png', 'Eddy Centric Phase Anomally ($\degree$)')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.sla_mean_fixed - df.sla_mean_bkg), 'gallery/map_ano_sla.png', 'Eddy Centric SLA Anomally (m)')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.vort_mean_fixed - df.vort_mean_bkg), 'gallery/map_ano_vort.png', 'Eddy Centric Vorticity Anomally (s$^{-1}$)')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.displacement_mean_fixed - df.displacement_mean_bkg), 'gallery/map_ano_disp.png', 'Eddy Centric Displacement Anomally ($\degree$)')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.ftle_mean_fixed - df.ftle_mean_bkg), 'gallery/map_ano_ftle.png', 'Eddy Centric FTLE Anomally ($\degree$)')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.sst_mean_fixed - df.sst_mean_bkg), 'gallery/map_ano_sst.png', 'Eddy Centric SST Anomally ($\degree$)')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.chl_mean_fixed - df.chl_mean_bkg), 'gallery/map_ano_chl.png', 'Eddy Centric CHL Anomally (mg.m$^{-3}$)', [-0.1, 0.1], False, 'bwr')
    spatial_map(np.array(df.eddy_lon), np.array(df.eddy_lat), np.array(df.CO2_mean_surface - df.CO2_mean_surface_bkg), 'gallery/map_ano_co2.png', 'Eddy Centric fCO2 Anomally ($\mu$atm)', [-5, 5], True, 'bwr')
    return
    
    
def spatial_maps(df, dataset):
    if dataset == 'Cores':
        core_spatial_maps(df)
    #if dataset == 'Tracks':
    #    track_spatial_maps(df)
    return


def add_fields(df):
    df['ano_phase_fixed'] = df.phase_integ_fixed - df.phase_mean_bkg 
    df['ano_phase_full'] = df.phase_integ_full - df.phase_mean_bkg 

    df['ano_sla_fixed'] = df.sla_mean_fixed - df.sla_mean_bkg 
    df['ano_sla_full'] = df.sla_mean_full - df.sla_mean_bkg  

    df['ano_vort_fixed'] = df.vort_mean_fixed - df.vort_mean_bkg 
    df['ano_vort_full'] = df.vort_mean_full - df.vort_mean_bkg  

    df['ano_disp_fixed'] = df.displacement_mean_fixed - df.displacement_mean_bkg 
    df['ano_disp_full'] = df.displacement_mean_full - df.displacement_mean_bkg  

    df['ano_ftle_fixed'] = df.ftle_mean_fixed - df.ftle_mean_bkg 
    df['ano_ftle_full'] = df.ftle_mean_full - df.ftle_mean_bkg  

    df['ano_sst_fixed'] = df.sst_mean_fixed - df.sst_mean_bkg 
    df['ano_sst_full'] = df.sst_mean_full - df.sst_mean_bkg  

    df['ano_chl_fixed'] = df.chl_mean_fixed - df.chl_mean_bkg 
    df['ano_chl_full'] = df.chl_mean_full - df.chl_mean_bkg  

    df['ano_co2'] = df.CO2_mean_surface - df.CO2_mean_surface_bkg 

    df['ano_mld_fixed'] = df.mld_mean_fixed - df.mld_mean_bkg 
    df['ano_mld_full'] = df.mld_mean_full - df.mld_mean_bkg  

    df['ano_sss_fixed'] = df.sss_mean_fixed - df.sss_mean_bkg 
    df['ano_sss_full'] = df.sss_mean_full - df.sss_mean_bkg  
    return df
    
    
    
def plot_lifetime():
    query = 'SELECT track, MAX(eddy_age) AS lifetime FROM tblChelton GROUP BY track'
    #query = 'SELECT lifetime FROM tblTracks where lifetime>28'
    conn = db_connect()
    df = sql.read_sql(query, conn)
    conn.close()
    
    data = np.array(df.lifetime)
    y, x = np.histogram(np.array(data), bins=range(np.nanmin(data), np.nanmax(data)+1))
    
    plt.clf()
    plt.loglog(x[:-1],y,'.')
    plt.savefig('gallery/zipf.png', format='png', dpi=300)    
            
    return
#########################################################################
#                                                                       #       
#                                                                       #       
#                                                                       #       
#                                                                       #
#                                MAIN CODE                              #       
#                                                                       #       
#                                                                       #
#                                                                       #
#                                                                       #
#########################################################################



global plot_transparency
plot_transparency=False

lines = get_query_file()
query_id = lines[0].strip()
dataset = lines[1].strip()
query = lines[2].strip()



#spatially_averaged_monthly_series(query)
#sys.exit()

#spatially_averaged_yearly_series(query)
#sys.exit()


##data = np.load('gallery/hovmoller_cyc_sss.npz')
##hovmoller_plot(data['X'], data['Y'], data['V'], 'gallery/hovmoller_cyc_mld.png', title='Cyclonic Eddy MLD (m)', col_map='jet') 

#hovmoller(query)
#sys.exit()



if not dataset in ['Cores', 'Tracks']:
    print('Invalid Dataset!')
    sys.exit()
        


sns.reset_orig()
sns.set(style='darkgrid')




############## ML Tracks ##############
if int(query_id) >= 500 and int(query_id) < 600:        
    if dataset == 'Tracks':
        query = join_attribute(query)
        
    conn = db_connect()
    df = sql.read_sql(query, conn)
    conn.close()

    if dataset == 'Cores':
        df = add_fields(df)

    if int(query_id) == 500:
        ML.ExtraTrees(df, lines) 

    if int(query_id) == 501:
        ML.RandomForest(df, lines) 

    if int(query_id) == 502:
        ML.GradientBoosting(df, lines) 

    sys.exit()
#######################################


############## Data Export ##############
if query_id == '91':
    conn = db_connect()
    df = sql.read_sql(query, conn)
    conn.close()
    df.to_csv('data/data.csv')   
    sys.exit()
    
if query_id == '92':
    conn = db_connect()
    df = sql.read_sql(query, conn)
    conn.close()
    df.to_excel('data/data.xlsx')   
    sys.exit()
    
if query_id == '93':
    conn = db_connect()
    df = sql.read_sql(query, conn)
    conn.close()
    df.to_json('data/data.json')   
    sys.exit()
    
if query_id == '94':
    conn = db_connect()
    df = sql.read_sql(query, conn)
    conn.close()
    df.to_html('data/data.html')   
    sys.exit()
#########################################



############## Time Series ##############

if dataset == 'Cores' and query_id == '3':
    error_band = False
    monthly_series(query, error_band)
    sys.exit()
if dataset == 'Cores' and query_id == '31':
    error_band = True
    monthly_series(query, error_band)
    sys.exit()

    
if dataset == 'Cores' and query_id == '4':
    error_band = False
    yearly_series(query, error_band)
    sys.exit()
if dataset == 'Cores' and query_id == '41':
    error_band = True
    yearly_series(query, error_band)
    sys.exit()




if dataset == 'Cores' and query_id == '32':
    error_band = False
    monthly_correlations(query, error_band)
    sys.exit()
    
if dataset == 'Cores' and query_id == '42':
    error_band = False
    yearly_correlations(query, error_band)
    sys.exit()
#########################################



    
    
conn = db_connect()
df = sql.read_sql(query, conn)
conn.close()




############## basemap ##############
'''
if dataset == 'Cores': 
    cores_map(np.array(df.eddy_lon), np.array(df.eddy_lat))

spatial_maps(df, dataset)
'''
#####################################



############## pairplot ##############

#sns_pairplot(df, dataset)

#####################################




single_hists(df, dataset)
if dataset == 'Cores':
    anomally_core_hists(df)
    eddy_bkg_core_hists(df)
trend(df, dataset)


if query_id in ['2', '22']:
    sp = query.split()
    indices = [i for i,x in enumerate(sp) if x == 'eddy_polarity=1']
    if len(indices) == 1:
        sp[indices[0]] = '*#'
        if sp[indices[0]-1].upper() == 'AND':
            indices.append(indices[0]-1)
            sp[indices[0]-1] = '*#'     
    for i in range(0, len(indices)):  
        sp.remove('*#')
    double_query = ' '.join(sp)
    

    sp = query.split()
    indices = [i for i,x in enumerate(sp) if x == 'eddy_polarity=-1']
    if len(indices) == 1:
        sp[indices[0]] = '*#'
        if sp[indices[0]-1].upper() == 'AND':
            indices.append(indices[0]-1)
            sp[indices[0]-1] = '*#'     
    for i in range(0, len(indices)):  
        sp.remove('*#')
    double_query = ' '.join(sp)
        
   
    if double_query.find('WHERE') >= 0:
        query1 = double_query + ' AND eddy_polarity=1'
        query2 = double_query + ' AND eddy_polarity=-1'
    else:
        query1 = double_query + ' WHERE eddy_polarity=1'
        query2 = double_query + ' WHERE eddy_polarity=-1'
    

    conn = db_connect()
    df1 = sql.read_sql(query1, conn)
    conn.close()

    conn = db_connect()
    df2 = sql.read_sql(query2, conn)
    conn.close()
    
    double_hist(df1, df2, dataset)
  




if dataset == 'Tracks':
    query = join_attribute(query)
    conn = db_connect()
    df = sql.read_sql(query, conn)
    conn.close()
    attribute_single_hists(df)
    attribute_trend(df)
    if query_id == '22':
        query1 = join_attribute(query1)
        query2 = join_attribute(query2)
        
        conn = db_connect()
        df1 = sql.read_sql(query1, conn)
        conn.close()
    
        conn = db_connect()
        df2 = sql.read_sql(query2, conn)
        conn.close()
        
        attribute_double_hist(df1, df2)

        
        
        
        