USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblApi_Routes](
	[ID] [int] PRIMARY KEY,
	[Description] [varchar](100) NOT NULL
) ON [FG2]
GO

-------- API Routes as of 4/5/19

USE [Opedia]
GO

INSERT INTO [dbo].[tblApi_Routes] (ID, Description)
VALUES (1, 'Root/Web app landing'),
	(2, 'Unmapped route'),
	(101, 'GET data catalog'),
	(201, 'POST new user info on sign-up'),
	(202, 'POST credentials for sign-in'),
	(301, 'GET data from custom query'),
	(302, 'GET data from stored procedure argument set')