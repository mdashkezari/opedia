function plot_SSH(DataSource,itnum);
  addpath(genpath('../'));  % adding floder and subfolders to the matlab path
  addpath('/home/mdehghani/matbox/OceanFTLE/m_map')

  if strcmp(DataSource,'AVISO')
    plotSSH_AVISO(itnum,DataSource);
  elseif strcmp(DataSource,'HYCOM')
    plotSSH_HYCOM(itnum,DataSource);
  elseif strcmp(DataSource,'CCRA')
    plotSSH_CCRA(itnum,DataSource);
  end

end





function plotSSH_HYCOM(itnum,DataSource);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% HYCOM %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lon=get_lon_obs(DataSource);
lat=get_lat_obs(DataSource);
SSH=getSSH_obs(DataSource,itnum);

imagesc(abs(lon-360),lat,SSH');
colorbar;
set(gca,'YDir','normal');
set(gca,'XDir','reverse');

xlabel('Longitude');
ylabel('Latitude');

ndt=datestr(now,'dd-mmm-yyyy');  %'20150626';
stamp=datenum(ndt);
ndt=datestr(now,'yyyymmdd'); 
stamp=addtodate(stamp,itnum-1,'day');
dt=datestr(stamp,'yyyymmdd');
if itnum>1
  title({'SSH, HYCOM', strcat(datestr(stamp,'dd-mmm-yyyy'),' (forecast)')})  
else
  title({'SSH, HYCOM', datestr(stamp,'dd-mm-yyyy')})
end

storage_folder=strcat('/nobackup1/mdehghani/llc_4320_hawaii/pics/stdFTLE/HYCOM/',ndt);
if exist(storage_folder)~=7
  mkdir(storage_folder);
end
print('-dpng','-r500',strcat(storage_folder,'/SSH_',dt,'.png')); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end





function plotSSH_CCRA(itnum,DataSource);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% CCRA %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lon=get_lon_obs(DataSource);
lat=get_lat_obs(DataSource);
SSH=getSSH_obs(DataSource,itnum);
SSH(isnan(SSH)==1)=0;
%%%%%
lon=lon(59:125);
lat=lat(23:55);
SSH=SSH(59:125,23:55);
%%%%



%%%%%%%%%%%%%%%%%%% interpolation %%%%%%%%%%%%%%%%%%%%%%
%  lon=get_lon_obs(DataSource);
%  lat=get_lat_obs(DataSource);

  Xres = 0.01;
  Yres = 0.01;
  [LON,LAT]=meshgrid(lon,lat);
  min_lon=min(lon);
  max_lon=max(lon);
  min_lat=min(lat);
  max_lat=max(lat);

    X=ceil(min_lon):Xres:fix(max_lon);
    Y=ceil(min_lat):Yres:fix(max_lat);
  [X,Y]=meshgrid(X,Y);

  SSH=interpolate(LON,LAT,SSH',X,Y);
  SSH=SSH';
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%





%colormap jet

imagesc(lon,lat,SSH');
colorbar;
set(gca,'YDir','normal');
%set(gca,'XDir','reverse');

xlabel('Longitude');
ylabel('Latitude');


itnum_str = num2str(itnum);
year = str2num(itnum_str(1:4));
day_of_year = str2num(itnum_str(5:end));
stamp = doy2date(day_of_year, year);
title({'SSH, CCAR', datestr(stamp,'mmm-dd-yyyy')})
%caxis([-25, 25])
colormap(b2r(-30,30))
daspect([1 1 1])

%hold on
%contour(X,Y,SSH',-25:5:25,'Linecolor',[0.3 0.3 0.3],'LineWidth',1)
%hold off

plot_Hawaii_mask;

storage_path=sprintf('/nobackup1/mdehghani/hawaii_tempo/colaboration_meeting/dec2015/SSH/%10.10d.png',itnum);
%if exist(storage_folder)~=7
%  mkdir(storage_folder);
%end
print('-dpng','-r500',storage_path);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end
