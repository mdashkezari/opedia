function [mlon,mlat]=get_global_mask_CCAR()

  [mask_lon mask_lat U]=get_obs('CCRA',3,2015001);   
  U(find(isinf(abs(U))==1))=0;
  U(find(abs(U)>=100))=NaN;
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
