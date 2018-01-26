USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE TABLE [dbo].[tblSeaFlow_Cruises](
	[name] [nvarchar](200) NULL,
	[FSC] [nvarchar](100) NULL,
	[approximat_location] [nvarchar](200) NULL,
	[official_name] [nvarchar](200) NULL,
	[other_name] [nvarchar](200) NULL,
	[ship] [nvarchar](100) NULL,
	[month] [nvarchar](50) NULL,
	[year] [int] NULL,
	[instrument] [int] NULL,
	[location] [nvarchar](100) NULL,
	[TSG] [nvarchar](100) NULL,
	[chl] [nvarchar](100) NULL,
	[PAR] [nvarchar](100) NULL,
	[discrete_FCM] [nvarchar](100) NULL,
	[chl_calibrated] [nvarchar](100) NULL,
	[1um_beads] [nvarchar](100) NULL,
	[comments] [nvarchar](max) NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblSeaFlow_Cruises] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG1]
) ON [FG1]

GO




