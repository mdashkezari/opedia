USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblGlobal_PicoPhytoPlankton](
	[time] [date] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[depth] [float] NOT NULL,
	[prochlorococcus_abundance] [float] NULL,
	[synechococcus_abundance] [float] NULL,
	[picoeukaryote_abundance] [float] NULL,
	[picophytoplankton_abundance] [float] NULL,
	[picophytoplankton_biomass] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblGlobal_PicoPhytoPlankton] PRIMARY KEY CLUSTERED
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

CREATE NONCLUSTERED INDEX [IX_tblGlobal_PicoPhytoPlankton_time_lat_lon] ON [dbo].[tblGlobal_PicoPhytoPlankton]
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
--
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblGlobal_PicoPhytoPlankton_prochlorococcus_abundance ON [dbo].[tblGlobal_PicoPhytoPlankton]
-- (
-- 	[prochlorococcus_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
-- CREATE NONCLUSTERED INDEX [IX_tblGlobal_PicoPhytoPlankton_synechococcus_abundance ON [dbo].[tblGlobal_PicoPhytoPlankton]
-- (
-- 	[synechococcus_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
-- CREATE NONCLUSTERED INDEX [IX_tblGlobal_PicoPhytoPlankton_picoeukaryote_abundance ON [dbo].[tblGlobal_PicoPhytoPlankton]
-- (
-- 	[picoeukaryote_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
--
-- CREATE NONCLUSTERED INDEX [IX_tblGlobal_PicoPhytoPlankton_picophytoplankton_abundance ON [dbo].[tblGlobal_PicoPhytoPlankton]
-- (
-- 	[picophytoplankton_abundance] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
--
-- CREATE NONCLUSTERED INDEX [IX_tblGlobal_PicoPhytoPlankton_picophytoplankton_biomass] ON [dbo].[tblGlobal_PicoPhytoPlankton]
-- (
-- 	[picophytoplankton_biomass] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG1]
-- GO
