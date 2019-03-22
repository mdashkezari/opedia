USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblApi_Keys](
	[uuid] [char] (36) PRIMARY KEY,
	[UserID] [int] NOT NULL,
	CONSTRAINT [FK_UserID] FOREIGN KEY (UserID)
	REFERENCES [dbo].[tblUsers] (UserID)
) ON [PRIMARY]
GO
		
		    
---------------------
-- Indices
---------------------
		    
USE [Opedia]
GO



CREATE NONCLUSTERED INDEX [IX_tblApi_Keys_UserID] ON [dbo].[tblApi_Keys]
(
	[UserID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO
