

################### matching more than one variable with cruise track ###################
script = ' ../../plotCruise.py'     # path to plotCruise.py script
expedition = ' 1'                   # fixed, keep it!  (1: expedition, 0: virtual cruise)
command = ' 2'                      # fixed, keep it!
source = ' tblSeaFlow'              # fixed, keep it!
cruise = ' SCOPE_16'                # cruise name
resample = ' H'                     # resample rate (H: hourly, 2H: 2hours period ..., 10T: 10 minute, D: daily)
fname = ' AlongTrack'               # plot filename (.html)
exportData = ' 1'                   # export data in csv format (1/0: yes/no)
spatialMargin = ' 0.5'              # matching margin (in degrees)
matchTable = ' tblPisces_NRT,tblPisces_NRT'    # matching table name
matchVar = ' NO3,Fe'                   # matching var name
extVar = ' depth,depth'                  # extra variable name ('hour' or 'depth', usually used for model outputs)
extVarValue = ' 0.494024991989,0.494024991989'             # extra variable value (usually used for model outputs)   
extVar2 = ' ignore,ignore'                 # extra variable name ('hour' or 'depth', usually used for model outputs)
extVarValue2 = ' ignore,ignore'            # extra variable value (usually used for model outputs) 
#########################################################################################



import os
cmd = 'python' + script + expedition + command + source + cruise \
      + resample + fname + exportData + spatialMargin + matchTable \
      + matchVar + extVar + extVarValue + extVar2 + extVarValue2
os.system(cmd)
