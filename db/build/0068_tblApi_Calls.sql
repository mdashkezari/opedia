USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblApi_Calls](
	[ID] [bigint] PRIMARY KEY IDENTITY(1,1),
	[Date_Time] [datetime] NOT NULL,
    [Ip_Address] [nvarchar](15) NOT NULL,
    [Host_Name] [nvarchar](150) NOT NULL,
    [User_ID] [int],
    [Route_ID] [int] NOT NULL,
    [Api_Key_Id] [int],
    [Auth_Method] [int],
    CONSTRAINT [FK_USER_ID] FOREIGN KEY (User_ID) REFERENCES [dbo].[tblUsers] (UserID),
    CONSTRAINT [FK_ROUTE_ID] FOREIGN KEY (Route_ID) REFERENCES [dbo].[tblApi_Routes] (ID),
    CONSTRAINT [FK_API_KEY_ID] FOREIGN KEY (Api_Key_Id) REFERENCES [dbo].[tblApi_Keys] (ID),
    CONSTRAINT [FK_AUTH_METHOD] FOREIGN KEY (Auth_Method) REFERENCES [dbo].[tblApi_Auth_Methods] (ID),
) ON [FG2]
GO

---------------------------
-- Additional Constraints
---------------------------

ALTER TABLE [dbo].[tblApi_Calls] ADD  CONSTRAINT [DF_tblApi_Calls_Date]  DEFAULT (getdate()) FOR [Date_Time]
GO

		    
-------------------
-- Indices
-------------------
		    
USE [Opedia]
GO

CREATE NONCLUSTERED INDEX [IX_tblApi_Calls_Date_Time] ON [dbo].[tblApi_Calls]
(
	[Date_Time] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG2]
GO

CREATE NONCLUSTERED INDEX [IX_tblApi_Calls_Ip_Address] ON [dbo].[tblApi_Calls]
(
	[Ip_Address] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG2]
GO

CREATE NONCLUSTERED INDEX [IX_tblApi_Calls_UserID] ON [dbo].[tblApi_Calls]
(
	[User_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG2]
GO

CREATE NONCLUSTERED INDEX [IX_tblApi_Calls_Route_ID] ON [dbo].[tblApi_Calls]
(
	[Route_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG2]
GO

CREATE NONCLUSTERED INDEX [IX_tblApi_Calls_Api_Key_Id] ON [dbo].[tblApi_Calls]
(
	[Api_Key_Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG2]
GO

CREATE NONCLUSTERED INDEX [IX_tblApi_Calls_Auth_Method] ON [dbo].[tblApi_Calls]
(
	[Auth_Method] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG2]
GO
