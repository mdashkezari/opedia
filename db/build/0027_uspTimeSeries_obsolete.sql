USE [Opedia]
GO

/****** Object:  StoredProcedure [dbo].[uspTimeSeries]    Script Date: 12/25/2017 8:00:17 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE PROC [dbo].[uspTimeSeries] @tableName NVARCHAR(MAX), @fields NVARCHAR(MAX), @dt NVARCHAR(MAX), @lat1 NVARCHAR(MAX), @lat2 NVARCHAR(MAX), @lon1 NVARCHAR(MAX), @lon2 NVARCHAR(MAX), @arg8_name NVARCHAR(MAX), @arg8_val NVARCHAR(MAX)
AS
BEGIN
	DECLARE @query as NVARCHAR(MAX)
	SET NOCOUNT ON;
	SET @query = 'SELECT lat, lon, ' + RTRIM(LTRIM(@fields)) + ' FROM ' + RTRIM(LTRIM(@tableName)) + 
	' WHERE [time] = ''' + RTRIM(LTRIM(@dt)) + '''' + 
	' AND lat >= ' + RTRIM(LTRIM(@lat1)) + ' AND lat <= ' + RTRIM(LTRIM(@lat2)) +
	' AND lon >= ' + RTRIM(LTRIM(@lon1)) + ' AND lon <= ' + RTRIM(LTRIM(@lon2)) + 
	' AND [' + RTRIM(LTRIM(@arg8_name)) + ']=' + RTRIM(LTRIM(@arg8_val))

	IF @arg8_name IS NULL
	BEGIN
	SET @query = 'SELECT lat, lon, ' + RTRIM(LTRIM(@fields)) + ' FROM ' + RTRIM(LTRIM(@tableName)) + 
	' WHERE [time] = ''' + RTRIM(LTRIM(@dt)) + '''' + 
	' AND lat >= ' + RTRIM(LTRIM(@lat1)) + ' AND lat <= ' + RTRIM(LTRIM(@lat2)) +
	' AND lon >= ' + RTRIM(LTRIM(@lon1)) + ' AND lon <= ' + RTRIM(LTRIM(@lon2))
	END


	EXEC(@query)
END
GO


