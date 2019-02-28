[![DOI](https://zenodo.org/badge/118988572.svg)](https://zenodo.org/badge/latestdoi/118988572)

![ocean cube](https://github.com/mdashkezari/opedia/blob/master/cube.png)
# Opedia
Opedia is an open source database service to integrate, visualize, and analyze ocean datasets such as satellite data, in-situ observations, and model outputs. The project is supported by [Simons Foundation](https://www.simonsfoundation.org/).

# System Requirements
* [Anaconda Distribution Pyhton 3.7 -- 2.7](https://www.anaconda.com/download/)
* Make sure python is in system path.
* Additional python modules:
	- shapely
	- fiona
	- geopandas

# Installation
1.  **Set up database drivers (only required on macOS).**<br>
	 install [homebrew](https://brew.sh/); a package manager for macOS.<br>
	 ODBC driver provides the connection to the Opedia database.

	```
	$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	$ brew install unixodbc
	$ brew install freetds --with-unixodbc
	```
2. **Install [Python Anaconda Distribution](https://www.anaconda.com/download/).**<br>
Make sure python is added to the system path.  Anaconda distribution covers the majority of python modules used by Opedia. There are a few more required modules that need to be installed using the conda package manager; run the following commands to install them. Finally pip-install the opedia package itself.

	```
	$ conda install shapely
	$ conda install fiona
	$ conda install -c conda-forge geopandas

	$ pip install opedia
	```
