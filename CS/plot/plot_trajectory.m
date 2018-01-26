function plot_trajectory(DataSource,run,itnum_start,day_of_year,year,dir,range)

%cc=hsv(15);
  if strcmp(DataSource,'AVISO')
    [mx,my]=get_global_mask_AVISO;
  elseif strcmp(DataSource,'CCRA')
    [mx,my]=get_global_mask_CCAR;
  end

for field=range
  disp(['field= ',num2str(field)])
  %start_date='04-10-2015';
%  stamp=datenum(start_date);
  stamp=doy2date(day_of_year,year);
  stamp=addtodate(stamp,dir*(field-1),'day');
  matdate=datestr(stamp,'mmm dd yyyy'); 
  
  load(sprintf('/pool001/mdehghani/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat',run,itnum_start,field));
  
  %%%%% Cut HOT Area  %%%%%%%%

  sp=1;
  wid=100;
%  lon0=4000;    %% above the islands
%  lat0=1750;    %% above the islands
  
%  lon0=5800;
%  lat0=2080;

%  lon0=5650;
%  lat0=1900;

  %%%%%%%% AVISO  %%%%%%%%
  lon0=3950;    %% above the islands
  lat0=2230;    %% above the islands

%  lon0=5800;     %% gulf stream - north 
%  lat0=2540;     %% gulf stream - north

%  lon0=5590;     %% gulf stream - south 
%  lat0=2330;     %% gulf stream - south
  %%%%%%%%%%%%%%%%%%%%%%%%

  n=1;
  m=1;
  X2=X1((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid));
  Y2=Y1((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid));
  x1=X2(:);
  y1=Y2(:);

  n=2;
  m=1;
  X2=X1((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid));
  Y2=Y1((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid));  
  x2=X2(:);
  y2=Y2(:);

  n=3;
  m=1;
  X2=X1((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid));
  Y2=Y1((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid));
  x3=X2(:);
  y3=Y2(:);


  n=1;
  m=2;
  X2=X1((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid));
  Y2=Y1((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid));
  x4=X2(:);
  y4=Y2(:);
  
  n=2;
  m=2;
  X2=X1((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid));
  Y2=Y1((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid)); 
  x5=X2(:);
  y5=Y2(:);

  n=3;
  m=2;
  X2=X1((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid));
  Y2=Y1((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid));
  x6=X2(:);
  y6=Y2(:);

  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  marsize=4;
%{
  subplot(2,1,1);
  h=plot(x1,y1,'.k',x2,y2,'.y',x3,y3,'.g',x4,y4,'.c',x5,y5,'.b',x6,y6,'.r',mx,my,'om');
  set(h,{'markers'},{4;4;4;4;4;4;4});
  set(h,{'MarkerFaceColor'},{[0 0 0];[1 1 0];[0 1 0];[0 1 1];[0 0 1];[1 0 0];[1 0 1]})
  xlim([185 220]);
  ylim([17 29]);
  title(strcat(matdate,' '));
  xlabel('Longitude');
  ylabel('Latitude');
  daspect([1,1,1])

  subplot(2,1,2);
  h=plot(x1,y1,'.k',x2,y2,'.y',x3,y3,'.g',x4,y4,'.c',x5,y5,'.b',x6,y6,'.r',mx,my,'om');
  set(h,{'markers'},{marsize;marsize;marsize;marsize;marsize;marsize;1});
  set(h,{'MarkerFaceColor'},{[0 0 0];[1 1 0];[0 1 0];[0 1 1];[0 0 1];[1 0 0];[1 0 1]})
  xlim([120 270]);
  ylim([0 50]);
  title(strcat(matdate,' (Zoomed-Out)'));
  xlabel('Longitude');
  ylabel('Latitude');
  daspect([1,1,1])

  subplot(2,2,[3 4]); 
%}
  %h=plot(x1,y1,'.k',x2,y2,'.y',x3,y3,'.g',x4,y4,'.c',x5,y5,'.b',x6,y6,'.r',mx,my,'om');
  %set(h,{'markers'},{marsize;marsize;marsize;marsize;marsize;marsize;2});
  %set(h,{'MarkerFaceColor'},{[0 0 0];[1 1 0];[0 1 0];[0 1 1];[0 0 1];[1 0 0];[1 0 1]})

  h=plot(x1,y1,'.',x2,y2,'.');
  set(h,{'markers'},{marsize;marsize});
  set(h,{'Color'},{[1 .2 0.6];[.2 .3 1]})

  xlim([180 220]);    % Islands
  ylim([15 31]);      % Islands
%  xlim([260 330]);   %GulfStream
%  ylim([15 50]);     %GulfStream 
%  xlim([0 360]);
%  ylim([-90 90]);
  title(strcat(matdate,' '));
  xlabel('Longitude');
  ylabel('Latitude');
  daspect([1,1,1])
  %axis equal

plot_Hawaii_mask;

  tracer_path=sprintf('/nobackup1/mdehghani/CS_Trunk/%10.10d/Lagrangian/FTLE/tracer/',run);
  if exist(tracer_path)~=7
    mkdir(tracer_path);
  end
  print('-dpng', '-r500', sprintf('%s%10.10d.png',tracer_path,field));

%  grid off
end


end



function [x y]=cutTracers(lon,lat,Xres,Yres,X,Y,lon_min_target,lon_max_target,lat_max_target,lat_min_target)

  min_lon=min(lon);
  max_lon=max(lon);
  min_lat=min(lat);
  max_lat=max(lat);
  lon=ceil(min_lon):Xres:fix(max_lon);
  lat=ceil(min_lat):Yres:fix(max_lat);

  [a lon_index_start]=min(abs(lon-lon_min_target));
  [a lon_index_end]=min(abs(lon-lon_max_target));
  [a lat_index_start]=min(abs(lat-lat_max_target));
  [a lat_index_end]=min(abs(lat-lat_min_target));

  X2=X(lon_index_start:5:lon_index_end,lat_index_start:5:lat_index_end);
  Y2=Y(lon_index_start:5:lon_index_end,lat_index_start:5:lat_index_end);

  x=X2(:);
  y=Y2(:);
end

