function plot_traj_grad2(run,itnum_start,day_of_year,year,dir,range)


[mx,my]=get_global_mask_AVISO;

for field=range
  disp(['field= ',num2str(field)])
  stamp=doy2date(day_of_year,year);
  stamp=addtodate(stamp,dir*(field-1),'day');
  matdate=datestr(stamp,'mmm dd yyyy'); 
  load(sprintf('F:/Mohammad/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat',run,itnum_start,field));
  
  sp=1;
  wid=50;

  lon0=4975;    %% above the islands
  lat0=3025;    %% Transition Zone
  %lat0=2800;    % South
  %lat0=3200;    % North
  

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

  xlim([190 220]);    % Islands
  ylim([18 45]);      % Islands

  title(strcat(matdate,' (Global)'));
  xlabel('Longitude');
  ylabel('Latitude');
  daspect([1,1,1])
  %axis equal

 
  tracer_path=sprintf('F:/Mohammad/CS_Trunk/%10.10d/Lagrangian/FTLE/tracer/',run);
  if exist(tracer_path)~=7
    mkdir(tracer_path);
  end
  print('-dpng', '-r500', sprintf('%s%10.10d.png',tracer_path,field));

%  grid off

end


end


