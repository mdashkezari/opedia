USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE PROC [dbo].[uspSectionMap] @tableName NVARCHAR(MAX), @fields NVARCHAR(MAX), 
								 @dt1 NVARCHAR(MAX), @dt2 NVARCHAR(MAX), 
								 @lat1 NVARCHAR(MAX), @lat2 NVARCHAR(MAX), 
								 @lon1 NVARCHAR(MAX), @lon2 NVARCHAR(MAX), 
								 @depth1 NVARCHAR(MAX), @depth2 NVARCHAR(MAX)
--WITH RECOMPILE 
AS
BEGIN
	DECLARE @query AS NVARCHAR(MAX);
	SET NOCOUNT ON;

	DECLARE @timeQuery AS NVARCHAR(MAX)
	DECLARE @latQuery AS NVARCHAR(MAX)
	DECLARE @lonQuery AS NVARCHAR(MAX)
	DECLARE @depthQuery AS NVARCHAR(MAX)
	SET @timeQuery = ' WHERE [time] BETWEEN ''' + RTRIM(LTRIM(@dt1)) + '''' + ' AND ''' + RTRIM(LTRIM(@dt2)) + '''';
	SET @latQuery = ' AND lat BETWEEN ' + RTRIM(LTRIM(@lat1)) + ' AND ' + RTRIM(LTRIM(@lat2));
	SET @lonQuery = ' AND lon BETWEEN ' + RTRIM(LTRIM(@lon1)) + ' AND ' + RTRIM(LTRIM(@lon2));
	SET @depthQuery = ' AND depth BETWEEN ' + RTRIM(LTRIM(@depth1)) + ' AND ' + RTRIM(LTRIM(@depth2));


	DECLARE @timeField AS NVARCHAR(50)
	SET @timeField = '[time]'
	IF @tableName LIKE '%_Climatology'			-- if table represents a climatology data set
	BEGIN
		IF COL_LENGTH(RTRIM(LTRIM(@tableName)), 'month') IS NOT NULL	-- if table has month field
		BEGIN
			SET @timeField = '[month]'
			SET @dt1 = DATEPART(month, @dt1);
			SET @dt2 = DATEPART(month, @dt2);
			SET @timeQuery = ' WHERE ' + @timeField + ' BETWEEN ' + RTRIM(LTRIM(@dt1)) + ' AND ' + RTRIM(LTRIM(@dt2));
		END
	END


    DECLARE @orderList AS NVARCHAR(MAX);
	SET @orderList = ' ORDER BY ' + RTRIM(LTRIM(@timeField));
	IF COL_LENGTH(RTRIM(LTRIM(@tableName)), 'hour') IS NOT NULL	-- if table has hour field
	BEGIN
		SET @orderList = @orderList + ', [hour]'
	END
    SET @orderList = @orderList + ', lat, lon, depth'

	DECLARE @selList AS NVARCHAR(MAX);
	
	-------------- construct the query --------------
	IF COL_LENGTH(RTRIM(LTRIM(@tableName)), 'depth') IS NOT NULL	-- if table has depth field
	BEGIN
		SET @selList = @timeField + ', lat, lon, depth, ' + RTRIM(LTRIM(@fields));
        SET @query = 'SELECT ' + @selList + ' FROM ' + RTRIM(LTRIM(@tableName)) + 
		@timeQuery +
		@latQuery +
		@lonQuery + 
		@depthQuery + 
        @orderList
	END
	-------------------------------------------------
	EXEC(@query)
END
GO