function [mlon,mlat]=get_global_mask_AVISO()

%  [mask_lon mask_lat U]=get_obs('AVISO',2,2014001);     
%  U=U/10000;
  [mask_lon mask_lat U]=get_obs('AVISO','ugosa',2017150);       % near real time
  U(find(abs(U)>=10))=NaN;
  U(find(isnan(U)==0))=0;
  U(find(isnan(U)==1))=1;
  mask=U;
  [rows cols]=find(mask);
  mlon=mask_lon(rows);
  mlat=mask_lat(cols);

%  hold on
%  plot(mlon,mlat,'.','MarkerSize',6,'Color',[.76 .1 .5])
%  xlim([0 360])
%  ylim([-70 70])
%  daspect([1 1 1]);
  %axis off;
%  hold off;             
