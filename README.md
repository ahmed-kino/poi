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

## Create superuser

* Run `$ make shell` to execute into the container
* Run `./manage.py createsuperuser`
* You will be prompted to enter the username, email address, and password for the superuser. Follow the prompts to enter this information.
* Once you have entered the information, the superuser will be created and you will see a message confirming the creation
* You can now use the superuser credentials to log in to the Django admin site and access all administrative features.

## Format

* Run `make shell` to execute into the container
* Run format `make format`

## Sort

* Run `make shell` to execute into the container
* Run sort `make sort`

## Format & Sort

* Run `make shell` to execute into the container
* Run `make fmt` to format and sort

## Tests

* Run `make shell` to execute into the container
* Run tests `make test`

## Reset DB:

* Run `make shell` to execute into the container

* Run `make clean` to reset the database **NOTE that this command will remove `*/migrations` directories from the code**


## Import data

* Run `make shell` to execute into the container
* Run `./manage.py import_poi_data /path/to/file1.csv /path/to/file2.json /path/to/file3.xml --log_file=/path/to/log_file.log` to import desired data into the db
