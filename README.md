### QCRI LiveNews Demo

## About This Project:
QCRI Live New Demonstration is an internship project that aims to provide the user with a platform to track and customize news of interest to the user in an effective manner.


## How To Install The Project:

1. Requirements:
	
	a. Web Server
	b. Php
	c. MySQL
	d. Python3+
		Packages: [Twitter](https://pypi.org/project/twitter/), [newspaper](https://github.com/codelucas/newspaper), [tweepy](http://tweepy.readthedocs.io/en/v3.5.0/), MySQLdb, reosette-api and json

			`pip install twitter newspaper3k mysqlclient reosette-api json`

		Note: Some dependencies might have to be in place when running the above command. Some hints on how to install these on various platforms:

		Ubuntu 14, Ubuntu 16, Debian 8.6 (jessie)
			`sudo apt-get install python-pip python-dev libmysqlclient-dev`
		Mac OS
			`brew install mysql-connector-c`
		if that fails, try

			`brew install mysql`

2. Import Database

	Import database from the sql files in DB folder

3. Run The fellow users script `run_followUsers.sh` in a screen
	
	screen -S run_FollowUsers
	run_followUsers.sh

4. Start the Web Server and go to `http://localhost/<path>/index.php`


## Contributors:

	Kritika Mishra
	Ishita Chopra
	Laila Elbeheiry
	Tanya Shastri  

## Mentors:

	Hamdy Mubarak
	Preslav Nakov
	Ahmed Abdelali


## License:
This package is being made  public for research purpose only. 
The package is distributed WITHOUT ANY WARRANTY; without even the 
implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## Copyright:

Copyright 2018 QCRI


