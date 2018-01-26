function plot_quiver(itnum, advec_time);

lon=get_lon;
lat=get_lat;
U=getU(itnum);
V=getV(itnum);
[LON LAT]=meshgrid(lon, lat);
[f s]=FTLE(itnum,advec_time);


figure; 
imagesc(lon,lat,f(:,:,1)'); 
title('FTLE + Flow Field');
set(gca,'YDir','normal'); 
colorbar; 
hold on; 
quiver(LON,LAT,U(:,:,1),V(:,:,1),2,'r');  


figure; 
imagesc(lon,lat,s(:,:,1)');   
title('Displacement + Flow Field');
set(gca,'YDir','normal'); 
colorbar; 
hold on; 
quiver(LON,LAT,U(:,:,1),V(:,:,1),2,'r');  

end
