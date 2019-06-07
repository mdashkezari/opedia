
USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblWOA_Climatology](
	[depth] [float] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[month] [smallint] NOT NULL,
	[DIC_darwin_clim] [float] NULL,
	[NH4_darwin_clim] [float] NULL,
	[NO2_darwin_clim] [float] NULL,
	[NO3_darwin_clim] [float] NULL,
	[PO4_darwin_clim] [float] NULL,
	[SiO2_darwin_clim] [float] NULL,
	[FeT_darwin_clim] [float] NULL,
	[DOC_darwin_clim] [float] NULL,
	[DON_darwin_clim] [float] NULL,
	[DOP_darwin_clim] [float] NULL,
	[DOFe_darwin_clim] [float] NULL,
	[POC_darwin_clim] [float] NULL,
	[PON_darwin_clim] [float] NULL,
	[POP_darwin_clim] [float] NULL,
	[POSi_darwin_clim] [float] NULL,
	[POFe_darwin_clim] [float] NULL,
	[PIC_darwin_clim] [float] NULL,
	[ALK_darwin_clim] [float] NULL,
	[O2_darwin_clim] [float] NULL,
	[CDOM_darwin_clim] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblDarwin_Nutrient_Climatology] PRIMARY KEY CLUSTERED
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


CREATE UNIQUE NONCLUSTERED INDEX [IX_tblDarwin_Nutrient_Climatology_month_lat_lon_depth] ON [dbo].[tblDarwin_Nutrient_Climatology]
(
	[month] ASC,
	[lat] ASC,
	[lon] ASC,
	[depth] ASC
)
INCLUDE ([DOFe_darwin_clim], [NH4_darwin_clim], [NO3_darwin_clim], [NO2_darwin_clim], [PO4_darwin_clim], [O2_darwin_clim])
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG4]
GO


CREATE NONCLUSTERED INDEX [IX_tblDarwin_Nutrient_Climatology_DOFe] ON [dbo].[tblDarwin_Nutrient_Climatology]
(
	[DOFe_darwin_clim] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG4]
GO


CREATE NONCLUSTERED INDEX [IX_tblDarwin_Nutrient_Climatology_NO3] ON [dbo].[tblDarwin_Nutrient_Climatology]
(
	[NO3_darwin_clim] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG4]
GO


CREATE NONCLUSTERED INDEX [IX_tblDarwin_Nutrient_Climatology_PO4] ON [dbo].[tblDarwin_Nutrient_Climatology]
(
	[PO4_darwin_clim] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG4]
GO


CREATE NONCLUSTERED INDEX [IX_tblDarwin_Nutrient_Climatology_O2] ON [dbo].[tblDarwin_Nutrient_Climatology]
(
	[O2_darwin_clim] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG4]
GO



*/
