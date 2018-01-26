
function vphase(run,itnum_start,range);

for field=range
  disp(['field: ' int2str(field)])
%{
  %U=getU_obs('AVISO',field);
  %V=getV_obs('AVISO',field);

  load(sprintf('/nobackup1/mdehghani/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat',run,itnum_start,field));
%  U=interp2(LON,LAT,U',X1,Y1,'lipear');
%  V=interp2(LON,LAT,V',X1,Y1,'linear');
 
  histogram2(X1,Y1,100,'FaceColor','flat');
%  c=cat(2,X1(:),Y1(:));
%  hist3(c,[100,100]);
  xlim([190 205]) 
  ylim([17 27])
  zlim([0 200])

  phase=atan0_2pi(V,U);
%  imagesc(phase');
%  axis xy;
%  colorbar;
%  daspect([1 1 1])
  drawnow
%}



%load(path); 
load(sprintf('/nobackup1/mdehghani/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat',run,itnum_start,field));
t=atan0_2pi(interpV,interpU); 
imagesc(lon,lat,t'); 
axis xy; 
colorbar; 
daspect([1 1 1])
drawnow

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


