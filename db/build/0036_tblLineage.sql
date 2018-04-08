USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblLineage](
	[tax_id] [int] NOT NULL,
	[superkingdom] [nchar](100) NULL,
	[phylum] [nchar](100) NULL,
	[class] [nchar](100) NULL,
	[order] [nchar](100) NULL,
	[family] [nchar](100) NULL,
	[genus] [nchar](100) NULL,
	[species] [nchar](200) NULL,
	[cohort] [nchar](100) NULL,
	[forma] [nchar](100) NULL,
	[infraclass] [nchar](100) NULL,
	[infraorder] [nchar](100) NULL,
	[kingdom] [nchar](100) NULL,
	[no_rank] [nchar](100) NULL,
	[no_rank1] [nchar](200) NULL,
	[no_rank10] [nvarchar](MAX) NULL,
	[no_rank11] [nvarchar](MAX) NULL,
	[no_rank12] [nvarchar](MAX) NULL,
	[no_rank13] [nvarchar](MAX) NULL,
	[no_rank14] [nvarchar](MAX) NULL,
	[no_rank15] [nvarchar](MAX) NULL,
	[no_rank16] [nvarchar](MAX) NULL,
	[no_rank17] [nvarchar](MAX) NULL,
	[no_rank18] [nvarchar](MAX) NULL,
	[no_rank19] [nvarchar](MAX) NULL,
	[no_rank2] [nvarchar](MAX) NULL,
	[no_rank20] [nvarchar](MAX) NULL,
	[no_rank21] [nvarchar](MAX) NULL,
	[no_rank3] [nvarchar](MAX) NULL,
	[no_rank4] [nvarchar](MAX) NULL,
	[no_rank5] [nvarchar](MAX) NULL,
	[no_rank6] [nvarchar](MAX) NULL,
	[no_rank7] [nvarchar](MAX) NULL,
	[no_rank8] [nvarchar](MAX) NULL,
	[no_rank9] [nvarchar](MAX) NULL,
	[parvorder] [nvarchar](MAX) NULL,
	[species_group] [nvarchar](MAX) NULL,
	[species_subgroup] [nvarchar](MAX) NULL,
	[species1] [nvarchar](MAX) NULL,
	[subclass] [nvarchar](MAX) NULL,
	[subfamily] [nvarchar](MAX) NULL,
	[subgenus] [nvarchar](MAX) NULL,
	[subkingdom] [nvarchar](MAX) NULL,
	[suborder] [nvarchar](MAX) NULL,
	[subphylum] [nvarchar](MAX) NULL,
	[subspecies] [nvarchar](MAX) NULL,
	[subtribe] [nvarchar](MAX) NULL,
	[superclass] [nvarchar](MAX) NULL,
	[superfamily] [nvarchar](MAX) NULL,
	[superfamily1] [nvarchar](MAX) NULL,
	[superorder] [nvarchar](MAX) NULL,
	[superphylum] [nvarchar](MAX) NULL,
	[tribe] [nvarchar](MAX) NULL,
	[varietas] [nvarchar](MAX) NULL,
 CONSTRAINT [PK_tblLineage] PRIMARY KEY CLUSTERED 
(
	[tax_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO



---------------------
-- Indices
---------------------


CREATE NONCLUSTERED INDEX [IX_tblLineage_superkingdom] ON [dbo].[tblLineage]
(
	[superkingdom] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblLineage_phylum] ON [dbo].[tblLineage]
(
	[phylum] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblLineage_class] ON [dbo].[tblLineage]
(
	[class] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblLineage_order] ON [dbo].[tblLineage]
(
	[order] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblLineage_family] ON [dbo].[tblLineage]
(
	[family] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblLineage_genus] ON [dbo].[tblLineage]
(
	[genus] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblLineage_species] ON [dbo].[tblLineage]
(
	[species] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblLineage_cohort] ON [dbo].[tblLineage]
(
	[cohort] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblLineage_forma] ON [dbo].[tblLineage]
(
	[forma] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblLineage_infraclass] ON [dbo].[tblLineage]
(
	[infraclass] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblLineage_infraorder] ON [dbo].[tblLineage]
(
	[infraorder] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblLineage_kingdom] ON [dbo].[tblLineage]
(
	[kingdom] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblLineage_no_rank] ON [dbo].[tblLineage]
(
	[no_rank] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO


CREATE NONCLUSTERED INDEX [IX_tblLineage_no_rank1] ON [dbo].[tblLineage]
(
	[no_rank1] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [PRIMARY]
GO

