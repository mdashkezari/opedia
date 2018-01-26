function temp()

itnums = [1993001:1993365, 1994001:1994365, 1995001:1995365, 1996001:1996366, 1997001:1997365, 1998001:1998365, 1999001:1999365, 2000001:2000366, 2001001:2001365, 2002001:2002365, 2003001:2003365, 2004001:2004366, 2005001:2005365, 2006001:2006365, 2007001:2007365, 2008001:2008366, 2009001:2009365, 2010001:2010365, 2011001:2011365, 2012001:2012366, 2013001:2013365, 2014001:2014365, 2015001:2015254];

for itnum=itnums
	%path=strcat('/nobackup1/mdehghani/obs/AVISO/ssh/sla_ssh_AVISO_',sprintf('%7.7d',itnum),'.nc');
	%path=strcat('/nobackup1/mdehghani/obs/AVISO/uv_anomally/uv_sla_AVISO_',sprintf('%7.7d',itnum),'.nc');
	%path=strcat('/nobackup1/mdehghani/CS_Trunk/ML/vphase/vphase_2pi_',sprintf('%10.10d',itnum),'.mat');
	path=strcat('/nobackup1/mdehghani/CS_Trunk/ML/identified_eddies/',sprintf('%10.10d',itnum),'.npz');
	if exist(path, 'file') ~= 2
		disp(num2str(itnum))
end

end 

%{
path=strcat('/nobackup1/mdehghani/obs/AVISO/ssh/sla_ssh_AVISO_',sprintf('%7.7d',itnum),'.nc'); 
ncid=netcdf.open(path);   % path: path of the netcdf file

%%%%  general info about the file structure  %%%%%%%

[numdims,numvars,numglobalatts,unlimdimid] = netcdf.inq(ncid)    

[name,xtype,dimids,natts] = netcdf.inqVar(ncid,channel)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%data=netcdf.getVar(ncid,channel);   % data extraction
%}

