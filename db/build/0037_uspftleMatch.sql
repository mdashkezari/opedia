USE [Opedia]
GO


SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROC [dbo].[uspftleMatch] @ftleTable NVARCHAR(MAX), @ftleField NVARCHAR(MAX), @ftleValue NVARCHAR(MAX), @bkgTable NVARCHAR(MAX), @bkgField NVARCHAR(MAX), @dt1 NVARCHAR(MAX), @dt2 NVARCHAR(MAX), @lat1 NVARCHAR(MAX), @lat2 NVARCHAR(MAX), @lon1 NVARCHAR(MAX), @lon2 NVARCHAR(MAX), @margin NVARCHAR(MAX), @extV NVARCHAR(MAX), @extVV NVARCHAR(MAX)
AS
BEGIN
	DECLARE @query as NVARCHAR(MAX)
	SET NOCOUNT ON;
	
	SET @query = 
	'DROP TABLE IF EXISTS #tblGeometry; ' + 
	'DROP TABLE IF EXISTS #tblBkg; ' +
	'SELECT * INTO #tblGeometry FROM '+ RTRIM(LTRIM(@ftleTable)) +' WHERE [time] >=''' + RTRIM(LTRIM(@dt1)) + '''' + ' AND [time] <= ''' + RTRIM(LTRIM(@dt2)) + '''' + ' AND lat>='+ RTRIM(LTRIM(@lat1)) +' AND lat<='+ RTRIM(LTRIM(@lat2)) +' AND lon>='+ RTRIM(LTRIM(@lon1)) +' AND lon<='+ RTRIM(LTRIM(@lat2)) +' AND '+ RTRIM(LTRIM(@ftleField)) +'>='+ RTRIM(LTRIM(@ftleValue)) +'; ' +    
	'SELECT * INTO #tblBkg FROM '+ RTRIM(LTRIM(@bkgTable)) +' WHERE [time] >=''' + RTRIM(LTRIM(@dt1)) + '''' + ' AND [time] <= ''' + RTRIM(LTRIM(@dt2)) + '''' + ' AND lat>='+ RTRIM(LTRIM(@lat1)) +' AND lat<='+ RTRIM(LTRIM(@lat2)) +' AND lon>='+ RTRIM(LTRIM(@lon1)) +' AND lon<='+ RTRIM(LTRIM(@lon2)) +'; ' +
	'SELECT [#tblBkg].[time], [#tblBkg].lat, [#tblBkg].lon, [#tblBkg].'+ RTRIM(LTRIM(@bkgField)) +' FROM #tblBkg WHERE EXISTS ' + 
	'(SELECT [#tblGeometry].[time], [#tblGeometry].lat, [#tblGeometry].lon FROM #tblGeometry WHERE ' +
	'[#tblGeometry].[time]=[#tblBkg].[time] AND ABS([#tblGeometry].lat-([#tblBkg].lat))<='+ RTRIM(LTRIM(@margin)) +' AND ABS([#tblGeometry].lon-([#tblBkg].lon))<='+ RTRIM(LTRIM(@margin)) +')'
	
	EXEC(@query)
END

GO


