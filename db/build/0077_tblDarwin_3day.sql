
USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblDarwin_3day](
	[time] [date] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[Chl050_darwin_3day] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblDarwin_3day] PRIMARY KEY CLUSTERED
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


CREATE UNIQUE NONCLUSTERED INDEX [IX_tblDarwin_3day_time_lat_lon] ON [dbo].[tblDarwin_3day]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC
)
INCLUDE ([Chl050_darwin_3day])
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG4]
GO



*/




/*
-- columnstore index

CREATE NONCLUSTERED COLUMNSTORE INDEX [IX_tblDarwin_3day_time_lat_lon] ON [dbo].[tblDarwin_3day]
(
	[time],
	[lat] ,
	[lon]
)
WITH (DATA_COMPRESSION = COLUMNSTORE)
ON [FG4]
GO

*/
