USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblGLODAP](
		[time] [date] NOT NULL,
		[lat] [float] NOT NULL,
		[lon] [float] NOT NULL,
		[depth] [float] NOT NULL,
		[pressure] [float] NULL,
		[temperature] [float] NULL,
		[theta_potential_temperature] [float] NULL,
		[salinity] [float] NULL,
		[sigma0_potential_density] [float] NULL,
		[sigma1_potential_density_ref_1000_dbar] [float] NULL,
		[sigma2_potential_density_ref_2000_dbar] [float] NULL,
		[sigma3_potential_density_ref_3000_dbar] [float] NULL,
		[sigma4_potential_density_ref_4000_dbar] [float] NULL,
		[gamma_neutral_density] [float] NULL,
		[oxygen] [float] NULL,
		[aou] [float] NULL,
		[nitrate] [float] NULL,
		[nitrite] [float] NULL,
		[silicate] [float] NULL,
		[phosphate] [float] NULL,
		[tco2] [float] NULL,
		[talk] [float] NULL,
		[phts25p0_pH_25C_0dbar] [float] NULL,
		[phtsinsitutp_pH_insitu] [float] NULL,
		[cfc11] [float] NULL,
		[pcfc11] [float] NULL,
		[cfc12] [float] NULL,
		[pcfc12] [float] NULL,
		[cfc113] [float] NULL,
		[pcfc113] [float] NULL,
		[ccl4] [float] NULL,
		[pccl4] [float] NULL,
		[sf6] [float] NULL,
		[psf6] [float] NULL,
		[c13] [float] NULL,
		[c14] [float] NULL,
		[c14err] [float] NULL,
		[h3] [float] NULL,
		[h3err] [float] NULL,
		[he3] [float] NULL,
		[he3err] [float] NULL,
		[he] [float] NULL,
		[heerr] [float] NULL,
		[neon] [float] NULL,
		[neonerr] [float] NULL,
		[o18] [float] NULL,
		[toc] [float] NULL,
		[doc] [float] NULL,
		[don] [float] NULL,
		[tdn] [float] NULL,
		[chla] [float] NULL,
		[cruise_expocode] [float] NULL,
		[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblGLODAP] PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG4]
) ON [FG4]

GO




--
--
-- ---------------------
-- -- Indices
-- ---------------------
--
--

CREATE NONCLUSTERED INDEX [IX_tblGLODAP_time_lat_lon_depth] ON [dbo].[tblGLODAP]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC,
	[depth] ASC
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG4]
GO
--
-- --
--
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblGLODAP_prochlorococcus_abundance ON [dbo].[tblGLODAP]
-- (
-- 	[prochlorococcus_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG4]
-- GO
--
-- CREATE NONCLUSTERED INDEX [IX_tblGLODAP_synechococcus_abundance ON [dbo].[tblGLODAP]
-- (
-- 	[synechococcus_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG4]
-- GO
--
-- CREATE NONCLUSTERED INDEX [IX_tblGLODAP_picoeukaryote_abundance ON [dbo].[tblGLODAP]
-- (
-- 	[picoeukaryote_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG4]
-- GO
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblGLODAP_picophytoplankton_abundance ON [dbo].[tblGLODAP]
-- (
-- 	[picophytoplankton_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG4]
-- GO
--
-- CREATE NONCLUSTERED INDEX [IX_tblGLODAP_picophytoplankton_biomass] ON [dbo].[tblGLODAP]
-- (
-- 	[picophytoplankton_biomass] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG4]
-- GO
