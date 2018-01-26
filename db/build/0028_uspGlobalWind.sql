USE [Opedia]
GO

/****** Object:  StoredProcedure [dbo].[uspGlobalWind]    Script Date: 12/23/2017 3:55:20 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO







CREATE PROC [dbo].[uspGlobalWind] @tableName NVARCHAR(MAX), @fields NVARCHAR(MAX), @dt NVARCHAR(MAX), @hr NVARCHAR(MAX)
WITH RECOMPILE AS
BEGIN
	DECLARE @query as NVARCHAR(MAX)
	SET NOCOUNT ON;
	SET @query = 'SELECT ' + RTRIM(LTRIM(@fields)) + ' FROM ' + RTRIM(LTRIM(@tableName)) + ' WHERE [time] = ''' + RTRIM(LTRIM(@dt)) + '''' + ' AND [hour]=' + @hr + ' ORDER BY lat, lon' 
	EXEC(@query)
END

GO


