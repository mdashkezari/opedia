function lon=get_lon

lon=getXC;
lon=lon(1,:);
lon(find(lon<0))=lon(find(lon<0))+360;

%%%%%%% Degrading Resolution %%%%%
lon=lon(1:30:end);

%disp('lon')
%size(lon)
