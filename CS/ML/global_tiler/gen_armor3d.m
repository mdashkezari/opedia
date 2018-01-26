
function gen_armor3d(itnums)

  Xres=0.01;
  Yres=0.01;
  addpath(genpath('~/matbox/CS'));

  %lon=get_lon_obs(DataSource);
  %lat=get_lat_obs(DataSource);
  [lon lat ssh U V T S depth]=get_armor3d_dt(itnums(1));    

  [LON,LAT]=meshgrid(lon,lat);
  min_lon=min(lon);
  max_lon=max(lon);
  min_lat=min(lat);
  max_lat=max(lat);

  X=(min_lon):Xres:(max_lon);
  Y=(min_lat):Yres:(max_lat);
  [X,Y]=meshgrid(X,Y);

  for itnum=itnums
    disp([num2str(itnum)])
    [lon lat ssh U V T S depth]=get_armor3d_dt(itnum); 
    mld=mixed_layer_depth(T, depth);	

    rows=2;
    cols=4;

    mld=interpolate(LON,LAT,mld',X,Y);
    data=mld;
    dh=size(data,1)/rows;
    dw=size(data,2)/cols;
    for i=1:rows
      for j=1:cols
        mld=data(1+(i-1)*dh:i*dh, 1+(j-1)*dw:j*dw);
        col=size(ssh,2);
        row=size(ssh,1);
        %save(sprintf('/nfs/micklab004/mdehghani/opedia_vault/tile/obs/rep/armor3d/rep_armor3d_mld_%10.10d_%d_%d.mat',itnum,i,j), 'mld', 'itnum', 'Xres', 'col', 'row');
        save(sprintf('/nobackup1/mdehghani/obs/armor3d/rep_armor3d_mld_%10.10d_%d_%d.mat',itnum,i,j), 'mld', 'itnum', 'Xres', 'col', 'row');
      end
    end
    data=[]; 
    mld=[];



    S=S(:,:,1);	
    S=interpolate(LON,LAT,S',X,Y);
    data=S;
    dh=size(data,1)/rows;
    dw=size(data,2)/cols;
    for i=1:rows
      for j=1:cols
        S=data(1+(i-1)*dh:i*dh, 1+(j-1)*dw:j*dw);
        col=size(ssh,2);
        row=size(ssh,1);
        %save(sprintf('/nfs/micklab004/mdehghani/opedia_vault/tile/obs/rep/armor3d/rep_armor3d_salinity_%10.10d_%d_%d.mat',itnum,i,j), 'S', 'itnum', 'Xres', 'col', 'row');
        save(sprintf('/nobackup1/mdehghani/obs/armor3d/rep_armor3d_salinity_%10.10d_%d_%d.mat',itnum,i,j), 'S', 'itnum', 'Xres', 'col', 'row');
      end
    end
    data=[]; 
    S=[];


%{
    %%% will not be used for now. remember U and V maps are also available!


    T=T(:,:,1);
    T=interpolate(LON,LAT,T',X,Y);
    data=T;
    dh=size(data,1)/rows;
    dw=size(data,2)/cols;
    for i=1:rows
      for j=1:cols
        T=data(1+(i-1)*dh:i*dh, 1+(j-1)*dw:j*dw);
        col=size(ssh,2);
        row=size(ssh,1);
        save(sprintf('/nfs/micklab004/mdehghani/opedia_vault/tile/obs/rep/armor3d/rep_armor3d_temperature_%10.10d_%d_%d.mat',itnum,i,j), 'T', 'itnum', 'Xres', 'col', 'row');
      end
    end
    data=[];
    T=[];

 
    ssh=ssh(:,:,1);
    ssh=interpolate(LON,LAT,ssh',X,Y);
    data=ssh;
    dh=size(data,1)/rows;
    dw=size(data,2)/cols;
    for i=1:rows
      for j=1:cols
        height_above_geoid=data(1+(i-1)*dh:i*dh, 1+(j-1)*dw:j*dw);
        col=size(ssh,2); 
        row=size(ssh,1);
        save(sprintf('/nfs/micklab004/mdehghani/opedia_vault/tile/obs/rep/armor3d/rep_armor3d_heigh_above_geoid_%10.10d_%d_%d.mat',itnum,i,j), 'height_above_geoid', 'itnum', 'Xres', 'col', 'row');
      end
    end
    data=[];
    ssh=[];
    height_above_geoid=[];
	
%}

  end

end





function [lon lat SSH U V T S depth]=get_armor3d_dt(itnum)    % SSH: height above goid
path=strcat('/nfs/micklab004/mdehghani/opedia_vault/raw/obs/rep/armor3d/rep_armor3d_',sprintf('%7.7d',itnum),'.nc');     
ncid=netcdf.open(path);


lon=double(netcdf.getVar(ncid,4));
lat=double(netcdf.getVar(ncid,5));


%%%%%%% height above geoid %%%%%%%%%%
SSH=double(netcdf.getVar(ncid,2));
SSH(find(abs(SSH)>32000))=NaN;   % _FillValue: 3.28e+04
SSH=SSH/1000;   % scale factor: 0.001 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%% UV %%%%%%%%%%%%%%%%%%
V=double(netcdf.getVar(ncid,3));
V(find(abs(V)>32000))=NaN;   % _FillValue: 3.28e+04
V=V/1000;   % scale factor: 0.001 

U=double(netcdf.getVar(ncid,0));
U(find(abs(U)>32000))=NaN;   % _FillValue: 3.28e+04
U=U/1000;   % scale factor: 0.001 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%% S %%%%%%%%%%%%%%%%%%%
S=double(netcdf.getVar(ncid,6));
S(find(abs(S)>32000))=NaN;   % _FillValue: 3.28e+04
S=S/1000;   % scale factor: 0.001 
S=S+20;   % add_offset: 20 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%% depth %%%%%%%%%%%%%%%%%
depth=double(netcdf.getVar(ncid,7));
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%% T %%%%%%%%%%%%%%%%%%%
T=double(netcdf.getVar(ncid,8));
T(find(abs(T)>32000))=NaN;   % _FillValue: 3.28e+04
T=T/1000;   % scale factor: 0.001 
T=T+20;   % add_offset: 20 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%% EXTENSION %%%%%%%%%%%%%%%%%	%%% >>>>  Adding extention to make it consistent with other maps
ext=(-89.75:0.25:-82.25)';
lat = cat(1, ext, lat);      

EXT=NaN*ones(size(T,1) ,size(ext,1), size(T,3));
T= cat(2, EXT, T);
S= cat(2, EXT, S);
U= cat(2, EXT, U);
V= cat(2, EXT, V);
SSH= cat(2, EXT, SSH);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

end





function [mld]=mixed_layer_depth(T, depth);

delT=T;
threshold=0.2;
reference_depth_index=2;   % reference: depth 10m
mld=T(:,:,1)*nan;

for z=1:size(T,3)
  delT(:,:,z)=abs(T(:,:,reference_depth_index)-T(:,:,z));  
end

for i=1:size(delT,1)
  for j=1:size(delT,2)
    for z=reference_depth_index+1:size(delT,3)
      if (delT(i,j,z)>=threshold) && (isnan(mld(i,j)))
        a=(depth(z)-depth(z-1)) / (delT(i,j,z)-delT(i,j,z-1));
        b=depth(z)-a*delT(i,j,z);
        mld(i,j)=a*threshold+b;

        if isnan(mld(i,j))
          mld(i,j)=nanmean(depth(z-1), depth(z));	
        end 
      end

    end
  end
end
  
end



function plot_ssh(lon,lat,data,ti)
%colormap jet;
imagesc(data');
axis xy;
%set(gca,'XDir','reverse');
%caxis([-1.5 1.5])       % height above geoid
%caxis([30 40])       % salinity
caxis([0 250])       % mld
colorbar;
title(ti);
daspect([1 1 1]);
drawnow;
end
