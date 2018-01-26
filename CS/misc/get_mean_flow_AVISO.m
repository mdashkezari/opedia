function [mU mV mSSH]=get_mean_flow_AVISO(range);

addpath(genpath('/home/mdehghani/matbox/CS'));
mU=0*getU_obs('AVISO',2014001);
mV=0*getV_obs('AVISO',2014001);
mSSH=0*getSSH_obs('AVISO',2014001);

for field=range
  disp(['field: ' num2str(field)])
  mU=mU+getU_obs('AVISO',field); 
  mV=mV+getV_obs('AVISO',field);  
  mSSH=mSSH+getSSH_obs('AVISO',field);
end
  
 mU=mU/length(range);
 mV=mV/length(range);
 mSSH=mSSH/length(range);

 save('/home/mdehghani/matbox/CS/misc/meanflow_AVISO.mat'); 
