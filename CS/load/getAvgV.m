% Read and return V field

function [V] = getAvgV(itnum, nlayer)

layers= getDRF;
depth=0;
for i=1:nlayer
  depth= depth + layers(i);
end
%depth= sum(layers);
layers= layers/depth;

fnam=sprintf('/nobackup1/cnh/llc_4320/hawaii_hots/vvel_extract/V.%10.10d.data.extract',itnum);
fid=fopen(fnam,'r','ieee-be');
phi=fread(fid,'float32');
fclose(fid);

temp= reshape(phi,[151,151,90]); 
temp2=temp(:,:,1);
temp2(find(temp2==0))=nan;
temp(:,:,1)=temp2;
V=zeros(151,151);
for i=1:nlayer
  V=  V + (layers(i) .* temp(:,:,i));
end


