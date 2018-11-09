USE [Opedia]
GO


SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblPisces_NRT_Calendar](
	[time] [date] NOT NULL
) ON [PRIMARY]
GO




---------------------
-- Indices
---------------------


USE [Opedia]
GO



CREATE UNIQUE NONCLUSTERED INDEX [IX_tblPisces_NRT_Calandar_time] ON [dbo].[tblPisces_NRT_Calendar]
(
	[time] ASC
)
ON [PRIMARY]
GO
