
function [GridX2,GridY2,Ux,Vy]=Propagate_RK4(LON,LAT,U,V,GridX1,GridY1,Tstep_sec,forward)

interp_method='linear';
% 1 degree longitude and latitude in meters
dx=111180*cos(GridY1*pi/180);
dy=111180;

if forward==false 
    dir=-1;
else
    dir=1;
end


iu1=interp2(LON,LAT,U',GridX1,GridY1,interp_method);
iv1=interp2(LON,LAT,V',GridX1,GridY1,interp_method);
iu1(isnan(iu1)==1)=0;
iv1(isnan(iv1)==1)=0;

iu2=interp2(LON,LAT,U',GridX1+dir*(Tstep_sec*iu1./dx)/2,GridY1+dir*(Tstep_sec*iv1/dy)/2,interp_method);
iv2=interp2(LON,LAT,V',GridX1+dir*(Tstep_sec*iu1./dx)/2,GridY1+dir*(Tstep_sec*iv1/dy)/2,interp_method);
iu2(isnan(iu2)==1)=0;
iv2(isnan(iv2)==1)=0;

iu3=interp2(LON,LAT,U',GridX1+dir*(Tstep_sec*iu2./dx)/2,GridY1+dir*(Tstep_sec*iv2/dy)/2,interp_method);
iv3=interp2(LON,LAT,V',GridX1+dir*(Tstep_sec*iu2./dx)/2,GridY1+dir*(Tstep_sec*iv2/dy)/2,interp_method);
iu3(isnan(iu3)==1)=0;
iv3(isnan(iv3)==1)=0;

iu4=interp2(LON,LAT,U',GridX1+dir*(Tstep_sec*iu3./dx),GridY1+dir*(Tstep_sec*iv3/dy),interp_method);
iv4=interp2(LON,LAT,V',GridX1+dir*(Tstep_sec*iu3./dx),GridY1+dir*(Tstep_sec*iv3/dy),interp_method);
iu4(isnan(iu4)==1)=0;
iv4(isnan(iv4)==1)=0;

Ux=(iu1+2*iu2+2*iu3+iu4)/6;
Vy=(iv1+2*iv2+2*iv3+iv4)/6;
GridX2=GridX1+dir*Tstep_sec*(Ux)./dx;
GridY2=GridY1+dir*Tstep_sec*(Vy)./dy;

