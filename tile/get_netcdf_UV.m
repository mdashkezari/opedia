function [data] = get_netcdf_UV(path, channel)
	ncid=netcdf.open(path);
	%ncdisp(path)
	data=double(netcdf.getVar(ncid, channel));  
	data(find(abs(data)>2147483646))=NaN;
	data=data/10000;
	data(find(abs(data)>10))=0;
end
