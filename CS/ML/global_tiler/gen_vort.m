
function gen_vort(DataSource,itnums,Xres,Yres)
%function gen_vort(itnums,Xres,Yres)

  addpath(genpath('~/matbox/CS'));

  lon=get_lon_obs(DataSource);
  lat=get_lat_obs(DataSource);


  [LON,LAT]=meshgrid(lon,lat);
  min_lon=min(lon);
  max_lon=max(lon);
  min_lat=min(lat);
  max_lat=max(lat);

  if Xres & Yres
%    X=ceil(min_lon):Xres:fix(max_lon);
%    Y=ceil(min_lat):Yres:fix(max_lat);

    X=(min_lon):Xres:(max_lon);
    Y=(min_lat):Yres:(max_lat);
  else
    X=lon;
    Y=lat;
  end
  [X,Y]=meshgrid(X,Y);
%  lon=ceil(min_lon):Xres:fix(max_lon);
%  lat=ceil(min_lat):Yres:fix(max_lat);

  lon=(min_lon):Xres:(max_lon);
  lat=(min_lat):Yres:(max_lat);

  for itnum=itnums
    disp([num2str(itnum)])

    %%%%%%%	
    %itnum_str = num2str(itnum);
    %year = str2num(itnum_str(1:4));
    %day_of_year = str2num(itnum_str(5:end));
    %stamp=doy2date(day_of_year,year);
    %date_str=datestr(stamp,'mmm dd yyyy');
    %%%%%%%%%%


    V=getV_obs(DataSource,itnum);
    U=getU_obs(DataSource,itnum);

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
	save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/vort/vorticity_%10.10d_%d_%d.mat',itnum,i,j), 'vort', 'itnum', 'Xres', 'col', 'row');
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
