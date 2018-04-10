

######################### setting arguments for a virtual cruise #########################
script = ' ../../plotCruise.py'     # path to plotCruise.py script
expedition = ' 0'                   # fixed, keep it!  (1: expedition, 0: virtual cruise)
command = ' 2'                      # fixed, keep it!
source = ' ../../../../virtual_parity_scope_2.csv'              # path to virtual cruise track (needs time/lat/lon columns)
cruise = ''                         # fixed, keep it!
resample = ' H'                     # resample rate (H: hourly, 2H: 2hours period ..., 10T: 10 minute, D: daily)
fname = ' AlongTrack'               # plot filename (.html)
exportData = ' 1'                   # export data in csv format (1/0: yes/no)
spatialMargin = ' 0.5'              # matching margin (in degrees)
matchTable = ' tblAltimetry_REP'    # matching table name
matchVar = ' sla'                   # matching var name
extVar = ' ignore'                  # extra variable name ('hour' or 'depth', usually used for model outputs)
extVarValue = ' ignore'             # extra variable value (usually used for model outputs)   
extVar2 = ' ignore'                 # extra variable name ('hour' or 'depth', usually used for model outputs)
extVarValue2 = ' ignore'            # extra variable value (usually used for model outputs) 
#########################################################################################


import os
cruise = ' ' + os.path.basename(source).split('.')[0]
cmd = 'python' + script + expedition + command + source + cruise \
      + resample + fname + exportData + spatialMargin + matchTable \
      + matchVar + extVar + extVarValue + extVar2 + extVarValue2
os.system(cmd)
