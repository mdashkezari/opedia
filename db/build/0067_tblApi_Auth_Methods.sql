USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblApi_Auth_Methods](
	[ID] [int] PRIMARY KEY,
	[Description] [varchar](50)
) ON [FG2]
GO

------ Auth Methods as of 4/5/19 ----
USE [Opedia]
GO

INSERT INTO [dbo].[tblApi_Auth_Methods] (ID, Description)
VALUES (1, 'Local username/password auth'),
	(2, 'JSON Web Token auth'),
	(3, 'API key auth')