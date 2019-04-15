USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE PROC [dbo].[uspGenericDenials] @obj NVARCHAR(MAX), @login NVARCHAR(MAX)
AS
BEGIN
	DECLARE @query AS NVARCHAR(MAX);
	SET NOCOUNT ON;

	SET @query = 'DENY VIEW DEFINITION ON  ' + RTRIM(LTRIM(@obj)) + ' TO ' + RTRIM(LTRIM(@login)) + '; '
	EXEC(@query);
	SET @query = 'DENY SELECT ON  ' + RTRIM(LTRIM(@obj)) + ' TO ' + RTRIM(LTRIM(@login)) + '; '
	EXEC(@query);
	SET @query = 'DENY UPDATE ON  ' + RTRIM(LTRIM(@obj)) + ' TO ' + RTRIM(LTRIM(@login)) + '; '
	EXEC(@query);
	SET @query = 'DENY INSERT ON  ' + RTRIM(LTRIM(@obj)) + ' TO ' + RTRIM(LTRIM(@login)) + '; '
	EXEC(@query);
	SET @query = 'DENY DELETE ON  ' + RTRIM(LTRIM(@obj)) + ' TO ' + RTRIM(LTRIM(@login)) + '; '
	EXEC(@query);
	SET @query = 'DENY ALTER ON  ' + RTRIM(LTRIM(@obj)) + ' TO ' + RTRIM(LTRIM(@login)) + '; '
	EXEC(@query);
END
GO
