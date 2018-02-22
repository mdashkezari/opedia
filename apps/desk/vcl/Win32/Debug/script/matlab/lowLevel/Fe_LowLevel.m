
%############## set parameters ################
table = 'tblPisces_NRT';
field = 'Fe';
dt1 = '2017-06-03';
dt2 = '2017-06-03';
lat1 = 10;
lat2 = 55;
lon1 = -180;
lon2 = -100;  
depth1 = 0;
depth2 = 1;
%##############################################

query = "SELECT [time], lat, lon, depth, %s FROM %s WHERE ";
query = query + "[time]>='%s' AND [time]<='%s' AND ";
query = query + "lat>=%f AND lat<=%f AND ";
query = query + "lon>=%f AND lon<=%f AND ";
query = query + "depth>=%f AND depth<=%f ";
query = query + "ORDER BY [time], lat, lon, depth ";
query  = sprintf(query, field, table, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2);
conn = database('Opedia', 'ArmLab', 'ArmLab2018');
data = select(conn, query);
lat = unique(data.lat);
lon = unique(data.lon);
vals = reshape(data.Fe, [size(lon), size(lat)]);
vals = squeeze(vals);
imagesc(vals'); colorbar; caxis([0, 1e-4]); axis xy