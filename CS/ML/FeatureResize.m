function FeatureResize(radius)

features_2pi=[];
features_pi=[];
features_pi2=[];
labels=[];
others=[];
feature_path_2pi='/nobackup1/mdehghani/CS_Trunk/ML/eddy_2pi.mat';
feature_path_pi='/nobackup1/mdehghani/CS_Trunk/ML/eddy_pi.mat';
feature_path_pi2='/nobackup1/mdehghani/CS_Trunk/ML/eddy_pi2.mat';
if exist(feature_path_2pi)==2
  load(feature_path_2pi,'');
end
if exist(feature_path_pi)==2
  load(feature_path_pi);
end
if exist(feature_path_pi2)==2
  load(feature_path_pi2);
end

feature_path_2pi='/nobackup1/mdehghani/CS_Trunk/ML/feature_21radius/eddy_2pi.mat';
feature_path_pi='/nobackup1/mdehghani/CS_Trunk/ML/feature_21radius/eddy_pi.mat';
feature_path_pi2='/nobackup1/mdehghani/CS_Trunk/ML/feature_21radius/eddy_pi2.mat';
features_2pi=[];
features_pi=[];
features_pi2=[];

for i=1:size(labels,2)
  disp(['i: ',num2str(i)])
  itnum = others(1,i);
  center(1) = others(4,i);
  center(2) = others(5,i);
  
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/vphase/vphase_2pi_%10.10d.mat',itnum) , 'phase')
  field_2pi=phase;
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/vphase/vphase_pi_%10.10d.mat',itnum) , 'phase')
  field_pi=phase;
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/vphase/vphase_pi2_%10.10d.mat',itnum) , 'phase')
  field_pi2=phase;
 
  slc_2pi = field_2pi(center(1)-radius:center(1)+radius , center(2)-radius:center(2)+radius);
  slc_pi = field_pi(center(1)-radius:center(1)+radius , center(2)-radius:center(2)+radius);
  slc_pi2 = field_pi2(center(1)-radius:center(1)+radius , center(2)-radius:center(2)+radius);
%  plot_slice(slc_2pi,'2pi');
%  plot_slice(slc_pi,'pi');
%  plot_slice(slc_pi2,'pi/2');



  features_2pi(:,:,end+1)=slc_2pi;
  features_pi(:,:,end+1)=slc_pi;
  features_pi2(:,:,end+1)=slc_pi2;
%  size(features_pi)
%  size(labels)
%  size(others)
  save(feature_path_2pi,'features_2pi','labels','others');
  save(feature_path_pi,'features_pi','labels','others');
  save(feature_path_pi2,'features_pi2','labels','others');

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
      
