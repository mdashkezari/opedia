
USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblDarwin_Chl_Climatology](
	[depth] [float] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[month] [smallint] NOT NULL,
	[chl01_darwin_clim] [float] NULL,
	[chl02_darwin_clim] [float] NULL,
	[chl03_darwin_clim] [float] NULL,
	[chl04_darwin_clim] [float] NULL,
	[chl05_darwin_clim] [float] NULL,
	[chl06_darwin_clim] [float] NULL,
	[chl07_darwin_clim] [float] NULL,
	[chl08_darwin_clim] [float] NULL,
	[chl09_darwin_clim] [float] NULL,
	[chl10_darwin_clim] [float] NULL,
	[chl11_darwin_clim] [float] NULL,
	[chl12_darwin_clim] [float] NULL,
	[chl13_darwin_clim] [float] NULL,
	[chl14_darwin_clim] [float] NULL,
	[chl15_darwin_clim] [float] NULL,
	[chl16_darwin_clim] [float] NULL,
	[chl17_darwin_clim] [float] NULL,
	[chl18_darwin_clim] [float] NULL,
	[chl19_darwin_clim] [float] NULL,
	[chl20_darwin_clim] [float] NULL,
	[chl21_darwin_clim] [float] NULL,
	[chl22_darwin_clim] [float] NULL,
	[chl23_darwin_clim] [float] NULL,
	[chl24_darwin_clim] [float] NULL,
	[chl25_darwin_clim] [float] NULL,
	[chl26_darwin_clim] [float] NULL,
	[chl27_darwin_clim] [float] NULL,
	[chl28_darwin_clim] [float] NULL,
	[chl29_darwin_clim] [float] NULL,
	[chl30_darwin_clim] [float] NULL,
	[chl31_darwin_clim] [float] NULL,
	[chl32_darwin_clim] [float] NULL,
	[chl33_darwin_clim] [float] NULL,
	[chl34_darwin_clim] [float] NULL,
	[chl35_darwin_clim] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblDarwin_Chl_Climatology] PRIMARY KEY CLUSTERED 
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


CREATE UNIQUE NONCLUSTERED INDEX [IX_tblDarwin_Chl_Climatology_month_lat_lon_depth] ON [dbo].[tblDarwin_Chl_Climatology]
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