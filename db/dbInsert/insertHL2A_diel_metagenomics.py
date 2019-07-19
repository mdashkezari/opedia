import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import config_vault as cfgv
import pandas as pd

############################
########### OPTS ###########

tableName = 'tblHL2A_diel_metagenomics'
rawFilePath = cfgv.rep_HL2A_diel_metagenomics_raw
rawFileName = 'HL2A_cmap_omics_ED2.xlsx'
usecols=['time','lat','lon','depth','station','cast_num','sra_experiment','sra_run','filter_type','filter_max','sra_bioproject','filter_min','library_kit','sequence_type','sequencing_method']



def makeHL2A_diel_metagenomics(rawFilePath, rawFileName, tableName):
    path = rawFilePath + rawFileName
    prefix = tableName
    exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
    export_path = '%s%s.csv' % (exportBase, prefix)
    df = pd.read_excel(path,  sep=',',sheet_name='data', usecols=usecols)
    df = ip.removeMissings(['time','lat', 'lon','depth'], df)
    df = ip.NaNtoNone(df)
    df = ip.colDatatypes(df)
    df = ip.addIDcol(df)
    df = ip.removeDuplicates(df)
    df.to_csv(export_path, index=False)
    ip.sortByTimeLatLonDepth(df, export_path, 'time', 'lat', 'lon', 'depth')
    print('export path: ' ,export_path)
    return export_path


export_path = makeHL2A_diel_metagenomics(rawFilePath, rawFileName, tableName)
iF.toSQLbcp(export_path, tableName)
