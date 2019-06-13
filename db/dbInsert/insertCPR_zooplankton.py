import sys
sys.path.append('../')
import insertFunctions as iF
import insertPrep as ip
import config_vault as cfgv
import pandas as pd

############################
########### OPTS ###########

tableName = 'tblCPR_zooplankton'
rawFilePath = cfgv.rep_CPR_zooplankton_raw
rawFileName = 'zoo_occurrence.txt'
usecols=['id', 'year', 'month', 'day','decimalLatitude', 'decimalLongitude', 'minimumDepthInMeters', 'taxonID', 'scientificNameID', 'scientificName', 'acceptedNameUsage']



# def makeCPR_zooplankton(rawFilePath, rawFileName, tableName):
path = rawFilePath + rawFileName
prefix = tableName
exportBase = cfgv.opedia_proj + 'db/dbInsert/export/'
export_path = '%s%s.csv' % (exportBase, prefix)
df = pd.read_csv(path, sep='\t', usecols=usecols)
df['time'] = pd.to_datetime(df[['year', 'month', 'day']])

combined_df = pd.DataFrame(columns=['taxonID','taxonID_counts','scientificNameID','scientificName','acceptedNameUsage', 'scientificNameID_counts', 'scientificName_counts', 'acceptedNameUsage_counts','time','lat','lon','depth'])
counter = 0
for unique_date in sorted(df['time'].unique()):
    counter += 1
    count_df = pd.DataFrame()
    df_select = df[df['time']==unique_date]
    # df_select = df[df['time'] == '2015-09-13']

    taxon_counts_df = df_select.taxonID.value_counts(sort=True).rename_axis('taxonID_counts').reset_index().rename(columns={'taxonID_counts': 'taxonID', 'taxonID': 'taxonID_counts'})
    scientificNameID_counts = df_select.scientificNameID.value_counts(sort=True).rename_axis('scientificNameID_counts').reset_index().rename(columns={'scientificNameID_counts': 'scientificNameID', 'scientificNameID': 'scientificNameID_counts'})
    scientificName_counts = df_select.scientificName.value_counts(sort=True).rename_axis('scientificName_counts').reset_index().rename(columns={'scientificName_counts': 'scientificName', 'scientificName': 'scientificName_counts'})
    acceptedName_counts = df_select.acceptedNameUsage.value_counts(sort=True).rename_axis('acceptedNameUsage_counts').reset_index().rename(columns={'acceptedNameUsage_counts': 'acceptedNameUsage', 'acceptedNameUsage': 'acceptedNameUsage_counts'})
    count_df['taxonID'] = taxon_counts_df['taxonID']
    count_df['taxonID_counts'] = taxon_counts_df['taxonID_counts']
    count_df['scientificNameID'] = scientificNameID_counts['scientificNameID']
    count_df['scientificNameID_counts'] = scientificNameID_counts['scientificNameID_counts']
    count_df['scientificName'] = scientificName_counts['scientificName']
    count_df['scientificName_counts'] = scientificName_counts['scientificName_counts']
    count_df['acceptedNameUsage'] = acceptedName_counts['acceptedNameUsage']
    count_df['acceptedNameUsage_counts'] = acceptedName_counts['acceptedNameUsage_counts']

    count_df['time'] = str(df_select['time'].iloc[0])
    count_df['lat'] = str(df_select['decimalLatitude'].iloc[0])
    count_df['lon'] = str(df_select['decimalLongitude'].iloc[0])
    count_df['depth'] = str(df_select['maximumDepthInMeters'].iloc[0])
    combined_df = combined_df.append(count_df)
    if counter == 20:
        break

    print('data appended for ', unique_date)
combined_df = ip.reorderCol(combined_df,['time','lat','lon','depth','taxonID','taxonID_counts','scientificNameID', 'scientificNameID_counts','scientificName','scientificName_counts', 'acceptedNameUsage', 'acceptedNameUsage_counts'])

    # df['year']= df['year'].astype('str')
    # df['month']= ((df['month'].astype('str')).apply(lambda x: x.zfill(2)))
    # df['day']= ((df['day'].astype('str')).apply(lambda x: x.zfill(2)))
    # print(len(df))
    # df = df[(df['day'] != '-9') & (df['day'] != '-1')]
    #
    # df['year'] = df['year'].replace('10', '2010')
    # df['year'] = df['year'].replace('11', '2011')
    # df['year'] = df['year'].replace('6', '2006')
    # # df = df[(df['year'] != '10') & (df['year'] != '11')& (df['year'] != '6')]
    # df['time'] = pd.to_datetime(df[['year', 'month', 'day']], format='%Y%m%d')
    # ip.renameCol(df,'Lat', 'lat')
    # ip.renameCol(df,'Long', 'lon')
    # ip.renameCol(df,'Depth', 'depth')
    # ip.renameCol(df,'PromL', 'prochlorococcus_abundance')
    # ip.renameCol(df,'SynmL', 'synechococcus_abundance')
    # ip.renameCol(df,'PEukmL', 'picoeukaryote_abundance')
    # ip.renameCol(df,'pico_abund', 'picophytoplankton_abundance')
    # ip.renameCol(df,'picophyto [ug C/L]', 'picophytoplankton_biomass')
    # ip.removeColumn(['year','day','month'],df)
    # df = ip.reorderCol(df,['time','lat','lon','depth','prochlorococcus_abundance','synechococcus_abundance','picoeukaryote_abundance','picophytoplankton_abundance','picophytoplankton_biomass'])
    # df = ip.removeMissings(['time','lat', 'lon','depth'], df)
    # df = ip.NaNtoNone(df)
    # df = ip.colDatatypes(df)
    # df = ip.addIDcol(df)
    # df = ip.removeDuplicates(df)
    # df.to_csv(export_path, index=False)
    # ip.sortByTimeLatLonDepth(df, export_path, 'time', 'lat', 'lon', 'depth')
    # print('export path: ' ,export_path)
    # return export_path
#     return combined_df
#
# df = makeCPR_zooplankton(rawFilePath, rawFileName, tableName)

# export_path = makeCPR_zooplankton(rawFilePath, rawFileName, tableName)
# iF.toSQLbcp(export_path, tableName)
