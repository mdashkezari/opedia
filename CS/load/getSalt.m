% Read and return salinity

function [S] = getSalt(itnum)

fnam=sprintf('/nobackup1/cnh/llc_4320/salt1_extract/Salt.%10.10d.data.extract',itnum);
%fnam=sprintf('/nobackup1/cnh/llc_4320/hawaii_hots/salt_extract/Salt.%10.10d.data.extract',itnum);


fid=fopen(fnam,'r','ieee-be');
phi=fread(fid,'float32');
fclose(fid);

phi(find(phi==0))=NaN;
S=reshape(phi,[1321,2001]); 

%S=reshape(phi,[151,151,90]); 
%S=S(:,:,1);
