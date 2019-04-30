
USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





CREATE TABLE [dbo].[tblBottle_Chisholm](
	[time] [date] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[depth] [float] NOT NULL,
	[theta_cmor] [float] NULL,
	[sigma_cmore] [float] NULL,
	[temp_cmore] [float] NULL,
	[csal_cmore] [float] NULL,
	[coxy_cmore] [float] NULL,
	[chlpig_cmore] [float] NULL,
	[boxy_cmore] [float] NULL,
	[dic_cmore] [float] NULL,
	[alk_cmore] [float] NULL,
	[phos_cmore] [float] NULL,
	[nit_cmore] [float] NULL,
	[sil_cmore] [float] NULL,
	[pc_cmore] [float] NULL,
	[pn_cmore] [float] NULL,
	[pp_cmore] [float] NULL,
	[chlda_cmore] [float] NULL,
	[chlplus_cmore] [float] NULL,
	[perid_cmore] [float] NULL,
	[but19_cmore] [float] NULL,
	[fuco_cmore] [float] NULL,
	[hex19_cmore] [float] NULL,
	[prasino_cmore] [float] NULL,
	[viol_cmore] [float] NULL,
	[diadino_cmore] [float] NULL,
	[allox_cmore] [float] NULL,
	[lutein_cmore] [float] NULL,
	[zeaxan_cmore] [float] NULL,
	[chlb_cmore] [float] NULL,
	[acar_cmore] [float] NULL,
	[bcar_cmore] [float] NULL,
	[dvchla_cmore] [float] NULL,
	[mvchla_cmore] [float] NULL,
	[hplc_cmore] [float] NULL,
	[hbact_cmore] [float] NULL,
	[pbact_Chisholm] [float] NULL,
	[sbact_cmore] [float] NULL,
	[ebact_cmore] [float] NULL,
	[NO2_cmore] [float] NULL,
	[NH4_cmore] [float] NULL,
	[pbact_quality_Chisholm] [float] NULL,
	[ProChl_Chisholm] [float] NULL,
	[ProFSC_Chisholm] [float] NULL,
	[MIT9312PCR_Chisholm] [float] NULL,
	[MIT9312PCR_quality_Chisholm] [float] NULL,
	[MED4PCR_Chisholm] [float] NULL,
	[MED4PCR_quality_Chisholm] [float] NULL,
	[HL3PCR_Chisholm] [float] NULL,
	[HL3PCR_quality_Chisholm] [float] NULL,
	[HL4PCR_Chisholm] [float] NULL,
	[HL4PCR_quality_Chisholm] [float] NULL,
	[NATL2APCR_Chisholm] [float] NULL,
	[NATL2APCR_quality_Chisholm] [float] NULL,
	[MIT9313PCR_Chisholm] [float] NULL,
	[MIT9313PCR_quality_Chisholm] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblBottle_Chisholm] PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (/*DATA_COMPRESSION = PAGE,*/ PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG1]
) ON [FG1]

GO



-- -------------------
-- Indices
-- -------------------
--


CREATE NONCLUSTERED INDEX [IX_tblBottle_Chisholm_time_lat_lon] ON [dbo].[tblBottle_Chisholm]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC,
	[depth] ASC
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG2]
GO
