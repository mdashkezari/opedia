function plot_tracers_CCRA(run,it_start,range)

llo=get_lon_obs('CCRA');
lla=get_lat_obs('CCRA');

for it=range

  disp(['field= ',num2str(it)])
  st=num2str(it_start + it);
  year=str2num(st(1:4));
  day_of_year=str2num(st(5:end));
  stamp=doy2date(day_of_year,year);
  matdate=datestr(stamp,'mmm dd yyyy');
 

  load(sprintf('/nobackup1/mdehghani/CS_Trunk/%10.10d/Lagrangian/MAT/%10.10d.mat',run,it_start+it-1 ));
  ft=ftle;
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat',run,it_start,it));
  field=[];

  
[llo lla X1]=Cut_CCRA_Results(get_lon_obs('CCRA'),get_lat_obs('CCRA'),Xres,Yres,150,165,18,26,X1);
[llo lla Y1]=Cut_CCRA_Results(get_lon_obs('CCRA'),get_lat_obs('CCRA'),Xres,Yres,150,165,18,26,Y1);

  %%%%% Cut HOT Area  %%%%%%%%


  X2=X1(810:830,620:640);   %green
  Y2=Y1(810:830,620:640);

  X7=X1(650:670,430:450);   %orang
  Y7=Y1(650:670,430:450);

  %%%%%%%%%%%%%%%%%%%%%%%%%%%

  x=X2(:);
  y=Y2(:);

  x7=X7(:);
  y7=Y7(:);
  %%%%%%%%%%%%% load drifter locations %%%%%%%%%%%%  
  [d1_lon,d1_lat,d2_lon,d2_lat,d3_lon,d3_lat]=load_drifters;
  
  lon_offset=0;
  lat_offset=0;

  d1_lon=d1_lon+lon_offset;
  d1_lat=d1_lat+lat_offset; 
  d2_lon=d2_lon+lon_offset;
  d2_lat=d2_lat+lat_offset;
  d3_lon=d3_lon+lon_offset;
  d3_lat=d3_lat+lat_offset;
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

  min_lon =  min(llo);
  max_lon =  max(llo);
  min_lat =  min(lla);
  max_lat =  max(lla);
  index_min_lat = 1;
  index_max_lat = size(X1,2);
  index_min_lon = 1;
  index_max_lon = size(X1,1);

  imagesc(llo,lla,ft');
  %colorbar;
  caxis([0 0.25]);
  title({'Tracer Trajectory, Drifter Trajectory, FTLE', matdate});

  hold on

  plot(x,y,'.','Color','y','markers',1);
  %plot(x7,y7,'.','Color',[1 0.5 0.25],'markers',1);
  plot(x7,y7,'.','Color','m','markers',1);

%if field==max(range)
  plot(abs(d1_lon+360),d1_lat,'.','Color','y','markers',5);
  plot(abs(d2_lon+360),d2_lat,'.','Color','r','markers',5);
  plot(abs(d3_lon+360),d3_lat,'.','Color','r','markers',5);      % ALOHA drifter
%end
  axis xy;

  yt=get(gca,'ytick');
  for k=1:numel(yt);
    yt1{k}=sprintf('%d°N',yt(k));
  end
  set(gca,'yticklabel',yt1);

  NumTicks = 16;
  L = get(gca,'XLim');
  set(gca,'XTick',linspace(L(1),L(2),NumTicks))
  set(gca,'FontSize',8);

  xt=get(gca,'xtick');
  for k=1:numel(xt);
    xt1{k}=sprintf('%3.3d°W',round(abs(xt(k)-360)));
  end
  set(gca,'xticklabel',xt1);

  daspect([1,1,1])
%  grid on
  set(gca,'Xcolor','k','Ycolor','k','GridLineStyle','-.','LineWidth',1);

plot_Hawaii_mask;

  tracer_path=sprintf('/nobackup1/mdehghani/CS_Trunk/%10.10d/Lagrangian/FTLE/tracer/',run);
  if exist(tracer_path)~=7
    mkdir(tracer_path);
  end
  print('-dpng', '-r500', sprintf('%s%10.10d.png',tracer_path,it));

  hold off
  grid off

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
