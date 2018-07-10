
USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblHOT_CTD](
	[cruise_number_HOT] [int] NOT NULL,
	[time] [date] NOT NULL,
	--[depth] [float] NOT NULL,
	[pressure_ctd_hot] [float] NULL,
	[potential_temperature_ctd_hot] [float] NULL,
	[potential_density_ctd_hot] [float] NULL,
	[temperature_ctd_hot] [float] NULL,
	[salinity_ctd_hot] [float] NULL,
	[oxygen_ctd_hot] [float] NULL,
	[transmission_ctd_hot] [float] NULL,
	[chloropigment_ctd_hot] [float] NULL,
	[nitrate_ctd_hot] [float] NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblHOT_CTD] PRIMARY KEY CLUSTERED 
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


CREATE NONCLUSTERED INDEX [IX_tblHOT_CTD_time_lat_lon_depth] ON [dbo].[tblHOT_CTD]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC
	--[depth] ASC
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG1]
GO

