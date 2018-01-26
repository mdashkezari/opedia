
function TileAVISO_REP_Vort_SLA(itnums,Xres,Yres)
  save_path = '/nfs/micklab004/mdehghani/opedia_vault/tile/obs/rep/vort_adt/rep_vort_adt_%10.10d_%d_%d.mat';	
  base_path = '/nfs/micklab004/mdehghani/opedia_vault/raw/obs/rep/uv_adt/rep_uv_adt_';
  lon_channel = 4;
  lat_channel = 5;
  V_channel = 1;
  U_channel = 2;
  path = strcat(base_path,sprintf('%7.7d',itnums(1)),'.nc');
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

  for itnum=itnums
    disp([num2str(itnum)])
    path=strcat(base_path,sprintf('%7.7d',itnum),'.nc');
    V = get_netcdf_UV(path, V_channel);	
    U = get_netcdf_UV(path, U_channel);     
    U=interpolate(LON,LAT,U',X,Y);
    V=interpolate(LON,LAT,V',X,Y);
    [W,sn,ss,vort] = Okubo_Weiss(U,V,Xres,Yres);
    %col=size(vort,2);
    %row=size(vort,1);	
    %save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/vort/vorticity_%10.10d.mat',itnum), 'vort', 'itnum', 'Xres', 'col', 'row');	
    %%plot_vort(lon,lat,vort,{'Vorticity',date_str});


    data=vort;
    rows=2;
    cols=4;
    dh=(size(data,1)+1)/rows;
    dw=(size(data,2)+1)/cols;
    for i=1:rows
      for j=1:cols
	row_end=i*dh;
	if row_end>size(data,1)
	  row_end=size(data,1);
	end
	
	col_end=j*dw;
        if col_end>size(data,2)
          col_end=size(data,2);
        end

        vort=data(1+(i-1)*dh:row_end, 1+(j-1)*dw:col_end);
        col=size(vort,2);
        row=size(vort,1);
	save(sprintf(save_path,itnum,i,j), 'vort', 'itnum', 'Xres', 'col', 'row');
      end
    end
  end
%  print('-dpng', '-r500', sprintf('pics/vorticity_%10.10d.png',itnum))
end


function plot_vort(lon,lat,vort,ti)
%colormap jet;
imagesc(360-lon,lat,vort);
%imagesc(vort);
axis xy;
set(gca,'XDir','reverse');
%caxis([-1.5 1.5])
colormap(b2r(-1.8,1.8));
colorbar;
title(ti);
daspect([1 1 1]);
drawnow; 
end
