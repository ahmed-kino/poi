## Run: DEV

### Prerequisites
1. make sure you have `docker` and `docker compose` installed. [Installation Guid](https://docs.docker.com/engine/install/)
2. make sure you have `cmake` installed. [Installation Guid](https://www.gnu.org/software/make/)

### Running the API

* change directory to the repo `$ cd poi_project`
* Run `cp .envrc.example .envrc`
* Run `$ make compose` to run the server

### Run migrations

* Run `$ make shell` to execute into the container

* Run migration `$ make init`


## Reset DB:

* Run `make shell` to execute into the container

* Run `make clean` to reset the database **NOTE that this command will remove `*/migrations` directories from the code**


## Import data

* Run `make shell` to execute into the container
* Run `./manage.py import_poi_data /path/to/file1.csv /path/to/file2.json /path/to/file3.xml --log_file=/path/to/log_file.log` to import desired data into the db
