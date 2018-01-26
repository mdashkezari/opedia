
%%%%%%%%%%% Geostrophic Velocity Anomally netCDF Format  %%%%%%%%%%%
%  Channel         Variable Name
%  0               v
%  1               u
%  2               lon
%  3               time
%  4               lat 
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


%%%%%%%%%%%%%%%%%%% NETCDF DataFormat of CCRA %%%%%%%%%%%%%%%%%%%%%
%  0               lon
%  1               lat
%  2               ssh
%  3               u_vel
%  4               v_vel
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [SSH] = getSSH_obs(DataSource,itnum)

  if strcmp(DataSource,'AVISO')
    [lon lat SSH]=getSSH_AVISO(DataSource,itnum);
  elseif strcmp(DataSource,'HYCOM')
    [lon lat SSH]=getSSH_HYCOM(DataSource,itnum);
  elseif strcmp(DataSource,'CCRA')
    [lon lat SSH]=getSSH_CCRA(DataSource,itnum);
  end

end



function [lon lat SSH]=getSSH_AVISO(DataSource,itnum)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  AVISO  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
path=strcat('/nobackup1/mdehghani/obs/AVISO/ssh/adt_ssh_AVISO_',sprintf('%7.7d',itnum),'.nc');
ncid=netcdf.open(path);

lon=double(netcdf.getVar(ncid,1));
lat=double(netcdf.getVar(ncid,4));

SSH=double(netcdf.getVar(ncid,3));
SSH(find(abs(SSH)>50000))=NaN;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end



function [lon lat SSH]=getSSH_HYCOM(DataSource,itnum)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  HYCOM  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[lon lat SSH]=get_obs(DataSource,8,itnum);
SSH(find(abs(SSH)>100))=NaN;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end



function [lon lat SSH]=getSSH_CCRA(DataSource,itnum)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  CCRA  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[lon lat SSH]=get_obs(DataSource,2,itnum);
SSH(find(abs(SSH)>1000))=NaN;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end
