USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblApi_Call_Details](
	[ID] [int] PRIMARY KEY IDENTITY(1,1),
	[Api_Call_ID] [bigint] NOT NULL,
	[Query] [nvarchar](500),
	[Stored_Procedure_Parameters] [nvarchar] (500),
	CONSTRAINT [FK_API_CALL_ID] FOREIGN KEY (Api_Call_ID) REFERENCES [dbo].[tblApi_Calls] (ID),
) ON [FG2]
GO

		    
---------------------
-- Indices
---------------------
		    
USE [Opedia]
GO

CREATE NONCLUSTERED INDEX [IX_tblApi_Call_Details_Api_Call_ID] ON [dbo].[tblApi_Call_Details]
(
	[Api_Call_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO