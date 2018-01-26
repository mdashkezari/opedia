import sys
import numpy as np

#from mpl_toolkits.basemap import Basemap

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pyodbc
import pandas.io.sql as sql
import pandas as pd
import matplotlib.ticker as mtick
#import ML
import seaborn as sns


global plot_transparency
plot_transparency=False


def db_connect():
    try:
        print('Connecting to Database ...')
        
        '''
        ## Local Database
        server = 'DESKTOP-IK6754L'
        db = 'Eddy2003_2015'
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')
        '''
        
        ## Cloud (Azure) Databe
        server = 'oceanatlas.database.windows.net'
        db = 'Eddy2003_2015'
        Uid = 'AdminAtlas@oceanatlas'
        psw = 'Ocean@2016@'
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Uid=' + Uid + ';Pwd='+ psw +';Encrypt=yes')
        

        print('Successful Database Connection')
    except Exception as e:
        print('Error in Database Connectio. Error message: '+str(e))
        
    return conn


def get_query_file():
    q = open('query.txt', 'r')
    lines = q.readlines()
    return lines


def plot_single_hist(data, clr='m', labelx='', labely='', leg='', yscale='linear', store_path='', bincount=200):   
    if len(filter(None, data)) < 1:
        return
    plt.clf()	
    bins = np.linspace(np.nanmin(data), np.nanmax(data), bincount)
    lw = 1

    data=np.nan_to_num(data)

    plt.hist(data, bins=bins, color=clr, histtype='step', linewidth=lw, alpha=1)
    plt.hist(data, bins=bins, color=clr, label=[leg], histtype='stepfilled', alpha=0.25)
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
    plt.clf()   

    mmin = np.array([np.nanmin(data1), np.nanmin(data2)])
    mmax = np.array([np.nanmax(data1), np.nanmax(data2)])
    bins = np.linspace(np.nanmin(mmin), np.nanmax(mmax), bincount)

    lw = 1        

    data1=np.nan_to_num(data1)
    data2=np.nan_to_num(data2)

    plt.hist(data1, bins=bins, color=clr1, histtype='step', linewidth=lw, alpha=1)
    plt.hist(data1, bins=bins, color=clr1, label=[leg1], histtype='stepfilled', alpha=0.25)
    plt.hist(data2, bins=bins, color=clr2, histtype='step', linewidth=lw, alpha=1)
    plt.hist(data2, bins=bins, color=clr2, label=[leg2], histtype='stepfilled', alpha=0.25)

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

    #plt.gca().xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))    
    plt.show(block=False)
    plt.tight_layout()
    if len(store_path) > 0:
        plt.savefig(store_path, format='png', dpi=300, transparent=plot_transparency)    
    return


def plot_double_trend(data1, data2, data2_up, data2_down, data3, data4, data4_up, data4_down, error_band=True, marker='o--', msize=1, clr1=[0.4, 0.1, 0.8], clr2='cyan', labelx='', labely='', leg1='', leg2='', store_path=''):
    #marker='o--'
    plt.clf()
    plt.plot(data1, data2, marker, markersize=msize, markerfacecolor=clr1, markeredgecolor=clr1, alpha=0.7, label=leg1)
    plt.plot(data3, data4, marker, markersize=msize, markerfacecolor=clr2, markeredgecolor=clr2, alpha=0.7, label=leg2)
    if error_band:
        plt.fill_between(data1, data2_up, data2_down, color=clr1, alpha=0.3)
        plt.fill_between(data3, data4_up, data4_down, color=clr2, alpha=0.3)
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
    plot_double_hist(np.array(df1.vort_mean_fixed), np.array(df2.vort_mean_fixed), 'b', 'm', 'Vorticity (s$^{-1}$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_vort.png')
    plot_double_hist(np.array(df1.displacement_mean_fixed), np.array(df2.displacement_mean_fixed), 'b', 'm', 'Displacement ($\delta\degree$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_displacement.png')
    plot_double_hist(np.array(df1.ftle_mean_fixed), np.array(df2.ftle_mean_fixed), 'b', 'm', 'FTLE (day$^{-1}$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_ftle.png')
    plot_double_hist(np.array(df1.sst_mean_fixed), np.array(df2.sst_mean_fixed), 'b', 'm', 'SST (c$\degree$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_sst.png')
    plot_double_hist(zero_to_nan(np.array(df1.chl_mean_fixed)), zero_to_nan(np.array(df2.chl_mean_fixed)), 'b', 'm', 'CHL (mg.m$^{-3}$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_chl.png')

    plot_double_hist(np.array(df1.CO2_mean_surface), np.array(df2.CO2_mean_surface), 'b', 'm', 'CO$_2$ (uatm)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_co2.png', 30)

    chl1 = np.array(df1.chl_mean_fixed)
    chl1 = chl1[np.where(chl1 < 0.5)]
    chl2 = np.array(df2.chl_mean_fixed)
    chl2 = chl2[np.where(chl2 < 0.5)]
    plot_double_hist(chl1, chl2, 'b', 'm', 'Filtered CHL (mg.m$^{-3}$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_filtered_chl.png', 100)
    return


def core_double_hist_xlim(df1, df2):
    chl1 = zero_to_nan(np.array(df1.chl_mean_fixed))
    chl2 = zero_to_nan(np.array(df2.chl_mean_fixed))
    plot_double_hist_xlim((chl1 - np.array(df1.chl_mean_bkg)) / np.array(df1.chl_std_bkg), (chl2 - np.array(df2.chl_mean_bkg)) / np.array(df2.chl_std_bkg), 100, np.linspace(-.75, .75, 100), -1, 'b', 'm', '(chl_mean_fixed - chl_mean_bkg) / chl_std_bkg ($\sigma$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_chl_sig.png')
    plot_double_hist_xlim((np.array(df1.sst_mean_fixed) - np.array(df1.sst_mean_bkg)) / np.array(df1.sst_std_bkg), (np.array(df2.sst_mean_fixed) - np.array(df2.sst_mean_bkg)) / np.array(df2.sst_std_bkg), 100, np.linspace(-.4, .4, 100), -1, 'b', 'm', '(sst_mean_fixed - sst_mean_bkg) / sst_std_bkg ($\sigma$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_sst_sig.png')
    plot_double_hist_xlim((np.array(df1.ftle_mean_fixed) - np.array(df1.ftle_mean_bkg)) / np.array(df1.ftle_std_bkg), (np.array(df2.ftle_mean_fixed) - np.array(df2.ftle_mean_bkg)) / np.array(df2.ftle_std_bkg), 100, np.linspace(-2, 2, 100), -1, 'b', 'm', '(ftle_mean_fixed - ftle_mean_bkg) / ftle_std_bkg ($\sigma$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_ftle_sig.png')
    plot_double_hist_xlim((np.array(df1.displacement_mean_fixed) - np.array(df1.displacement_mean_bkg)) / np.array(df1.displacement_std_bkg), (np.array(df2.displacement_mean_fixed) - np.array(df2.displacement_mean_bkg)) / np.array(df2.displacement_std_bkg), 100, np.linspace(-2, 2, 100), -1, 'b', 'm', '(displacement_mean_fixed - displacement_mean_bkg) / displacement_std_bkg ($\sigma$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_displacement_sig.png')
    plot_double_hist_xlim((np.array(df1.vort_mean_fixed) - np.array(df1.vort_mean_bkg)) / np.array(df1.vort_std_bkg), (np.array(df2.vort_mean_fixed) - np.array(df2.vort_mean_bkg)) / np.array(df2.vort_std_bkg), 200, np.linspace(-100, 100, 200), -1, 'b', 'm', '(vort_mean_fixed - vort_mean_bkg) / vort_std_bkg ($\sigma$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_vort_sig.png')
    plot_double_hist_xlim((np.array(df1.sla_mean_fixed) - np.array(df1.sla_mean_bkg)) / np.array(df1.sla_std_bkg), (np.array(df2.sla_mean_fixed) - np.array(df2.sla_mean_bkg)) / np.array(df2.sla_std_bkg), 100, np.linspace(-5, 5, 100), -1, 'b', 'm', '(sla_mean_fixed - sla_mean_bkg) / sla_std_bkg ($\sigma$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_sla_sig.png')
    plot_double_hist_xlim((np.array(df1.phase_integ_fixed) - np.array(df1.phase_mean_bkg)) / np.array(df1.phase_std_bkg), (np.array(df2.phase_integ_fixed) - np.array(df2.phase_mean_bkg)) / np.array(df2.phase_std_bkg), 100, np.linspace(-3, 3, 100), -1, 'b', 'm', '(phase_integ_fixed - phase_mean_bkg) / phase_std_bkg ($\sigma$)', 'Density', 'Cyclonic', 'Anti-Cyclonic', 'linear', 'gallery/double_phase_sig.png')
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
        
        cyc_n = np.append(cyc_n, len(np.array(df1.year)))
        cyc_n_up = np.append(cyc_n_up, len(np.array(df1.year)))
        cyc_n_down = np.append(cyc_n_down, len(np.array(df1.year)))
        lat = np.append(lat, np.nanmean(np.array(df1.eddy_lat))) 
        lat_up = np.append(lat_up, np.nanmean(np.array(df1.eddy_lat)) + np.nanstd(np.array(df1.eddy_lat)) ) 
        lat_down = np.append(lat_down, np.nanmean(np.array(df1.eddy_lat)) - np.nanstd(np.array(df1.eddy_lat)) ) 
        lon = np.append(lon, np.nanmean(np.array(df1.eddy_lon))) 
        lon_up = np.append(lon_up, np.nanmean(np.array(df1.eddy_lon)) + np.nanstd(np.array(df1.eddy_lon)) ) 
        lon_down = np.append(lon_down, np.nanmean(np.array(df1.eddy_lon)) - np.nanstd(np.array(df1.eddy_lon)) ) 
        radius = np.append(radius, np.nanmean(np.array(df1.eddy_radius))) 
        radius_up = np.append(radius_up, np.nanmean(np.array(df1.eddy_radius)) + np.nanstd(np.array(df1.eddy_radius)) ) 
        radius_down = np.append(radius_down, np.nanmean(np.array(df1.eddy_radius)) - np.nanstd(np.array(df1.eddy_radius)) ) 
        phase = np.append(phase, np.nanmean(np.array(df1.phase_integ_fixed))) 
        phase_up = np.append(phase_up, np.nanmean(np.array(df1.phase_integ_fixed)) + np.nanstd(np.array(df1.phase_integ_fixed)) ) 
        phase_down = np.append(phase_down, np.nanmean(np.array(df1.phase_integ_fixed))  - np.nanstd(np.array(df1.phase_integ_fixed)) ) 
        sla = np.append(sla, np.nanmean(np.array(df1.sla_mean_fixed))) 
        sla_up = np.append(sla_up, np.nanmean(np.array(df1.sla_mean_fixed)) + np.nanstd(np.array(df1.sla_mean_fixed)) ) 
        sla_down = np.append(sla_down, np.nanmean(np.array(df1.sla_mean_fixed)) - np.nanstd(np.array(df1.sla_mean_fixed)) ) 
        vort = np.append(vort, np.nanmean(np.array(df1.vort_mean_fixed))) 
        vort_up = np.append(vort_up, np.nanmean(np.array(df1.vort_mean_fixed)) + np.nanstd(np.array(df1.vort_mean_fixed)) ) 
        vort_down = np.append(vort_down, np.nanmean(np.array(df1.vort_mean_fixed)) - np.nanstd(np.array(df1.vort_mean_fixed)) ) 
        disp = np.append(disp, np.nanmean(np.array(df1.displacement_mean_fixed))) 
        disp_up = np.append(disp_up, np.nanmean(np.array(df1.displacement_mean_fixed)) + np.nanstd(np.array(df1.displacement_mean_fixed)) ) 
        disp_down = np.append(disp_down, np.nanmean(np.array(df1.displacement_mean_fixed)) - np.nanstd(np.array(df1.displacement_mean_fixed)) ) 
        ftle = np.append(ftle, np.nanmean(np.array(df1.ftle_mean_fixed))) 
        ftle_up = np.append(ftle_up, np.nanmean(np.array(df1.ftle_mean_fixed)) + np.nanstd(np.array(df1.ftle_mean_fixed)) ) 
        ftle_down = np.append(ftle_down, np.nanmean(np.array(df1.ftle_mean_fixed)) - np.nanstd(np.array(df1.ftle_mean_fixed)) ) 
        sst = np.append(sst, np.nanmean(np.array(df1.sst_mean_fixed))) 
        sst_up = np.append(sst_up, np.nanmean(np.array(df1.sst_mean_fixed)) + np.nanstd(np.array(df1.sst_mean_fixed)) ) 
        sst_down = np.append(sst_down, np.nanmean(np.array(df1.sst_mean_fixed)) - np.nanstd(np.array(df1.sst_mean_fixed)) ) 
        chl = np.append(chl, np.nanmean(np.array(df1.chl_mean_fixed))) 
        chl_up = np.append(chl_up, np.nanmean(np.array(df1.chl_mean_fixed)) + np.nanstd(np.array(df1.chl_mean_fixed)) ) 
        chl_down = np.append(chl_down, np.nanmean(np.array(df1.chl_mean_fixed)) - np.nanstd(np.array(df1.chl_mean_fixed)) ) 
        co2 = np.append(co2, np.nanmean(np.array(df1.CO2_mean_surface))) 
        co2_up = np.append(co2_up, np.nanmean(np.array(df1.CO2_mean_surface)) + np.nanstd(np.array(df1.CO2_mean_surface)) ) 
        co2_down = np.append(co2_down, np.nanmean(np.array(df1.CO2_mean_surface)) - np.nanstd(np.array(df1.CO2_mean_surface)) ) 

        anti_cyc_n = np.append(anti_cyc_n, len(np.array(df2.year)))
        anti_cyc_n_up = np.append(anti_cyc_n_up, len(np.array(df2.year)))
        anti_cyc_n_down = np.append(anti_cyc_n_down, len(np.array(df2.year)))
        anti_lat = np.append(anti_lat, np.nanmean(np.array(df2.eddy_lat))) 
        anti_lat_up = np.append(anti_lat_up, np.nanmean(np.array(df2.eddy_lat)) + np.nanstd(np.array(df2.eddy_lat)) ) 
        anti_lat_down = np.append(anti_lat_down, np.nanmean(np.array(df2.eddy_lat)) - np.nanstd(np.array(df2.eddy_lat)) ) 
        anti_lon = np.append(anti_lon, np.nanmean(np.array(df2.eddy_lon))) 
        anti_lon_up = np.append(anti_lon_up, np.nanmean(np.array(df2.eddy_lon)) + np.nanstd(np.array(df2.eddy_lon)) ) 
        anti_lon_down = np.append(anti_lon_down, np.nanmean(np.array(df2.eddy_lon)) - np.nanstd(np.array(df2.eddy_lon)) ) 
        anti_radius = np.append(anti_radius, np.nanmean(np.array(df2.eddy_radius))) 
        anti_radius_up = np.append(anti_radius_up, np.nanmean(np.array(df2.eddy_radius)) + np.nanstd(np.array(df2.eddy_radius)) ) 
        anti_radius_down = np.append(anti_radius_down, np.nanmean(np.array(df2.eddy_radius)) - np.nanstd(np.array(df2.eddy_radius)) ) 
        anti_phase = np.append(anti_phase, np.nanmean(np.array(df2.phase_integ_fixed))) 
        anti_phase_up = np.append(anti_phase_up, np.nanmean(np.array(df2.phase_integ_fixed)) + np.nanstd(np.array(df2.phase_integ_fixed)) ) 
        anti_phase_down = np.append(anti_phase_down, np.nanmean(np.array(df2.phase_integ_fixed))  - np.nanstd(np.array(df2.phase_integ_fixed)) ) 
        anti_sla = np.append(anti_sla, np.nanmean(np.array(df2.sla_mean_fixed))) 
        anti_sla_up = np.append(anti_sla_up, np.nanmean(np.array(df2.sla_mean_fixed)) + np.nanstd(np.array(df2.sla_mean_fixed)) ) 
        anti_sla_down = np.append(anti_sla_down, np.nanmean(np.array(df2.sla_mean_fixed)) - np.nanstd(np.array(df2.sla_mean_fixed)) ) 
        anti_vort = np.append(anti_vort, np.nanmean(np.array(df2.vort_mean_fixed))) 
        anti_vort_up = np.append(anti_vort_up, np.nanmean(np.array(df2.vort_mean_fixed)) + np.nanstd(np.array(df2.vort_mean_fixed)) ) 
        anti_vort_down = np.append(anti_vort_down, np.nanmean(np.array(df2.vort_mean_fixed)) - np.nanstd(np.array(df2.vort_mean_fixed)) ) 
        anti_disp = np.append(anti_disp, np.nanmean(np.array(df2.displacement_mean_fixed))) 
        anti_disp_up = np.append(anti_disp_up, np.nanmean(np.array(df2.displacement_mean_fixed)) + np.nanstd(np.array(df2.displacement_mean_fixed)) ) 
        anti_disp_down = np.append(anti_disp_down, np.nanmean(np.array(df2.displacement_mean_fixed)) - np.nanstd(np.array(df2.displacement_mean_fixed)) ) 
        anti_ftle = np.append(anti_ftle, np.nanmean(np.array(df2.ftle_mean_fixed))) 
        anti_ftle_up = np.append(anti_ftle_up, np.nanmean(np.array(df2.ftle_mean_fixed)) + np.nanstd(np.array(df2.ftle_mean_fixed)) ) 
        anti_ftle_down = np.append(anti_ftle_down, np.nanmean(np.array(df2.ftle_mean_fixed)) - np.nanstd(np.array(df2.ftle_mean_fixed)) ) 
        anti_sst = np.append(anti_sst, np.nanmean(np.array(df2.sst_mean_fixed))) 
        anti_sst_up = np.append(anti_sst_up, np.nanmean(np.array(df2.sst_mean_fixed)) + np.nanstd(np.array(df2.sst_mean_fixed)) ) 
        anti_sst_down = np.append(anti_sst_down, np.nanmean(np.array(df2.sst_mean_fixed)) - np.nanstd(np.array(df2.sst_mean_fixed)) ) 
        anti_chl = np.append(anti_chl, np.nanmean(np.array(df2.chl_mean_fixed))) 
        anti_chl_up = np.append(anti_chl_up, np.nanmean(np.array(df2.chl_mean_fixed)) + np.nanstd(np.array(df2.chl_mean_fixed)) ) 
        anti_chl_down = np.append(anti_chl_down, np.nanmean(np.array(df2.chl_mean_fixed)) - np.nanstd(np.array(df2.chl_mean_fixed)) ) 
        anti_co2 = np.append(anti_co2, np.nanmean(np.array(df2.CO2_mean_surface))) 
        anti_co2_up = np.append(anti_co2_up, np.nanmean(np.array(df2.CO2_mean_surface)) + np.nanstd(np.array(df2.CO2_mean_surface)) ) 
        anti_co2_down = np.append(anti_co2_down, np.nanmean(np.array(df2.CO2_mean_surface)) - np.nanstd(np.array(df2.CO2_mean_surface)) ) 
        
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

        cyc_n = np.append(cyc_n, len(np.array(df1.year)))
        cyc_n_up = np.append(cyc_n_up, len(np.array(df1.year)))
        cyc_n_down = np.append(cyc_n_down, len(np.array(df1.year)))
        lat = np.append(lat, np.nanmean(np.array(df1.eddy_lat))) 
        lat_up = np.append(lat_up, np.nanmean(np.array(df1.eddy_lat)) + np.nanstd(np.array(df1.eddy_lat)) ) 
        lat_down = np.append(lat_down, np.nanmean(np.array(df1.eddy_lat)) - np.nanstd(np.array(df1.eddy_lat)) ) 
        lon = np.append(lon, np.nanmean(np.array(df1.eddy_lon))) 
        lon_up = np.append(lon_up, np.nanmean(np.array(df1.eddy_lon)) + np.nanstd(np.array(df1.eddy_lon)) ) 
        lon_down = np.append(lon_down, np.nanmean(np.array(df1.eddy_lon)) - np.nanstd(np.array(df1.eddy_lon)) ) 
        radius = np.append(radius, np.nanmean(np.array(df1.eddy_radius))) 
        radius_up = np.append(radius_up, np.nanmean(np.array(df1.eddy_radius)) + np.nanstd(np.array(df1.eddy_radius)) ) 
        radius_down = np.append(radius_down, np.nanmean(np.array(df1.eddy_radius)) - np.nanstd(np.array(df1.eddy_radius)) ) 
        phase = np.append(phase, np.nanmean(np.array(df1.phase_integ_fixed))) 
        phase_up = np.append(phase_up, np.nanmean(np.array(df1.phase_integ_fixed)) + np.nanstd(np.array(df1.phase_integ_fixed)) ) 
        phase_down = np.append(phase_down, np.nanmean(np.array(df1.phase_integ_fixed))  - np.nanstd(np.array(df1.phase_integ_fixed)) ) 
        sla = np.append(sla, np.nanmean(np.array(df1.sla_mean_fixed))) 
        sla_up = np.append(sla_up, np.nanmean(np.array(df1.sla_mean_fixed)) + np.nanstd(np.array(df1.sla_mean_fixed)) ) 
        sla_down = np.append(sla_down, np.nanmean(np.array(df1.sla_mean_fixed)) - np.nanstd(np.array(df1.sla_mean_fixed)) ) 
        vort = np.append(vort, np.nanmean(np.array(df1.vort_mean_fixed))) 
        vort_up = np.append(vort_up, np.nanmean(np.array(df1.vort_mean_fixed)) + np.nanstd(np.array(df1.vort_mean_fixed)) ) 
        vort_down = np.append(vort_down, np.nanmean(np.array(df1.vort_mean_fixed)) - np.nanstd(np.array(df1.vort_mean_fixed)) ) 
        disp = np.append(disp, np.nanmean(np.array(df1.displacement_mean_fixed))) 
        disp_up = np.append(disp_up, np.nanmean(np.array(df1.displacement_mean_fixed)) + np.nanstd(np.array(df1.displacement_mean_fixed)) ) 
        disp_down = np.append(disp_down, np.nanmean(np.array(df1.displacement_mean_fixed)) - np.nanstd(np.array(df1.displacement_mean_fixed)) ) 
        ftle = np.append(ftle, np.nanmean(np.array(df1.ftle_mean_fixed))) 
        ftle_up = np.append(ftle_up, np.nanmean(np.array(df1.ftle_mean_fixed)) + np.nanstd(np.array(df1.ftle_mean_fixed)) ) 
        ftle_down = np.append(ftle_down, np.nanmean(np.array(df1.ftle_mean_fixed)) - np.nanstd(np.array(df1.ftle_mean_fixed)) ) 
        sst = np.append(sst, np.nanmean(np.array(df1.sst_mean_fixed))) 
        sst_up = np.append(sst_up, np.nanmean(np.array(df1.sst_mean_fixed)) + np.nanstd(np.array(df1.sst_mean_fixed)) ) 
        sst_down = np.append(sst_down, np.nanmean(np.array(df1.sst_mean_fixed)) - np.nanstd(np.array(df1.sst_mean_fixed)) ) 
        chl = np.append(chl, np.nanmean(np.array(df1.chl_mean_fixed))) 
        chl_up = np.append(chl_up, np.nanmean(np.array(df1.chl_mean_fixed)) + np.nanstd(np.array(df1.chl_mean_fixed)) ) 
        chl_down = np.append(chl_down, np.nanmean(np.array(df1.chl_mean_fixed)) - np.nanstd(np.array(df1.chl_mean_fixed)) ) 
        co2 = np.append(co2, np.nanmean(np.array(df1.CO2_mean_surface))) 
        co2_up = np.append(co2_up, np.nanmean(np.array(df1.CO2_mean_surface)) + np.nanstd(np.array(df1.CO2_mean_surface)) ) 
        co2_down = np.append(co2_down, np.nanmean(np.array(df1.CO2_mean_surface)) - np.nanstd(np.array(df1.CO2_mean_surface)) ) 

        anti_cyc_n = np.append(anti_cyc_n, len(np.array(df2.year)))
        anti_cyc_n_up = np.append(anti_cyc_n_up, len(np.array(df2.year)))
        anti_cyc_n_down = np.append(anti_cyc_n_down, len(np.array(df2.year)))
        anti_lat = np.append(anti_lat, np.nanmean(np.array(df2.eddy_lat))) 
        anti_lat_up = np.append(anti_lat_up, np.nanmean(np.array(df2.eddy_lat)) + np.nanstd(np.array(df2.eddy_lat)) ) 
        anti_lat_down = np.append(anti_lat_down, np.nanmean(np.array(df2.eddy_lat)) - np.nanstd(np.array(df2.eddy_lat)) ) 
        anti_lon = np.append(anti_lon, np.nanmean(np.array(df2.eddy_lon))) 
        anti_lon_up = np.append(anti_lon_up, np.nanmean(np.array(df2.eddy_lon)) + np.nanstd(np.array(df2.eddy_lon)) ) 
        anti_lon_down = np.append(anti_lon_down, np.nanmean(np.array(df2.eddy_lon)) - np.nanstd(np.array(df2.eddy_lon)) ) 
        anti_radius = np.append(anti_radius, np.nanmean(np.array(df2.eddy_radius))) 
        anti_radius_up = np.append(anti_radius_up, np.nanmean(np.array(df2.eddy_radius)) + np.nanstd(np.array(df2.eddy_radius)) ) 
        anti_radius_down = np.append(anti_radius_down, np.nanmean(np.array(df2.eddy_radius)) - np.nanstd(np.array(df2.eddy_radius)) ) 
        anti_phase = np.append(anti_phase, np.nanmean(np.array(df2.phase_integ_fixed))) 
        anti_phase_up = np.append(anti_phase_up, np.nanmean(np.array(df2.phase_integ_fixed)) + np.nanstd(np.array(df2.phase_integ_fixed)) ) 
        anti_phase_down = np.append(anti_phase_down, np.nanmean(np.array(df2.phase_integ_fixed))  - np.nanstd(np.array(df2.phase_integ_fixed)) ) 
        anti_sla = np.append(anti_sla, np.nanmean(np.array(df2.sla_mean_fixed))) 
        anti_sla_up = np.append(anti_sla_up, np.nanmean(np.array(df2.sla_mean_fixed)) + np.nanstd(np.array(df2.sla_mean_fixed)) ) 
        anti_sla_down = np.append(anti_sla_down, np.nanmean(np.array(df2.sla_mean_fixed)) - np.nanstd(np.array(df2.sla_mean_fixed)) ) 
        anti_vort = np.append(anti_vort, np.nanmean(np.array(df2.vort_mean_fixed))) 
        anti_vort_up = np.append(anti_vort_up, np.nanmean(np.array(df2.vort_mean_fixed)) + np.nanstd(np.array(df2.vort_mean_fixed)) ) 
        anti_vort_down = np.append(anti_vort_down, np.nanmean(np.array(df2.vort_mean_fixed)) - np.nanstd(np.array(df2.vort_mean_fixed)) ) 
        anti_disp = np.append(anti_disp, np.nanmean(np.array(df2.displacement_mean_fixed))) 
        anti_disp_up = np.append(anti_disp_up, np.nanmean(np.array(df2.displacement_mean_fixed)) + np.nanstd(np.array(df2.displacement_mean_fixed)) ) 
        anti_disp_down = np.append(anti_disp_down, np.nanmean(np.array(df2.displacement_mean_fixed)) - np.nanstd(np.array(df2.displacement_mean_fixed)) ) 
        anti_ftle = np.append(anti_ftle, np.nanmean(np.array(df2.ftle_mean_fixed))) 
        anti_ftle_up = np.append(anti_ftle_up, np.nanmean(np.array(df2.ftle_mean_fixed)) + np.nanstd(np.array(df2.ftle_mean_fixed)) ) 
        anti_ftle_down = np.append(anti_ftle_down, np.nanmean(np.array(df2.ftle_mean_fixed)) - np.nanstd(np.array(df2.ftle_mean_fixed)) ) 
        anti_sst = np.append(anti_sst, np.nanmean(np.array(df2.sst_mean_fixed))) 
        anti_sst_up = np.append(anti_sst_up, np.nanmean(np.array(df2.sst_mean_fixed)) + np.nanstd(np.array(df2.sst_mean_fixed)) ) 
        anti_sst_down = np.append(anti_sst_down, np.nanmean(np.array(df2.sst_mean_fixed)) - np.nanstd(np.array(df2.sst_mean_fixed)) ) 
        anti_chl = np.append(anti_chl, np.nanmean(np.array(df2.chl_mean_fixed))) 
        anti_chl_up = np.append(anti_chl_up, np.nanmean(np.array(df2.chl_mean_fixed)) + np.nanstd(np.array(df2.chl_mean_fixed)) ) 
        anti_chl_down = np.append(anti_chl_down, np.nanmean(np.array(df2.chl_mean_fixed)) - np.nanstd(np.array(df2.chl_mean_fixed)) ) 
        anti_co2 = np.append(anti_co2, np.nanmean(np.array(df2.CO2_mean_surface))) 
        anti_co2_up = np.append(anti_co2_up, np.nanmean(np.array(df2.CO2_mean_surface)) + np.nanstd(np.array(df2.CO2_mean_surface)) ) 
        anti_co2_down = np.append(anti_co2_down, np.nanmean(np.array(df2.CO2_mean_surface)) - np.nanstd(np.array(df2.CO2_mean_surface)) ) 
        
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
    
    plt.savefig('gallery/map.png', bbox_inches='tight' , dpi=900, transparent=plot_transparency)

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



lines = get_query_file()
query_id = lines[0].strip()
dataset = lines[1].strip()
query = lines[2].strip()

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

#########################################



    
    
conn = db_connect()
df = sql.read_sql(query, conn)
conn.close()




############## basemap ##############
#if dataset == 'Cores': 
#    cores_map(np.array(df.eddy_lon), np.array(df.eddy_lat))
#####################################



############## pairplot ##############

#sns_pairplot(df, dataset)

#####################################




single_hists(df, dataset)
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
        
        

        
        
        
        
