function plot_traj_AVISO(DataSource,run,itnum_start,day_of_year,year,dir,range)

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
  
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat',run,itnum_start,field));
  
  %%%%% Cut HOT Area  %%%%%%%%

%  [x1 y1]=cutTracers(lon,lat,Xres,Yres,X1,Y1,180,190,0,10);
%  [x2 y2]=cutTracers(lon,lat,Xres,Yres,X1,Y1,190,200,0,10);
%  [x3 y3]=cutTracers(lon,lat,Xres,Yres,X1,Y1,200,210,0,10);

%  [x4 y4]=cutTracers(lon,lat,Xres,Yres,X1,Y1,180,190,10,20);
%  [x5 y5]=cutTracers(lon,lat,Xres,Yres,X1,Y1,190,200,10,20);
%  [x6 y6]=cutTracers(lon,lat,Xres,Yres,X1,Y1,200,210,10,20);


  sp=1;
  wid=50;

%  lon0=900;     %% res: 0.01
%  lat0=250;

  lon0=170;     %% res: 0.05
  lat0=30;




%  lon0=4000;    %% above the islands
%  lat0=1750;    %% above the islands
  
%  lon0=5800;
%  lat0=2080;

%  lon0=5650;
%  lat0=1900;

  %%%%%%%% AVISO  %%%%%%%%
%  lon0=3990;    %% above the islands
%  lat0=2210;    %% above the islands

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
  h=plot(x1,y1,'.k',x2,y2,'.y',x3,y3,'.g',x4,y4,'.c',x5,y5,'.b',x6,y6,'.r',mx,my,'om');
  set(h,{'markers'},{marsize;marsize;marsize;marsize;marsize;marsize;2});
  set(h,{'MarkerFaceColor'},{[0 0 0];[1 1 0];[0 1 0];[0 1 1];[0 0 1];[1 0 0];[1 0 1]})
  xlim([186 211]);    % Islands
  ylim([16 30]);      % Islands
%  xlim([260 330]);   %GulfStream
%  ylim([15 50]);     %GulfStream 
%  xlim([0 360]);
%  ylim([-90 90]);
  title(strcat(matdate,' (Global)'));
  xlabel('Longitude');
  ylabel('Latitude');
  daspect([1,1,1])
  %axis equal

%{
  hold on
  plot(mx,my,'.','Color',[0.1 0.1 0.1],'markers',marsize); 
  plot(x1,y1,'.','Color','k','markers',marsize);
  plot(x2,y2,'.','Color','y','markers',marsize);
  plot(x3,y3,'.','Color','g','markers',marsize);
  plot(x4,y4,'.','Color','r','markers',marsize);
  plot(x5,y5,'.','Color','b','markers',marsize);
  plot(x6,y6,'.','Color','m','markers',marsize);
  hold off
%}  
%  title(matdate);
%  xlabel('Longitude');
%  ylabel('Latitude');
%%  xlim([0 360]);
%%  ylim([-70 70]);
%  xlim([140 260]);
%  ylim([1 45]);
%  daspect([1,1,1])
%  grid on
%  set(gca,'Xcolor','k','Ycolor','k','GridLineStyle','-.','LineWidth',1);  
  tracer_path=sprintf('/nobackup1/mdehghani/CS_Trunk/%10.10d/Lagrangian/FTLE/tracer/',run);
  if exist(tracer_path)~=7
    mkdir(tracer_path);
  end
  print('-dpng', '-r500', sprintf('%s%10.10d.png',tracer_path,field));

%  grid off


  %%%%%%%%%%%%%%%%%%%%%%  vphase plot   %%%%%%%%%%%%%%%%%%%%%%%
  phi=atan0_2pi(interpV,interpU);
  imagesc(lon,lat,phi');
  axis xy;
  %colorbar;
  title(strcat(matdate,' (Global)'));
  xlabel('Longitude');
  ylabel('Latitude');
  daspect([1 1 1])
  print('-dpng', '-r500', sprintf('%s%s%10.10d.png',tracer_path,'vphase_',field));
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

end


end


function t=atan0_2pi(y,x)
t = Inf*x; %atan(y./x);

con = x>0 & y>=0;
t(con) = atan(y(con)./x(con));

con = x==0 & y>0;
t(con) = pi/2;

con = x<0;
t(con) = atan(y(con)./x(con)) + pi;

con = x==0 & y<0;
t(con) = 3*pi/2;

con = x>0 & y<0;
t(con) = atan(y(con)./x(con)) + 2*pi;

%con = x==0 & y==0;
%t(con) = 0;

t = 180 * t /pi;
end
