#! /usr/bin/env python

"""
usage:      
    opedia <command> [options]
    opedia (-h | --help | --version)


options:
   --tab <datasets>                      Query parameter: comma-separated data set names (tables) [default: tblSST_AVHRR_OI_NRT]    
   --var <variables>                     Query parameter: comma-separated variable names (fields) [default: sst]     
   --d1 <startDate>                      Query parameter: start date [default: 2016-04-30]  
   --d2 <endDate>                        Query parameter: end date [default: 2016-04-30]
   --h1 <startHour>                      Query parameter: start hour [default: 0]  
   --h2 <endHour>                        Query parameter: end hour [default: 0]
   --lat1 <startLat>                     Query parameter: start latitude [default: 20]
   --lat2 <endLat>                       Query parameter: end latitude [default: 45]
   --lon1 <startLon>                     Query parameter: start longitude [default: -180]
   --lon2 <endLon>                       Query parameter: end longitude [default: -126]
   --extV1 <extraV1>                     Query parameter: comma-separated extra query parameter names [default: ignore]   
   --extVV1 <extraVV1>                   Query parameter: comma-separated extra query parameter values [default: ignore]   
   --extV2 <extraV2>                     Query parameter: comma-separated extra query parameter names [default: ignore]   
   --extVV2 <extraVV2>                   Query parameter: comma-separated extra query parameter values [default: ignore]   
   --dep1 <startDepth>                   Query parameter: start depth [default: 0]
   --dep2 <endDepth>                     Query parameter: end depth [default: 0]
   -e <eflag>, --export <eflag>          Export data flag [default: 0]
   --eFile <dataFile>                    Export data file name [default: ./data/data.csv]   
   --shape <shapeFlag>                   Generate shape file [default: 1]
   --shpFile <shapeFile>                 Shape filename [default: shape]
   --match <matchFlag>                   Match/Colocate with other data sets [default: 0]
   --bkg <bkgFlag>                       Background comparison flag [default: 0]
   --pd <plotDir>                        Plot directory [default: ./embed]   
   --pname <plotFile>                    Plot file name [default: plot]   
   --sds <sourceDataset>                 Source data set(table name) to be matched with the matching data sets            
   --mds <matchDataset>...               Matching data sets(table names) to be matched with the source data set 
   --cruiseName <crsName>                Cruise name
   --fCruise <fcflag>                    Field (vs virtual) cruise flag [default: 1] 
   --cruiseTrack <crsTrack>              Generate cruise track shape file [default: 1] 
   --cruiseTab <cruiseTable>             Cruise data set (table) name  
   --vcFile <virtualCruiseFile>          Path to virtual cruise file 
   --resampleRate <resampleTau>          Resample cruise data set (disabled by default) [default: 0]
   
   --dbMatch <dbMatchFlag>               Match with a data set (table) in database (0 if local file) [default: 1]     
   --sourceMatch <srcMatch>              Source data set to be matched with (table name if dbMatch, file name if local file)
   --sMatch <spatialMatch>               Spatial matching range in degrees [default: 0.3]     
   --tMatch <spatialMatch>               Temporal matching range in days [default: 1]                           

   --dtAdvect <timeStep>                 Advection time step (in seconds, 3600*24=86400) [default: 86400]
   --dirAdvect <direction>               Advection direction (forward/backward 1/-1) [default: 1]
   --latAdvect <initialLat>              Initial latitude of the passive tracer
   --lonAdvect <initialLon>              Initial longitude of the passive tracer

   --eddySource <srcEddy>                Eddy data set (table) name [default: tblChelton]
   --ftleSource <srcFTLE>                FTLE data set (table) name [default: tblLCS_REP]
   --ftleVar <ftleField>                 FTLE field name [default: ftle_bw_sla]
   --ftleValue <ftleCutoff>              FTLE high-pass filter threshold [default: 0.22]

   --name                                Your name             
   --lastname                            Your last name             
   -u <username>, --username <username>  Your username [default: ArmLab]
   -p <password>, --password <password>  Your password [default: ArmLab2018]
   --email <email>                       Your email address   
   --server                              Server IP address [default: 128.208.239.15]  
   --port                                Server port number [default: 1433]        
   --db                                  Database name [default: Opedia]   
   -a, --all                             Print all options and arguments                   
   -h, --help                            Show usage doc string and exit



commands:
   auth                                  User authentication (NOT IMPLEMENTED YET)    
   regional                              Retrieve regional subset of data sets 
   timeseries                            Retrieve timeseries subset of data sets 
   trend                                 Retrieve mutual trend between a pair of data sets 
   dist                                  Retrieve a generic subset of data sets 
   section                               Retrieve section (depth vs lat/lon) subset of data sets    
   depth                                 Retrieve depth profile     
   season                                Retrieve data set seasonality    
   cat                                   Retrieve opedia catalog    
   cruise                                Retrieve and match cruise track with other data sets
   match                                 Match/Colocalize a data set with other data sets    
   advect                                Advect a paccive tracer and match/colocate other data sets along track    
   eddy                                  Retrieve and match/colocate eddy cores with other data sets    
   ftle                                  Retrieve and match/colocate ftle fronts with other data sets    




Examples:
__________________________________________________________________________________________________________


REGIONAL MAP:
    opedia regional [options] [--tab=<datasets>] [--var=<variables>] [--d1=<startDate>] [--lat1=<startLat>] [--lat2=<endLat>] [--lon1=<startLon>] [--lon2=<endLon>] [--pname=<plotFile>] [--export=<eflag>] [--extV1=<extraV1>] [--extVV1=<extraVV1>]
=====================================================

TIMESERIES:
    opedia timeseries [options] [--tab=<datasets>] [--var=<variables>] [--d1=<startDate>] [--d2=<endDate>] [--lat1=<startLat>] [--lat2=<endLat>] [--lon1=<startLon>] [--lon2=<endLon>] [--pname=<plotFile>] [--export=<eflag>] [--extV1=<extraV1>] [--extVV1=<extraVV1>] [--extV2=<extraV2>] [--extVV2=<extraVV2>]
=====================================================

MUTUAL TREND:
    opedia trend [options] [--tab=<datasets>] [--var=<variables>] [--d1=<startDate>] [--d2=<endDate>] [--lat1=<startLat>] [--lat2=<endLat>] [--lon1=<startLon>] [--lon2=<endLon>] [--pname=<plotFile>] [--export=<eflag>] [--extV1=<extraV1>] [--extVV1=<extraVV1>] [--extV2=<extraV2>] [--extVV2=<extraVV2>]
=====================================================

GENERIC DISTRIBUTION:
    opedia dist [options] [--tab=<datasets>] [--var=<variables>] [--d1=<startDate>] [--d2=<endDate>] [--lat1=<startLat>] [--lat2=<endLat>] [--lon1=<startLon>] [--lon2=<endLon>] [--pname=<plotFile>] [--export=<eflag>] [--extV1=<extraV1>] [--extVV1=<extraVV1>] [--extV2=<extraV2>] [--extVV2=<extraVV2>]
=====================================================

SECTION:
    opedia section [options] [--tab=<datasets>] [--var=<variables>] [--d1=<startDate>] [--lat1=<startLat>] [--lat2=<endLat>] [--lon1=<startLon>] [--lon2=<endLon>] [--pname=<plotFile>] [--export=<eflag>] [--extVV1=<extraVV1>] [--extVV2=<extraVV2>]
=====================================================

DEPTH PROFILE:
    opedia depth [options] [--tab=<datasets>] [--var=<variables>] [--d1=<startDate>] [--lat1=<startLat>] [--lat2=<endLat>] [--lon1=<startLon>] [--lon2=<endLon>] [--pname=<plotFile>] [--export=<eflag>] [--extVV1=<extraVV1>] [--extVV2=<extraVV2>]
=====================================================

SEASON:
    opedia season [options] [--tab=<datasets>] [--var=<variables>] [--lat1=<startLat>] [--lat2=<endLat>] [--lon1=<startLon>] [--lon2=<endLon>] [--pname=<plotFile>] [--export=<eflag>] [--extV1=<extraV1>] [--extVV1=<extraVV1>] [--extV2=<extraV2>] [--extVV2=<extraVV2>]
=====================================================

CATALOG:
    opedia cat [options]
=====================================================

CRUISE:
    opedia cruise [options] [--fCruise=<fCruise>] [--cruiseTrack=<crsTrack>] [--cruiseName=<crsName>] [--resampleRate=<resampleTau>] [--pname=<plotFile>] [--export=<eflag>] [--sMatch=<spatialMatch>] [--tab=<datasets>] [--var=<variables>] [--extV1=<extraV1>] [--extVV1=<extraVV1>] [--extV2=<extraV2>] [--extVV2=<extraVV2>]
=====================================================

MATCH:
    opedia match [options] [--dbMatch=<dbMatchFlag> ] [--sourceMatch=<srcMatch>] [--sMatch=<spatialMatch> ] [--tMatch=<spatialMatch> ] [--tab=<datasets>] [--var=<variables>] [--eFile=<dataFile>]
=====================================================

ADVECT:
    opedia advect [options] [--dtAdvect=<timeStep>] [--dirAdvect=<direction> ] [--d1=<startDate>] [--d2=<endDate>] [--latAdvect=<initialLat>] [--lonAdvect=<initialLon>] [--shape=<shapeFlag>] [--match=<matchFlag>] [--shpFile=<shapeFile>] [--export=<eflag>] [--sMatch=<spatialMatch>] [--tab=<datasets>] [--var=<variables>] [--extV1=<extraV1>] [--extVV1=<extraVV1>] [--extV2=<extraV2>] [--extVV2=<extraVV2>] [--pname=<plotFile>]
=====================================================

EDDY:
    opedia eddy [options] [--eddySource=<srcEddy>] [--d1=<startDate>] [--d2=<endDate>] [--lat1=<startLat>] [--lat2=<endLat>] [--lon1=<startLon>] [--lon2=<endLon>] [--shape=<shapeFlag>] [--match=<matchFlag>] [--shpFile=<shapeFile>] [--export=<eflag>] [--sMatch=<spatialMatch>] [--tab=<datasets>] [--var=<variables>] [--extV1=<extraV1>] [--extVV1=<extraVV1>] [--extV2=<extraV2>] [--extVV2=<extraVV2>] [--pname=<plotFile>]
=====================================================

FTLE:
    opedia ftle [options] [--ftleSource=<srcFTLE>] [--ftleVar=<ftleField>] [--ftleValue=<ftleCutoff>] [--bkg=<bkgFlag>] [--d1=<startDate>] [--d2=<endDate>] [--lat1=<startLat>] [--lat2=<endLat>] [--lon1=<startLon>] [--lon2=<endLon>] [--shape=<shapeFlag>] [--match=<matchFlag>] [--shpFile=<shapeFile>] [--export=<eflag>] [--sMatch=<spatialMatch>] [--tab=<datasets>] [--var=<variables>] [--extV1=<extraV1>] [--extVV1=<extraVV1>] [--extV2=<extraV2>] [--extVV2=<extraVV2>] [--pname=<plotFile>]
=====================================================

"""




from docopt import docopt
from subprocess import call
import os
import json


def run(cmd, subProc=True):
    if args['--all']:
        print(json.dumps(args, indent=5))
    if subProc:
        ## subprocess call
        exit(call(cmd))
    else:  
        ## os 
        os.system(' '.join(cmd))


if __name__ == '__main__':
    args = docopt(__doc__, version='opedia 0.1.52', options_first=False)

    if args['<command>'] == 'regional':
        elems = [args['--tab'], args['--var'], args['--d1'], args['--lat1'], args['--lat2'], args['--lon1'], args['--lon2'], args['--pname'], args['--export'], args['--extV1'], args['--extVV1'] ]
        run(['python', 'plotRegional.py'] + elems)

    elif args['<command>'] == 'timeseries':
        elems = [args['--tab'], args['--var'], args['--d1'], args['--d2'], args['--lat1'], args['--lat2'], args['--lon1'], args['--lon2'], args['--pname'], args['--export'], args['--extV1'], args['--extVV1'], args['--extV2'], args['--extVV2'] ]
        run(['python', 'plotTS.py'] + elems)

    elif args['<command>'] == 'trend':
        elems = [args['--tab'], args['--var'], args['--d1'], args['--d2'], args['--lat1'], args['--lat2'], args['--lon1'], args['--lon2'], args['--pname'], args['--export'], args['--extV1'], args['--extVV1'], args['--extV2'], args['--extVV2'] ]
        run(['python', 'plotXY.py'] + elems)

    elif args['<command>'] == 'dist':
        elems = [args['--tab'], args['--var'], args['--d1'], args['--d2'], args['--lat1'], args['--lat2'], args['--lon1'], args['--lon2'], args['--pname'], args['--export'], args['--extV1'], args['--extVV1'], args['--extV2'], args['--extVV2'] ]
        run(['python', 'plotDist.py'] + elems)

    elif args['<command>'] == 'section':
        elems = [args['--tab'], args['--var'], args['--d1'], args['--lat1'], args['--lat2'], args['--lon1'], args['--lon2'], args['--pname'], args['--export'], args['--extVV1'], args['--extVV2'] ]
        run(['python', 'plotSection.py'] + elems)

    elif args['<command>'] == 'depth':
        elems = [args['--tab'], args['--var'], args['--d1'], args['--lat1'], args['--lat2'], args['--lon1'], args['--lon2'], args['--pname'], args['--export'], args['--extVV1'], args['--extVV2'] ]
        run(['python', 'plotDepthProfile.py'] + elems)

    elif args['<command>'] == 'season':
        elems = [args['--tab'], args['--var'], args['--lat1'], args['--lat2'], args['--lon1'], args['--lon2'], args['--pname'], args['--export'], args['--extV1'], args['--extVV1'], args['--extV2'], args['--extVV2'] ]
        run(['python', 'plotMonthly.py'] + elems)

    elif args['<command>'] == 'cat':
        run(['python', 'getCatalog.py'])

    if args['<command>'] == 'cruise':
        if bool(int(args['--fCruise'])):
            cruiseSource = args['--cruiseTab']    # cruise table name
        else:    
            cruiseSource = args['--vcFile']       # virtaul cruise file
        elems = [args['--fCruise'], args['--cruiseTrack'], cruiseSource, args['--cruiseName'], args['--resampleRate'], args['--pname'], args['--export'], args['--sMatch'], args['--tab'], args['--var'], args['--extV1'], args['--extVV1'], args['--extV2'], args['--extVV2'] ]
        run(['python', 'plotCruise.py'] + elems)

    elif args['<command>'] in ['help', None]:
        run(['python', 'opedia.py', '--help'])

    elif args['<command>'] == 'match':
        elems = [args['--dbMatch'], args['--sourceMatch'], args['--sMatch'], args['--tMatch'], args['--tab'], args['--var'], args['--eFile'] ]
        run(['python', 'match.py'] + elems)

    elif args['<command>'] == 'advect':
        elems = [args['--dtAdvect'], args['--dirAdvect'], args['--d1'], args['--d2'], args['--latAdvect'], args['--lonAdvect'], args['--shape'], args['--match'], args['--shpFile'], args['--export'], args['--sMatch'], args['--tab'], args['--var'], args['--extV1'], args['--extVV1'], args['--extV2'], args['--extVV2'], args['--pname'] ]
        run(['python', 'Lagrangian.py'] + elems)

    elif args['<command>'] == 'eddy':
        elems = [args['--eddySource'], args['--d1'], args['--d2'], args['--lat1'], args['--lat2'], args['--lon1'], args['--lon2'], args['--shape'], args['--match'], args['--shpFile'], args['--export'], args['--sMatch'], args['--tab'], args['--var'], args['--extV1'], args['--extVV1'], args['--extV2'], args['--extVV2'], args['--pname'] ]
        run(['python', 'eddy.py'] + elems)

    elif args['<command>'] == 'ftle':
        elems = [args['--ftleSource'], args['--ftleVar'], args['--ftleValue'], args['--bkg'], args['--d1'], args['--d2'], args['--lat1'], args['--lat2'], args['--lon1'], args['--lon2'], args['--shape'], args['--match'], args['--shpFile'], args['--export'], args['--sMatch'], args['--tab'], args['--var'], args['--extV1'], args['--extVV1'], args['--extV2'], args['--extVV2'], args['--pname'] ]
        run(['python', 'ftle.py'] + elems)

    else:
        exit("%r is not an opedia command. Run 'opedia.py help'." % args['<command>'])
    