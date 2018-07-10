
USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblHOT_PP](
	[cruise_number_HOT] [int] NOT NULL,
	[time] [date] NOT NULL,
	[start_time] [nvarchar](4) NULL,
	[end_time] [nvarchar](4) NULL,
	[itype] [smallint] NULL,
	[depth] [float] NOT NULL,
	[chl_hot] [float] NULL,
	[pheopigments_hot] [float] NULL,
	[light_12_hot] [float] NULL,
	[dark_12_hot] [float] NULL,
	[salinity_hot] [float] NULL,
	[prochlorococcus_hot] [float] NULL,
	[heterotrophic_bacteria_hot] [float] NULL,
	[synechococcus_hot] [float] NULL,
	[eukaryotes_hot] [float] NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblHOT_PP] PRIMARY KEY CLUSTERED 
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


CREATE UNIQUE NONCLUSTERED INDEX [IX_tblHOT_PP_time_lat_lon_depth] ON [dbo].[tblHOT_PP]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC,
	[depth] ASC,
	[itype] ASC
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG1]
GO

