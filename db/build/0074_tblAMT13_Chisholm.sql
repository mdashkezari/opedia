
USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE TABLE [dbo].[tblAMT13_Chisholm](
	[time] [datetime] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[depth] [float] NOT NULL,
	[pbact_Chisholm] [float] NULL,
	[TQPCR_MED4_MIT9312_MIT9211_NATL2A_SS120_MIT9313_Chisholm] [float] NULL,
	[MED4PCR_Chisholm] [float] NULL,
	[MIT9312PCR_Chisholm] [float] NULL,
	[MIT9211PCR_Chisholm] [float] NULL,
	[NATL2APCR_Chisholm] [float] NULL,
	[SS120PCR_Chisholm] [float] NULL,
	[MIT9313PCR_Chisholm] [float] NULL,
	[sbact_Chisholm] [float] NULL,
	[density_AMT13] [float] NULL,
	[temp_C_AMT13] [float] NULL,
	[csal_ppt_AMT13] [float] NULL,
	[Light_Quanta_m2_sec_AMT13] [float] NULL,
	[chlA_AMT13] [float] NULL,
	[DCM_AMT13] [float] NULL,
	[05C_AMT13] [float] NULL,
	[25C_AMT13] [float] NULL,
	[03Density_AMT13] [float] NULL,
	[125Density_AMT13] [float] NULL,
	[TotalDepth_AMT13] [float] NULL,
	[MED4PCR_quality_Chisholm] [float] NULL,
	[MIT9312PCR_quality_Chisholm] [float] NULL,
	[MIT9211PCR_quality_Chisholm] [float] NULL,
	[NATL2APCR_quality_Chisholm] [float] NULL,
	[SS120PCR_quality_Chisholm] [float] NULL,
	[MIT9313PCR_quality_Chisholm] [float] NULL,
	[TQPCR_MED4_MIT9312_MIT9211_NATL2A_SS120_MIT9313_quality_Chisholm] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblAMT13_Chisholm] PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (/*DATA_COMPRESSION = PAGE,*/ PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG1]
) ON [FG1]

GO




---------------------
-- Indices
---------------------



CREATE UNIQUE NONCLUSTERED INDEX [IX_tblAMT13_Chisholm_time_lat_lon_depth] ON [dbo].[tblAMT13_Chisholm]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC,
	[depth] ASC
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG2]
GO
