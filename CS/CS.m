function CS(itnum_starts, stop_time_day);


%*****************************    Inputs   ****************************** 
%
%  itnum_starts:    The iteration number of the first flow field file.
%
%  stop_time_day:      The period over which the advection occurs (day)
%
%************************************************************************   

addpath(genpath('./'));  % adding current floder and all subfolders to the matlab path
config_CS;
copyfile('./config/config_CS.m', trunk);
for flowloop=itnum_starts
  itnum_start=flowloop;
  [rep nrt filepath] = get_filepath(itnum_start);
  %******************** Compute Coherent Structures ************************* 
  Compute_CS;
  %************************************************************************** 
  %****************************** Plotting ********************************** 
  if flgPlot
    if flgCrop
      crop;
    end 
    if flgEulerian
      plot_Eulerian;
    end
    if flgLagrangian 
      plot_Lagrangian;
    end 
  end
  %************************************************************************** 

  %************************ Store FTLE/Vort in Vault ************************
  %vault_path = 'H:/Dropbox (MIT)/opedia_vault/raw/obs/%s/%s/%s%10.10d.mat';
  vault_path = 'H:/Dropbox (MIT)/Apps/opediaVault/observation/remote/satellite/%s/%s/%s%10.10d.mat';
  
  
  if flgEulerian         
    if nrt
        proc_level = 'nrt';
        prefix = 'nrt_';
    else    
        proc_level = 'rep';
        prefix = 'rep_';
    end    
      
    if SLA_Based
        folder = 'vort_sla';
        prefix = strcat(prefix, 'vort_sla_');
    else    
        folder = 'vort_adt';
        prefix = strcat(prefix, 'vort_adt_');
    end 
    save(sprintf(vault_path, folder, proc_level, prefix, itnum_start), 'nrt', 'rep', 'SLA_Based', 'lon', 'lat', 'vort');
  end
  
  if flgLagrangian         
    if nrt
        proc_level = 'nrt';
        prefix = 'nrt_';
    else    
        proc_level = 'rep';
        prefix = 'rep_';
    end    
    
    if forward
        folder = 'ftle_fw_';
        prefix = strcat(prefix, 'ftle_fw_');
    else
        folder = 'ftle_bw_';
        prefix = strcat(prefix, 'ftle_bw_');
    end
    
    if SLA_Based
        folder = strcat(folder, 'sla');
        prefix = strcat(prefix, 'sla_');
    else    
        folder = strcat(folder, 'adt');
        prefix = strcat(prefix, 'adt_');
    end 
    save(sprintf(vault_path, folder, proc_level, prefix, itnum_start), 'nrt', 'rep', 'SLA_Based', 'forward', 'stop_time_day', 'Xres', 'Yres', 'lon', 'lat', 'ftle', 'displacement');
  end  
  %**************************************************************************

  
  %**************************** Store Workspace *****************************
  save(strcat(MAT_Path, sprintf('%10.10d.mat',itnum_start)));
  %************************************************************************** 
end
