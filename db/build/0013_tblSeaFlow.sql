USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO
--



CREATE TABLE [dbo].[tblSeaFlow](
	[time] [datetime] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[depth] [float] NOT NULL,
  [prochloro_abundance] [float] NULL,
  [prochloro_diameter] [float] NULL,
  [prochloro_carbon_content] [float] NULL,
  [prochloro_biomass] [float] NULL,
  [synecho_abundance] [float] NULL,
  [synecho_diameter] [float] NULL,
  [synecho_carbon_content] [float] NULL,
  [synecho_biomass] [float] NULL,
  [croco_abundance] [float] NULL,
  [croco_diameter] [float] NULL,
  [croco_carbon_content] [float] NULL,
  [croco_biomass] [float] NULL,
  [picoeuk_abundance] [float] NULL,
  [picoeuk_diameter] [float] NULL,
  [picoeuk_carbon_content] [float] NULL,
  [picoeuk_biomass] [float] NULL,
  [unknown_abundance] [float] NULL,
  [unknown_diameter] [float] NULL,
  [unknown_carbon_content] [float] NULL,
  [unknown_biomass] [float] NULL,
  [total_biomass] [float] NULL,
  [par] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblSeaFlow] PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG1]
) ON [FG1]

GO




CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_time_lat_lon] ON [dbo].[tblSeaFlow]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC
)
INCLUDE (
[prochloro_abundance],
[prochloro_diameter],
[prochloro_carbon_content],
[prochloro_biomass],
[synecho_abundance],
[synecho_diameter],
[synecho_carbon_content],
[synecho_biomass],
[croco_abundance],
[croco_diameter],
[croco_carbon_content],
[croco_biomass],
[picoeuk_abundance],
[picoeuk_diameter],
[picoeuk_carbon_content],
[picoeuk_biomass],
[unknown_abundance],
[unknown_diameter],
[unknown_carbon_content],
[unknown_biomass],
[total_biomass]
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG1]
GO



--
--
-- CREATE TABLE [dbo].[tblSeaFlow](
-- 	[time] [datetime] NOT NULL,
-- 	[lat] [float] NOT NULL,
-- 	[lon] [float] NOT NULL,
-- 	[depth] [float] NOT NULL,
--   [prochloro_abundance] [float] NULL,
--   [prochloro_diameter] [float] NULL,
--   [prochloro_carbon_content] [float] NULL,
--   [prochloro_biomass] [float] NULL,
--   [synecho_abundance] [float] NULL,
--   [synecho_diameter] [float] NULL,
--   [synecho_carbon_content] [float] NULL,
--   [synecho_biomass] [float] NULL,
--   [croco_abundance] [float] NULL,
--   [croco_diameter] [float] NULL,
--   [croco_carbon_content] [float] NULL,
--   [croco_biomass] [float] NULL,
--   [picoeuk_abundance] [float] NULL,
--   [picoeuk_diameter] [float] NULL,
--   [picoeuk_carbon_content] [float] NULL,
--   [picoeuk_biomass] [float] NULL,
--   [unknown_abundance] [float] NULL,
--   [unknown_diameter] [float] NULL,
--   [unknown_carbon_content] [float] NULL,
--   [unknown_biomass] [float] NULL,
--   [total_biomass] [float] NULL,
--   [temp] [float] NULL,
--   [salinity] [float] NULL,
--   [par] [float] NULL,
--   [quantile] [float] NULL,
--   [pop] [nvarchar](50) NULL,
--   [chl_small] [float] NULL,
--   [pe] [float] NULL,
--   [fsc_small] [float] NULL,
--   [diam_lwr] [float] NULL,
--   [diam_mid] [float] NULL,
--   [diam_upr] [float] NULL,
--   [Qc_lwr] [float] NULL,
--   [Qc_mid] [float] NULL,
--   [Qc_upr] [float] NULL,
--   [abundance] [float] NULL,
--   [abundance_se] [float] NULL,
--   [cruise] [nvarchar](100) NULL,
--   [serial] [float] NULL,
--   [flag] [float] NULL,
-- 	[ID] [bigint] IDENTITY(1,1) NOT NULL,
--  CONSTRAINT [PK_tblSeaFlow] PRIMARY KEY CLUSTERED
-- (
-- 	[ID] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG1]
-- ) ON [FG1]
--
-- GO

-- CREATE TABLE [dbo].[tblSeaFlow](
-- 	[time] [datetime] NOT NULL,
-- 	[lat] [float] NOT NULL,
-- 	[lon] [float] NOT NULL,
-- 	[cruise] [nvarchar](100) NULL,
-- 	[opp_evt_ratio] [float] NULL,
-- 	[flow_rate] [float] NULL,
-- 	[file_duration] [float] NULL,
-- 	[pop] [nvarchar](50) NULL,
-- 	[n_count] [float] NULL,
-- 	[abundance] [float] NULL,
-- 	[fsc_small_mean] [float] NULL,
-- 	[chl_small_mean] [float] NULL,
-- 	[pe_mean] [float] NULL,
-- 	[fsc_perp_mean] [float] NULL,
-- 	[flag] [float] NULL,
-- 	[year] [float] NULL,
-- 	[month] [float] NULL,
-- 	[day] [float] NULL,
-- 	[hour] [float] NULL,
-- 	[minute] [float] NULL,
-- 	[second] [float] NULL,
-- 	[sla] [float] NULL,
-- 	[grad_sla] [float] NULL,
-- 	[sst] [float] NULL,
-- 	[grad_sst] [float] NULL,
-- 	[chl] [float] NULL,
-- 	[grad_chl] [float] NULL,
-- 	[wind_stress] [float] NULL,
-- 	[grad_wind_stress] [float] NULL,
-- 	[REP_ftle_BWD_ADT] [float] NULL,
-- 	[REP_ftle_BWD_SLA] [float] NULL,
-- 	[REP_ftle_FWD_ADT] [float] NULL,
-- 	[REP_ftle_FWD_SLA] [float] NULL,
-- 	[NRT_ftle_BWD_ADT] [float] NULL,
-- 	[NRT_ftle_BWD_SLA] [float] NULL,
-- 	[NRT_ftle_FWD_ADT] [float] NULL,
-- 	[NRT_ftle_FWD_SLA] [float] NULL,
-- 	[REP_grad_ftle_BWD_ADT] [float] NULL,
-- 	[REP_grad_ftle_BWD_SLA] [float] NULL,
-- 	[REP_grad_ftle_FWD_ADT] [float] NULL,
-- 	[REP_grad_ftle_FWD_SLA] [float] NULL,
-- 	[NRT_grad_ftle_BWD_ADT] [float] NULL,
-- 	[NRT_grad_ftle_BWD_SLA] [float] NULL,
-- 	[NRT_grad_ftle_FWD_ADT] [float] NULL,
-- 	[NRT_grad_ftle_FWD_SLA] [float] NULL,
-- 	[REP_disp_BWD_ADT] [float] NULL,
-- 	[REP_disp_BWD_SLA] [float] NULL,
-- 	[REP_disp_FWD_ADT] [float] NULL,
-- 	[REP_disp_FWD_SLA] [float] NULL,
-- 	[NRT_disp_BWD_ADT] [float] NULL,
-- 	[NRT_disp_BWD_SLA] [float] NULL,
-- 	[NRT_disp_FWD_ADT] [float] NULL,
-- 	[NRT_disp_FWD_SLA] [float] NULL,
-- 	[REP_grad_disp_BWD_ADT] [float] NULL,
-- 	[REP_grad_disp_BWD_SLA] [float] NULL,
-- 	[REP_grad_disp_FWD_ADT] [float] NULL,
-- 	[REP_grad_disp_FWD_SLA] [float] NULL,
-- 	[NRT_grad_disp_BWD_ADT] [float] NULL,
-- 	[NRT_grad_disp_BWD_SLA] [float] NULL,
-- 	[NRT_grad_disp_FWD_ADT] [float] NULL,
-- 	[NRT_grad_disp_FWD_SLA] [float] NULL,
-- 	[ID] [bigint] IDENTITY(1,1) NOT NULL,
--  CONSTRAINT [PK_tblSeaFlow] PRIMARY KEY CLUSTERED
-- (
-- 	[ID] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG1]
-- ) ON [FG1]
--
-- GO
--
--
--
--
-- ---------------------
-- -- Indices
-- ---------------------
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_time_lat_lon] ON [dbo].[tblSeaFlow]
-- (
-- 	[time] ASC,
-- 	[lat] ASC,
-- 	[lon] ASC
-- )
-- INCLUDE ([abundance], [pop], [sla], [sst], [chl], [wind_stress])
-- WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_cruise] ON [dbo].[tblSeaFlow]
-- (
-- 	[cruise] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_year] ON [dbo].[tblSeaFlow]
-- (
-- 	[year] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
-- CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_month] ON [dbo].[tblSeaFlow]
-- (
-- 	[month] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_sla] ON [dbo].[tblSeaFlow]
-- (
-- 	[sla] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_sst] ON [dbo].[tblSeaFlow]
-- (
-- 	[sst] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_chl] ON [dbo].[tblSeaFlow]
-- (
-- 	[chl] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_wind_stress] ON [dbo].[tblSeaFlow]
-- (
-- 	[wind_stress] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_hour] ON [dbo].[tblSeaFlow]
-- (
-- 	[hour] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_abundance] ON [dbo].[tblSeaFlow]
-- (
-- 	[abundance] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_pop] ON [dbo].[tblSeaFlow]
-- (
-- 	[pop] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
--
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_REP_ftle_BWD_ADT] ON [dbo].[tblSeaFlow]
-- (
-- 	[REP_ftle_BWD_ADT] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_REP_ftle_FWD_ADT] ON [dbo].[tblSeaFlow]
-- (
-- 	[REP_ftle_FWD_ADT] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
