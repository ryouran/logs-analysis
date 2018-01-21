#Logs Analysis
This project was completed for [Udacity's Full Stack Web Developer Nanodegree program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Project Overview
This project is to write a Python program which uses `psycopg2` module to connect to the Postgres database and aggregate data from the database and print out reports in plain text to a console.

### Requirements
  * [Python2](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

### Set up the project
1. Install [VirtualBox](https://www.vagrantup.com/) and [Vagrant](https://www.vagrantup.com/).
2. Download or clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
3. Download or clone this repository.
4. Place reporting_tool.py and create\_view.sql in the vagrant directory.

### Load the data	
1. Click [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to dowlonad newsdata.zip.
2. Unzip the file and place newsdata.sql into the vagrant directory which is shared with the vagrant virtual machine. 
3. Run 'vagrant up' to launch the virtual machine from the vagrant directory.
4. Run 'vagrant ssh' to log in.
5. Change the directory to vagrant.
6. Use the command to load the data.
`psql -d news -f newsdata.sql`

### Run the program
1. Run the vagrant virtual machine and log in as described above if not running
2. Use the command `python reporting_tool.py' to run the program.


##Test Environment
* Python 2.7.14
