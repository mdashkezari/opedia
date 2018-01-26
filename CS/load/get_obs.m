%%%%%%%%%%% Absolute Geostrophic Velocity netCDF Format  %%%%%%%%%%%
%  Channel         Variable Name
%  0               crs
%  1               v
%  2               u
%  3               lon
%  4               time
%  5               lat 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%% Geostrophic Velocity Anomally netCDF Format  %%%%%%%%%%%
%  Channel         Variable Name
%  0               v
%  1               u
%  2               lon
%  3               time
%  4               lat 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%% Near-Real-Time Absolute Geostrophic Velocity netCDF Format  %%%
%  Channel         Variable Name
%  0               crs
%  1               time
%  2               lat
%  3               lat_bnds
%  4               lon
%  5               lon_bands
%  6               nv
%  7               u
%  8               v 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%  NETCDF DataFormat of HYCOM %%%%%%%%%%%%%%%%%%%%
%  Channel          Variable Name
%  0                MT 
%  1                Date 
%  2                Y
%  3                X
%  4                lat
%  5                lon
%  6                ice_coverage
%  7                ice_thickness
%  8                ssh
%  9                u_barotropic_velocity 
%  10               v_barotropic_velocity
%  11               surface_boundary_layer
%  12               mixed_layer_thickness
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [lon lat data]=get_obs(DataSource,channel,iteration, lonLabel, latLabe)
  
  if strcmp(DataSource,'AVISO')
    [lon lat data]=get_AVISO(channel,iteration, lonLabel, latLabe);
  elseif strcmp(DataSource,'HYCOM')
    [lon lat data]=get_HYCOM(channel,iteration);
  elseif strcmp(DataSource,'CCRA')
    [lon lat data]=get_CCRA(channel,iteration);
  end  

end






function [lon lat data]=get_AVISO(channel,iteration, lonLabel, latLabel)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  AVISO  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%{
repDataPath = 'H:/opedia_vault/raw/obs/rep/alt/rep_alt_';
nrtDataPath = 'H:/opedia_vault/raw/obs/nrt/alt/nrt_alt_';
path=strcat(repDataPath, sprintf('%7.7d',iteration),'.nc');     % first assumes that the reprocessed file exist
if exist(path, 'file') ~= 2                                     % if reprocessed file didn't exist, look for nrt file    
  path=strcat(nrtDataPath, sprintf('%7.7d',iteration),'.nc');
  assert(exist(path,'file') ~= 2, 'NetCDF file not found.' );
end  
%}

[rep nrt path] = get_filepath(iteration);
ncid=netcdf.open(path);

%%%%%%%%%%%% near real time %%%%%%%%%%%%
%lon=double(netcdf.getVar(ncid,3));
%lat=double(netcdf.getVar(ncid,2));
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%data=double(netcdf.getVar(ncid,channel));


lon=double(ncread(path, lonLabel));
lat=double(ncread(path, latLabel));
data=double(ncread(path, channel));


data(find(abs(data)>2147483646))=NaN;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end




function [lon lat data]=get_HYCOM(channel,iteration)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  HYCOM  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
today_folder=datestr(now,'YYYYmmdd');
%today_folder='20150625';

if iteration==1
  path=strcat('/nobackup1/mdehghani/obs/HYCOM/',today_folder,'/rtofs_glo_2ds_n024_3hrly_diag.nc'); 
else
  path=strcat('/nobackup1/mdehghani/obs/HYCOM/',today_folder,'/rtofs_glo_2ds_f',sprintf('%0.3d',iteration*24),'_3hrly_diag.nc');     
end


ncid=netcdf.open(path);

lon=double(netcdf.getVar(ncid,5));
lat=double(netcdf.getVar(ncid,4));

data=double(netcdf.getVar(ncid,channel));

lon=lon(1400:1700,1720:1900);
lat=lat(1400:1700,1720:1900);
data=data(1400:1700,1720:1900);

%[numdims,numvars,numglobalatts,unlimdimid] = netcdf.inq(ncid)
%[name,xtype,dimids,natts] = netcdf.inqVar(ncid,channel)

%data(find(abs(data)>100))=NaN;
lon=lon(:,1);
lat=lat(1,:);
lat=lat';
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end




function [lon lat data]=get_CCRA(channel,iteration)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  CCRA  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%offset=doy(now)-1;   
%path=strcat('/nobackup1/mdehghani/obs/CCAR/GeoVel/geoVel_global_wrt_mean_',datestr(now,'yyyy'),sprintf('%3.3d',offset+iteration-1),'.nc')
path=strcat('/nobackup1/mdehghani/obs/CCAR/GeoVel/geoVel_global_wrt_mean_',sprintf('%7.7d',iteration),'.nc');

ncid=netcdf.open(path);

lon=double(netcdf.getVar(ncid,0));
lat=double(netcdf.getVar(ncid,1));
data=double(netcdf.getVar(ncid,channel));


lon=lon(720:870);
lat=lat(315:405);
data=data(720:870,315:405);


%lon=lon(400:1200);
%lat=lat(200:500);
%data=data(400:1200,200:500);

%[numdims,numvars,numglobalatts,unlimdimid] = netcdf.inq(ncid)
%[name,xtype,dimids,natts] = netcdf.inqVar(ncid,channel)

%data(find(abs(data)>100))=NaN;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end
