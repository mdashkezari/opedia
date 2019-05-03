import os, os.path
import sys
sys.path.append('../login')
sys.path.append('../../config')
import pandas as pd
import config_vault as cfgv
import credentials as cr

def toSQLbcp(export_path, tableName,  usr=cr.usr, psw=cr.psw, ip=cr.ip):
    print('Inserting Bulk %s into %s.' % (tableName[3:], tableName))
    str = """bcp Opedia.dbo.""" + tableName + """ in """ + export_path + """ -e error -c -t, -U  """ + usr + """ -P """ + psw + """ -S """ + ip + """,1433"""
    os.system(str)
    print('BCP insert finished')
