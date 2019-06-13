
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
  [AOU_WOA_clim] [float] NULL,
  [AOU_stat_mean_WOA_clim] [float] NULL,
  [AOU_num_obs_WOA_clim] [float] NULL,
  [AOU_stdev_WOA_clim] [float] NULL,
  [AOU_stderr_WOA_clim] [float] NULL,
  [density_WOA_clim] [float] NULL,
  [density_stat_mean_WOA_clim] [float] NULL,
  [density_num_obs_WOA_clim] [float] NULL,
  [density_stdev_WOA_clim] [float] NULL,
  [o2sat_WOA_clim] [float] NULL,
  [o2sat_stat_mean_WOA_clim] [float] NULL,
  [o2sat_num_obs_WOA_clim] [float] NULL,
  [o2sat_stdev_WOA_clim] [float] NULL,
  [o2sat_stderr_WOA_clim] [float] NULL,
  [oxygen_WOA_clim] [float] NULL,
  [oxygen_stat_mean_WOA_clim] [float] NULL,
  [oxygen_num_obs_WOA_clim] [float] NULL,
  [oxygen_stdev_WOA_clim] [float] NULL,
  [oxygen_stderr_WOA_clim] [float] NULL,
  [salinity_WOA_clim] [float] NULL,
  [salinity_stat_mean_WOA_clim] [float] NULL,
  [salinity_num_obs_WOA_clim] [float] NULL,
  [salinity_stdev_WOA_clim] [float] NULL,
  [salinity_stderr_WOA_clim] [float] NULL,
  [conductivity_WOA_clim] [float] NULL,
  [conductivity_stat_mean_WOA_clim] [float] NULL,
  [conductivity_num_obs_WOA_clim] [float] NULL,
  [conductivity_stdev_WOA_clim] [float] NULL,
  [sea_water_temp_WOA_clim] [float] NULL,
  [sea_water_temp_stat_mean_WOA_clim] [float] NULL,
  [sea_water_temp_num_obs_WOA_clim] [float] NULL,
  [sea_water_temp_stdev_WOA_clim] [float] NULL,
  [sea_water_temp_stderr_WOA_clim] [float] NULL,
  [nitrate_WOA_clim] [float] NULL,
  [nitrate_stat_mean_WOA_clim] [float] NULL,
  [nitrate_num_obs_WOA_clim] [float] NULL,
  [nitrate_stdev_WOA_clim] [float] NULL,
  [nitrate_stderr_WOA_clim] [float] NULL,
  [phosphate_WOA_clim] [float] NULL,
  [phosphate_stat_mean_WOA_clim] [float] NULL,
  [phosphate_num_obs_WOA_clim] [float] NULL,
  [phosphate_stdev_WOA_clim] [float] NULL,
  [phosphate_stderr_WOA_clim] [float] NULL,
  [silicate_WOA_clim] [float] NULL,
  [silicate_stat_mean_WOA_clim] [float] NULL,
  [silicate_num_obs_WOA_clim] [float] NULL,
  [silicate_stdev_WOA_clim] [float] NULL,
  [silicate_stderr_WOA_clim] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblWOA_Climatology] PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (/*DATA_COMPRESSION = PAGE,*/ PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG4]
) ON [FG4]

GO




---------------------
-- Indices
---------------------



USE [Opedia]
GO


CREATE UNIQUE NONCLUSTERED INDEX [IX_tblWOA_Climatology_month_lat_lon_depth] ON [dbo].[tblWOA_Climatology]
(
	[month] ASC,
	[lat] ASC,
	[lon] ASC,
	[depth] ASC
)
INCLUDE ([AOU_WOA_clim],[density_WOA_clim],[o2sat_WOA_clim],[oxygen_WOA_clim],[salinity_WOA_clim],[conductivity_WOA_clim],[sea_water_temp_WOA_clim],[nitrate_WOA_clim],[phosphate_WOA_clim],[silicate_WOA_clim]
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG4]
GO
