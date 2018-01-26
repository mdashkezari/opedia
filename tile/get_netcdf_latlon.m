function [data] = get_netcdf_latlon(path, channel)
	ncid=netcdf.open(path);
	%ncdisp(path)
	data=double(netcdf.getVar(ncid, channel));  
end
