# Paranuara
=============
# Steps to try API

### 1 Local build
sudo docker-compose -f local.yml build
sudo docker-compose -f local.yml up

### 2 load models on database
sudo docker-compose -f local.yml run --rm django python manage.py makemigrations
sudo docker-compose -f local.yml run --rm django python manage.py migrate

### 3 load data from json (if you are going to change the json files please keep the same format)
sudo docker-compose -f local.yml run --rm django python manage.py populate  companies.json company
sudo docker-compose -f local.yml run --rm django python manage.py populate  people.json person

### 4 Use API

### 5 Validate unit test
sudo docker-compose -f local.yml run --rm django pytest

### Celery Flower (the process to asociate citizens free to an empty company is released by celery)
Server: http://localhost:5555/
User: paranuara
Password: P4r4nu4r4

### PostgreSql Credentials
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=paranuara
POSTGRES_USER=sBLRWyyPsInwHftmHAWmYJURGWBGFpLs
POSTGRES_PASSWORD=tuXL3XSF8O7tsGrcGHoMos4tVNtL3tnrRshSCZokGnIfk4ArDyzaa297k2WgQPSL

# TO DO
Only get friends service has tests. Load unit test and integration test to others services
Adapt json files to use fixtures instead of use BaseCommand 