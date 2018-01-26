function plot_tracers_formick(run,it_start,range)

llo=get_lon_obs('CCRA');
lla=get_lat_obs('CCRA');

for it=range

  disp(['field= ',num2str(it)])
  st=num2str(it_start + it);
  year=str2num(st(1:4));
  day_of_year=str2num(st(5:end));
  stamp=doy2date(day_of_year+1,year);
  matdate=datestr(stamp,'mmm dd yyyy');
 

  load(sprintf('/nobackup1/mdehghani/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat',run,it_start,it));
  field=[];

  
[llo lla X1]=Cut_CCRA_Results(get_lon_obs('CCRA'),get_lat_obs('CCRA'),Xres,Yres,150,165,18,26,X1);
[llo lla Y1]=Cut_CCRA_Results(get_lon_obs('CCRA'),get_lat_obs('CCRA'),Xres,Yres,150,165,18,26,Y1);

  %%%%% Cut HOT Area  %%%%%%%%


  X2=X1(810:830,620:640);   %green
  Y2=Y1(810:830,620:640);

  X7=X1(650:670,430:450);   %orang
  Y7=Y1(650:670,430:450);

  X7=X1(690:710,470:490);   %orang
  Y7=Y1(690:710,470:490);

  n=5;
  X7=X1(1:n:end,1:n:end);   %orang
  Y7=Y1(1:n:end,1:n:end);
  %%%%%%%%%%%%%%%%%%%%%%%%%%%

  x=X2(:);
  y=Y2(:);

  x7=X7(:);
  y7=Y7(:);

  min_lon =  min(llo);
  max_lon =  max(llo);
  min_lat =  min(lla);
  max_lat =  max(lla);
  index_min_lat = 1;
  index_max_lat = size(X1,2);
  index_min_lon = 1;
  index_max_lon = size(X1,1);

  hold on

%  plot(x,y,'.','Color','b','markers',1);
  %plot(x7,y7,'.','Color',[1 0.5 0.25],'markers',1);
  plot(x7,y7,'.','Color','m','markers',1);


  daspect([1,1,1])
  grid on
  set(gca,'Xcolor','k','Ycolor','k','GridLineStyle','-.','LineWidth',1);

plot_Hawaii_mask;

%xlim([198,208])
%ylim([20,25])

xlabel('Longitude')
ylabel('Latitude')
title(matdate)

  tracer_path=sprintf('/nobackup1/mdehghani/CS_Trunk/%10.10d/Lagrangian/FTLE/tracer/',run);
  if exist(tracer_path)~=7
    mkdir(tracer_path);
  end
  print('-dpng', '-r500', sprintf('%s%10.10d.png',tracer_path,it));

  hold off
  grid off
  close
end


end




function [lon lat ftle]=Cut_CCRA_Results(lon,lat,Xres,Yres,lon_min_target,lon_max_target,lat_min_target,lat_max_target,ftle)
  min_lon=min(lon);
  max_lon=max(lon);
  min_lat=min(lat);
  max_lat=max(lat);
  lon=ceil(min_lon):Xres:fix(max_lon);
  lat=ceil(min_lat):Yres:fix(max_lat);

  [a lon_index_start]=min(abs(abs(lon-360)-lon_max_target));
  [a lon_index_end]=min(abs(abs(lon-360)-lon_min_target));
  [a lat_index_start]=min(abs(lat-lat_min_target));
  [a lat_index_end]=min(abs(lat-lat_max_target));

  lon=lon(lon_index_start:lon_index_end);
  lat=lat(lat_index_start:lat_index_end);
  ftle=ftle(lon_index_start:lon_index_end, lat_index_start:lat_index_end);
end
