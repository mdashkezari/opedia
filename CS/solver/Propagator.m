function [X2,Y2,Ux,Vy,seized]=Propagator(max_lon,min_lon,max_lat,min_lat,LON,LAT,U,V,T,Tstep,X1,Y1,seized,nx,ny,forward,method)


if method==1       
    [X2,Y2,Ux,Vy]=Propagate_Euler(LON,LAT,U,V,X1,Y1,Tstep,forward);
else
    [X2,Y2,Ux,Vy]=Propagate_RK4(LON,LAT,U,V,X1,Y1,Tstep,forward);
end

% if the tracer had previously left the domian, keep it standstill
X2(seized==1)=X1(seized==1);
Y2(seized==1)=Y1(seized==1); 

% if the tracer has left the domian just now
just_left=(X2-min_lon).*(X2-max_lon)>=0 | (Y2-min_lat).*(Y2-max_lat)>=0;
X2(just_left)=X1(just_left);
Y2(just_left)=Y1(just_left);
seized(just_left)=1;

