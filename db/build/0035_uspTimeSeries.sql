USE [Opedia]
GO


SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





CREATE PROC [dbo].[uspTimeSeries] @tableName NVARCHAR(MAX), @fields NVARCHAR(MAX), @dt1 NVARCHAR(MAX), @dt2 NVARCHAR(MAX), @lat1 NVARCHAR(MAX), @lat2 NVARCHAR(MAX), @lon1 NVARCHAR(MAX), @lon2 NVARCHAR(MAX), @arg8_name NVARCHAR(MAX), @arg8_val NVARCHAR(MAX)
AS
BEGIN
	DECLARE @query as NVARCHAR(MAX)
	SET NOCOUNT ON;
	SET @query = 'SELECT [time], AVG(lat), AVG(lon) ' + ', AVG(' + RTRIM(LTRIM(@fields)) + ') AS ' + RTRIM(LTRIM(@fields)) + ', STDEV(' + RTRIM(LTRIM(@fields)) + ') AS ' + RTRIM(LTRIM(@fields)) +'_std FROM ' + RTRIM(LTRIM(@tableName)) + 
	' WHERE [time] >= ''' + RTRIM(LTRIM(@dt1)) + '''' + ' AND [time] <= ''' + RTRIM(LTRIM(@dt2)) + '''' +
	' AND lat >= ' + RTRIM(LTRIM(@lat1)) + ' AND lat <= ' + RTRIM(LTRIM(@lat2)) +
	' AND lon >= ' + RTRIM(LTRIM(@lon1)) + ' AND lon <= ' + RTRIM(LTRIM(@lon2)) + 
	' AND ABS(' + RTRIM(LTRIM(@fields)) + ')<1e30' + 
	' AND [' + RTRIM(LTRIM(@arg8_name)) + ']=' + RTRIM(LTRIM(@arg8_val)) + 
	' GROUP BY [time] ORDER BY [time]'

	IF @arg8_name IS NULL
	BEGIN
	SET @query = 'SELECT [time], AVG(lat), AVG(lon) ' + ', AVG(' + RTRIM(LTRIM(@fields)) + ') AS ' + RTRIM(LTRIM(@fields)) + ', STDEV(' + RTRIM(LTRIM(@fields)) + ') AS ' + RTRIM(LTRIM(@fields)) +'_std FROM ' + RTRIM(LTRIM(@tableName)) + 
	' WHERE [time] >= ''' + RTRIM(LTRIM(@dt1)) + '''' + ' AND [time] <= ''' + RTRIM(LTRIM(@dt2)) + '''' +
	' AND lat >= ' + RTRIM(LTRIM(@lat1)) + ' AND lat <= ' + RTRIM(LTRIM(@lat2)) +
	' AND lon >= ' + RTRIM(LTRIM(@lon1)) + ' AND lon <= ' + RTRIM(LTRIM(@lon2)) + 
	' AND ABS(' + RTRIM(LTRIM(@fields)) + ')<1e30' + 
	' GROUP BY [time] ORDER BY [time]'
	END


	EXEC(@query)
END

GO


