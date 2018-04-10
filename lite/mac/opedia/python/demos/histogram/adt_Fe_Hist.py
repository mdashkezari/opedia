
#########################################################################################
script = ' ../../plotDist.py'      # path to plotDist.py script
tables = ' tblAltimetry_REP,tblPisces_NRT'
fields = ' adt,Fe'
startDate, endDate = ' 2017-01-07', ' 2017-01-07'
lat1, lat2, lon1, lon2 = ' 30.57', ' 35.21', ' -163.43', ' -156.17' 
fname = ' Dist'                     # plot filename (.html)
exportData = ' 1'                   # export data in csv format (1/0: yes/no)
extV, extVV, extV2, extVV2 = ' ignore,depth', ' ignore,0.494024991989', ' ignore,ignore', ' ignore,ignore'
#########################################################################################



import os
cmd = 'python' + script + tables + fields + startDate + endDate \
      + lat1 + lat2 + lon1 + lon2 + fname \
      + exportData + extV + extVV + extV2 + extVV2
os.system(cmd)
