#!/usr/bin/env python

import os
#here = os.path.dirname(os.path.abspath(__file__)) + '/'
import dbCore as dbc
import math




def valsPlaceHolder(vals):
    Result = ''
    for i in range(0, len(vals)-1):
        Result = Result + "?, "
    Result = Result + "?"
    return Result


def nanToNone(rec):
        for index, item in enumerate(rec):
                rec[index] = item
                if math.isnan(item):
                        rec[index] = None
        return rec



def updateChecklist(dayn, year, month, day, field, val):
        table = 'tblChecklist'
        key = 'dayn'
        vals = [dayn, year, month, day, val]
	t_sql = '''
	BEGIN Try
		BEGIN TRANSACTION
		IF EXISTS(SELECT dayn FROM %s WHERE dayn = %d)
		BEGIN
			UPDATE %s SET %s = %d WHERE dayn = %d
		END
		ELSE
		BEGIN
			INSERT INTO %s (%s) VALUES (%s)
		END
		Commit Transaction
	End Try
	Begin Catch
		Rollback Transaction
	End Catch
	'''
	t_sql = t_sql % (table, dayn, table, field, val, dayn, table, 'dayn, year, month, day, ' + field, valsPlaceHolder(vals) )
        vals = nanToNone(vals)
        dbc.dbExecute(t_sql, vals)
	return



mergeChecklist(2015001, 2015, 1, 1, 'NRT_CHL_Raw', 1)
mergeChecklist(2015001, 2015, 1, 1, 'NRT_CHL_Raw', 1)
mergeChecklist(2013001, 2013, 1, 1, 'NRT_SLA_tile', 1)
mergeChecklist(2013001, 2013, 1, 1, 'NRT_SLA_RAW', 1)

