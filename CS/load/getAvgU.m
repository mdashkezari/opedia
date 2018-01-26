% Read and return U field

function [U] = getAvgU(itnum, nlayer)

layers= getDRF;
depth=0;
for i=1:nlayer
  depth= depth + layers(i);
end
%depth= sum(layers);
layers= layers/depth;

fnam=sprintf('/nobackup1/cnh/llc_4320/hawaii_hots/uvel_extract/U.%10.10d.data.extract',itnum);
fid=fopen(fnam,'r','ieee-be');
phi=fread(fid,'float32');
fclose(fid);

temp= reshape(phi,[151,151,90]); 
temp2=temp(:,:,1);
temp2(find(temp2==0))=nan;
temp(:,:,1)=temp2;
U=zeros(151,151);
for i=1:nlayer
  U=  U + (layers(i) .* temp(:,:,i));
end


