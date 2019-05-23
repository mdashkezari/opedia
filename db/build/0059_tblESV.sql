
USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblESV](
	[time] [date] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[depth] [float] NOT NULL,
	[centroid] [nchar](50) NULL,
	[relative_abundance] [float] NULL,
	[max_abundance] [float] NULL,
	[cluster_level] [smallint] NULL,
	[num_cluster_members] [int] NULL,
	[domain] [nchar](50) NULL,
	[kingdom] [nchar](50) NULL,
	[phylum] [nchar](50) NULL,
	[class] [nchar](50) NULL,
	[order] [nchar](50) NULL,
	[genus] [nchar](60) NULL,
	[species] [nchar](60) NULL,
	[esv_tempreature] [float] NULL,
	[esv_salinity] [float] NULL,
	[esv_chl] [float] NULL,
	[size_frac_lower] [float] NULL,
	[size_frac_upper] [float] NULL,
	[cruise_name] [nchar](30) NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblESV] PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (/*DATA_COMPRESSION = PAGE,*/ PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG1]
) ON [FG1]

GO




---------------------
-- Indices
---------------------

/*

USE [Opedia]
GO



CREATE NONCLUSTERED INDEX [IX_tblESV_centroid] ON [dbo].[tblESV]
(
	[centroid] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG1]
GO




-- Rowstore index

CREATE UNIQUE NONCLUSTERED INDEX [IX_tblESV_time_lat_lon_depth_cluster_levels_and_members] ON [dbo].[tblESV]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC,
	[depth] ASC,
	[cluster_level] ASC,
	[num_cluster_members] ASC
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG1]
GO




-- columnstore index

CREATE NONCLUSTERED COLUMNSTORE INDEX [IX_ColumnStore_tblESV_time_lat_lon_depth_levels_and_members] ON [dbo].[tblESV]
(
	[time],
	[lat] ,
	[lon] ,
	[depth] ,
	[cluster_level] ,
	[num_cluster_members]
)
WITH (DATA_COMPRESSION = COLUMNSTORE)
ON [FG1]
GO



-- columnstore index

CREATE NONCLUSTERED COLUMNSTORE INDEX [IX_ColumnStore_tblESV_time_space_cluster_size_taxon] ON [dbo].[tblESV]
(
	[time],
	[lat] ,
	[lon] ,
	[depth],
	[cruise_name],
	[cluster_level] ,
	[num_cluster_members],
	[size_frac_lower],
	[size_frac_upper],
	[domain],
	[kingdom],
	[phylum],
	[class],
	[order]
)
WITH (DATA_COMPRESSION = COLUMNSTORE)
ON [FG1]
GO


*/
