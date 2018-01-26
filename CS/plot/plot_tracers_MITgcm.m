function plot_tracers_MITgcm(range)

load(sprintf('/nobackup1/mdehghani/CS_Trunk/0000000009/Lagrangian/MAT/%10.10d.mat',10368));
lon1=1000;
lon2=1600;
lat1=700;
lat2=1100;

last_ftle=ftle(lon1:lon2,lat1:lat2);
%[llo lla last_ftle]=crop_map(get_lon_obs('CCRA'),get_lat_obs('CCRA'),Xres,Yres,150,165,18,26,last_ftle);

%last_ftle(isinf(abs(last_ftle))==0)=0;
%last_ftle(isinf(abs(last_ftle))==1)=0;
%colormap white
colormap default

for field=range
  disp(['field= ',num2str(field)])
  start_date='04-16-2015';
  stamp=datenum(start_date);
  stamp=addtodate(stamp,0,'day');
  matdate=datestr(stamp,'yyyymmdd') 
  
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/0000000009/Lagrangian/MAT/Trajectory/0000010368_%10.10d.mat',field));
  
   X1=X1(lon1:lon2,lat1:lat2);
   Y1=Y1(lon1:lon2,lat1:lat2); 
%  [llo lla X1]=crop_map(get_lon_obs('CCRA'),get_lat_obs('CCRA'),Xres,Yres,150,165,18,26,X1);
%  [llo lla Y1]=crop_map(get_lon_obs('CCRA'),get_lat_obs('CCRA'),Xres,Yres,150,165,18,26,Y1);
  llo=get_lon;
  lla=get_lat;
  llo=llo(lon1:lon2);
  lla=lla(lat1:lat2);
  %%%%% Cut HOT Area  %%%%%%%%

  X2=X1(1:1:end,1:1:end);    %magneta
  Y2=Y1(1:1:end,1:1:end);

%{
  X2=X1(500:540,250:290);    %magneta
  Y2=Y1(500:540,250:290);

  X_HOT=X1(730:770,200:240);   %yellow
  Y_HOT=Y1(730:770,200:240);

  X3=X1(740:780,430:470);   %black
  Y3=Y1(740:780,430:470);

  X4=X1(900:940,670:710);   %green
  Y4=Y1(900:940,670:710);

  X5=X1(980:1020,460:500);   %red
  Y5=Y1(980:1020,460:500);

  X6=X1(980:1020,320:360);   %white
  Y6=Y1(980:1020,320:360);

  X7=X1(650:690,500:540);   %orang
  Y7=Y1(650:690,500:540);
  %%%%%%%%%%%%%%%%%%%%%%%%%%%
%}
  x=X2(:);
  y=Y2(:);
%{
  x_HOT=X_HOT(:);
  y_HOT=Y_HOT(:);

  x3=X3(:);
  y3=Y3(:);

  x4=X4(:);
  y4=Y4(:);

  x5=X5(:);
  y5=Y5(:);

  x6=X6(:);
  y6=Y6(:);

  x7=X7(:);
  y7=Y7(:);
%}

  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

  min_lon =  min(llo);
  max_lon =  max(llo);
  min_lat =  min(lla);
  max_lat =  max(lla);
  index_min_lat = 1;
  index_max_lat = size(X1,2);
  index_min_lon = 1;
  index_max_lon = size(X1,1);
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



  imagesc(llo,lla,last_ftle');
%  colorbar;
  caxis([0 0.7]);
%  title({'Tracer Trajectory, FTLE', matdate});

  hold on

  plot(x,y,'.','Color','m','markers',1);
%{  
  plot(x_HOT,y_HOT,'.','Color','y','markers',1);
  plot(x3,y3,'.','Color','k','markers',1);
  plot(x4,y4,'.','Color','g','markers',1);
  plot(x5,y5,'.','Color','r','markers',1);
  plot(x6,y6,'.','Color','w','markers',1);
  plot(x7,y7,'.','Color',[1 0.5 0.25],'markers',1);
%}
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
  grid on
  set(gca,'Xcolor','k','Ycolor','k','GridLineStyle','-.','LineWidth',1);
  
%  plot_Hawaii_mask;  

  print('-dpng', '-r500', sprintf('/nobackup1/mdehghani/CS_Trunk/0000000009/Lagrangian/FTLE/tracer/%10.10d.png',field));

  hold off
  grid off

%last_ftle(isinf(abs(last_ftle))==1)=nan;
%nanmin(last_ftle(:))
%nanmax(last_ftle(:))
%figure; imagesc(isinf(abs(last_ftle)))

end



