USE [Opedia]
GO


SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROC [dbo].[uspftleMatch] @ftleTable NVARCHAR(MAX), @ftleField NVARCHAR(MAX), @ftleValue NVARCHAR(MAX), 
								@bkgTable NVARCHAR(MAX), @bkgField NVARCHAR(MAX), 
								@dt1 NVARCHAR(MAX), @dt2 NVARCHAR(MAX), 
								@lat1 NVARCHAR(MAX), @lat2 NVARCHAR(MAX), 
								@lon1 NVARCHAR(MAX), @lon2 NVARCHAR(MAX), 
								@depth1 NVARCHAR(MAX), @depth2 NVARCHAR(MAX),
								@margin NVARCHAR(MAX), @bkg NVARCHAR(MAX)
--WITH RECOMPILE								
AS
BEGIN
	SET NOCOUNT ON;
	DECLARE @query as NVARCHAR(MAX)
	DECLARE @sub_query as NVARCHAR(MAX)
	DECLARE @bkg_query as NVARCHAR(MAX)
	DECLARE @timeQuery AS NVARCHAR(MAX)
	DECLARE @bkg_timeQuery AS NVARCHAR(MAX)
	DECLARE @latQuery AS NVARCHAR(MAX)
	DECLARE @lonQuery AS NVARCHAR(MAX)
	DECLARE @depthQuery AS NVARCHAR(MAX)
	DECLARE @bkgTimeField AS NVARCHAR(MAX)
	DECLARE @bkg_dt1 AS NVARCHAR(MAX)
	DECLARE @bkg_dt2 AS NVARCHAR(MAX)
	DECLARE @bkg_selList AS NVARCHAR(MAX)
	DECLARE @bkg_cond AS NVARCHAR(MAX)
	DECLARE @geom_subQuery_time AS NVARCHAR(MAX)

	SET @timeQuery = ' WHERE [time] BETWEEN ''' + RTRIM(LTRIM(@dt1)) + '''' + ' AND ''' + RTRIM(LTRIM(@dt2)) + '''';
	SET @bkg_timeQuery =  @timeQuery
	SET @latQuery = ' AND lat BETWEEN ' + RTRIM(LTRIM(@lat1)) + ' AND ' + RTRIM(LTRIM(@lat2));
	SET @lonQuery = ' AND lon BETWEEN ' + RTRIM(LTRIM(@lon1)) + ' AND ' + RTRIM(LTRIM(@lon2));
	SET @depthQuery = ' AND depth BETWEEN ' + RTRIM(LTRIM(@depth1)) + ' AND ' + RTRIM(LTRIM(@depth2));

	SET @bkg_cond = ''
	IF RTRIM(LTRIM(@bkg)) IN ('1')
	BEGIN
		SET @bkg_cond = ' NOT '
	END


	SET @bkgTimeField = '[time]'
	SET @bkg_dt1 = @dt1
	SET @bkg_dt2 = @dt2
	SET @geom_subQuery_time = '[#tblGeometry].[time]'
	IF @bkgTable LIKE '%_Climatology'			-- if the background table represents a climatology data set
	BEGIN
		IF COL_LENGTH(RTRIM(LTRIM(@bkgTable)), 'month') IS NOT NULL	-- if table has month field
		BEGIN
			SET @bkgTimeField = '[month]'
			SET @bkg_dt1 = DATEPART(month, @dt1);
			SET @bkg_dt2 = DATEPART(month, @dt2);
			SET @bkg_timeQuery = ' WHERE ' + @bkgTimeField + ' BETWEEN ' + RTRIM(LTRIM(@bkg_dt1)) + ' AND ' + RTRIM(LTRIM(@bkg_dt2));

			SET @geom_subQuery_time = 'DATEPART(month, [#tblGeometry].[time])'
		END
	END


	SET @query = 
	'DROP TABLE IF EXISTS #tblGeometry; ' + 'DROP TABLE IF EXISTS #tblBkg; ' +
	'SELECT * INTO #tblGeometry FROM '+ RTRIM(LTRIM(@ftleTable)) + @timeQuery + @latQuery +	@lonQuery + 
	' AND '+ RTRIM(LTRIM(@ftleField)) +'>='+ RTRIM(LTRIM(@ftleValue)) +'; '; 
	
	
	SET @bkg_selList = 'SELECT [#tblBkg].'+ @bkgTimeField +', [#tblBkg].lat, [#tblBkg].lon, [#tblBkg].'+ RTRIM(LTRIM(@bkgField));
	SET @bkg_query = 'SELECT * INTO #tblBkg FROM '+ RTRIM(LTRIM(@bkgTable)) + @bkg_timeQuery + @latQuery + @lonQuery;
	IF COL_LENGTH(RTRIM(LTRIM(@bkgTable)), 'depth') IS NOT NULL	-- if backgroundtable has depth field
	BEGIN
		SET @bkg_query = @bkg_query + @depthQuery;
		SET @bkg_selList = 'SELECT [#tblBkg].'+ @bkgTimeField +', [#tblBkg].lat, [#tblBkg].lon, [#tblBkg].depth, [#tblBkg].'+ RTRIM(LTRIM(@bkgField))
	END
	SET @bkg_query = @bkg_query + '; '


	SET @sub_query = @bkg_selList +' FROM #tblBkg WHERE ' + @bkg_cond + ' EXISTS ' + 
	'(SELECT [#tblGeometry].[time], [#tblGeometry].lat, [#tblGeometry].lon FROM #tblGeometry WHERE ' +
	@geom_subQuery_time + '=[#tblBkg].'+ @bkgTimeField +' AND ABS([#tblGeometry].lat-([#tblBkg].lat))<='+ RTRIM(LTRIM(@margin)) +' AND ABS([#tblGeometry].lon-([#tblBkg].lon))<='+ RTRIM(LTRIM(@margin)) +')';
	

	SET @query = @query + @bkg_query + @sub_query;
	
	EXEC(@query)
END

GO





/*
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

*/
