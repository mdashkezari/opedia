USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblKM1709_mesoscope](
	[time] [date] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[depth] [float] NOT NULL,
	[Station] [float] NULL,
	[Cast] [float] NULL,
	[RosPos] [float] NULL,
	[CTD_Temperature] [float] NULL,
	[CTD_Salinity] [float] NULL,
	[CTD_Oxygen] [float] NULL,
	[CTD_Chloropigment] [float] NULL,
	[Potential_Temperature] [float] NULL,
	[Potential_Density] [float] NULL,
	[Bottle_Oxygen] [float] NULL,
	[DIC] [float] NULL,
	[Alkalinity] [float] NULL,
	[pH] [float] NULL,
	[PO4] [float] NULL,
	[NO3+NO2] [float] NULL,
	[SiO4] [float] NULL,
	[LLN] [float] NULL,
	[LLP] [float] NULL,
	[PC] [float] NULL,
	[PN] [float] NULL,
	[PP] [float] NULL,
	[Psi] [float] NULL,
	[Chlorophyll] [float] NULL,
	[Pheopigment] [float] NULL,
	[Heterotrophic_Bacteria] [float] NULL,
	[Prochlorococcus] [float] NULL,
	[Synechococcus] [float] NULL,
	[Eukaryotes] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblKM1709_mesoscope] PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG1]
) ON [FG1]

GO




--
--
-- ---------------------
-- -- Indices
-- ---------------------
--
--

CREATE NONCLUSTERED INDEX [IX_tblKM1709_mesoscope_time_lat_lon_depth] ON [dbo].[tblKM1709_mesoscope]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC,
	[depth] ASC
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG1]
GO
--
-- --
--
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblKM1709_mesoscope_prochlorococcus_abundance ON [dbo].[tblKM1709_mesoscope]
-- (
-- 	[prochlorococcus_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
-- CREATE NONCLUSTERED INDEX [IX_tblKM1709_mesoscope_synechococcus_abundance ON [dbo].[tblKM1709_mesoscope]
-- (
-- 	[synechococcus_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
-- CREATE NONCLUSTERED INDEX [IX_tblKM1709_mesoscope_picoeukaryote_abundance ON [dbo].[tblKM1709_mesoscope]
-- (
-- 	[picoeukaryote_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblKM1709_mesoscope_picophytoplankton_abundance ON [dbo].[tblKM1709_mesoscope]
-- (
-- 	[picophytoplankton_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
-- CREATE NONCLUSTERED INDEX [IX_tblKM1709_mesoscope_picophytoplankton_biomass] ON [dbo].[tblKM1709_mesoscope]
-- (
-- 	[picophytoplankton_biomass] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
