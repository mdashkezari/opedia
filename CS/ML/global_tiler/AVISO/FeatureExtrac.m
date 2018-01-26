function FeatureExtrac(itnum)


Xres=0.01;
Yres=0.01;
field_2pi=Compute_vPhase('AVISO',itnum,2*pi,Xres,Yres);
field_pi=Compute_vPhase('AVISO',itnum,pi,Xres,Yres);
field_pi2=Compute_vPhase('AVISO',itnum,pi/2,Xres,Yres);

features_2pi=[];
features_pi=[];
features_pi2=[];
labels=[];
others=[];
feature_path_2pi='/nobackup1/mdehghani/CS_Trunk/ML/gulf_eddy_2pi.mat';
feature_path_pi='/nobackup1/mdehghani/CS_Trunk/ML/gulf_eddy_pi.mat';
feature_path_pi2='/nobackup1/mdehghani/CS_Trunk/ML/gulf_eddy_pi2.mat';
if exist(feature_path_2pi)==2
  load(feature_path_2pi,'');
end
if exist(feature_path_pi)==2
  load(feature_path_pi);
end
if exist(feature_path_pi2)==2
  load(feature_path_pi2);
end


while 1
  center = input('Enter the center [row col]   ');
%  radius = input('Enter the radius   ');
  radius = 10;

  slc_2pi = field_2pi(center(1)-radius:center(1)+radius , center(2)-radius:center(2)+radius);
  slc_pi = field_pi(center(1)-radius:center(1)+radius , center(2)-radius:center(2)+radius);
  slc_pi2 = field_pi2(center(1)-radius:center(1)+radius , center(2)-radius:center(2)+radius);
  plot_slice(slc_2pi,'2pi');
%  plot_slice(slc_pi,'pi');
%  plot_slice(slc_pi2,'pi/2');

  ans = input('Do you accept the feature? (y/n)    ','s');
  if ans=='n'
    continue
  end


  lbl = input('Enter Labels [eddy polarity]    if is eddy, then eddy=1 else eddy=-1     if ccw, polarity=1. if cw, polarity=-1. if not eddy, polarity=0    ');
  if length(lbl)~=2
    disp(['You must enter 2 labels!'])
    error
  end

  features_2pi(:,:,end+1)=slc_2pi;
  features_pi(:,:,end+1)=slc_pi;
  features_pi2(:,:,end+1)=slc_pi2;
  labels(:,end+1)=lbl;
  others(:,end+1)=[itnum Xres Yres center(1) center(2) radius];
  size(features_pi)
  size(labels)
  size(others)
  save(feature_path_2pi,'features_2pi','labels','others');
  save(feature_path_pi,'features_pi','labels','others');
  save(feature_path_pi2,'features_pi2','labels','others');

  ans = input('Would you like to continue? (y/n)    ','s');
  if ans=='n'
    return
  end
end

end







function plot_slice(phase,ti)
figure;
colormap jet;
imagesc(phase);
axis xy;
colorbar;
title(ti);
daspect([1 1 1]);
drawnow;
end
      
