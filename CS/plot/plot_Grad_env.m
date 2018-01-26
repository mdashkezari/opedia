function []=store_environmental(itnum,field)


first_itnum=10368;          % the first iteration number of the run
timestep=20;                % elapsed time between sequential itnums (in minutes) 
itnum_step=144;             % diffrence between sequential itnums 
elapsed_min= ((itnum-first_itnum)/itnum_step)*timestep;
elapsed_hour= floor(elapsed_min/60);
elapsed_day= floor(elapsed_min/(60*24));
elapsed=sprintf( 'Elapsed time (day:hour:min) %s:%s:%s',  sprintf('%2.2d',elapsed_day), sprintf('%2.2d',elapsed_hour-elapsed_day*24), sprintf('%2.2d',elapsed_min-elapsed_hour*60) );
frame=floor((itnum-first_itnum)/itnum_step);

T=getT(itnum);
deltaTemp=envGrad(T)';
S=getSalt(itnum);
deltaSalt=envGrad(S)';
E=getEta(itnum);
deltaEta=envGrad(E)';

lon=get_lon;
lat=get_lat;





    islands=false;
    map_title=sprintf('|Grad| SST \n %s',elapsed);
    color_range=[0 0.5];
    map_path=sprintf('/nobackup1/mdehghani/llc_4320_hawaii/pics/temperature/full/%10.10d.png',field);
    plot_map(deltaTemp,lon,lat,islands,map_title,color_range,map_path,false);
    
    islands=true;
    map_title=sprintf('|Grad| SST \n %s',elapsed);
    color_range=[0 0.5];
    map_path=sprintf('/nobackup1/mdehghani/llc_4320_hawaii/pics/temperature/islands/%10.10d.png',field);
    plot_map(deltaTemp,lon,lat,islands,map_title,color_range,map_path,false);



    islands=false;
    map_title=sprintf('|Grad| Salinity \n %s',elapsed);
    color_range=[0 0.2];
    map_path=sprintf('/nobackup1/mdehghani/llc_4320_hawaii/pics/salinity/full/%10.10d.png',field);
    plot_map(deltaSalt,lon,lat,islands,map_title,color_range,map_path,false);

    islands=true;
    map_title=sprintf('|Grad| Salinity \n %s',elapsed);
    color_range=[0 0.2];
    map_path=sprintf('/nobackup1/mdehghani/llc_4320_hawaii/pics/salinity/islands/%10.10d.png',field);
    plot_map(deltaSalt,lon,lat,islands,map_title,color_range,map_path,false);



    islands=false;
    map_title=sprintf('|Grad| SSH \n %s',elapsed);
    color_range=[0 0.02];
    map_path=sprintf('/nobackup1/mdehghani/llc_4320_hawaii/pics/eta/full/%10.10d.png',field);
    plot_map(deltaEta,lon,lat,islands,map_title,color_range,map_path,false);

    islands=true;
    map_title=sprintf('|Grad| SSH \n %s',elapsed);
    color_range=[0 0.02];
    map_path=sprintf('/nobackup1/mdehghani/llc_4320_hawaii/pics/eta/islands/%10.10d.png',field);
    plot_map(deltaEta,lon,lat,islands,map_title,color_range,map_path,false);

