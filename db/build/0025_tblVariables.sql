USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblVariables](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[DB] [nvarchar](50) NOT NULL,
	[Dataset_ID] [int] NOT NULL,
	[Table_Name] [nvarchar](50) NULL,
	[Short_Name] [nvarchar](50) NULL,
	[Long_Name] [nvarchar](500) NULL,
	[Unit] [nvarchar](50) NULL,
	[Temporal_Res_ID] [int] NOT NULL,
	[Spatial_Res_ID] [int] NOT NULL,
	[Temporal_Coverage_Begin] [nvarchar](50) NOT NULL,
	[Temporal_Coverage_End] [nvarchar](50) NOT NULL,
	[Lat_Coverage_Begin] [nvarchar](50) NOT NULL,
	[Lat_Coverage_End] [nvarchar](50) NOT NULL,
	[Lon_Coverage_Begin] [nvarchar](50) NOT NULL,
	[Lon_Coverage_End] [nvarchar](50) NOT NULL,
	[Grid_Mapping] [nvarchar](50) NOT NULL,
	[Make_ID] [int] NOT NULL,	                 -- obs/model
	[Sensor_ID] [int] NOT NULL,	                 -- sat/in-situ
	[Process_ID] [int] NOT NULL,	             -- NRT/REP
	[Study_Domain_ID] [int] NOT NULL,	         -- phys/chem/bio/biogeochem
	[Keywords] [nvarchar](500) NULL,
	[Comment] [nvarchar](max) NULL,
 CONSTRAINT [PK_tblVariables] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO



ALTER TABLE [dbo].[tblVariables]  WITH CHECK ADD  CONSTRAINT [FK_tblVariables_tblDatasets] FOREIGN KEY([Dataset_ID])
REFERENCES [dbo].[tblDatasets] ([ID])
GO

ALTER TABLE [dbo].[tblVariables] CHECK CONSTRAINT [FK_tblVariables_tblDatasets]
GO

ALTER TABLE [dbo].[tblVariables]  WITH CHECK ADD  CONSTRAINT [FK_tblVariables_tblMakes] FOREIGN KEY([Make_ID])
REFERENCES [dbo].[tblMakes] ([ID])
GO

ALTER TABLE [dbo].[tblVariables] CHECK CONSTRAINT [FK_tblVariables_tblMakes]
GO

ALTER TABLE [dbo].[tblVariables]  WITH CHECK ADD  CONSTRAINT [FK_tblVariables_tblProcess_Stages] FOREIGN KEY([Process_ID])
REFERENCES [dbo].[tblProcess_Stages] ([ID])
GO

ALTER TABLE [dbo].[tblVariables] CHECK CONSTRAINT [FK_tblVariables_tblProcess_Stages]
GO

ALTER TABLE [dbo].[tblVariables]  WITH CHECK ADD  CONSTRAINT [FK_tblVariables_tblSpatial_Resolutions] FOREIGN KEY([Spatial_Res_ID])
REFERENCES [dbo].[tblSpatial_Resolutions] ([ID])
GO

ALTER TABLE [dbo].[tblVariables] CHECK CONSTRAINT [FK_tblVariables_tblSpatial_Resolutions]
GO

ALTER TABLE [dbo].[tblVariables]  WITH CHECK ADD  CONSTRAINT [FK_tblVariables_tblStudy_Domains] FOREIGN KEY([Study_Domain_ID])
REFERENCES [dbo].[tblStudy_Domains] ([ID])
GO

ALTER TABLE [dbo].[tblVariables] CHECK CONSTRAINT [FK_tblVariables_tblStudy_Domains]
GO

ALTER TABLE [dbo].[tblVariables]  WITH CHECK ADD  CONSTRAINT [FK_tblVariables_tblTemporal_Resolutions] FOREIGN KEY([Temporal_Res_ID])
REFERENCES [dbo].[tblTemporal_Resolutions] ([ID])
GO

ALTER TABLE [dbo].[tblVariables] CHECK CONSTRAINT [FK_tblVariables_tblTemporal_Resolutions]
GO



---------------------
-- Indices
---------------------





CREATE NONCLUSTERED INDEX [IX_tblVariables_Dataset_ID] ON [dbo].[tblVariables]
(
	[Dataset_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblVariables_Temporal_Res_ID] ON [dbo].[tblVariables]
(
	[Temporal_Res_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblVariables_Spatial_Res_ID] ON [dbo].[tblVariables]
(
	[Spatial_Res_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO



CREATE NONCLUSTERED INDEX [IX_tblVariables_Make_ID] ON [dbo].[tblVariables]
(
	[Make_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblVariables_Sensor_ID] ON [dbo].[tblVariables]
(
	[Sensor_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblVariables_Process_ID] ON [dbo].[tblVariables]
(
	[Process_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblVariables_Study_Domain_ID] ON [dbo].[tblVariables]
(
	[Study_Domain_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblVariables_Short_Name] ON [dbo].[tblVariables]
(
	[Short_Name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblVariables_Keywords] ON [dbo].[tblVariables]
(
	[Keywords] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO
