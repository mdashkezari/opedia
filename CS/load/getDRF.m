% Read and return YC coordinates

function [DRF] = getDRF()

fnam='/nobackup1/cnh/llc_4320/hawaii_hots/grid_extract/DRF.data';

fid=fopen(fnam,'r','ieee-be');
phi=fread(fid,'float32');
fclose(fid);

DRF= phi;
%YC=reshape(phi,[151,151]); 


