function [mU mV mSSH]=get_mean_flow_CCAR(range);

addpath(genpath('/home/mdehghani/matbox/CS'));
mU=0*getU_obs('CCRA',2015001);
mV=0*getV_obs('CCRA',2015001);
mSSH=0*getSSH_obs('CCRA',2015001);

for field=range
  disp(['field: ' num2str(field)])
  mU=mU+getU_obs('CCRA',field); 
  mV=mV+getV_obs('CCRA',field);  
  mSSH=mSSH+getSSH_obs('CCRA',field);
end
  
 mU=mU/length(range);
 mV=mV/length(range);
 mSSH=mSSH/length(range);

 save('/home/mdehghani/matbox/CS/misc/meanflow.mat'); 
