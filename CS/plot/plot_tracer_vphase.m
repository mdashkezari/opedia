function plot_tracer_vpahse(DataSource,run,itnum_start,day_of_year,year,dir,range)

%cc=hsv(15);
  if strcmp(DataSource,'AVISO')
    [mx,my]=get_global_mask_AVISO;
  elseif strcmp(DataSource,'CCRA')
    [mx,my]=get_global_mask_CCAR;
  end

  colormap jet
for field=range
  disp(['field= ',num2str(field)])
  %start_date='04-10-2015';
%  stamp=datenum(start_date);
  stamp=doy2date(day_of_year,year);
  stamp=addtodate(stamp,dir*(field-1),'day');
  matdate=datestr(stamp,'mmm dd yyyy'); 
  
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat',run,itnum_start,field));

  phase=atan0_2pi(interpV,interpU);

  X1=X1(1:2:end,1:2:end);
  Y1=Y1(1:2:end,1:2:end);
  phase=phase(1:2:end,1:2:end);;

  x1=X1(:);
  y1=Y1(:);
  p1=phase(:);

%{  
  %%%%% Cut HOT Area  %%%%%%%%
  sp=1;
  wid=100;

%  lon0=900;     %% res: 0.01
%  lat0=250;

  lon0=180;     %% res: 0.05
  lat0=40;
  %%%%%%%%%%%%%%%%%%%%%%%%

  n=1;
  m=1;
  X2=X1((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid));
  Y2=Y1((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid));
  P2=phase((lon0+(n-1)*wid):sp:(lon0+n*wid),(lat0+(m-1)*wid):sp:(lat0+m*wid));
  x1=X2(:);
  y1=Y2(:);
  p1=P2(:);

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
%}
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  marsize=2;
%  h=plot(x1,y1,'.k',x2,y2,'.y',x3,y3,'.g',x4,y4,'.c',x5,y5,'.b',x6,y6,'.r',mx,my,'om');
%  set(h,{'markers'},{marsize;marsize;marsize;marsize;marsize;marsize;2});
%  set(h,{'MarkerFaceColor'},{[0 0 0];[1 1 0];[0 1 0];[0 1 1];[0 0 1];[1 0 0];[1 0 1]})

  scatter(x1,y1,marsize,p1,'o','filled');

  xlim([186 211]);    % Islands
  ylim([16 30]);      % Islands
%  xlim([260 330]);   %GulfStream
%  ylim([15 50]);     %GulfStream 
%  xlim([0 360]);
%  ylim([-90 90]);
  title(strcat(matdate,' (Global)'));
  colorbar;
  xlabel('Longitude');
  ylabel('Latitude');
  daspect([1,1,1])
  %axis equal

  tracer_path=sprintf('/nobackup1/mdehghani/CS_Trunk/%10.10d/Lagrangian/FTLE/tracer/',run);
  if exist(tracer_path)~=7
    mkdir(tracer_path);
  end
  drawnow
  print('-dpng', '-r500', sprintf('%s%s%10.10d%s%10.10d.png',tracer_path,'tracer_vphase_',itnum_start,'_',field));
  
%  grid off

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
