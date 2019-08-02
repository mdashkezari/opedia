
import numpy as np
import pandas as pd


def convertYYYYMMDD(df):
    # df['time'] = pd.to_datetime(df['time'].astype(str), format='%Y-%m-%d')
    df['time'] = pd.to_datetime(df['time'].astype(str))

    df['time'] = df['time'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return df

def removeColumn(cols, df):
    for col in cols:
        df.drop(col, axis=1, inplace=True)
    return df

def removeDuplicates(df):
    df = df.drop_duplicates(keep='first')
    return df

def addIDcol(df):
    df['ID'] = None
    return df

def removeMissings(cols, df):
    for col in cols:
        df[col].replace('', np.nan, inplace=True)
        df.dropna(subset=[col], inplace=True)
    return df

def NAtoNone(df):
    df.replace(r'\s+', np.nan, regex=True, inplace=True)
    return df

def renameCol(df, oldColName, newColName):
    df.rename(columns={oldColName: newColName},inplace=True)
    return df

def reorderCol(df,ColList):
    df = df[ColList]
    return df

def NaNtoNone(df):
    df = df.replace(np.nan, '', regex=True)
    return df

def colDatatypes(df):
    try:
        df['time']=pd.to_datetime(df['time'], format='%Y-%m-%d')
        df['lat'] = df['lat'].astype(float)
        df['lon'] = df['lon'].astype(float)
        df['depth'] = df['depth'].astype(float)
        return df
    except:
        df['time']=pd.to_datetime(df['time'], format='%Y-%m-%d')
        df['lat'] = df['lat'].astype(float)
        df['lon'] = df['lon'].astype(float)
        return df

def convertcolDatatype(df,ColList):
    df[ColList] = df[ColList].apply(pd.to_numeric)
    return df

def mapTo180180(export_path, lonName):
    df = pd.read_csv(export_path)
    df.ix[df[lonName] > 180, lonName] = df.ix[df[lonName] > 180, lonName] - 360
    df.to_csv(export_path, index = False)
    return


def sortByLatLon(df, export_path, lonName, latName):
    df = pd.read_csv(export_path)
    df.sort_values([latName, lonName], ascending=[True, True], inplace=True)
    df.to_csv(export_path, index=False)
    return

def sortByTimeLatLon(df, export_path, timeName, latName, lonName):
    df = pd.read_csv(export_path)
    df.sort_values([timeName, latName, lonName], ascending=[True, True, True], inplace=True)
    df.to_csv(export_path, index=False)
    return

def sortByDepthLatLon(df, export_path, lonName, latName, depthName):
    df = pd.read_csv(export_path)
    df.sort_values([depthName, latName, lonName], ascending=[True, True, True], inplace=True)
    df.to_csv(export_path, index=False)
    return


def sortByTimeLatLonDepth(df, export_path, timeName, latName, lonName, depthName):
    df = pd.read_csv(export_path)
    df.sort_values([timeName, latName, lonName, depthName], ascending=[True, True, True, True], inplace=True)
    df.to_csv(export_path, index=False)
    return


def arrangeColumns(cols, df):
    ## arrange the columns: making sure that the columns are arranged in the correct (consistent with the undelying table) order
    df = df[cols]
    return df


def sortByDepthLatLon_AddClim(df, export_path, lonName, latName, depthName):
    df = pd.read_csv(export_path)
    df.sort_values([depthName, latName, lonName], ascending=[True, True, True], inplace=True)
    ## adding month and year columns (could be useful to compute climatology)
    df['month'] = pd.DatetimeIndex(df['time_counter']).month
    df['year'] = pd.DatetimeIndex(df['time_counter']).year
    df.to_csv(export_path, index=False)
    return
