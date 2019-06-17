[![DOI](https://zenodo.org/badge/118988572.svg)](https://zenodo.org/badge/latestdoi/118988572)

![ocean cube](https://github.com/mdashkezari/opedia/blob/master/cube.png)
# Opedia
Opedia is an open source database service to integrate, visualize, and analyze ocean datasets such as satellite data, in-situ observations, and model outputs. The project is supported by [Simons Foundation](https://www.simonsfoundation.org/).

# Documentation
https://cmap.readthedocs.io/en/latest/

# System Requirements
* [Anaconda Distribution Pyhton 3.7 -- 2.7](https://www.anaconda.com/download/)
* Make sure python is in system path.

# Installation
1.  **Set up database drivers (only required on macOS).**<br>
	 install [homebrew](https://brew.sh/); a package manager for macOS.<br>
	 ODBC driver provides the connection to the Opedia database.

	```
	$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	$ brew install unixodbc freetds ffmpeg
	```

	ffmpeg package is used to generate video contents.
	

2. **Install [Python Anaconda Distribution](https://www.anaconda.com/download/).**<br>
Make sure python is added to the system path.  Anaconda distribution covers the majority of python modules used by Opedia. Finally pip-install the opedia package itself.

	```
	$ pip install opedia
	```

# Author
Mohammad Dehghani Ashkezari <mdehghan@uw.edu>