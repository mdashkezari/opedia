
USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblArgoMerge_REP](
	[float_id] [int] NOT NULL,
	[cycle] [int] NOT NULL,
	[time] [date] NOT NULL,
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[depth] [float] NOT NULL,
	[position_qc] [int] NULL,
	[direction] [char](1) NULL,
	[data_mode] [char](1) NULL,
	[data_centre] [char](2) NULL,
	
	[argo_merge_cdnc] [float] NULL,
	[argo_merge_cdnc_qc] [float] NULL,
	[argo_merge_cdnc_adj] [float] NULL,
	[argo_merge_cdnc_adj_qc] [float] NULL,
	[argo_merge_cdnc_adj_err] [float] NULL,

	[argo_merge_pressure] [float] NULL,
	[argo_merge_pressure_qc] [float] NULL,
	[argo_merge_pressure_adj] [float] NULL,
	[argo_merge_pressure_adj_qc] [float] NULL,
	[argo_merge_pressure_adj_err] [float] NULL,

	[argo_merge_salinity] [float] NULL,
	[argo_merge_salinity_qc] [float] NULL,
	[argo_merge_salinity_adj] [float] NULL,
	[argo_merge_salinity_adj_qc] [float] NULL,
	[argo_merge_salinity_adj_err] [float] NULL,

	[argo_merge_temperature] [float] NULL,
	[argo_merge_temperature_qc] [float] NULL,
	[argo_merge_temperature_adj] [float] NULL,
	[argo_merge_temperature_adj_qc] [float] NULL,
	[argo_merge_temperature_adj_err] [float] NULL,

	[argo_merge_O2] [float] NULL,
	[argo_merge_O2_qc] [float] NULL,
	[argo_merge_O2_adj] [float] NULL,
	[argo_merge_O2_adj_qc] [float] NULL,
	[argo_merge_O2_adj_err] [float] NULL,

	[argo_merge_bbp] [float] NULL,
	[argo_merge_bbp_qc] [float] NULL,
	[argo_merge_bbp_adj] [float] NULL,
	[argo_merge_bbp_adj_qc] [float] NULL,
	[argo_merge_bbp_adj_err] [float] NULL,

	[argo_merge_bbp470] [float] NULL,
	[argo_merge_bbp470_qc] [float] NULL,
	[argo_merge_bbp470_adj] [float] NULL,
	[argo_merge_bbp470_adj_qc] [float] NULL,
	[argo_merge_bbp470_adj_err] [float] NULL,

	[argo_merge_bbp532] [float] NULL,
	[argo_merge_bbp532_qc] [float] NULL,
	[argo_merge_bbp532_adj] [float] NULL,
	[argo_merge_bbp532_adj_qc] [float] NULL,
	[argo_merge_bbp532_adj_err] [float] NULL,

	[argo_merge_bbp700] [float] NULL,
	[argo_merge_bbp700_qc] [float] NULL,
	[argo_merge_bbp700_adj] [float] NULL,
	[argo_merge_bbp700_adj_qc] [float] NULL,
	[argo_merge_bbp700_adj_err] [float] NULL,

	[argo_merge_turbidity] [float] NULL,
	[argo_merge_turbidity_qc] [float] NULL,
	[argo_merge_turbidity_adj] [float] NULL,
	[argo_merge_turbidity_adj_qc] [float] NULL,
	[argo_merge_turbidity_adj_err] [float] NULL,

	[argo_merge_cp] [float] NULL,
	[argo_merge_cp_qc] [float] NULL,
	[argo_merge_cp_adj] [float] NULL,
	[argo_merge_cp_adj_qc] [float] NULL,
	[argo_merge_cp_adj_err] [float] NULL,

	[argo_merge_cp660] [float] NULL,
	[argo_merge_cp660_qc] [float] NULL,
	[argo_merge_cp660_adj] [float] NULL,
	[argo_merge_cp660_adj_qc] [float] NULL,
	[argo_merge_cp660_adj_err] [float] NULL,

	[argo_merge_chl] [float] NULL,
	[argo_merge_chl_qc] [float] NULL,
	[argo_merge_chl_adj] [float] NULL,
	[argo_merge_chl_adj_qc] [float] NULL,
	[argo_merge_chl_adj_err] [float] NULL,

	[argo_merge_cdom] [float] NULL,
	[argo_merge_cdom_qc] [float] NULL,
	[argo_merge_cdom_adj] [float] NULL,
	[argo_merge_cdom_adj_qc] [float] NULL,
	[argo_merge_cdom_adj_err] [float] NULL,

	[argo_merge_NO3] [float] NULL,
	[argo_merge_NO3_qc] [float] NULL,
	[argo_merge_NO3_adj] [float] NULL,
	[argo_merge_NO3_adj_qc] [float] NULL,
	[argo_merge_NO3_adj_err] [float] NULL,

	[argo_merge_bisulfide] [float] NULL,
	[argo_merge_bisulfide_qc] [float] NULL,
	[argo_merge_bisulfide_adj] [float] NULL,
	[argo_merge_bisulfide_adj_qc] [float] NULL,
	[argo_merge_bisulfide_adj_err] [float] NULL,

	[argo_merge_ph] [float] NULL,
	[argo_merge_ph_qc] [float] NULL,
	[argo_merge_ph_adj] [float] NULL,
	[argo_merge_ph_adj_qc] [float] NULL,
	[argo_merge_ph_adj_err] [float] NULL,

	[argo_merge_down_irr] [float] NULL,
	[argo_merge_down_irr_qc] [float] NULL,
	[argo_merge_down_irr_adj] [float] NULL,
	[argo_merge_down_irr_adj_qc] [float] NULL,
	[argo_merge_down_irr_adj_err] [float] NULL,

	[argo_merge_down_irr380] [float] NULL,
	[argo_merge_down_irr380_qc] [float] NULL,
	[argo_merge_down_irr380_adj] [float] NULL,
	[argo_merge_down_irr380_adj_qc] [float] NULL,
	[argo_merge_down_irr380_adj_err] [float] NULL,

	[argo_merge_down_irr412] [float] NULL,
	[argo_merge_down_irr412_qc] [float] NULL,
	[argo_merge_down_irr412_adj] [float] NULL,
	[argo_merge_down_irr412_adj_qc] [float] NULL,
	[argo_merge_down_irr412_adj_err] [float] NULL,

	[argo_merge_down_irr443] [float] NULL,
	[argo_merge_down_irr443_qc] [float] NULL,
	[argo_merge_down_irr443_adj] [float] NULL,
	[argo_merge_down_irr443_adj_qc] [float] NULL,
	[argo_merge_down_irr443_adj_err] [float] NULL,

	[argo_merge_down_irr490] [float] NULL,
	[argo_merge_down_irr490_qc] [float] NULL,
	[argo_merge_down_irr490_adj] [float] NULL,
	[argo_merge_down_irr490_adj_qc] [float] NULL,
	[argo_merge_down_irr490_adj_err] [float] NULL,

	[argo_merge_down_irr555] [float] NULL,
	[argo_merge_down_irr555_qc] [float] NULL,
	[argo_merge_down_irr555_adj] [float] NULL,
	[argo_merge_down_irr555_adj_qc] [float] NULL,
	[argo_merge_down_irr555_adj_err] [float] NULL,

	[argo_merge_up_irr] [float] NULL,
	[argo_merge_up_irr_qc] [float] NULL,
	[argo_merge_up_irr_adj] [float] NULL,
	[argo_merge_up_irr_adj_qc] [float] NULL,
	[argo_merge_up_irr_adj_err] [float] NULL,

	[argo_merge_up_irr412] [float] NULL,
	[argo_merge_up_irr412_qc] [float] NULL,
	[argo_merge_up_irr412_adj] [float] NULL,
	[argo_merge_up_irr412_adj_qc] [float] NULL,
	[argo_merge_up_irr412_adj_err] [float] NULL,

	[argo_merge_up_irr443] [float] NULL,
	[argo_merge_up_irr443_qc] [float] NULL,
	[argo_merge_up_irr443_adj] [float] NULL,
	[argo_merge_up_irr443_adj_qc] [float] NULL,
	[argo_merge_up_irr443_adj_err] [float] NULL,

	[argo_merge_up_irr490] [float] NULL,
	[argo_merge_up_irr490_qc] [float] NULL,
	[argo_merge_up_irr490_adj] [float] NULL,
	[argo_merge_up_irr490_adj_qc] [float] NULL,
	[argo_merge_up_irr490_adj_err] [float] NULL,

	[argo_merge_up_irr555] [float] NULL,
	[argo_merge_up_irr555_qc] [float] NULL,
	[argo_merge_up_irr555_adj] [float] NULL,
	[argo_merge_up_irr555_adj_qc] [float] NULL,
	[argo_merge_up_irr555_adj_err] [float] NULL,

	[argo_merge_down_par] [float] NULL,
	[argo_merge_down_par_qc] [float] NULL,
	[argo_merge_down_par_adj] [float] NULL,
	[argo_merge_down_par_adj_qc] [float] NULL,
	[argo_merge_down_par_adj_err] [float] NULL,

	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblArgoMerge_REP] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG3]
) ON [FG3]

GO




---------------------
-- Indices
---------------------


USE [Opedia]
GO


CREATE NONCLUSTERED INDEX [IX_tblArgoMerge_REP_time_lat_lon_depth] ON [dbo].[tblArgoMerge_REP]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC,
	[depth] ASC
)
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG3]
GO

