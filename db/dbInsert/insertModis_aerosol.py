
import sys
sys.path.append('../')
import insertFunctions as iF
import config_vault as cfgv


############################
########### OPTS ###########
tableName = 'tblModis_AOD_REP'
rawFilePath = cfgv.rep_modis_aerosol_raw
removeCols = ['Cloud_Optical_Thickness_bnds', 'Cloud_Top_Pressure_bnds', 'Cloud_Top_Pressure_Total_Mean','Cloud_Top_Pressure_Pixel_Counts','Cloud_Fraction_Mask_Total_Mean','Cloud_Mask_Pixel_Counts','Cloud_Optical_Thickness_Liquid_Mean','Cloud_Optical_Thickness_Liquid_Uncertainty_in_Mean','Cloud_Optical_Thickness_Liquid_Uncertainty_in_MeanLog10','Cloud_Optical_Thickness_Liquid_MeanLog10','Cloud_Optical_Thickness_Ice_Mean','Cloud_Optical_Thickness_Ice_Uncertainty_in_Mean','Cloud_Optical_Thickness_Ice_Uncertainty_in_MeanLog10','Cloud_Optical_Thickness_Ice_MeanLog10','Cloud_Optical_Thickness_Total_MeanLog10','Optical_Thickness_vs_Cloud_Top_Pressure','Cloud_Particle_Size_Liquid_Mean','Cloud_Particle_Size_Liquid_Uncertainty_in_Mean','Cloud_Particle_Size_Ice_Mean','Cloud_Particle_Size_Ice_Uncertainty_in_Mean','Cloud_Fraction_Retrieval_Liquid_Mean','Cloud_Retrieval_Liquid_Pixel_Counts','Cloud_Fraction_Retrieval_Ice_Mean','Cloud_Retrieval_Ice_Pixel_Counts','Cloud_Fraction_Retrieval_Total_Mean','Cloud_Retrieval_Total_Pixel_Counts','Liquid_Path_Mean','Liquid_Path_Uncertainty_in_Mean','Ice_Path_Mean','Ice_Path_Uncertainty_in_Mean','Cloud_Fraction_Retrieval_High_Mean','Cloud_Fraction_Retrieval_Mid_Mean','Cloud_Fraction_Retrieval_Low_Mean','Cloud_Fraction_Mask_High_Mean','Cloud_Fraction_Mask_Mid_Mean','Cloud_Fraction_Mask_Low_Mean']

keepCols = ['AOD_550_Dark_Target_Deep_Blue_Combined_Mean_Mean']
############################
############################

iF.cleanStrucHDF_modis(rawFilePath, tableName, removeCols, opt_select_cols=keepCols)

iF.toSQLbcp(rawFileName, tableName, removeCols)
