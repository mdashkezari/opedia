% Read and return eta (SSH)

function [E] = getEta(itnum)

fnam=sprintf('/nobackup1/cnh/llc_4320/Eta_extract/Eta.%10.10d.data.extract',itnum);
%fnam=sprintf('/nobackup1/cnh/llc_4320/hawaii_hots/eta_extract/Eta.%10.10d.data.extract',itnum);


fid=fopen(fnam,'r','ieee-be');
phi=fread(fid,'float32');
fclose(fid);

phi(find(phi==0))=NaN;
E=reshape(phi,[1321,2001]); 

%E=reshape(phi,[151,151,90]); 
%E=E(:,:,1);
