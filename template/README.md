# Dataset File Strucure
This document describes the common file structure to store the data/meta-data produced by the labs funded by the Simons Foundation, Oceanography program. The file format is excel spreadsheet. Data is stored in the first sheet and the sheet title is "data". The second sheet stores the dataset meta-data and is called "dataset_meta_data". Meta-data associated with the variables in the dataset are kept in the third sheet, "vars_meta_data". An example template can be found [here](http://opedia.io/template). 


## Dataset Filename Convention
Dataset filename: &lt;dataset_short_name&gt;**_**&lt;dataset_release_data&gt;**_v**&lt;dataset_version&gt;**.xlxs**<br>Example: seaflow_2018-05-25_v1.0.xlxs

* &lt;dataset_short_name&gt;: short name of the dataset
	- length: less than 50 characters
* &lt;dataset_release_data&gt;: date of dataset release
	- format: %Y-%m-%d
	- note: zero padding required
* &lt;dataset_version&gt;: associated dataset version
	- length: less than 50 characters


## First Sheet: "data"
Columns by order:

1. **time**: corresponding datetime
	- type: datetime
	- format: %Y-%m-%d %H:%M:%S [example: 2018-03-29 18:05:55]
	- time zone: UTC
	- note: there is a blank space between date and time
	- note: zero padding required

2. **lat**: latitude
	- type: float
	- format: Decimal (not military grid system)
	- unit: degree
	- range: [-90, 90]

3. **lon**: longitude
	- type: float
	- format: Decimal (not military grid system)
	- unit: degree
	- range: [-180, 180]

3. **&lt;v_1&gt;**: first variable (short name)

Add more columns similar to the last column, if dataset has more than one variable. 	



## Second Sheet: "dataset_meta_data"
Columns by order:

1. **dataset_short_name**: dataset short name
	- type: string
	- length: <50 chars

2. **dataset_long_name**: descriptive dataset name
	- type: string
	- length: <500 chars

3. **dataset_version**: dataset version
	- type: string
	- length: <50 chars

4. **dataset_release_date**: dataset release date
	- type: date
	- format: %Y-%m-%d  (zero padding required)

5. **dataset_make**: how dataset is made (fixed options= [assimilation, model, observation])
	- type: string
	- length: <50 chars

6. **dataset_source**: name of your lab and/or institution
	- type: string
	- length: <100 chars

7. **dataset_doi**: digital object identifier (doi) associated with the dataset. Below is an example list of entities that may issue and link your dataset to a unique doi:
	- [Dryad](https://datadryad.org/) (only accepts published datsets)
	- [FigShare](https://figshare.com/)
	- [Zenodo](https://zenodo.org/)
	- [Open Science Foundation](https://osf.io/) (more details [here](http://help.osf.io/m/faqs/l/726460-faqs))
	- [Harvard Dataverse](https://dataverse.harvard.edu/)
Alternatively, one may choose to obtain the dataset doi by submitting their dataset to a domain-specific repository. Note that each repository has its own submission requirements. Below are a few suggestions:
	- [NCEI](https://www.nodc.noaa.gov/)
	- [ORNL DAAC](https://daac.ornl.gov/)
	- [EDI](https://portal.edirepository.org/nis/home.jsp)
	- [PANGAEA](https://www.pangaea.de/)
	- [SEANOE](http://www.seanoe.org/)
	- [NASA Goddard](https://disc.gsfc.nasa.gov/)
	- [NERC](https://nerc.ukri.org/research/sites/data/)
8. **dataset_history**: notes regarding the evolution of the dataset with respect to the previous versions, if applicable
	- type: string
	- length: no limit
	
9. **dataset_description**: any additional descriptions
	- type: string
	- length: no limit

10. **dataset_references**: links/citations associated with the dataset documentations/publications (enter each ref. in a separate row)
	- type: string
	- length: <500 chars per item



## Third Sheet: "vars_meta_data"
Columns by order:

1. **var_short_name**: variable short name
	- type: string
	- length: <50 chars

2. **var_long_name**: descriptive variable name
	- type: string
	- length: <500 chars

3. **var_standard_name**: standard variable name (more details in [CF Conventions](http://cfconventions.org/Data/cf-standard-names/49/build/cf-standard-name-table.html
) and [COARDS Conventions](http://ferret.pmel.noaa.gov/Ferret/documentation/coards-netcdf-conventions))
	- type: string
	- length: <500 chars

4. **var_unit**: variable unit
	- type: string
	- length: <50 chars

5. **var_sensor**: device by which variable is measured
	- type: string
	- length: <50 chars	
	- examples: [satellite, cruise_name, simulation, ...]		

6. **var_spatial_res**: variable spatial resolution
	- type: string
	- length: <50 chars	
	- examples: [1/25° X 1/25° , 50km X 50km, Irregular, ...]

7. **var_temporal_res**: variable temporal resolution
	- type: string
	- length: <50 chars	
	- examples: [Hourly, Daily, Irregular, ...]	

8. **var_missing_value**: placeholder for missing values
	- type: string
	- length: <50 chars	
	- examples: [empty cell, "nan", "unknown", #FFFF, -999, ...]		

9. **var_discipline**: the closest discipline(s) associated with the variable
	- type: string
	- length: <100 chars	
	- examples: [Physics, Chemistry, Biology, BioGeoChemistry, ...]		

10. **var_keywords**: keywords pertinent to the variable (separated by comma)
	- type: string
	- length: <500 chars	
	- examples: [field sample, Biology, abundance, synechococcus, ...]		

11. **var_comment**: any other comment about the variable
	- type: string
	- length: no limit		