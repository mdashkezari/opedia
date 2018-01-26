
function phase = Compute_vPhase(DataSource,itnum,phase_range,Xres,Yres)

  addpath(genpath('~/matbox/CS'));

  lon=get_lon_obs(DataSource);
  lat=get_lat_obs(DataSource);

  [LON,LAT]=meshgrid(lon,lat);
  min_lon=min(lon);
  max_lon=max(lon);
  min_lat=min(lat);
  max_lat=max(lat);

  if Xres & Yres
%    X=ceil(min_lon):Xres:fix(max_lon);
%    Y=ceil(min_lat):Yres:fix(max_lat);

    X=(min_lon):Xres:(max_lon);
    Y=(min_lat):Yres:(max_lat);
  else
    %the horizontal resolution of the input data is used
    X=lon;
    Y=lat;
  end
  [X,Y]=meshgrid(X,Y);

%  if observation
    V=getV_obs(DataSource,itnum);
    U=getU_obs(DataSource,itnum);
%  else
%    V=-1.*getU(itnum_start)';
%    U=getV(itnum_start)';
%  end

  U=interpolate(LON,LAT,U',X,Y);
  V=interpolate(LON,LAT,V',X,Y);
  phase=vPhase(U,V,phase_range);
  %plotPhase(phase,{'vPhase',num2str(itnum)});


  %%%%%%%%%%%%%%%%%  Breaking into the "tiles". If you want one single tile, comment this section and uncomment the section below %%%%%%%%%%%%%%
  data=phase;
  rows=2;
  cols=4;
  dh=size(data,1)/rows;
  dw=size(data,2)/cols;
  for i=1:rows
    for j=1:cols
	  if phase_range==2*pi
	    phase=data(1+(i-1)*dh:i*dh, 1+(j-1)*dw:j*dw);
	    save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/vphase/vphase_2pi_%10.10d_%d_%d.mat',itnum,i,j),'phase','itnum','phase_range','Xres','Yres')
	  end
	
    end
  end
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%{
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% One single tile  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%	
  if phase_range==2*pi
    %save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/vphase/vphase_2pi_%10.10d.mat',itnum),'phase','itnum','phase_range','Xres','Yres', '-v7.3')
    save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/vphase/vphase_2pi_%10.10d.mat',itnum),'phase','itnum','phase_range','Xres','Yres')	
  end

  if phase_range==pi
    %save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/vphase/vphase_pi_%10.10d.mat',itnum),'phase','itnum','phase_range','Xres','Yres', '-v7.3')
    save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/vphase/vphase_pi_%10.10d.mat',itnum),'phase','itnum','phase_range','Xres','Yres')
  end

  if phase_range==pi/2
    %save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/vphase/vphase_pi2_%10.10d.mat',itnum),'phase','itnum','phase_range','Xres','Yres', '-v7.3')
    save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/vphase/vphase_pi2_%10.10d.mat',itnum),'phase','itnum','phase_range','Xres','Yres')
  end
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%}  


end


function plotPhase(phase,ti)
figure;
colormap jet;
imagesc(phase);
axis xy;
colorbar;
title(ti);
daspect([1 1 1]);
drawnow; 
grid on;
end
