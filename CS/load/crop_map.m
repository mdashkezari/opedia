function [lon lat map]=crop_map(lon,lat,Xres,Yres,lon_min_target,lon_max_target,lat_min_target,lat_max_target,map)
  min_lon=min(lon);
  max_lon=max(lon);
  min_lat=min(lat);
  max_lat=max(lat);
  lon=ceil(min_lon):Xres:fix(max_lon);
  lat=ceil(min_lat):Yres:fix(max_lat);
 
  [a lon_index_start]=min(abs(abs(lon-360)-lon_max_target));
  [a lon_index_end]=min(abs(abs(lon-360)-lon_min_target));
  [a lat_index_start]=min(abs(lat-lat_min_target));
  [a lat_index_end]=min(abs(lat-lat_max_target));

  lon=lon(lon_index_start:lon_index_end);
  lat=lat(lat_index_start:lat_index_end);
  map=map(lon_index_start:lon_index_end, lat_index_start:lat_index_end);

end
