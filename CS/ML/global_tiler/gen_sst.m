

function gen_sst(itnums);

  for itnum=itnums
    disp(itnum);
    path = sprintf('/nobackup1/mdehghani/obs/SST/MURSST/sst_%d.nc', itnum);
    [lon lat sst]=get_data(path, 3);

    sst=double(sst);
    sst(find(abs(sst)>=32768))=NaN;
    sst = sst /1000;
    sst = sst + 298.19;
    sst = sst - 273.15;    %% Kelvin to Celcius
    %plot_data(lon,lat,sst);
    %save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/sst/sst_%10.10d.mat',itnum), 'sst', 'lon', 'lat');


    d2=sst(1+size(sst,1)/2 : end, :);
    d1=sst(1:size(sst,1)/2, :);
    sst=vertcat(d2,d1);
    %sst=fliplr(sst);

    d2=lon(1+size(lon,1)/2 : end, :);
    d1=lon(1:size(lon,1)/2, :);
    lon=vertcat(d2,d1);
    lon(lon<0) = lon(lon<0)+360;
    	


    data=sst';
    rows=2;
    cols=4;
    dh=(size(data,1)+1)/rows;
    dw=size(data,2)/cols;
    for i=1:rows
      for j=1:cols
	if i==1
          sst=data(1+(i-1)*dh:i*dh, 1+(j-1)*dw:j*dw);
	else
          sst=data(1+(i-1)*dh:end, 1+(j-1)*dw:j*dw);
	end
        save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/sst/sst_%10.10d_%d_%d.mat',itnum,i,j), 'sst', 'lon', 'lat');
      end
    end

  end

end




function [lon lat data]=get_data(path, channel)
  ncid=netcdf.open(path);
  lon=netcdf.getVar(ncid,2);
  lat=netcdf.getVar(ncid,1);
  data=netcdf.getVar(ncid,channel);
end




function plot_data(lon,lat,data)
  imagesc(lon,lat,data');
  colorbar;
  axis xy;
  title({'Temperatuer MUR SST'})

  xt=get(gca,'xtick');
  for k=1:numel(xt);
  xt1{k}=sprintf('%d°',xt(k));
  end
  set(gca,'xticklabel',xt1);
  yt=get(gca,'ytick');
  for k=1:numel(yt);
  yt1{k}=sprintf('%d°N',yt(k));
  end
  set(gca,'yticklabel',yt1);

  %caxis([-.4e4 .4e4])
end
