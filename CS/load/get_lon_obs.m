function lon=get_lon_obs(DataSource, lonLabel, latLabel)
  if strcmp(DataSource,'AVISO')
    lon=get_lon_AVISO(DataSource, lonLabel, latLabel);
  elseif strcmp(DataSource,'HYCOM')
    lon=get_lon_HYCOM(DataSource);
  elseif strcmp(DataSource,'CCRA')
    lon=get_lon_CCRA(DataSource);
  end

end


function lon=get_lon_AVISO(DataSource, lonLabel, latLabel)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  AVISO  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[lon lat V]=get_obs(DataSource, lonLabel, 2017090, lonLabel, latLabel);
%lon=lon';
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end

function lon=get_lon_HYCOM(DataSource)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  HYCOM  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[lon lat V]=get_obs(DataSource,10,1);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end

function lon=get_lon_CCRA(DataSource)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  CCRA  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[lon lat V]=get_obs(DataSource,4,2015001);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end
