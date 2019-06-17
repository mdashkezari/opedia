import os
import pandas as pd
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import db


def catQuery():
    return "SELECT * FROM dbo.udfCatalog()" 

def exportData(df, path):
    df.to_csv(path, index=False, encoding='utf-8')    
    return

def catalog(dirPath):   
    query = catQuery()
    df = db.dbFetch(query)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)                
    exportData(df, path=dirPath + 'catalog.csv')
    return


dirPath = 'data/'
catalog(dirPath)