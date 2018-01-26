USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblSeaFlow](
	[cruise] [nvarchar](100) NULL,
	[time] [datetime] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[opp_evt_ratio] [float] NULL,
	[flow_rate] [float] NULL,
	[file_duration] [float] NULL,
	[pop] [nvarchar](50) NULL,
	[n_count] [float] NULL,
	[abundance] [float] NULL,
	[fsc_small_mean] [float] NULL,
	[chl_small_mean] [float] NULL,
	[pe_mean] [float] NULL,
	[fsc_perp_mean] [float] NULL,
	[flag] [float] NULL,
	[year] [float] NULL,
	[month] [float] NULL,
	[day] [float] NULL,
	[hour] [float] NULL,
	[minute] [float] NULL,
	[second] [float] NULL,
	[sla] [float] NULL,
	[grad_sla] [float] NULL,
	[sst] [float] NULL,
	[grad_sst] [float] NULL,
	[chl] [float] NULL,
	[grad_chl] [float] NULL,
	[wind_stress] [float] NULL,
	[grad_wind_stress] [float] NULL,
	[REP_ftle_BWD_ADT] [float] NULL,
	[REP_ftle_BWD_SLA] [float] NULL,
	[REP_ftle_FWD_ADT] [float] NULL,
	[REP_ftle_FWD_SLA] [float] NULL,
	[NRT_ftle_BWD_ADT] [float] NULL,
	[NRT_ftle_BWD_SLA] [float] NULL,
	[NRT_ftle_FWD_ADT] [float] NULL,
	[NRT_ftle_FWD_SLA] [float] NULL,
	[REP_grad_ftle_BWD_ADT] [float] NULL,
	[REP_grad_ftle_BWD_SLA] [float] NULL,
	[REP_grad_ftle_FWD_ADT] [float] NULL,
	[REP_grad_ftle_FWD_SLA] [float] NULL,
	[NRT_grad_ftle_BWD_ADT] [float] NULL,
	[NRT_grad_ftle_BWD_SLA] [float] NULL,
	[NRT_grad_ftle_FWD_ADT] [float] NULL,
	[NRT_grad_ftle_FWD_SLA] [float] NULL,
	[REP_disp_BWD_ADT] [float] NULL,
	[REP_disp_BWD_SLA] [float] NULL,
	[REP_disp_FWD_ADT] [float] NULL,
	[REP_disp_FWD_SLA] [float] NULL,
	[NRT_disp_BWD_ADT] [float] NULL,
	[NRT_disp_BWD_SLA] [float] NULL,
	[NRT_disp_FWD_ADT] [float] NULL,
	[NRT_disp_FWD_SLA] [float] NULL,
	[REP_grad_disp_BWD_ADT] [float] NULL,
	[REP_grad_disp_BWD_SLA] [float] NULL,
	[REP_grad_disp_FWD_ADT] [float] NULL,
	[REP_grad_disp_FWD_SLA] [float] NULL,
	[NRT_grad_disp_BWD_ADT] [float] NULL,
	[NRT_grad_disp_BWD_SLA] [float] NULL,
	[NRT_grad_disp_FWD_ADT] [float] NULL,
	[NRT_grad_disp_FWD_SLA] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblSeaFlow] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG1]
) ON [FG1]

GO




---------------------
-- Indices
---------------------


CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_time_lat_lon] ON [dbo].[tblSeaFlow]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC
)
INCLUDE ([abundance], [pop], [sla], [sst], [chl], [wind_stress]) 
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG1]
GO


CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_cruise] ON [dbo].[tblSeaFlow]
(
	[cruise] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO


CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_year] ON [dbo].[tblSeaFlow]
(
	[year] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO

CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_month] ON [dbo].[tblSeaFlow]
(
	[month] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO


CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_sla] ON [dbo].[tblSeaFlow]
(
	[sla] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO


CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_sst] ON [dbo].[tblSeaFlow]
(
	[sst] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO


CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_chl] ON [dbo].[tblSeaFlow]
(
	[chl] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO


CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_wind_stress] ON [dbo].[tblSeaFlow]
(
	[wind_stress] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO


CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_hour] ON [dbo].[tblSeaFlow]
(
	[hour] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO


CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_abundance] ON [dbo].[tblSeaFlow]
(
	[abundance] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO


CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_pop] ON [dbo].[tblSeaFlow]
(
	[pop] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO




CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_REP_ftle_BWD_ADT] ON [dbo].[tblSeaFlow]
(
	[REP_ftle_BWD_ADT] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO



CREATE NONCLUSTERED INDEX [IX_tblSeaFlow_REP_ftle_FWD_ADT] ON [dbo].[tblSeaFlow]
(
	[REP_ftle_FWD_ADT] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO
