USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblModis_AOD_REP](
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[time] [date] NOT NULL,
	[AOD] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_Modis_AOD_REP] PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG2]
) ON [FG2]

GO




---------------------
-- Indices
---------------------



CREATE UNIQUE NONCLUSTERED INDEX [IX_tblModis_AOD_REP_time_lat_lon] ON [dbo].[tblModis_AOD_REP]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC
)
INCLUDE ([AOD])
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG2]
GO