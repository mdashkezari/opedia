function gen_nrt(itnums)
  for itnum=itnums
    disp([num2str(itnum)])	
    gen_nrt_vPhase(itnum)
    gen_nrt_ssh(itnum)
  end
end







function gen_nrt_vPhase(itnum)

  phase_range = 2*pi;
  Xres = 0.01;
  Yres = 0.01;
	
  lon=get_lon_obs();
  lat=get_lat_obs();

  [LON,LAT]=meshgrid(lon,lat);
  min_lon=min(lon);
  max_lon=max(lon);
  min_lat=min(lat);
  max_lat=max(lat);

  X=(min_lon):Xres:(max_lon);
  Y=(min_lat):Yres:(max_lat);
  [X,Y]=meshgrid(X,Y);

  V=getV_obs(itnum);
  U=getU_obs(itnum);

  U=interpolate(LON,LAT,U',X,Y);
  V=interpolate(LON,LAT,V',X,Y);
  phase=vPhase(U,V,phase_range);


  data=phase;
  rows=2;
  cols=4;
  dh=size(data,1)/rows;
  dw=size(data,2)/cols;
  for i=1:rows
    for j=1:cols
          if phase_range==2*pi
            phase=data(1+(i-1)*dh:i*dh, 1+(j-1)*dw:j*dw);
            save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/vphase/nrt_vphase_2pi_%10.10d_%d_%d.mat',itnum,i,j),'phase','itnum','phase_range','Xres','Yres')
          end

    end
  end



  %%%%%%%%%%%%%%%%%%%% Vort %%%%%%%%%%%%%%%%%%%%%%
  %{
  [W,sn,ss,vort] = Okubo_Weiss(U,V,Xres,Yres);
  data=vort;
  rows=2;
  cols=4;
  dh=(size(data,1)+1)/rows;
  dw=(size(data,2)+1)/cols;
  for i=1:rows
    for j=1:cols
      row_end=i*dh;
      if row_end>size(data,1)
        row_end=size(data,1);
      end

      col_end=j*dw;
      if col_end>size(data,2)
        col_end=size(data,2);
      end

      vort=data(1+(i-1)*dh:row_end, 1+(j-1)*dw:col_end);
      col=size(vort,2);
      row=size(vort,1);
      save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/vort/nrt_vorticity_%10.10d_%d_%d.mat',itnum,i,j), 'vort', 'itnum', 'Xres', 'col', 'row');
    end
  end
  %}
end



function gen_nrt_ssh(itnum)
  Xres = 0.01;
  Yres = 0.01;

  [lon lat ssh]=getSSH_AVISO_nrt(itnum);       

  [LON,LAT]=meshgrid(lon,lat);
  min_lon=min(lon);
  max_lon=max(lon);
  min_lat=min(lat);
  max_lat=max(lat);

  X=(min_lon):Xres:(max_lon);
  Y=(min_lat):Yres:(max_lat);

  [X,Y]=meshgrid(X,Y);
  ssh=interpolate(LON,LAT,ssh',X,Y);



    data=ssh;
    rows=2;
    cols=4;
    dh=size(data,1)/rows;
    dw=size(data,2)/cols;
    for i=1:rows
      for j=1:cols
        ssh=data(1+(i-1)*dh:i*dh, 1+(j-1)*dw:j*dw);
        col=size(ssh,2);
        row=size(ssh,1);
        save(sprintf('/nobackup1/mdehghani/CS_Trunk/ML/ssh/nrt_ssh_%10.10d_%d_%d.mat',itnum,i,j), 'ssh', 'itnum', 'Xres', 'col', 'row');
      end
    end


end



function [lon lat SSH]=getSSH_AVISO_nrt(itnum)
path=strcat('/nobackup1/mdehghani/obs/AVISO/ssh_nrt/nrt_sla_ssh_AVISO_',sprintf('%7.7d',itnum),'.nc');
ncid=netcdf.open(path);

lon=double(netcdf.getVar(ncid,4));
lat=double(netcdf.getVar(ncid,2));

SSH=double(netcdf.getVar(ncid,7));  
SSH(find(abs(SSH)>50000))=NaN;
SSH=SSH/10000;

%lon=lon(750:840);
%lat=lat(425:480);
%SSH=SSH(750:840,425:480);
end



function [W,sn,ss,vort] = Okubo_Weiss(U,V,delX,delY)
  vx=(V(2:end,2:end)-V(2:end,1:end-1)) ./ delX;
  uy=(U(2:end,2:end)-U(1:end-1,2:end)) ./ delY;
  %vy=(V(2:end,2:end)-V(1:end-1,2:end)) ./ delY;
  %ux=(U(2:end,2:end)-U(2:end,1:end-1)) ./ delX;
  sn=0;
  ss=0;
  W=0;
  %sn= ux-vy;   % normal component of strain
  %ss= vx+uy;   % shear component of strain 
  vort= vx-uy;    % relative voticity of the flow  
  %W= sn.^2 + ss.^2 - vort.^2;   % OW parameter
end

function phase = vPhase(U,V,range)

  if range==2*pi
    phase = atan0_2pi(V,U);
  elseif range==pi
    phase = atan2(V,U);
  elseif range==pi/2
    phase = atan(V./U);
  else
    disp(['The third argument should be one of these values: 2*pi, pi, pi/2'])
    error
  end
  phase = 180 * phase /pi;
end


function t=atan0_2pi(y,x)
  t = Inf*x; %atan(y./x);

  con = x>0 & y>=0;
  t(con) = atan(y(con)./x(con));

  con = x==0 & y>0;
  t(con) = pi/2;

  con = x<0;
  t(con) = atan(y(con)./x(con)) + pi;

  con = x==0 & y<0;
  t(con) = 3*pi/2;

  con = x>0 & y<0;
  t(con) = atan(y(con)./x(con)) + 2*pi;

  %con = x==0 & y==0;
  %t(con) = 0;
end


function [iField]=interpolate(LON,LAT,Field,GridX1,GridY1)
  interp_method='linear';
  iField=interp2(LON,LAT,Field,GridX1,GridY1,interp_method);
end

function lat=get_lat_obs()
[lon lat V]=get_obs(8,2016277);  % absolute near real time
%lat=lat';
end


function lon=get_lon_obs()
[lon lat V]=get_obs(8,201277);  % absolute near real time
%lon=lon';
end


function [lon lat U] = getU_obs(itnum)
[lon lat U]=get_obs(7,itnum);       % absolute near real time
U=U/10000;

U(find(abs(U)>10))=0;
end


function [lon lat V]=getV_obs(itnum)
[lon lat V]=get_obs(8,itnum);    % absolute near real time
V=V/10000;

V(find(abs(V)>10))=0;
end



function [lon lat data]=get_obs(channel,iteration)
path=strcat('/nobackup1/mdehghani/obs/AVISO/uv_abs/nrt_uv_abs_AVISO_',sprintf('%7.7d',iteration),'.nc');  % Near Real-Time
ncid=netcdf.open(path);

%{
%%%%%%%%%%%% absolute near real time %%%%%%%%%%%%
lon=double(netcdf.getVar(ncid,4));
lat=double(netcdf.getVar(ncid,2));
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%}


%%%%%%%%%%%% absolute delayed time %%%%%%%%%%%%
lon=double(netcdf.getVar(ncid,3));
lat=double(netcdf.getVar(ncid,5));
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%{
%%%%%%%%%%%% anomally %%%%%%%%%%%%
lon=double(netcdf.getVar(ncid,2));
lat=double(netcdf.getVar(ncid,4));
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%}

data=double(netcdf.getVar(ncid,channel));

%data=data(:,:,iteration);
data(find(abs(data)>2147483646))=NaN;
end

