
USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblDarwin_Plankton_Climatology](
	[depth] [float] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[month] [smallint] NOT NULL,
	[prokaryote_c01_darwin_clim] [float] NULL,
	[prokaryote_c02_darwin_clim] [float] NULL,
	[picoeukaryote_c03_darwin_clim] [float] NULL,
	[picoeukaryote_c04_darwin_clim] [float] NULL,
	[cocco_c05_darwin_clim] [float] NULL,
	[cocco_c06_darwin_clim] [float] NULL,
	[cocco_c07_darwin_clim] [float] NULL,
	[cocco_c08_darwin_clim] [float] NULL,
	[cocco_c09_darwin_clim] [float] NULL,
	[diazotroph_c10_darwin_clim] [float] NULL,
	[diazotroph_c11_darwin_clim] [float] NULL,
	[diazotroph_c12_darwin_clim] [float] NULL,
	[diazotroph_c13_darwin_clim] [float] NULL,
	[diazotroph_c14_darwin_clim] [float] NULL,
	[diatom_c15_darwin_clim] [float] NULL,
	[diatom_c16_darwin_clim] [float] NULL,
	[diatom_c17_darwin_clim] [float] NULL,
	[diatom_c18_darwin_clim] [float] NULL,
	[diatom_c19_darwin_clim] [float] NULL,
	[diatom_c20_darwin_clim] [float] NULL,
	[diatom_c21_darwin_clim] [float] NULL,
	[diatom_c22_darwin_clim] [float] NULL,
	[diatom_c23_darwin_clim] [float] NULL,
	[diatom_c24_darwin_clim] [float] NULL,
	[diatom_c25_darwin_clim] [float] NULL,
	[dinoflagellate_c26_darwin_clim] [float] NULL,
	[dinoflagellate_c27_darwin_clim] [float] NULL,
	[dinoflagellate_c28_darwin_clim] [float] NULL,
	[dinoflagellate_c29_darwin_clim] [float] NULL,
	[dinoflagellate_c30_darwin_clim] [float] NULL,
	[dinoflagellate_c31_darwin_clim] [float] NULL,
	[dinoflagellate_c32_darwin_clim] [float] NULL,
	[dinoflagellate_c33_darwin_clim] [float] NULL,
	[dinoflagellate_c34_darwin_clim] [float] NULL,
	[dinoflagellate_c35_darwin_clim] [float] NULL,
	[zooplankton_c36_darwin_clim] [float] NULL,
	[zooplankton_c37_darwin_clim] [float] NULL,
	[zooplankton_c38_darwin_clim] [float] NULL,
	[zooplankton_c39_darwin_clim] [float] NULL,
	[zooplankton_c40_darwin_clim] [float] NULL,
	[zooplankton_c41_darwin_clim] [float] NULL,
	[zooplankton_c42_darwin_clim] [float] NULL,
	[zooplankton_c43_darwin_clim] [float] NULL,
	[zooplankton_c44_darwin_clim] [float] NULL,
	[zooplankton_c45_darwin_clim] [float] NULL,
	[zooplankton_c46_darwin_clim] [float] NULL,
	[zooplankton_c47_darwin_clim] [float] NULL,
	[zooplankton_c48_darwin_clim] [float] NULL,
	[zooplankton_c49_darwin_clim] [float] NULL,
	[zooplankton_c50_darwin_clim] [float] NULL,
	[zooplankton_c51_darwin_clim] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblDarwin_Plankton_Climatology] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (/*DATA_COMPRESSION = PAGE,*/ PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG4]
) ON [FG4]

GO




---------------------
-- Indices
---------------------

/*

USE [Opedia]
GO


CREATE UNIQUE NONCLUSTERED INDEX [IX_tblDarwin_Plankton_Climatology_month_lat_lon_depth] ON [dbo].[tblDarwin_Plankton_Climatology]
(
	[month] ASC,
	[lat] ASC,
	[lon] ASC,
	[depth] ASC
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG4]
GO


*/