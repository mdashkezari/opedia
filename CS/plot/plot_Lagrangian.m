
figure;
map_title=sprintf('Displacement \n %10.10d',itnum_start);
color_range=[0 4.5];
%color_range=[0 1.8];
map_path=strcat(Displacement_Path,sprintf('%10.10d.png',itnum_start));
plot_map(displacement,lon,lat,Xres,Yres,map_title,color_range,map_path,false,DataSource);

if flgDispersion
  figure;
  map_title=sprintf('Dispersion \n %10.10d',itnum_start);
  color_range=[0 0.3];
  map_path=strcat(Dispersion_Path,sprintf('%10.10d.png',itnum_start));
  plot_map(dispersion,lon,lat,Xres,Yres,map_title,color_range,map_path,false,DataSource);
end

figure;
map_title=sprintf('FTLE \n %10.10d',itnum_start);
color_range=[0 0.55];
%color_range=[0.01 0.1];
map_path=strcat(FTLE_Path,sprintf('%10.10d.png',itnum_start));
plot_map(ftle,lon,lat,Xres,Yres,map_title,color_range,map_path,false,DataSource);

figure;
map_title=sprintf('Tracers Left out the Domain \n %10.10d',itnum_start);
color_range=[];
map_path=strcat(Seized_Path,sprintf('%10.10d.png',itnum_start));
plot_map(seized,lon,lat,Xres,Yres,map_title,color_range,map_path,false,DataSource);


figure;
map_title=sprintf('Velocity Phase Mold \n %10.10d',itnum_start);
color_range=[];
map_path=strcat(vPhaseMold_Path,sprintf('%10.10d.png',itnum_start));
vel_phase = vPhase(interpU,interpV,2*pi);
plot_map(vel_phase,lon,lat,Xres,Yres,map_title,color_range,map_path,false,DataSource);
