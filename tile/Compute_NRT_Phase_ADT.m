
function phase = Compute_NRT_Phase_ADT(itnum,phase_range,Xres,Yres)
  save_path = '/nfs/micklab004/mdehghani/opedia_vault/tile/obs/nrt/phase_adt/nrt_phase_adt_%10.10d_%d_%d.mat';
  base_path = '/nfs/micklab004/mdehghani/opedia_vault/raw/obs/nrt/uv_adt/nrt_uv_adt_';
  lon_channel = 4;
  lat_channel = 2;
  V_channel = 8;
  U_channel = 7;
  path = strcat(base_path,sprintf('%7.7d',itnum),'.nc');
  lon = get_netcdf_latlon(path, lon_channel);
  lat = get_netcdf_latlon(path, lat_channel);

  [LON,LAT]=meshgrid(lon,lat);
  min_lon=min(lon);
  max_lon=max(lon);
  min_lat=min(lat);
  max_lat=max(lat);

  lon=(min_lon):Xres:(max_lon);
  lat=(min_lat):Yres:(max_lat);

  [X,Y]=meshgrid(lon,lat);

  V = get_netcdf_UV(path, V_channel);
  U = get_netcdf_UV(path, U_channel);

  U=interpolate(LON,LAT,U',X,Y);
  V=interpolate(LON,LAT,V',X,Y);
  phase=vPhase(U,V,phase_range);
  %plotPhase(phase,{'vPhase',num2str(itnum)});


  %%%%%%%%%%%%%%%%%  Breaking into the "tiles". If you want one single tile, comment this section and uncomment the section below %%%%%%%%%%%%%%
  data=phase;
  rows=2;
  cols=4;
  dh=size(data,1)/rows;
  dw=size(data,2)/cols;
  for i=1:rows
    for j=1:cols
	  if phase_range==2*pi
	    phase=data(1+(i-1)*dh:i*dh, 1+(j-1)*dw:j*dw);
	    save(sprintf(save_path,itnum,i,j),'phase','itnum','phase_range','Xres','Yres')
	  end
	
    end
  end
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

end


function plotPhase(phase,ti)
figure;
colormap jet;
imagesc(phase);
axis xy;
colorbar;
title(ti);
daspect([1 1 1]);
drawnow; 
grid on;
end
