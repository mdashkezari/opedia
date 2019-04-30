
USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE TABLE [dbo].[tblAMT13_ProchlorococcusAbundanceAndMetadata_Chisholm](
	[time] [date] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[TEMP_Chisholm] [float] NOT NULL,
	[SALINITY_Chisholm] [float] NOT NULL,
	[light_Chisholm] [float] NOT NULL,
	[chlA_Chisholm] [float] NOT NULL,
	[NH4_Chisholm] [float] NOT NULL,
	[NO2_Chisholm] [float] NOT NULL,
	[NO3_Chisholm] [float] NOT NULL,
	[PO4_Chisholm] [float] NOT NULL,
	[Silicate_Chisholm] [float] NOT NULL,
	[DCM_Chisholm] [float] NOT NULL,
	[05C_Chisholm] [float] NOT NULL,
	[25C_Chisholm] [float] NOT NULL,
	[03Density_Chisholm] [float] NOT NULL,
	[125Density_Chisholm] [float] NOT NULL,
	[TotalDepth_Chisholm] [float] NOT NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblAMT13_ProchlorococcusAbundanceAndMetadata_Chisholm] PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (/*DATA_COMPRESSION = PAGE,*/ PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG1]
) ON [FG1]

GO




---------------------
-- Indices
---------------------



CREATE NONCLUSTERED INDEX [IX_tblAMT13_ProchlorococcusAbundanceAndMetadata_Chisholm_time_lat_lon_depth] ON [dbo].[tblAMT13_ProchlorococcusAbundanceAndMetadata_Chisholm]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC,
	[depth] ASC
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG2]
GO
