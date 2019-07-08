

USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblDarwin_Phytoplankton](
	[time] [date] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[depth] [float] NOT NULL,
	[diatom] [float] NULL,
	[coccolithophore] [float] NULL,
	[mixotrophic_dinoflagellate] [float] NULL,
	[picoeukaryote] [float] NULL,
	[picoprokaryote] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblDarwin_Phytoplankton] PRIMARY KEY CLUSTERED
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


CREATE UNIQUE NONCLUSTERED INDEX [IX_tblDarwin_Phytoplankton_time_lat_lon_depth] ON [dbo].[tblDarwin_Phytoplankton]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC,
	[depth] ASC
)
INCLUDE ([diatom],[coccolithophore],[mixotrophic_dinoflagellate],[picoeukaryote],[picoprokaryote])
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG4]
GO

--
--
-- CREATE NONCLUSTERED INDEX [IX_tblDarwin_Phytoplankton_irradiance_reflectance_waveband_3] ON [dbo].[tblDarwin_Phytoplankton]
-- (
-- 	[irradiance_reflectance_waveband_3] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG4]
-- GO
-- --
-- --
-- CREATE NONCLUSTERED INDEX [IX_tblDarwin_Phytoplankton_irradiance_reflectance_waveband_7] ON [dbo].[tblDarwin_Phytoplankton]
-- (
-- 	[irradiance_reflectance_waveband_7] ASC
-- )WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
-- ON [FG4]
-- GO
--
