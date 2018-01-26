
function [iField]=interpolate(LON,LAT,Field,GridX1,GridY1)

interp_method='linear';
iField=interp2(LON,LAT,Field,GridX1,GridY1,interp_method);

%avg=nanmean(iField(:));
%iField(isnan(iField)==1)=avg;
