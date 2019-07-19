USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblHL2A_diel_metagenomics](
		[time] [date] NOT NULL,
		[lat] [float] NOT NULL,
		[lon] [float] NOT NULL,
		[depth] [float] NOT NULL,
		[station] [int] NULL,
		[cast_num] [int] NULL,
		[sra_experiment] [nvarchar](100),
		[sra_run] [nvarchar](100),
		[filter_type] [nvarchar](100),
		[filter_max] [float] NULL,
		[sra_bioproject] [nvarchar](100),
		[filter_min] [float] NULL,
		[library_kit] [nvarchar](100),
		[sequence_type] [nvarchar](100),
		[sequencing_method] [nvarchar](100),
		[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblHL2A_diel_metagenomics] PRIMARY KEY CLUSTERED
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

CREATE NONCLUSTERED INDEX [IX_tblHL2A_diel_metagenomics_time_lat_lon_depth] ON [dbo].[tblHL2A_diel_metagenomics]
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
-- CREATE NONCLUSTERED INDEX [IX_tblHL2A_diel_metagenomics_prochlorococcus_abundance ON [dbo].[tblHL2A_diel_metagenomics]
-- (
-- 	[prochlorococcus_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG4]
-- GO
--
-- CREATE NONCLUSTERED INDEX [IX_tblHL2A_diel_metagenomics_synechococcus_abundance ON [dbo].[tblHL2A_diel_metagenomics]
-- (
-- 	[synechococcus_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG4]
-- GO
--
-- CREATE NONCLUSTERED INDEX [IX_tblHL2A_diel_metagenomics_picoeukaryote_abundance ON [dbo].[tblHL2A_diel_metagenomics]
-- (
-- 	[picoeukaryote_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG4]
-- GO
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblHL2A_diel_metagenomics_picophytoplankton_abundance ON [dbo].[tblHL2A_diel_metagenomics]
-- (
-- 	[picophytoplankton_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG4]
-- GO
--
-- CREATE NONCLUSTERED INDEX [IX_tblHL2A_diel_metagenomics_picophytoplankton_biomass] ON [dbo].[tblHL2A_diel_metagenomics]
-- (
-- 	[picophytoplankton_biomass] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG4]
-- GO
