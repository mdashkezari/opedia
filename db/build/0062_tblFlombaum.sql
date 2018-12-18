USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblFlombaum](
	[time] [datetime] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[depth] [float] NOT NULL,
	[prochloro_abundance] [float] NOT NULL,
	[synecho_abundance] [float] NOT NULL
) ON [FG1]
GO




--
--
-- ---------------------
-- -- Indices
-- ---------------------
--
--

CREATE NONCLUSTERED INDEX [IX_tblFlombaum_time_lat_lon] ON [dbo].[tblFlombaum]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG1]
GO






CREATE NONCLUSTERED INDEX [IX_tblFlombaum_prochloro_abundance] ON [dbo].[tblFlombaum]
(
	[prochloro_abundance] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG1]
GO




CREATE NONCLUSTERED INDEX [IX_tblFlombaum_synecho_abundance] ON [dbo].[tblFlombaum]
(
	[synecho_abundance] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG1]
GO
