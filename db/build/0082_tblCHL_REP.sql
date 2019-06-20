USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblCHL_REP](
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[time] [date] NOT NULL,
	[chl] [float] NULL
) ON [FG2]
GO




---------------------
-- Indices
---------------------



CREATE UNIQUE NONCLUSTERED INDEX [IX_tblCHL_REP_time_lat_lon] ON [dbo].[tblCHL_REP]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC
)
INCLUDE ([chl]) 
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG2]
GO

