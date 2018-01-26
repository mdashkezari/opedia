function plot_deviation(range)

counter=0;
dims=[];
avg_diff2=[];
std_diff2=[];
avg_diff4=[];
std_diff4=[];
avg_diff8=[];
std_diff8=[];
avg_diff16=[];
std_diff16=[];
avg_diff12=[];
std_diff12=[];
avg_diff20=[];
std_diff20=[];
avg_diff25=[];
std_diff25=[];
avg_diff30=[];
std_diff30=[];
T=20*60;
lon1=2000;
lon2=3300;
lat1=400;
lat2=1200;

for field=range
  disp(['field= ',num2str(field)])
  counter=counter+1;
  %dim=counter;
  dim=1;
  dims(end+1)=counter;

  load(sprintf('/nobackup1/mdehghani/CS_Trunk/0000000014/Lagrangian/MAT/Trajectory/0000010368_%10.10d.mat',field));
  X11=X2;
  Y11=Y2;   
%{
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/0000000015/Lagrangian/MAT/Trajectory/0000010368_%10.10d.mat',field));
  X12=X2;
  Y12=Y2; 
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/0000000016/Lagrangian/MAT/Trajectory/0000010368_%10.10d.mat',field));
  X14=X2;
  Y14=Y2; 
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/0000000017/Lagrangian/MAT/Trajectory/0000010368_%10.10d.mat',field));
  X18=X2;
  Y18=Y2; 
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/0000000018/Lagrangian/MAT/Trajectory/0000010368_%10.10d.mat',field));
  X116=X2;
  Y116=Y2; 
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/0000000019/Lagrangian/MAT/Trajectory/0000010368_%10.10d.mat',field));
  X112=X2;
  Y112=Y2;
%}
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/0000000020/Lagrangian/MAT/Trajectory/0000010368_%10.10d.mat',field));
  X120=X2;
  Y120=Y2;
%  load(sprintf('/nobackup1/mdehghani/CS_Trunk/0000000021/Lagrangian/MAT/Trajectory/0000010368_%10.10d.mat',field));
%  X125=X2;
%  Y125=Y2;
  load(sprintf('/nobackup1/mdehghani/CS_Trunk/0000000022/Lagrangian/MAT/Trajectory/0000010368_%10.10d.mat',field));
  X130=X2;
  Y130=Y2;

%{
  diffX2(:,:,dim)=X12-X11;
  diffY2(:,:,dim)=Y12-Y11;
  diffX4(:,:,dim)=X14-X11;
  diffY4(:,:,dim)=Y14-Y11;
  diffX8(:,:,dim)=X18-X11;
  diffY8(:,:,dim)=Y18-Y11;
  diffX16(:,:,dim)=X116-X11;
  diffY16(:,:,dim)=Y116-Y11;
  diffX12(:,:,dim)=X112-X11;
  diffY12(:,:,dim)=Y112-Y11;
%}
  diffX20(:,:,dim)=X120-X11;
  diffY20(:,:,dim)=Y120-Y11;
%  diffX25(:,:,dim)=X125-X11;
%  diffY25(:,:,dim)=Y125-Y11;
  diffX30(:,:,dim)=X130-X11;
  diffY30(:,:,dim)=Y130-Y11;

%{
  diff2(:,:,dim)= sqrt(diffX2(:,:,dim).^2 + diffY2(:,:,dim).^2);
  diff4(:,:,dim)= sqrt(diffX4(:,:,dim).^2 + diffY4(:,:,dim).^2);
  diff8(:,:,dim)= sqrt(diffX8(:,:,dim).^2 + diffY8(:,:,dim).^2);
  diff16(:,:,dim)= sqrt(diffX16(:,:,dim).^2 + diffY16(:,:,dim).^2);
  diff12(:,:,dim)= sqrt(diffX12(:,:,dim).^2 + diffY12(:,:,dim).^2);
%}
  diff20(:,:,dim)= sqrt(diffX20(:,:,dim).^2 + diffY20(:,:,dim).^2);
%  diff25(:,:,dim)= sqrt(diffX25(:,:,dim).^2 + diffY25(:,:,dim).^2);
  diff30(:,:,dim)= sqrt(diffX30(:,:,dim).^2 + diffY30(:,:,dim).^2);

%{
  d=diff2(:,:,dim);
  d(d==0)=NaN;
  avg_diff2(end+1)=nanmean(d(:)); 
  std_diff2(end+1)=nanstd(d(:));
  d=diff4(:,:,dim);
  d(d==0)=NaN;
  avg_diff4(end+1)=nanmean(d(:));
  std_diff4(end+1)=nanstd(d(:));
  d=diff8(:,:,dim);
  d(d==0)=NaN;
  avg_diff8(end+1)=nanmean(d(:));
  std_diff8(end+1)=nanstd(d(:));
  d=diff16(:,:,dim);
  d(d==0)=NaN;
  avg_diff16(end+1)=nanmean(d(:));
  std_diff16(end+1)=nanstd(d(:));
  d=diff12(:,:,dim);
  d(d==0)=NaN;
  avg_diff12(end+1)=nanmean(d(:));
  std_diff12(end+1)=nanstd(d(:));
%}
  d=diff20(:,:,dim);
  d(d==0)=NaN;
  avg_diff20(end+1)=nanmean(d(:));
  std_diff20(end+1)=nanstd(d(:));
%  d=diff25(:,:,dim);
%  d(d==0)=NaN;
%  avg_diff25(end+1)=nanmean(d(:));
%  std_diff25(end+1)=nanstd(d(:));
  d=diff30(:,:,dim);
  d(d==0)=NaN;
  avg_diff30(end+1)=nanmean(d(:));
  std_diff30(end+1)=nanstd(d(:));

  elapsed_min= floor(field*T/60);
  elapsed_hour= floor(elapsed_min/60);
  elapsed_day= floor(elapsed_min/(60*24));
  elapsed=sprintf( 'Elapsed time (day:hour:min) %s:%s:%s',  sprintf('%2.2d',elapsed_day), sprintf('%2.2d',elapsed_hour-elapsed_day*24), sprintf('%2.2d',elapsed_min-elapsed_hour*60) );
  
%{
%  figure;
%  hold on;
  plot(dims,avg_diff2,'-o',dims,avg_diff4,'-o',dims,avg_diff8,'-o',dims,avg_diff12,'-o',dims,avg_diff16,'-o',dims,avg_diff20,'-o',dims,avg_diff30,'-o');
%  errorbar(dims,avg_diff2,std_diff2,'-bo');
%  errorbar(dims,avg_diff4,std_diff4,'-r*');
%  errorbar(dims,avg_diff8,std_diff8,'-gx');
%  errorbar(dims,avg_diff12,std_diff12,'-y>'); 
%  errorbar(dims,avg_diff16,std_diff16,'-c^');  
  
%  shadedErrorBar(range,avg_diff16,std_diff16,{'-or','markerfacecolor',[1,0.2,0.2]},1); 
%  shadedErrorBar(range,avg_diff12,std_diff12,{'-oy','markerfacecolor',[0.2,1,1]},1); 
%  shadedErrorBar(range,avg_diff8,std_diff8,{'-ob','markerfacecolor',[0.2,0.2,1]},1); 
%  shadedErrorBar(range,avg_diff4,std_diff4,{'-og','markerfacecolor',[0.2,1,0.2]},1);
%  shadedErrorBar(range,avg_diff2,std_diff2,{'-ok','markerfacecolor',[0.2,0.2,0.2]},1);   

  legend('X2 Degraded','X4 Degraded','X8 Degraded','X12 Degraded','X16 Degraded','X20 Degraded','X30 Degraded','Location','northwest');
  title({'Averaged Deviation (deg)',elapsed});
%  hold off; 
  print('-dpng', '-r500', '/nobackup1/mdehghani/CS_Trunk/deviation/average_deviation_NaN_NoError.png');
%  close;

  imagesc(diff2(lon1:lon2,lat1:lat2,dim)');
  colorbar;
  title({'Deviation of X2 Degraded Flow Fields (deg)',elapsed}); 
  axis xy;
  caxis([0 0.06]);
  daspect([1,1,1])
  print('-dpng', '-r500', sprintf('/nobackup1/mdehghani/CS_Trunk/deviation/X2/%10.10d.png',field));
 
  imagesc(diff4(lon1:lon2,lat1:lat2,dim)');
  colorbar;
  title({'Deviation of X4 Degraded Flow Fields (deg)',elapsed});
  axis xy;
  caxis([0 0.2]);
  daspect([1,1,1])
  print('-dpng', '-r500', sprintf('/nobackup1/mdehghani/CS_Trunk/deviation/X4/%10.10d.png',field));

  imagesc(diff8(lon1:lon2,lat1:lat2,dim)');
  colorbar;
  title({'Deviation of X8 Degraded Flow Fields (deg)',elapsed});
  axis xy;
  caxis([0 0.4]);
  daspect([1,1,1])
  print('-dpng', '-r500', sprintf('/nobackup1/mdehghani/CS_Trunk/deviation/X8/%10.10d.png',field));

  imagesc(diff16(lon1:lon2,lat1:lat2,dim)');
  colorbar;
  title({'Deviation of X16 Degraded Flow Fields (deg)',elapsed});
  axis xy;
  caxis([0 0.7]);
  daspect([1,1,1])
  print('-dpng', '-r500', sprintf('/nobackup1/mdehghani/CS_Trunk/deviation/X16/%10.10d.png',field));

  imagesc(diff12(lon1:lon2,lat1:lat2,dim)');
  colorbar;
  title({'Deviation of X12 Degraded Flow Fields (deg)',elapsed});
  axis xy;
  caxis([0 0.7]);
  daspect([1,1,1])
  print('-dpng', '-r500', sprintf('/nobackup1/mdehghani/CS_Trunk/deviation/X12/%10.10d.png',field));

  imagesc(diff20(lon1:lon2,lat1:lat2,dim)');
  colorbar;
  title({'Deviation of X20 Degraded Flow Fields (deg)',elapsed});
  axis xy;
  caxis([0 0.7]);
  daspect([1,1,1])
  print('-dpng', '-r500', sprintf('/nobackup1/mdehghani/CS_Trunk/deviation/X20/%10.10d.png',field));

%  imagesc(diff25(lon1:lon2,lat1:lat2,dim)');
%  colorbar;
%  title({'Deviation of X25 Degraded Flow Fields (deg)',elapsed});
%  axis xy;
%  caxis([0 0.7]);
%  daspect([1,1,1])
%  print('-dpng', '-r500', sprintf('/nobackup1/mdehghani/CS_Trunk/deviation/X25/%10.10d.png',field));

  imagesc(diff30(lon1:lon2,lat1:lat2,dim)');
  colorbar;
  title({'Deviation of X30 Degraded Flow Fields (deg)',elapsed});
  axis xy;
  caxis([0 0.7]);
  daspect([1,1,1])
  print('-dpng', '-r500', sprintf('/nobackup1/mdehghani/CS_Trunk/deviation/X30/%10.10d.png',field));
%}
 save('/nobackup1/mdehghani/CS_Trunk/deviation/stat_divs_NaN_NoError.mat','range','avg_diff2','avg_diff4','avg_diff8','avg_diff12','avg_diff16','avg_diff20','avg_diff25','avg_diff30','std_diff2','std_diff4','std_diff8','std_diff12','std_diff16','std_diff20','std_diff25','std_diff30'); 
end


 % save('/nobackup1/mdehghani/CS_Trunk/deviation/diffs.mat','range','diff2','diff4','diff8','diff16');
