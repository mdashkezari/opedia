

figure;
map_title=sprintf('Okubo Weiss Parameter \n %10.10d',itnum_start);
color_range=[];
map_path=strcat(OW_Path,sprintf('%10.10d.png',itnum_start));
plot_map(OW,lon,lat,Xres,Yres,map_title,color_range,map_path,false,DataSource);

%plot_map(OW(1000:1600,700:1100),lon(1000:1600),lat(700:1100),Xres,Yres,map_title,color_range,map_path,true,DataSource);


figure;
map_title=sprintf('Relative Vorticity \n %10.10d',itnum_start);
color_range=[-2e-5 2e-5];
map_path=strcat(Vorticity_Path,sprintf('%10.10d.png',itnum_start));
plot_map(vort,lon,lat,Xres,Yres,map_title,color_range,map_path,true,DataSource);

%plot_map(vort(1000:1600,700:1100),lon(1000:1600),lat(700:1100),Xres,Yres,map_title,color_range,map_path,true,DataSource);
