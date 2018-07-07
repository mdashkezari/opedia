import os
import pandas as pd
import db



def catQuery():
    query = ""    
    query = query + "SELECT RTRIM(LTRIM(Short_Name)) AS Variable, "
    query = query + "RTRIM(LTRIM(Long_Name)) AS [Long Name], "
    query = query + "RTRIM(LTRIM(Unit)) AS Unit, "
    query = query + "RTRIM(LTRIM(Make)) AS Make, "
    query = query + "RTRIM(LTRIM(Sensor)) AS Sensor, "
    query = query + "RTRIM(LTRIM(Process_Stage_Long)) AS [Process Level], "
    query = query + "RTRIM(LTRIM(Study_Domain)) AS [Study Domain], "
    query = query + "RTRIM(LTRIM(Temporal_Resolution)) AS [Temporal Resolution], "
    query = query + "RTRIM(LTRIM(Spatial_Resolution)) AS [Spatial Resolution], "
    query = query + "RTRIM(LTRIM(Comment)) AS [Comment], "

    query = query + "RTRIM(LTRIM(Dataset_Long_Name)) AS [Dataset Name], "
    query = query + "RTRIM(LTRIM(Data_Source)) AS [Data Source], "
    query = query + "RTRIM(LTRIM(Distributor)) AS [Distributor], "
    query = query + "RTRIM(LTRIM(Description)) AS [Dataset Description], "
    query = query + "[tblVariables].Dataset_ID AS [Dataset_ID], "
    query = query + "[tblVariables].ID AS [ID] "
    
    query = query + "FROM tblVariables "
    query = query + "JOIN tblDatasets ON [tblVariables].Dataset_ID=[tblDatasets].ID "
    query = query + "JOIN tblTemporal_Resolutions ON [tblVariables].Temporal_Res_ID=[tblTemporal_Resolutions].ID "
    query = query + "JOIN tblSpatial_Resolutions ON [tblVariables].Spatial_Res_ID=[tblSpatial_Resolutions].ID "
    query = query + "JOIN tblMakes ON [tblVariables].Make_ID=[tblMakes].ID "
    query = query + "JOIN tblSensors ON [tblVariables].Sensor_ID=[tblSensors].ID "
    query = query + "JOIN tblProcess_Stages ON [tblVariables].Process_ID=[tblProcess_Stages].ID "
    query = query + "JOIN tblStudy_Domains ON [tblVariables].Study_Domain_ID=[tblStudy_Domains].ID "
    return query




def exportData(df, path):
    df.to_csv(path, index=False, encoding='utf-8')    
    return

def catalog():   
    query = catQuery()
    df = db.dbFetch(query)

    dirPath = 'data/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)                
    exportData(df, path=dirPath + 'catalog.csv')
    return




catalog()