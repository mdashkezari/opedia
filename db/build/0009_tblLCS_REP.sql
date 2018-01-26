USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblLCS_REP](
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[time] [date] NOT NULL,
	[ftle_bw_adt] [float] NULL,
	[disp_bw_adt] [float] NULL,
	[ftle_fw_adt] [float] NULL,
	[disp_fw_adt] [float] NULL,
	[ftle_bw_sla] [float] NULL,
	[disp_bw_sla] [float] NULL,
	[ftle_fw_sla] [float] NULL,
	[disp_fw_sla] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblLCS_REP] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (/*DATA_COMPRESSION = PAGE,*/ PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG4]
) ON [FG4]

GO




---------------------
-- Indices
---------------------

/*

CREATE UNIQUE NONCLUSTERED INDEX [IX_tblLCS_REP_time_lat_lon] ON [dbo].[tblLCS_REP]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC
)
INCLUDE ([ftle_bw_adt], [ftle_fw_adt], [disp_bw_adt]) 
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG4]
GO


CREATE NONCLUSTERED INDEX [IX_tblLCS_REP_ftle_bw_adt] ON [dbo].[tblLCS_REP]
(
	[ftle_bw_adt] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG4]
GO


CREATE NONCLUSTERED INDEX [IX_tblLCS_REP_ftle_fw_adt] ON [dbo].[tblLCS_REP]
(
	[ftle_fw_adt] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG4]
GO

*/