function Tile_NRT_Phase_SLA(itnums,Xres,Yres)
  for itnum=itnums
    disp=(['itnum: ',num2str(itnum)])
    Compute_NRT_Phase_SLA(itnum,2*pi,Xres,Yres);
  end
end
