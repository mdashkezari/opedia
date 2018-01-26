USE [Opedia]
GO


SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblSOCAT](
	[year] [int] NOT NULL,
	[month] [int] NOT NULL,
	[day] [int] NOT NULL,
	[hour] [int] NOT NULL,
	[minute] [int] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[quality_control] [smallint] NOT NULL,
	[salinity] [float] NULL,
	[insitu_sst] [float] NULL,
	[pressure_atm] [float] NULL,
	[delta_pco2] [float] NULL,
	[delta_fco2] [float] NULL,
	[fco2] [float] NOT NULL,
	[phase] [float] NULL,
	[sla] [float] NULL,
	[vort] [float] NULL,
	[displacement] [float] NULL,
	[ftle] [float] NULL,
	[sst] [float] NULL,
	[chl] [float] NULL,
	[mld] [float] NULL,
	[sss] [float] NULL,
	[eddy] [int] NULL,
	[climatology] [float] NULL,
	[edd_sla_ano] [float] NULL,
	[edd_sst_ano] [float] NULL,
	[edd_mld_ano] [float] NULL,
	[edd_vort_ano] [float] NULL,
	[edd_sla] [float] NULL,
	[edd_sst] [float] NULL,
	[edd_mld] [float] NULL,
	[edd_vort] [float] NULL
) ON [FG1]
GO



---------------------
-- Indices
---------------------





CREATE CLUSTERED INDEX [IX_tblSOCAT_year_month_others] ON [dbo].[tblSOCAT]
(
	[year] ASC,
	[month] ASC,
	[day] ASC,
	[lat] ASC,
	[lon] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO


CREATE NONCLUSTERED INDEX [IX_tblSOCAT_lat_lon] ON [dbo].[tblSOCAT]
(
	[lat] ASC,
	[lon] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO


CREATE NONCLUSTERED INDEX [IX_tblSOCAT_quality_control] ON [dbo].[tblSOCAT]
(
	[quality_control] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO


CREATE NONCLUSTERED INDEX [IX_tblSOCAT_fco2] ON [dbo].[tblSOCAT]
(
	[fco2] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO


CREATE NONCLUSTERED INDEX [IX_tblSOCAT_eddy] ON [dbo].[tblSOCAT]
(
	[eddy] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO


