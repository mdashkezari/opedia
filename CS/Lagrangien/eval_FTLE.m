
function ftle=eval_FTLE(ix,iy,grid_x1,grid_y1,grid_x0,grid_y0,tau)

[nx ny]=size(grid_x1);

if (ix-1)*(ix-nx)<0 & (iy-1)*(iy-ny)<0
    A11=(grid_x1(ix+1,iy)-grid_x1(ix-1,iy))/(grid_x0(ix+1,iy)-grid_x0(ix-1,iy));
    A12=(grid_x1(ix,iy+1)-grid_x1(ix,iy-1))/(grid_y0(ix,iy+1)-grid_y0(ix,iy-1));
    A21=(grid_y1(ix+1,iy)-grid_y1(ix-1,iy))/(grid_x0(ix+1,iy)-grid_x0(ix-1,iy));
    A22=(grid_y1(ix,iy+1)-grid_y1(ix,iy-1))/(grid_y0(ix,iy+1)-grid_y0(ix,iy-1));
    A=[A11 A12;A21 A22];
    B=A'*A;
    lambda=max(eig(B));
    ftle=log(lambda)/(2*tau);
else
    ftle=0;
end

