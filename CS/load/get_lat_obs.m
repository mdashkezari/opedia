function lat=get_lat_obs(DataSource, lonLabel, latLabel)

  if strcmp(DataSource,'AVISO')
    lat=get_lat_AVISO(DataSource, lonLabel, latLabel);
  elseif strcmp(DataSource,'HYCOM')
    lat=get_lat_HYCOM(DataSource);
  elseif strcmp(DataSource,'CCRA')
    lat=get_lat_CCRA(DataSource);
  end

end


function lat=get_lat_AVISO(DataSource, lonLabel, latLabel)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  AVISO  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[lon lat V]=get_obs(DataSource, latLabel, 2017090, lonLabel, latLabel); 
%lat=lat';
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end


function lat=get_lat_HYCOM(DataSource)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  HYCOM  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[lon lat V]=get_obs(DataSource,10,1);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end

function lat=get_lat_CCRA(DataSource)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  CCRA  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[lon lat V]=get_obs(DataSource,4,2015001);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end
