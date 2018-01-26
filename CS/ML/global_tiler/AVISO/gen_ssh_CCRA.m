
function gen_ssh_CCRA(itnums,Xres,Yres)

  addpath(genpath('~/matbox/CS'));

  lon=get_lon_obs('CCRA');
  lat=get_lat_obs('CCRA');

  [LON,LAT]=meshgrid(lon,lat);
  min_lon=min(lon);
  max_lon=max(lon);
  min_lat=min(lat);
  max_lat=max(lat);

  if Xres & Yres
    X=ceil(min_lon):Xres:fix(max_lon);
    Y=ceil(min_lat):Yres:fix(max_lat);
  else
    X=lon;
    Y=lat;
  end
  [X,Y]=meshgrid(X,Y);
  lon=ceil(min_lon):Xres:fix(max_lon);
  lat=ceil(min_lat):Yres:fix(max_lat);

    
  for itnum=itnums
    disp([num2str(itnum)])

    [lon lat ssh]=getSSH_CCRA('CCRA',itnum);                   

    ssh=interpolate(LON,LAT,ssh',X,Y);
    col=size(ssh,2);
    row=size(ssh,1);   
    save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/ssh/ssh_%10.10d.mat',itnum), 'ssh', 'itnum', 'Xres', 'col', 'row');
    %plot_ssh(lon,lat,ssh,{'SSH', num2str(itnum)});
  end

end



function [lon lat SSH]=getSSH_CCRA(DataSource,itnum)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  CCRA  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[lon lat SSH]=get_obs(DataSource,2,itnum);
SSH(find(abs(SSH)>1000))=NaN;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end



function [lon lat SSH]=getSSH_AVISO_dt(itnum)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  AVISO  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
path=strcat('/nobackup1/mdehghani/obs/AVISO/ssh/adt_ssh_AVISO_',sprintf('%7.7d',itnum),'.nc');
ncid=netcdf.open(path);

lon=double(netcdf.getVar(ncid,1));
if itnum < 2014001
  lon=double(netcdf.getVar(ncid,2));
end
lat=double(netcdf.getVar(ncid,4));

SSH=double(netcdf.getVar(ncid,3));
SSH(find(abs(SSH)>50000))=NaN;
SSH=SSH/10000;

%mean_SSH = nanmean(SSH(:));
%sigma_SSH = nanstd(SSH(:));

lon=lon(750:840);
lat=lat(425:480);
SSH=SSH(750:840,425:480);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end


function plot_ssh(lon,lat,ssh,ti)
%colormap jet;
imagesc(ssh);
axis xy;
%set(gca,'XDir','reverse');
caxis([-20 20])
colorbar;
title(ti);
daspect([1 1 1]);
drawnow;
end
