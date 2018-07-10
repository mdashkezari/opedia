
USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblHOT_EpiMicroscopy](
	[botid_HOT] [int] NOT NULL,
	[time] [date] NOT NULL,
	[depth] [float] NOT NULL,
	[diatom_hot] [float] NULL,
	[prymnesiophytes_hot] [float] NULL,
	[autotrophic_dinoflagellates_hot] [float] NULL,
	[crocosphaera_hot] [float] NULL,
	[trichodesmium_hot] [float] NULL,
	[other_autotrophs_hot] [float] NULL,
	[autotroph_biomass_frac1_hot] [float] NULL,
	[autotroph_biomass_frac2_hot] [float] NULL,
	[autotroph_biomass_frac3_hot] [float] NULL,
	[autotroph_biomass_frac4_hot] [float] NULL,
	[autotroph_biomass_frac5_hot] [float] NULL,
	[autotroph_biomass_frac6_hot] [float] NULL,
	[heterotrophic_dinoflagellate_hot] [float] NULL,
	[other_heterotrophs_hot] [float] NULL,
	[heterotroph_biomass_frac1_hot] [float] NULL,
	[heterotroph_biomass_frac2_hot] [float] NULL,
	[heterotroph_biomass_frac3_hot] [float] NULL,
	[heterotroph_biomass_frac4_hot] [float] NULL,
	[heterotroph_biomass_frac5_hot] [float] NULL,
	[heterotroph_biomass_frac6_hot] [float] NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblHOT_EpiMicroscopy] PRIMARY KEY CLUSTERED 
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


CREATE NONCLUSTERED INDEX [IX_tblHOT_EpiMicroscopy_time_lat_lon_depth] ON [dbo].[tblHOT_EpiMicroscopy]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC,
	[depth] ASC
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG1]
GO

