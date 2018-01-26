
function TileAVISO_REP_ADT(itnums,Xres,Yres)
  [lon lat ssh]=getAVISO_dt_adt(itnums(1));              %%%%   CHANGE TO NRT OR DT
  %[lon lat ssh]=getAVISO_nrt_adt(itnums(1));              %%%%   CHANGE TO NRT OR DT

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
    [lon lat ssh]=getAVISO_dt_adt(itnum);                   %%%%   CHANGE TO NRT OR DT
    %[lon lat ssh]=getAVISO_nrt_adt(itnum);                   %%%%   CHANGE TO NRT OR DT

    ssh=interpolate(LON,LAT,ssh',X,Y);
    %col=size(ssh,2);
    %row=size(ssh,1);   
    %save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/ssh/ssh_%10.10d.mat',itnum), 'ssh', 'itnum', 'Xres', 'col', 'row');
    %plot_ssh(lon,lat,ssh,{'SSH', num2str(itnum)});

    data=ssh;
    rows=2;
    cols=4;
    dh=size(data,1)/rows;
    dw=size(data,2)/cols;
    for i=1:rows
      for j=1:cols
        ssh=data(1+(i-1)*dh:i*dh, 1+(j-1)*dw:j*dw);
        col=size(ssh,2); 
        row=size(ssh,1);
        save(sprintf('/nfs/micklab004/mdehghani/opedia_vault/tile/obs/rep/adt/rep_adt_%10.10d_%d_%d.mat',itnum,i,j), 'ssh', 'itnum', 'Xres', 'col', 'row');
        %save(sprintf('/nfs/micklab004/mdehghani/opedia_vault/tile/obs/nrt/adt/nrt_adt_%10.10d_%d_%d.mat',itnum,i,j), 'ssh', 'itnum', 'Xres', 'col', 'row');
      end
    end

  end

end




function [lon lat SSH]=getAVISO_nrt_adt(itnum)
path=strcat('/nfs/micklab004/mdehghani/opedia_vault/raw/obs/nrt/adt/nrt_adt_',sprintf('%7.7d',itnum),'.nc');
ncid=netcdf.open(path);

%[numdims,numvars,numglobalatts,unlimdimid] = netcdf.inq(ncid)   
%[name,xtype,dimids,natts] = netcdf.inqVar(ncid,3);
%for i=1:natts
%  attname = netcdf.inqAttName(ncid,3,i)
%  attval = netcdf.getAtt(ncid,3,attname)
%end

lon=double(netcdf.getVar(ncid,4));
lat=double(netcdf.getVar(ncid,2));

SSH=double(netcdf.getVar(ncid,7));  
SSH(find(abs(SSH)>50000))=NaN;
SSH=SSH/10000;
end



function [lon lat SSH]=getAVISO_dt_adt(itnum)
path=strcat('/nfs/micklab004/mdehghani/opedia_vault/raw/obs/rep/adt/rep_adt_',sprintf('%7.7d',itnum),'.nc');
ncid=netcdf.open(path);
%[numdims,numvars,numglobalatts,unlimdimid] = netcdf.inq(ncid)   
%[name,xtype,dimids,natts] = netcdf.inqVar(ncid,3)

lon=double(netcdf.getVar(ncid,2));
lat=double(netcdf.getVar(ncid,4));

SSH=double(netcdf.getVar(ncid,3));
SSH(find(abs(SSH)>50000))=NaN;
SSH=SSH/10000;
end


function plot_ssh(lon,lat,ssh,ti)
%colormap jet;
imagesc(ssh);
axis xy;
%set(gca,'XDir','reverse');
%caxis([0.7 1.3])	% >>>>>>  absoloute dynamic topography
caxis([-0.18 0.18])        %>>>>>>>>>  sea level anomaly
colorbar;
title(ti);
daspect([1 1 1]);
drawnow;
end
