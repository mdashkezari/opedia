# Opedia
Opedia is a database service to integrate, visualize, and analyze ocean datasets.

# System Requirements
* [Anaconda Distribution Pyhton 2.7](https://www.anaconda.com/download/)
* Make sure python is in system path.
* Additional python modules:
	- pyodbc
	- bokeh
	- geopandas

# Installation
1.  **Set up database drivers (on required on macOS).**
	 install [homebrew](https://brew.sh/); a package manager for macOS.
	 set up odbc driver providing connection to the Opedia database.

	```
	$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	$ brew install unixodbc
	$ brew install freetds --with-unixodbc
	```
2. **Install [Anaconda Distribution Pyhton 2.7](https://www.anaconda.com/download/).**
Make sure python is added to the system path.  Anaconda distribution covers the majority of python modules used by Opedia. There are a few more required modules; run the following commands to install them.

	```
	$ conda update --all
	$ conda install pyodbc
	$ conda install dropbox
	$ conda install -c conda-forge geopandas
	```
