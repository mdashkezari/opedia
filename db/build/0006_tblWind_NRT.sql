USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblWind_NRT](
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[time] [date] NOT NULL,
	[wind_speed_rms] [float] NULL,
	[eastward_wind_rms] [float] NULL,
	[wind_stress] [float] NULL,
	[eastward_wind] [float] NULL,
	[surface_downward_eastward_stress] [float] NULL,
	[wind_speed] [float] NULL,
	[surface_downward_northward_stress] [float] NULL,
--	[sampling_length] [float] NULL,
	[northward_wind] [float] NULL,
	[northward_wind_rms] [float] NULL,
	[hour] [tinyint] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblWind_NRT] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG3]
) ON [FG3]

GO




---------------------
-- Indices
---------------------

-- No index is defined on the wind velocity fields. This may change in future, if needed.


CREATE UNIQUE NONCLUSTERED INDEX [IX_tblWind_NRT_time_lat_lon_hour] ON [dbo].[tblWind_NRT]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC,
	[hour] ASC
)
INCLUDE ([wind_stress]) 
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG3]
GO


CREATE NONCLUSTERED INDEX [IX_tblWind_NRT_windStress] ON [dbo].[tblWind_NRT]
(
	[wind_stress] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG3]
GO

/*
CREATE NONCLUSTERED INDEX [IX_tblWind_NRT_hour] ON [dbo].[tblWind_NRT]
(
	[hour] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG3]
GO
*/

