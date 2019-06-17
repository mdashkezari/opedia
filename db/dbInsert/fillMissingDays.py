import os
import sys
sys.path.append('../../config')
import config_vault as cfgv
sys.path.append('../../lib')
import dateLib as dl
sys.path.append('../')
import dbCore as dc
from datetime import date
from datetime import datetime
from datetime import timedelta





def dayExists(tableName, day):
    query = "select [time] from %s where [time]='%s' " % (tableName, day)
    query += 'and lat between 20 and 40 '
    query += 'and lon between -160 and -140 '
    df = dc.dbRead(query, usr='', psw='', ip='', port='', db='')
    if len(df) > 100:
        return True
    else:        
        return False



dt1 = datetime.strptime(sys.argv[1], '%Y-%m-%d')
dt2 = datetime.strptime(sys.argv[2], '%Y-%m-%d')
tableName = sys.argv[3]
script = sys.argv[4]
nrt = sys.argv[5]

dt = dt1
while(dt<=dt2):
    dayn = dl.dateToDayn(dt)
    dateStr = datetime.strftime(dt, '%Y-%m-%d')

    print('Checking %s, date: %s, Dayn: %d' % (tableName, dateStr, dayn), end ="\r")
    if not dayExists(tableName, dateStr):
        print('\nfilling %s at table: %s' % (dateStr, tableName))
        os.system('python ' + script +'.py ' + str(int(dayn)) + ' ' + str(int(dayn)) + ' ' + nrt)
    dt = dt + timedelta(days=1)
