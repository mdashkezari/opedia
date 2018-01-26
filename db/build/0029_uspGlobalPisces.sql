USE [Opedia]
GO

/****** Object:  StoredProcedure [dbo].[uspGlobalWind]    Script Date: 12/23/2017 4:51:30 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO








CREATE PROC [dbo].[uspGlobalPisces] @tableName NVARCHAR(MAX), @fields NVARCHAR(MAX), @dt NVARCHAR(MAX), @dp NVARCHAR(MAX)
WITH RECOMPILE AS
BEGIN
	DECLARE @query as NVARCHAR(MAX)
	SET NOCOUNT ON;
	SET @query = 'SELECT ' + RTRIM(LTRIM(@fields)) + ' FROM ' + RTRIM(LTRIM(@tableName)) + ' WHERE [time] = ''' + RTRIM(LTRIM(@dt)) + '''' + ' AND [depth]=' + @dp + ' ORDER BY lat, lon' 
	EXEC(@query)
END

GO
