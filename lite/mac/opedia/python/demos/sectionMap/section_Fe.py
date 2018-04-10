
################### parameters to plot section map for a single variable ###################
script = ' ../../plotSection.py'     # path to plotSection.py script
tables = ' tblPisces_NRT'
fields = ' Fe'
startDate = ' 2017-06-03'
lat1, lat2, lon1, lon2 = ' 22.57', ' 44.47', ' -158.3', ' -157.4' 
depth1, depth2 = ' 0', ' 5728'
fname = ' Sec'                     # plot filename (.html)
exportData = ' 1'                   # export data in csv format (1/0: yes/no)
###################################################################################################


import os
cmd = 'python' + script + tables + fields + startDate + lat1 \
      + lat2 + lon1 + lon2 + fname + exportData \
      + depth1 + depth2
os.system(cmd)
