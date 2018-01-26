% Read and return U field

function [U] = getU(itnum)

fnam=sprintf('/nobackup1/cnh/llc_4320/uvel1_extract/U.%10.10d.data.extract',itnum);
%fnam=sprintf('/nobackup1/cnh/llc_4320/hawaii_hots/uvel_extract/U.%10.10d.data.extract',itnum);


fid=fopen(fnam,'r','ieee-be');
phi=fread(fid,'float32');
fclose(fid);

%phi(find(phi==0))=NaN;
U=reshape(phi,[1321,2001]); 
%U=CellCenterU(U);

%U=reshape(phi,[151,151,90]); 
%U=U(:,:,1);


%%%%%%% Degrading Resolution %%%%%
%U=U(1:end-1,1:end-1);
U=U(1:30:end,1:30:end);

%disp('U')
%size(U)

end


function [CenteredU]=CellCenterU(U);
  ShiftedToRight=circshift(U,[0 1]);
  CenteredU=(U+ShiftedToRight)/2;
end
