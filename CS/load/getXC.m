% Read and return XC coordinates

function [XC] = getXC()

fnam='/nobackup1/cnh/llc_4320/grid_extract/XC_extract.data';            
%fnam='/nobackup1/cnh/llc_4320/hawaii_hots/grid_extract/XC.data';            

fid=fopen(fnam,'r','ieee-be');
phi=fread(fid,'float32');
fclose(fid);
XC=reshape(phi,[1321,2001]); 
%XC=reshape(phi,[151,151]); 




