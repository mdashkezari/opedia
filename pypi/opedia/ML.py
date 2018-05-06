import sys
import os
import time
import math
import numpy as np
import matplotlib.pyplot as plt
import pyodbc
import pandas.io.sql as sql
import pandas as pd
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble.forest import RandomForestRegressor
import seaborn as sns




############# spatial map ##################
from mpl_toolkits.basemap import Basemap

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
        margin = 2
        minlat = np.nanmin(eddy_lat) - margin
        maxlat = np.nanmax(eddy_lat) + margin
        minlon = np.nanmin(eddy_lon) - margin 
        maxlon = np.nanmax(eddy_lon) + margin + 5
        
           
    
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
    
        map.drawparallels(np.arange(minlat,maxlat, (maxlat-minlat)/5 ), linewidth=1, color=[.2,.2,.2], labels=[1,1,0,0], fontsize=5)
        map.drawmeridians(np.arange(minlon,maxlon, (maxlon-minlon)/5 ), linewidth=1, color=[.2,.2,.2], labels=[0,0,0,1], fontsize=5)
    
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
        sc = map.scatter(x_map, y_map, c=vals, vmin=bounds[0], vmax=bounds[1], cmap=cm, lw=0, alpha=0.6) #, s=5
        cb = map.colorbar(sc, 'bottom', size='5%', pad='7%')
        cb.ax.tick_params(labelsize=7)
        if len(title) > 0:
            plt.title(title)
        
        if len(store_path) > 0:
            plt.savefig(store_path, bbox_inches='tight' , dpi=600, transparent=False)
            
    except Exception as e:
        print('Error in spatial_map. Error message: '+str(e))
    return

############################################




def pars_queryFile(lines):
    query = lines[2].strip()
    target = lines[3].strip()
    features = []
    for i in range(4, len(lines)):
        features.append(lines[i].strip())
    return query, target, features        

def fetch(query):
    conn = db_connect()
    df = sql.read_sql(query, conn)
    conn.close()
    return df

def getXY(df, queryFile):
    query, target, features = pars_queryFile(queryFile)
    #df = fetch(conn, query)
    Y = np.array(df[target])
    X = np.array(df[features])
    return X, Y
    

def plot_ML_pred(y_true, y_pred, target, score, store_path=''):
    g = sns.jointplot(y_true, y_pred, kind="reg", line_kws={'color':'indianred', 'linewidth':'0.5'}, marginal_kws={'kde_kws':{'color':'indianred', 'linewidth':'1'}})
    g.set_axis_labels('True "' + target + '"', 'Predicted "' + target + '"')

    #plt.setp(g.ax_marg_x.get_yticklabels(), visible=True)
    #plt.setp(g.ax_marg_y.get_xticklabels(), visible=True)
    
    #plt.plot(y_true, y_pred, 'o', markersize=8, markerfacecolor='purple', markeredgecolor='purple', alpha=0.35)    
    #for axis in ['top','bottom','left','right']:
    #  plt.gca().spines[axis].set_linewidth(1.5)
    
    plt.title(score)
    plt.tight_layout()
    if len(store_path) > 0:
        plt.savefig(store_path, format='png', dpi=600)
    return

    
 
def plot_importances(forest, X, fea_list, target):
    importances = forest.feature_importances_
    std = np.std([tree.feature_importances_ for tree in forest.estimators_],
                 axis=0)
    indices = np.argsort(importances)[::-1]
    
    tik=[]
    for i in range(0, len(indices)):
        tik.append(fea_list[indices[i]])
        

    plt.figure()
    plt.bar(range(X.shape[1]), importances[indices],
           color="springgreen", yerr=std[indices], align="center", alpha=0.35, error_kw=dict(ecolor='m', lw=1, capsize=2, capthick=1))

        
    #plt.xticks(range(X.shape[1]), indices)
    plt.xticks(range(X.shape[1]), tik, rotation=70)
    plt.gca().set_xticklabels(tik, fontsize=7)
    
    plt.xlim([-1, X.shape[1]])
    plt.title('Predictive model for "' + target + '"')

    plt.xticks(fontsize = 8) 

    #plt.xlabel('')
    plt.ylabel("Feature Importance")
    plt.tight_layout()
    plt.savefig('ML/predictors.png' , format='png', dpi=600) 
    
    return

 
def MLRegression(model, df, queryFile):
    X = np.float64([])
    y = np.float64([])
    
    query, target, features = pars_queryFile(queryFile)
    X, y = getXY(df, queryFile)
    
    print(X.shape, y.shape)    
    
    #scores = cross_val_score(model, X, y, cv=5, n_jobs=-1)
    #print("R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    X_tests = np.array([])
    y_tests = np.array([])
    y_predicts = np.array([])
    scores = np.array([])
    mses = np.array([])
    tic = time.clock()
    for i in range(0,1):
        '''
        ###################
        n = 7 * len(y) / 8
        X_train = X[:n, :]
        y_train = y[:n]
        X_test = X[n:, :]
        y_test = y[n:]
        ##################        
        '''
        
        X_train, X_test, y_train, y_test = train_test_split(X , y, test_size=0.20)
        model.fit(X_train, y_train)

        pred = model.predict(X_test)


        if i == 0:
            X_tests = X_test
        else:  
            X_tests = np.concatenate((X_tests, X_test), axis=0)
        y_tests = np.append(y_tests, y_test)
        y_predicts = np.append(y_predicts, pred)
        
        tt_score = model.score(X_test, y_test)
        mse = mean_squared_error(y_test, pred)  
        
        #print i, model.n_features_, tt_score, mse
        scores = np.append(scores, tt_score)
        mses = np.append(mses, mse)
        
    
    '''    
    ####################  spatial map #############
    lons = np.array([])    
    lats = np.array([])    
    true_vals = np.array([])    
    pred_vals = np.array([])    
    lon_index = features.index('eddy_lon')
    lat_index = features.index('eddy_lat')
    if lon_index >= 0 and lat_index >= 0:
        lons = X_tests[:, lon_index]
        lats = X_tests[:, lat_index]
        true_vals = y_tests
        pred_vals = y_predicts

        spatial_map(lons, lats, true_vals, 'ML/true_target.png', 'True ' + target , None)
        spatial_map(lons, lats, pred_vals, 'ML/pred_target.png', 'Predicted ' + target , None)
    ###############################################        
    '''    
        
     
    tt_score = scores.mean()
    mse = mses.mean()
    tt_score_sig = scores.std()
    mse_sig = mses.std()
    print('tt_score_sig: ', tt_score_sig)
    print('mse_sig: ',mse_sig)
    
    print('X_train.shape: ',X_train.shape)
    print('X.shape: ',X.shape)
    print('y_test.shape: ',y_test.shape)
    print('y.shape: ',y.shape)
    toc = time.clock()

    res = '$R^2:$ $%.3f\pm%.3f$' % (tt_score, tt_score_sig) 
    plot_ML_pred(y_tests, y_predicts, target, res, 'ML/ML_pred.png')
    plot_importances(model, X, features, target)

    print('*******************************************')
    print('Evaluation Using split: %.4f' % tt_score)
    print('feature_importances: ', model.feature_importances_)
    print('Root Mean Squared Error: %.2f' % math.sqrt(mse))
    print('Process Time: '+str(toc-tic))
    print('*******************************************')
        
    return
    
   
   
def ExtraTrees(df, queryFile):
    model = ExtraTreesRegressor(random_state=0, n_estimators=200, n_jobs=-1)  
    MLRegression(model, df, queryFile)      
    return
   
    
def RandomForest(df, queryFile):
    model = RandomForestRegressor(random_state=0, n_estimators=200, n_jobs=-1)        
    MLRegression(model, df, queryFile)
    return

  
def GradientBoosting(df, queryFile):
    model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.5, max_depth=4, random_state=0, loss='ls')       
    MLRegression(model, df, queryFile)
    return
    