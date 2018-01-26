function n = doy(S) 
d = datevec(S); 
n = datenum([d(1:3), 0, 0, 0]) - datenum([d(1), 1, zeros(1, 4)]); 