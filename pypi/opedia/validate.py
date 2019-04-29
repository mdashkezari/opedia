import sys
import os
sys.path.append(os.path.dirname(__file__))


def stringCheck(tablesName, field):
    valid = False
    if not isinstance(tablesName, str):
        print('Error: table name is expected to be string.')
        return valid
    if not isinstance(field, str):
        print('Error: variable name is expected to be string.')
        return valid
    valid = True
    return valid


def listCheck(tables, variables):
    valid = False
    if not isinstance(tables, list):
        print('Error: table names are expected to be a list of strings.')
        return valid
    if not isinstance(variables, list):
        print('Error: variable names are expected to be a list of strings.')
        return valid
    if len(tables) != len(variables):
        print('Error: please provide equal number of tables and variables.')
        return valid    
    valid = True
    return valid


