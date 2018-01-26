USE [Opedia]
GO


SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblEddyCoresML](
	[year] [int] NOT NULL,
	[month] [int] NOT NULL,
	[day] [int] NOT NULL,
	[eddy_centers_i] [float] NOT NULL,
	[eddy_centers_j] [float] NOT NULL,
	[eddy_polarity] [float] NOT NULL,
	[eddy_radius] [float] NOT NULL,
	[radius_rv2] [float] NOT NULL,
	[radius_pv] [float] NOT NULL,
	[eddy_lat] [float] NOT NULL,
	[eddy_lon] [float] NOT NULL,
	[phase_integ_fixed] [float] NULL,
	[phase_integ_full] [float] NULL,
	[phase_norm_fixed] [float] NULL,
	[phase_norm_full] [float] NULL,
	[phase_mean_bkg] [float] NULL,
	[phase_std_bkg] [float] NULL,
	[sla_mean_fixed] [float] NULL,
	[sla_mean_full] [float] NULL,
	[sla_std_fixed] [float] NULL,
	[sla_std_full] [float] NULL,
	[sla_mean_bkg] [float] NULL,
	[sla_std_bkg] [float] NULL,
	[vort_mean_fixed] [float] NULL,
	[vort_mean_full] [float] NULL,
	[vort_std_fixed] [float] NULL,
	[vort_std_full] [float] NULL,
	[vort_mean_bkg] [float] NULL,
	[vort_std_bkg] [float] NULL,
	[displacement_mean_fixed] [float] NULL,
	[displacement_mean_full] [float] NULL,
	[displacement_std_fixed] [float] NULL,
	[displacement_std_full] [float] NULL,
	[displacement_mean_bkg] [float] NULL,
	[displacement_std_bkg] [float] NULL,
	[ftle_mean_fixed] [float] NULL,
	[ftle_mean_full] [float] NULL,
	[ftle_std_fixed] [float] NULL,
	[ftle_std_full] [float] NULL,
	[ftle_mean_bkg] [float] NULL,
	[ftle_std_bkg] [float] NULL,
	[sst_mean_fixed] [float] NULL,
	[sst_mean_full] [float] NULL,
	[sst_std_fixed] [float] NULL,
	[sst_std_full] [float] NULL,
	[sst_mean_bkg] [float] NULL,
	[sst_std_bkg] [float] NULL,
	[chl_mean_fixed] [float] NULL,
	[chl_mean_full] [float] NULL,
	[chl_std_fixed] [float] NULL,
	[chl_std_full] [float] NULL,
	[chl_mean_bkg] [float] NULL,
	[chl_std_bkg] [float] NULL,
	[CO2_mean_surface] [float] NULL,
	[CO2_mean_surface_bkg] [float] NULL,
	[CO2_mean_surface_std] [float] NULL,
	[mld_mean_fixed] [float] NULL,
	[mld_mean_full] [float] NULL,
	[mld_std_fixed] [float] NULL,
	[mld_std_full] [float] NULL,
	[mld_mean_bkg] [float] NULL,
	[mld_std_bkg] [float] NULL,
	[sss_mean_fixed] [float] NULL,
	[sss_mean_full] [float] NULL,
	[sss_std_fixed] [float] NULL,
	[sss_std_full] [float] NULL,
	[sss_mean_bkg] [float] NULL,
	[sss_std_bkg] [float] NULL
) ON [FG1]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_phase_integ_fixed]  DEFAULT (NULL) FOR [phase_integ_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_phase_integ_full]  DEFAULT (NULL) FOR [phase_integ_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_phase_norm_fixed]  DEFAULT (NULL) FOR [phase_norm_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_phase_norm_full]  DEFAULT (NULL) FOR [phase_norm_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_sla_mean_fixed]  DEFAULT (NULL) FOR [sla_mean_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_sla_mean_full]  DEFAULT (NULL) FOR [sla_mean_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_sla_std_fixed]  DEFAULT (NULL) FOR [sla_std_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_sla_std_full]  DEFAULT (NULL) FOR [sla_std_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_vort_mean_fixed]  DEFAULT (NULL) FOR [vort_mean_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_vort_mean_full]  DEFAULT (NULL) FOR [vort_mean_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_vort_std_fixed]  DEFAULT (NULL) FOR [vort_std_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_vort_std_full]  DEFAULT (NULL) FOR [vort_std_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_displacement_mean_fixed]  DEFAULT (NULL) FOR [displacement_mean_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_displacement_mean_full]  DEFAULT (NULL) FOR [displacement_mean_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_displacement_std_fixed]  DEFAULT (NULL) FOR [displacement_std_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_displacement_std_full]  DEFAULT (NULL) FOR [displacement_std_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_ftle_mean_fixed]  DEFAULT (NULL) FOR [ftle_mean_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_ftle_mean_full]  DEFAULT (NULL) FOR [ftle_mean_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_ftle_std_fixed]  DEFAULT (NULL) FOR [ftle_std_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_ftle_std_full]  DEFAULT (NULL) FOR [ftle_std_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_sst_mean_fixed]  DEFAULT (NULL) FOR [sst_mean_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_sst_mean_full]  DEFAULT (NULL) FOR [sst_mean_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_sst_std_fixed]  DEFAULT (NULL) FOR [sst_std_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_sst_std_full]  DEFAULT (NULL) FOR [sst_std_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_chl_mean_fixed]  DEFAULT (NULL) FOR [chl_mean_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_chl_mean_full]  DEFAULT (NULL) FOR [chl_mean_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_chl_std_fixed]  DEFAULT (NULL) FOR [chl_std_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_cores_chl_std_full]  DEFAULT (NULL) FOR [chl_std_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_tblEddyCoresML_chl_mean_fixed1]  DEFAULT (NULL) FOR [mld_mean_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_tblEddyCoresML_chl_mean_full1]  DEFAULT (NULL) FOR [mld_mean_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_tblEddyCoresML_chl_std_fixed1]  DEFAULT (NULL) FOR [mld_std_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_tblEddyCoresML_chl_std_full1]  DEFAULT (NULL) FOR [mld_std_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_tblEddyCoresML_chl_mean_fixed1_1]  DEFAULT (NULL) FOR [sss_mean_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_tblEddyCoresML_chl_mean_full1_1]  DEFAULT (NULL) FOR [sss_mean_full]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_tblEddyCoresML_chl_std_fixed1_1]  DEFAULT (NULL) FOR [sss_std_fixed]
GO

ALTER TABLE [dbo].[tblEddyCoresML] ADD  CONSTRAINT [DF_tblEddyCoresML_chl_std_full1_1]  DEFAULT (NULL) FOR [sss_std_full]
GO





---------------------
-- Indices
---------------------



CREATE CLUSTERED INDEX [IX_tblEddyCoresML_year_month_others] ON [dbo].[tblEddyCoresML]
(
	[year] ASC,
	[month] ASC,
	[day] ASC,
	[eddy_polarity] ASC,
	[eddy_lat] ASC,
	[eddy_lon] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO




CREATE NONCLUSTERED INDEX [IX_tblEddyCoresML_radius_polarity_lat_lon] ON [dbo].[tblEddyCoresML]
(
	[eddy_radius] ASC,
	[eddy_polarity] ASC,
	[eddy_lat] ASC,
	[eddy_lon] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG1]
GO


