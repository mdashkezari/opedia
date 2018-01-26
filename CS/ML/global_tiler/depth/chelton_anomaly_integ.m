function chelton_anomaly_integ(itnum)
	track = [];
	load('/nobackup1/mdehghani/CS_Trunk/ML/chelton_eddies/chelton_v4.mat');
	load('/nobackup1/mdehghani/CS_Trunk/ML/chelton_eddies/chelton_v4_yearDay.mat');
	yearDayn = yearDayn';
	lon(find(lon>360)) = lon(find(lon>360)) - 360;     % transform longitude to 0 - 360
	cyc = -1 * cyc; 				   % make polarity consistent with my database


        A = A(find(yearDayn==itnum));	
        L = L(find(yearDayn==itnum));
        U = U(find(yearDayn==itnum));
        cyc = cyc(find(yearDayn==itnum));
        j1 = j1(find(yearDayn==itnum));
        lat = lat(find(yearDayn==itnum));
        lon = lon(find(yearDayn==itnum));
        n = n(find(yearDayn==itnum));
        track = track(find(yearDayn==itnum));
	yearDayn = yearDayn(find(yearDayn==itnum));

	[armor_lon armor_lat ssh U V T S depth]=get_armor3d_dt(itnum);

	eddies = size(yearDayn,1);
	T_anomaly = NaN * ones(eddies, size(T,3));
	S_anomaly = NaN * ones(eddies, size(T,3));
	for i = 1:eddies
%		itnum = yearDayn(i);
%		[armor_lon armor_lat ssh U V T S depth]=get_armor3d_dt(itnum);
		[c lon_ind] = nanmin(abs(armor_lon - lon(i)));
                [c lat_ind] = nanmin(abs(armor_lat - lat(i)));

		edd_rad = round(L(i)/25);
		bkg_rad = round(200/25);

		for z = 1:size(T,3)
			T_anomaly(i, z) = get_anomaly(lon_ind, lat_ind, edd_rad, bkg_rad, T(:,:,z)); 					
                        S_anomaly(i, z) = get_anomaly(lon_ind, lat_ind, edd_rad, bkg_rad, S(:,:,z));
		end

	end


	clear armor_lon;
	clear armor_lat;
	clear ssh;
	clear U;
	clear V;
	clear T;
	clear S;

	save(sprintf('anomaly/%d.mat', itnum));
end




function [anomaly] = get_anomaly(lon_ind, lat_ind, edd_rad, bkg_rad, data);
	try
		r = edd_rad;
		x = data(lon_ind-r:lon_ind+r, lat_ind-r:lat_ind+r);
		edd = nanmean(x(:));

		r = bkg_rad;
		x = data(lon_ind-r:lon_ind+r, lat_ind-r:lat_ind+r);
		bkg = nanmean(x(:));

		anomaly = edd - bkg;
	catch
		anomaly = NaN;
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

end
