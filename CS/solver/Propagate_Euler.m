
function [GridX2,GridY2,Ux,Vy]=Propagate_Euler(LON,LAT,U,V,GridX1,GridY1,Tstep_sec,forward)

interp_method='linear';
% interpolate velocity on the tracer grid
Ux=interp2(LON,LAT,U',GridX1,GridY1,interp_method);
Ux(isnan(Ux)==1)=0;
Vy=interp2(LON,LAT,V',GridX1,GridY1,interp_method);
Vy(isnan(Vy)==1)=0;


if forward==false 
    dir=-1;
else
    dir=1;
end
    
% compute new coordinates of the tracer points as they are advected by
% the flow; the displacements are converted from meters to degrees (1
% degree at the equator equals about 111180 m)

GridX2=GridX1+dir*Ux*Tstep_sec./(111180*cos(GridY1*pi/180));
GridY2=GridY1+dir*Vy*Tstep_sec./111180;

