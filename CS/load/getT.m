% Read and return temperature

function [T] = getT(itnum)

fnam=sprintf('/nobackup1/cnh/llc_4320/theta1_extract/theta.%10.10d.data.extract',itnum);
%fnam=sprintf('/nobackup1/cnh/llc_4320/hawaii_hots/theta_extract/theta.%10.10d.data.extract',itnum);


fid=fopen(fnam,'r','ieee-be');
phi=fread(fid,'float32');
fclose(fid);

phi(find(phi==0))=NaN;
T=reshape(phi,[1321,2001]); 

%T=reshape(phi,[151,151,90]); 
%T=T(:,:,1);
