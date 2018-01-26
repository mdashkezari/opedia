

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%                                                                Compute_CS.m  

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  inputs   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%   observation     if true the flow fields from observations are used, otherwise the flow fields of MITgcm are used  
%
%   stop_time:      The period over which the advection continues (s)
%
%   T:              Total advection time at each flow field (s)
%
%   t_step:         Advection time step (s)
%
%   itnum_start:    The iteration number of the first flow field file
%
%   itnum_steop:    Difference between two sequential iteration numbers
%
%   itnum_end:      The iteration number of the last available flow field file
%
%   Xres, Yres:     Spatial resolution used tracer grid (degree) 
%
%   forward:        Determines the direction of the temporal integration. (backward (false), forward (true))
%                                                                                                                           
%   method:         Integration method (Euler (1), Runge-Kutta4 (2))                                                        
%                                                                                                                           
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


if observation
 % [lon lat temp]=get_obs(1,1);
  lon=get_lon_obs(DataSource, lonLabel, latLabel);
  lat=get_lat_obs(DataSource, lonLabel, latLabel);
else 
  lon=get_lon;
  lat=get_lat;
end


[LON,LAT]=meshgrid(lon,lat);
min_lon=min(lon);
max_lon=max(lon);
min_lat=min(lat);
max_lat=max(lat);


disp('Dimensions of the domain under study:')
disp(' ')
disp('=====================================================================')
disp(sprintf('Longitude: %.3f - %.3f degrees',min_lon,max_lon))
disp(sprintf('Latitude: %.3f - %.3f degrees',min_lat,max_lat))
disp(' ')
w=111180*cos(max_lat*pi/180)*(max_lon-min_lon);
disp([sprintf('Width at higher latitude: %.2f', w/1000), ' km'])
w=111180*cos(min_lat*pi/180)*(max_lon-min_lon);
disp([sprintf('Width at lower latitude: %.2f', w/1000), ' km'])
w=111180*(max_lat-min_lat);
disp([sprintf('Height: %.2f', w/1000), ' km'])
disp('=====================================================================')
disp(' ')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% define the initial tracer grid which will be advected by the flow

if Xres & Yres
    X=(min_lon):Xres:(max_lon);
    Y=(min_lat):Yres:(max_lat);
else 
    %the horizontal resolution of the input data is used
    X=lon; Y=lat;
end

nx=length(X);
ny=length(Y);
[X,Y]=meshgrid(X,Y);
X0=X'; 
Y0=Y';
X1=X0; 
Y1=Y0;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Eulerian %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if flgEulerian
  if observation
    %V=getV_obs(DataSource,itnum_start);
    %U=getU_obs(DataSource,itnum_start);
    V=getV_obs(DataSource,itnum_start, lonLabel, latLabel, vLabel);
    U=getU_obs(DataSource,itnum_start, lonLabel, latLabel, uLabel);
  else
    V=-1.*getU(itnum_start)';
    U=getV(itnum_start)';
  end

  ECS;                    % Eulerian Coherent Structures (ESC)  
end  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Lagrangian %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if flgLagrangian
  LCS;                    % Lagrangian Coherent Structures (LCS)
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


