

function gen_Lagrangian(its)
	Res = 0.01;	
	addpath(genpath('~/matbox/CS'));
	for it=its
		disp(it);
		path = sprintf('/nobackup1/mdehghani/CS_Trunk/0002015240/Lagrangian/MAT/%10.10d.mat',it);
		load(path);

		lon=(min_lon):Xres:(max_lon);
		lat=(min_lat):Yres:(max_lat);
		[LON,LAT]=meshgrid(lon,lat);
		min_lon=min(lon);
		max_lon=max(lon);
		min_lat=min(lat);
		max_lat=max(lat);
		X=(min_lon):Res:(max_lon);
		Y=(min_lat):Res:(max_lat);
		[X,Y]=meshgrid(X,Y);

%imagesc(ftle'); axis xy; caxis([0.01,0.4]);
		ftle=interpolate(LON,LAT,ftle',X,Y);
		displacement=interpolate(LON,LAT,displacement',X,Y);
%		ftle=ftle';
%		displacement=displacement';
%figure; imagesc(ftle'); axis xy; caxis([0.01,0.4]);

		%%%%%%%%%%%%%%%%%  Breaking into the "tiles". If you want one single tile, comment this section and uncomment the section below %%%%%%%%%%%%%%
		data=ftle;
		data2=displacement;
		rows=2;
		cols=4;
		dh=(size(data,1)+3)/rows;
		dw=(size(data,2)+3)/cols;
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
		
			ftle=data(1+(i-1)*dh:row_end, 1+(j-1)*dw:col_end);
			displacement=data2(1+(i-1)*dh:row_end, 1+(j-1)*dw:col_end);
        		save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/ftle/ftle_%10.10d_%d_%d.mat',it,i,j),'ftle')
			save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/displacement/displacement_%10.10d_%d_%d.mat',it,i,j),'displacement')
		  end
		end
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	end	

end
