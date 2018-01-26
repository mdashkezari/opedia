function plot_map(map,lon,lat,Xres,Yres,map_title,color_range,filename,br,DataSource)

if nargin<9
  br=false;
  DataSource='MITgcm';
end;


if strcmp(DataSource,'MITgcm')
  imagesc(abs(lon-360),lat,map');
  set(gca,'YDir','reverse');
  set(gca,'XDir','reverse');
%{
  NumTicks=16;
  L=get(gca,'XLim');
  set(gca,'XTick',linspace(L(1),L(2),NumTicks))
  set(gca,'FontSize',8);
%}
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

  title(map_title);
  colorbar;
  if ~isempty(color_range)
    if br
      colormap(b2r(color_range(1),color_range(end)));
    else
      colormap jet;
      caxis(color_range);
    end
  end

  daspect([1 1 1]);
  grid on;
  if ~isempty(filename)
    print('-dpng', '-r500', filename);
  end
  grid off;

else

  imagesc(lon,lat,map');
  axis xy;

  NumTicks=16;
  L=get(gca,'XLim');
  set(gca,'XTick',linspace(L(1),L(2),NumTicks))
  set(gca,'FontSize',8);

  xt=get(gca,'xtick');
  for k=1:numel(xt);
    xt1{k}=sprintf('%3.3d',round(abs(xt(k)-360)));
  end
  set(gca,'xticklabel',xt1);

  yt=get(gca,'ytick');
  for k=1:numel(yt);
    yt1{k}=sprintf('%d',yt(k));
  end
  set(gca,'yticklabel',yt1);

  title(map_title);
  colorbar;
  if ~isempty(color_range)
    if br
      colormap(b2r(color_range(1),color_range(end)));
    else
      colormap jet;
      caxis(color_range);
    end
  end


  daspect([1 1 1]);
  grid on;
  
  if strcmp(DataSource,'CCRA')
    plot_Hawaii_mask;
  end

  if ~isempty(filename)
    print('-dpng', '-r500', filename);
  end
  grid off;
end







