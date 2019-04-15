#!/usr/bin/env python


import os
import sys
sys.path.append('../config')
import config_vault as cfgv
from datetime import date
from datetime import datetime



def dateToDayn(dt):
	dayn = int(format(dt, '%j'))
	dayn += dt.year * 1000
	return dayn


def daynToDate(dt):
	year = int(dt / 1000)
	dayn = int(dt % 1000)
	dat = date.fromordinal(date(year, 1, 1).toordinal() + dayn - 1)
	return dat
