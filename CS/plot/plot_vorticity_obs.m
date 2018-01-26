function [] = plot_vorticity_obs(DataSource,lon,lat,vort,plot_title,filename)

  if strcmp(DataSource,'AVISO')
    plot_vorticity_AVISO(lon,lat,vort,plot_title,filename);
  elseif strcmp(DataSource,'HYCOM')
    plot_vorticity_HYCOM(lon,lat,vort,plot_title,filename);
  elseif strcmp(DataSource,'CCRA')
    plot_vorticity_CCRA(lon,lat,vort,plot_title,filename);
  end

end


function plot_vorticity_HYCOM(lon,lat,vort,plot_title,filename)

  imagesc(abs(lon-360),lat,vort);colorbar;title(plot_title);
  set(gca,'XDir','reverse');
  set(gca,'YDir','normal');
  xt=get(gca,'xtick');
  for k=1:numel(xt);
  xt1{k}=sprintf('%d°W',xt(k));
  end
  set(gca,'xticklabel',xt1);
  yt=get(gca,'ytick');
  for k=1:numel(yt);
  yt1{k}=sprintf('%d°N',yt(k));
  end
  set(gca,'yticklabel',yt1);
  colormap(b2r(-1e-6,1e-6));

  ndt=datestr(now,'yyyymmdd');
  storage_folder=strcat('/nobackup1/mdehghani/llc_4320_hawaii/pics/stdFTLE/HYCOM/',ndt);
  if exist(storage_folder)~=7
    mkdir(storage_folder);
  end

  print('-dpng','-r500',strcat(storage_folder,'/',filename,'.png'));
end



function plot_vorticity_CCRA(lon,lat,vort,plot_title,filename)

  imagesc(abs(lon-360),lat,vort);colorbar;title(plot_title);
  set(gca,'XDir','reverse');
  set(gca,'YDir','normal');
  xt=get(gca,'xtick');
  for k=1:numel(xt);
  xt1{k}=sprintf('%d°W',xt(k));
  end
  set(gca,'xticklabel',xt1);
  yt=get(gca,'ytick');
  for k=1:numel(yt);
  yt1{k}=sprintf('%d°N',yt(k));
  end
  set(gca,'yticklabel',yt1);
  colormap(b2r(-1e-5,1e-5));

  ndt=datestr(now,'yyyymmdd');
  storage_folder=strcat('/nobackup1/mdehghani/llc_4320_hawaii/pics/stdFTLE/CCRA/',ndt);
  if exist(storage_folder)~=7
    mkdir(storage_folder);
  end

  print('-dpng','-r500',strcat(storage_folder,'/',filename,'.png'));
end

