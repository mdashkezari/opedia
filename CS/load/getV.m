% Read and return V field

function [V] = getV(itnum)

fnam=sprintf('/nobackup1/cnh/llc_4320/vvel1_extract/V.%10.10d.data.extract',itnum);
%fnam=sprintf('/nobackup1/cnh/llc_4320/hawaii_hots/vvel_extract/V.%10.10d.data.extract',itnum);

fid=fopen(fnam,'r','ieee-be');
phi=fread(fid,'float32');
fclose(fid);

%phi(find(phi==0))=NaN;
V=reshape(phi,[1321,2001]); 
%V=CellCenterV(V);

%V=reshape(phi,[151,151,90]);
%V=V(:,:,1); 


%%%%%%% Degrading Resolution %%%%%
%V=V(1:end-1,1:end-1);
V=V(1:30:end,1:30:end);

%disp('V')
%size(V)

end



function [CenteredV]=CellCenterV(V);
  ShiftedToBottom=circshift(V,[1 0]);
  CenteredV=(V+ShiftedToBottom)/2;
end

