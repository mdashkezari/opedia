USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblDatasets](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[DB] [nvarchar](50) NOT NULL,
	[Dataset_Name] [nvarchar](100) NOT NULL,
	[Dataset_Long_Name] [nvarchar](500) NULL,
	[Variables] [nvarchar](max) NULL,
	[Climatology] [bit] NULL,
	[Data_Source] [nvarchar](100) NULL,
	[Distributor] [nvarchar](50) NULL,
	[Description] [nvarchar](max) NULL,
 CONSTRAINT [PK_tblDatasets] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO




---------------------
-- Indices
---------------------


CREATE UNIQUE NONCLUSTERED INDEX [IX_tblDatasets_Dataset_Names] ON [dbo].[tblDatasets]
(
	[Dataset_Name] ASC
)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [PRIMARY]
GO

CREATE NONCLUSTERED INDEX [IX_tblDatasets_Variables] ON [dbo].[tblDatasets]
(
	[Variables] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO

