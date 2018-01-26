
function gen_ssh(itnums,Xres,Yres)

  addpath(genpath('~/matbox/CS'));

  %lon=get_lon_obs(DataSource);
  %lat=get_lat_obs(DataSource);
  [lon lat ssh]=getSSH_AVISO_dt(itnums(1));              %%%%   CHANGE TO NRT OR DT


  [LON,LAT]=meshgrid(lon,lat);
  min_lon=min(lon);
  max_lon=max(lon);
  min_lat=min(lat);
  max_lat=max(lat);


  if Xres & Yres
%    X=ceil(min_lon):Xres:fix(max_lon);
%    Y=ceil(min_lat):Yres:fix(max_lat);

    X=(min_lon):Xres:(max_lon);
    Y=(min_lat):Yres:(max_lat);
  else
    X=lon;
    Y=lat;
  end
  [X,Y]=meshgrid(X,Y);
%  lon=ceil(min_lon):Xres:fix(max_lon);
%  lat=ceil(min_lat):Yres:fix(max_lat);


  lon=(min_lon):Xres:(max_lon);
  lat=(min_lat):Yres:(max_lat);    

  for itnum=itnums
    disp([num2str(itnum)])

    [lon lat ssh]=getSSH_AVISO_dt(itnum);                   %%%%   CHANGE TO NRT OR DT

    ssh=interpolate(LON,LAT,ssh',X,Y);
    %col=size(ssh,2);
    %row=size(ssh,1);   
    %save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/ssh/ssh_%10.10d.mat',itnum), 'ssh', 'itnum', 'Xres', 'col', 'row');
    %%plot_ssh(lon,lat,ssh,{'SSH', num2str(itnum)});



    data=ssh;
    rows=2;
    cols=4;
    dh=size(data,1)/rows;
    dw=size(data,2)/cols;
    for i=1:rows
      for j=1:cols
        ssh=data(1+(i-1)*dh:i*dh, 1+(j-1)*dw:j*dw);
        col=size(ssh,2); 
        row=size(ssh,1);
        save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/ssh/ssh_%10.10d_%d_%d.mat',itnum,i,j), 'ssh', 'itnum', 'Xres', 'col', 'row');
      end
    end

  end

end




function [lon lat SSH]=getSSH_AVISO_nrt(itnum)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  AVISO  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
path=strcat('/nobackup1/mdehghani/obs/AVISO/ssh/nrt_adt_ssh_AVISO_',sprintf('%7.7d',itnum),'.nc');
ncid=netcdf.open(path);

lon=double(netcdf.getVar(ncid,4));
lat=double(netcdf.getVar(ncid,2));

SSH=double(netcdf.getVar(ncid,7));   % this is infact ADT not SSH!
SSH(find(abs(SSH)>50000))=NaN;
SSH=SSH/10000;

%mean_SSH = nanmean(SSH(:));
%sigma_SSH = nanstd(SSH(:));


lon=lon(750:840);
lat=lat(425:480);
SSH=SSH(750:840,425:480);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end



function [lon lat SSH]=getSSH_AVISO_dt(itnum)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  AVISO  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%path=strcat('/nobackup1/mdehghani/obs/AVISO/ssh/adt_ssh_AVISO_',sprintf('%7.7d',itnum),'.nc');     %>>>>>>>>>  absoloute dynamic topography
path=strcat('/nobackup1/mdehghani/obs/AVISO/ssh/sla_ssh_AVISO_',sprintf('%7.7d',itnum),'.nc');     %>>>>>>>>>  sea level anomaly
ncid=netcdf.open(path);

lon=double(netcdf.getVar(ncid,1));
%if itnum < 2014001				%>>>>>>>>>  absoloute dynamic topography
%  lon=double(netcdf.getVar(ncid,2));		%>>>>>>>>>  absoloute dynamic topography
%end						%>>>>>>>>>  absoloute dynamic topography		


lat=double(netcdf.getVar(ncid,4));

SSH=double(netcdf.getVar(ncid,3));
SSH(find(abs(SSH)>50000))=NaN;
SSH=SSH/10000;

%mean_SSH = nanmean(SSH(:));
%sigma_SSH = nanstd(SSH(:));


%%%%%%%%%%%%%%  Hawaii, SCOPE  %%%%%%%%%%%%
%lon=lon(750:840);
%lat=lat(425:480);
%SSH=SSH(750:840,425:480);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%  Gulf Stream  %%%%%%%%%%%%%%
%lon=lon(1101:1249);
%lat=lat(449:549);
%SSH=SSH(1101:1249,449:549);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end


function plot_ssh(lon,lat,ssh,ti)
%colormap jet;
imagesc(ssh);
axis xy;
%set(gca,'XDir','reverse');
%caxis([0.7 1.3])	% >>>>>>  absoloute dynamic topography
caxis([-0.18 0.18])        %>>>>>>>>>  sea level anomaly
colorbar;
title(ti);
daspect([1 1 1]);
drawnow;
end
