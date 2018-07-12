
USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblHOT_Bottle_KAENA](
	[botid_HOT] [bigint] NOT NULL,
	[time] [date] NOT NULL,
	[date_time] [nvarchar](6) NULL,
	--[depth] [float] NOT NULL,
	[pressure_ctd_bottle_kaena_hot] [float] NULL,
	[potential_temperature_ctd_bottle_kaena_hot] [float] NULL,
	[potential_density_ctd_bottle_kaena_hot] [float] NULL,
	[temperature_ctd_bottle_kaena_hot] [float] NULL,
	[salinity_ctd_bottle_kaena_hot] [float] NULL,
	[oxygen_ctd_bottle_kaena_hot] [float] NULL,
	[salinity_bottle_kaena_hot] [float] NULL,   		--Bottle Salinity 
	[oxygen_bottle_kaena_hot] [float] NULL,     		--Bottle Dissolved Oxygen
	[dic_bottle_kaena_hot] [float] NULL,        		--Dissolved Inorganic Carbon
	[ph_bottle_kaena_hot] [float] NULL,         		--pH
	[alk_bottle_kaena_hot] [float] NULL,        		--Alkalinity
	[PO4_bottle_kaena_hot] [float] NULL,        		--Phosphate (PO4)
	[NO2_NO3_bottle_kaena_hot] [float] NULL,    		--Nitrate (NO2 + NO3) 
	[SiO4_bottle_kaena_hot] [float] NULL,       		--Silicate (SiO4)
	[dop_bottle_kaena_hot] [float] NULL,        		--Dissolved Organic Phosphorus
	[don_bottle_kaena_hot] [float] NULL,        		--Dissolved Organic Nitrogen
	[doc_bottle_kaena_hot] [float] NULL,        		--Dissolved Organic Carbon
	[tdp_bottle_kaena_hot] [float] NULL,        		--Total Dissolved Phosphorus
	[tdn_bottle_kaena_hot] [float] NULL,    	  		--Total Dissolved Nitrogen
	[pc_bottle_kaena_hot] [float] NULL,         		--Particulate Carbon
	[pn_bottle_kaena_hot] [float] NULL,         		--Particulate Nitrogen
	[pp_bottle_kaena_hot] [float] NULL,         		--Particulate Phosphorus
	[lln_bottle_kaena_hot] [float] NULL,        		--Low-Level Nitrogen  
	[llp_bottle_kaena_hot] [float] NULL,        		--Low-Level Phosphorus
	[chl_bottle_kaena_hot] [float] NULL,        		--Fluorometric Chlorophyll a
	[phaeo_bottle_kaena_hot] [float] NULL,      		--Pheopigments
	[HPLC_chl3_bottle_kaena_hot] [float] NULL,  		--HPLC Chlorophyll c3
	[HPLC_chl12_bottle_kaena_hot] [float] NULL, 		--HPLC Chlorophyll c1+c2 
	[HPLC_chlplus_bottle_kaena_hot] [float] NULL,  		--HPLC Chlorophyll c1+c2+c3
	[HPLC_peridinin_bottle_kaena_hot] [float] NULL,   	--HPLC Peridinin
	[HPLC_but19_bottle_kaena_hot] [float] NULL,       	--HPLC 19'-Butanoyloxyfucoxanthin 
	[HPLC_fuco_bottle_kaena_hot] [float] NULL,			--HPLC Fucoxanthin	
	[HPLC_hex19_bottle_kaena_hot] [float] NULL,			--HPLC 19'-Hexanoyloxyfucoxanthin
	[HPLC_prasino_bottle_kaena_hot] [float] NULL,     	--HPLC Prasinoxanthin
	[HPLC_diadino_bottle_kaena_hot] [float] NULL,		--HPLC Diadinoxanthin
	[HPLC_zeaxan_bottle_kaena_hot] [float] NULL,		--HPLC Zeaxanthin
	[HPLC_chlb_bottle_kaena_hot] [float] NULL,			--HPLC Chlorophyll b
	[HPLC_chla_bottle_kaena_hot] [float] NULL,			--HPLC Chlorophyll a
	[HPLC_chlc4_bottle_kaena_hot] [float] NULL,			--HPLC Chlorophyll c4
	[HPLC_acar_bottle_kaena_hot] [float] NULL,			--HPLC α-Carotene
	[HPLC_bcar_bottle_kaena_hot] [float] NULL,			--HPLC β-Carotene
	[HPLC_carotenes_bottle_kaena_hot] [float] NULL,		--HPLC Carotenes (α+β)
	[HPLC_chlda_bottle_kaena_hot] [float] NULL,			--HPLC Chlorophyllide a
	[HPLC_viol_bottle_kaena_hot] [float] NULL,			--HPLC Violaxanthin
	[HPLC_lutein_bottle_kaena_hot] [float] NULL,		--HPLC Lutein
	[HPLC_mvchla_bottle_kaena_hot] [float] NULL,		--HPLC Monovinyl Chlorophyll a
	[HPLC_dvchla_bottle_kaena_hot] [float] NULL,		--HPLC Divinyl Chlorophyll a
	[hetero_bact_bottle_kaena_hot] [float] NULL,		--Heterotrophic Bacteria
	[prochlorococcus_bottle_kaena_hot] [float] NULL,	--Prochlorococcus
	[synechococcus_bottle_kaena_hot] [float] NULL,		--Synechococcus
	[eukaryotes_bottle_kaena_hot] [float] NULL,			--Eukaryotes
	[atp_bottle_kaena_hot] [float] NULL,				--Adenosine 5'-Triphosphate
	[N2O_bottle_kaena_hot] [float] NULL,				--Nitrous Oxide
	[psi_bottle_kaena_hot] [float] NULL,				--Particulate Silica	
	[pe4_bottle_kaena_hot] [float] NULL,				--Phycoerythrin 0.4µ fraction
	[pe5_bottle_kaena_hot] [float] NULL,				--Phycoerythrin 5µ fraction
	[pe10_bottle_kaena_hot] [float] NULL,				--Phycoerythrin 10µ fraction
	[p15n_bottle_kaena_hot] [float] NULL,				--δ15N of PN
	[PP_l12_bottle_kaena_hot] [float] NULL,				--Primary Production: Light 12
	[PP_d12_bottle_kaena_hot] [float] NULL,				--Primary Production: Dark 12	
	[NO2_bottle_kaena_hot] [float] NULL,				--Nitrite (NO2)	
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblHOT_Bottle_KAENA] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG1]
) ON [FG1]

GO




---------------------
-- Indices
---------------------


USE [Opedia]
GO


CREATE NONCLUSTERED INDEX [IX_tblHOT_Bottle_KAENA_time_lat_lon_depth] ON [dbo].[tblHOT_Bottle_KAENA]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC
	--[depth] ASC
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG1]
GO

