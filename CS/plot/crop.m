
clon=lon;
clat=lat;

if flgEulerian
  [clon clat OW]=crop_map(lon,lat,Xres,Yres,crop_lon1,crop_lon2,crop_lat1,crop_lat2,OW);
  [clon clat vort]=crop_map(lon,lat,Xres,Yres,crop_lon1,crop_lon2,crop_lat1,crop_lat2,vort);
end

if flgLagrangian
  [clon clat displacement]=crop_map(lon,lat,Xres,Yres,crop_lon1,crop_lon2,crop_lat1,crop_lat2,displacement);
  [clon clat ftle]=crop_map(lon,lat,Xres,Yres,crop_lon1,crop_lon2,crop_lat1,crop_lat2,ftle);
  [clon clat seized]=crop_map(lon,lat,Xres,Yres,crop_lon1,crop_lon2,crop_lat1,crop_lat2,seized);
  if flgDispersion
    [clon clat dispersion]=crop_map(lon,lat,Xres,Yres,crop_lon1,crop_lon2,crop_lat1,crop_lat2,dispersion);
  end
end




%%%%%%%%%%%%%%%%%%%%%%%%% These should be the last lines! %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lon=clon;
lat=clat;

