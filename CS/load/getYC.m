% Read and return YC coordinates

function [YC] = getYC()

fnam='/nobackup1/cnh/llc_4320/grid_extract/YC_extract.data';
%fnam='/nobackup1/cnh/llc_4320/hawaii_hots/grid_extract/YC.data';

fid=fopen(fnam,'r','ieee-be');
phi=fread(fid,'float32');
fclose(fid);
YC=reshape(phi,[1321,2001]); 

%YC=reshape(phi,[151,151]); 


