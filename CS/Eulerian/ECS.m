
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Okubo Weiss %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%[iU]=interpolate(LON,LAT,U',X0,Y0); 
%[iV]=interpolate(LON,LAT,V',X0,Y0);
earth_radius = 6400 * 1000;
deg_to_rad = pi / 180;

%XC=getXC;
%YC=getYC;
%deltaXC = (XC(2:end,2:end)-XC(2:end,1:end-1)) * earth_radius * deg_to_rad;
%deltaYC = (YC(2:end,2:end)-YC(1:end-1,2:end)) * earth_radius * deg_to_rad;

sat_res_lon = get_lon_obs(DataSource, lonLabel, latLabel);
sat_res_lat = get_lat_obs(DataSource, lonLabel, latLabel);
sat_res_lon = sat_res_lon(2) - sat_res_lon(1);
sat_res_lat = sat_res_lat(2) - sat_res_lat(1);

deltaXC = (sat_res_lon) * earth_radius * deg_to_rad;
deltaYC = (sat_res_lat) * earth_radius * deg_to_rad;

[OW,sn,ss,vort]=Okubo_Weiss(U',V',deltaXC,deltaYC);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

OW=OW';
vort=vort';

%%%%%%%% Duplicating the first row and column. 
%%%%%%%% This is to match the size of U/V/ftle matrices
vort = vertcat(vort(1,:), vort);
vort = horzcat(vort(:,1), vort);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
