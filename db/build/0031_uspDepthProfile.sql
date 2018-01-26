USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE PROC [dbo].[uspDepthProfile] @tableName NVARCHAR(MAX), @fields NVARCHAR(MAX), @dt NVARCHAR(MAX), @lat1 NVARCHAR(MAX), @lat2 NVARCHAR(MAX), @lon1 NVARCHAR(MAX), @lon2 NVARCHAR(MAX), @depth NVARCHAR(MAX)
AS
BEGIN
	DECLARE @query as NVARCHAR(MAX)
	SET NOCOUNT ON;
	SET @query = 'SELECT lat, lon, depth, ' + RTRIM(LTRIM(@fields)) + ' FROM ' + RTRIM(LTRIM(@tableName)) + 
	' WHERE [time] = ''' + RTRIM(LTRIM(@dt)) + '''' + 
	' AND lat >= ' + RTRIM(LTRIM(@lat1)) + ' AND lat <= ' + RTRIM(LTRIM(@lat2)) +
	' AND lon >= ' + RTRIM(LTRIM(@lon1)) + ' AND lon <= ' + RTRIM(LTRIM(@lon2)) + 
	' AND depth = ' + RTRIM(LTRIM(@depth))

	EXEC(@query)
END
GO