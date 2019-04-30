
USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





CREATE TABLE [dbo].[tblHOT224 ](
	[time] [date] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[depth] [float] NOT NULL,
	[pressure] [float] NULL,
	[synechococcus_abundance] [float] NULL,
	[particulate_phosphorus] [float] NULL,
	[sra_study] [nchar](50) NULL,
	[sra_biosample] [nchar](50) NULL,
	[filter_min] [float] NULL,
	[nitrate_and_nitrite] [float] NULL,
	[alkalinity] [float] NULL,
	[silicate] [float] NULL,
	[chlorophyll_c] [float] NULL,
	[temperature_potential] [float] NULL,
	[carotene-alpha] [float] NULL,
	[sra_experiment] [nchar](50) NULL,
	[dissolved_oxygen] [float] NULL,
	[temperature_ctd] [float] NULL,
	[sra_run] [nchar](50) NULL,
	[filter_max] [float] NULL,
	[carotene-beta] [float] NULL,
	[19-prime-butanoyloxyfucoxanthin] [float] NULL,
	[salinity_ctd] [float] NULL,
	[dissolved_organic_carbon] [float] NULL,
	[divinyl_chlorophyll_a] [float] NULL,
	[violaxanthin] [float] NULL,
	[atp] [float] NULL,
	[sra_sample] [nchar](50) NULL,
	[fluorometric_chlorophyll_a] [float] NULL,
	[total_phaeopigment] [float] NULL,
	[19-prime-hexanoyloxyfucoxanthin] [float] NULL,
	[monovinyl_chlorophyll_a] [float] NULL,
	[peridinin] [float] NULL,
	[rosette_position] [float] NULL,
	[chlorophyll_a] [float] NULL,
	[diadinoxanthin] [float] NULL,
	[fucoxanthin] [float] NULL,
	[dissolved_inorganic_carbon] [float] NULL,
	[prochlorococcus_abundance] [float] NULL,
	[heterotrophic_bacteria_abundance] [float] NULL,
	[sequencing_method] [nchar](50) NULL,
	[library_kit][nchar](50) NULL,
	[sequence_type] [nchar](50) NULL,
	[pico_eukaryote_abundance] [float] NULL,
	[particulate_nitrogen] [float] NULL,
	[chlorophyll_b] [float] NULL,
	[filter_type] [nchar](50) NULL,
	[low_level_phosphorus] [float] NULL,
	[zeaxanthin] [float] NULL,
	[particulate_silica] [float] NULL,
	[density_potential] [float] NULL,
	[low_level_nitrogen] [float] NULL,
	[phosphate] [float] NULL,
	[particulate_carbon] [float] NULL,
	[sra_bioproject] [nchar](50) NULL,
	[dissolved_oxygen_ctd] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblHOT224 ] PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (/*DATA_COMPRESSION = PAGE,*/ PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG1]
) ON [FG1]

GO



-- -------------------
-- Indices
-- -------------------
--


CREATE NONCLUSTERED INDEX [IX_tblHOT224 _time_lat_lon] ON [dbo].[tblHOT224 ]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC,
	[depth] ASC
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG2]
GO
