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
)
	
