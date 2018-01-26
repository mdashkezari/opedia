
function gen_chl_MODIS(itnums)
	addpath(genpath('~/matbox/CS'));
	Res = 0.01;

	for itnum = itnums
		disp(itnum);
		path = get_path(itnum);
		[lon lat data] = get_data(path, 0);
		data=double(data);
		data(find(abs(data)>=30768))=NaN;

		d2=data(1+size(data,1)/2 : end, :);
		d1=data(1:size(data,1)/2, :);
		data=vertcat(d2,d1);
		data=fliplr(data);

		d2=lon(1+size(lon,1)/2 : end, :);  
		d1=lon(1:size(lon,1)/2, :);  
		lon=vertcat(d2,d1);
		lon(lon<0) = lon(lon<0)+360;		

		lat = flipud(lat);
		[LON,LAT]=meshgrid(lon,lat);
		min_lon=min(lon);
		max_lon=max(lon);
		min_lat=min(lat);
		max_lat=max(lat);

    		X=(min_lon):Res:(max_lon);
    		Y=(min_lat):Res:(max_lat);
		[X,Y]=meshgrid(X,Y);


		data=interpolate(LON,LAT,data',X,Y);


    		rows=2;
    		cols=4;
    		dh=(size(data,1)-20)/rows;
    		dw=(size(data,2)-20)/cols;
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

        			chl=data(1+(i-1)*dh:row_end, 1+(j-1)*dw:col_end);
	        		col=size(chl,2);
        			row=size(chl,1);
        			save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/chl/chl_%10.10d_%d_%d.mat',itnum,i,j), 'chl', 'itnum', 'Res', 'col', 'row');
      			end
    		end
	end
end



function [path] = get_path(itnum)
	path = '/nobackup1/mdehghani/obs/CHL/MODIS-Aqua/Mapped/8Day/4km/chl_%d.nc';
	itnum = floor((itnum-1)/8)*8 +1;
	path = sprintf(path, itnum);
end


function [lon lat data]=get_data(path, channel)
  ncid=netcdf.open(path);
  lon=netcdf.getVar(ncid,2);
  lat=netcdf.getVar(ncid,1);
  data=netcdf.getVar(ncid,channel);

%[numdims,numvars,numglobalatts,unlimdimid] = netcdf.inq(ncid)    
%[name,xtype,dimids,natts] = netcdf.inqVar(ncid,0);
%varid = netcdf.inqVarID(ncid,'chlor_a');
%attname = netcdf.inqAttName(ncid,varid,11)
%attval = netcdf.getAtt(ncid,varid,attname)
end
