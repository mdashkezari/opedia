
import numpy as np
import pandas as pd


def removeColumn(cols, df):
    for col in cols:
        df.drop(col, axis=1, inplace=True)
    return df


def removeMissings(cols, df):
    for col in cols:
        df[col].replace('', np.nan, inplace=True)
        df.dropna(subset=[col], inplace=True)
    return df


def NaNtoNone(df):
    df = df.where((pd.notnull(df)), None)
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