# Paranuara
=============
# Steps to try API

### 1 Local build
sudo docker-compose -f local.yml build
__sudo docker-compose -f local.yml up

### 2 load models on database
sudo docker-compose -f local.yml run --rm django python manage.py makemigrations
__sudo docker-compose -f local.yml run --rm django python manage.py migrate

### 3 load data from json (if you are going to change the json files please keep the same format)
sudo docker-compose -f local.yml run --rm django python manage.py populate  companies.json company
__sudo docker-compose -f local.yml run --rm django python manage.py populate  people.json person

### 4 Use API
- Given a company, the API needs to return all their employees. 
http://localhost:8000/companies/STRALUM/employees
Provide the appropriate solution if the company does not have any employees.
first of all you have to know who company has employees, for suppliyed data is NETBOOK
http://localhost:8000/companies/NETBOOK/employees
* this service returns an URL to associate the citizens who do not have an associated company
* similar to this: http://localhost:8000/companies/NETBOOK/add_free_employees/ 

- Given 2 people, provide their information (Age, Name, Address, phone) and the list of their friends in common which have brown eyes and are still alive.
http://localhost:8000/citizens/friends_in_common?users=XXX,XXX
Where XXX and XXX has to be the IDs of the citizens, to search their IDs use this url:
http://localhost:8000/citizens

- Given 1 people, provide a list of fruits and vegetables they like.
http://localhost:8000/citizens/XXX/get_food
Where XXX is the citizen ID who you want to find

If you want in the project root there is a Postman export with the End Points. (called: )

### 5 Validate unit test
sudo docker-compose -f local.yml run --rm django pytest

# Additional Information

### Celery Flower (the process to asociate citizens free to an empty company is released by celery)
Server: http://localhost:5555/
__User: paranuara
__Password: P4r4nu4r4

### PostgreSql Credentials
POSTGRES_HOST=localhost
__POSTGRES_PORT=5432
__POSTGRES_DB=paranuara
__POSTGRES_USER=sBLRWyyPsInwHftmHAWmYJURGWBGFpLs
__POSTGRES_PASSWORD=tuXL3XSF8O7tsGrcGHoMos4tVNtL3tnrRshSCZokGnIfk4ArDyzaa297k2WgQPSL

# TO DO
Only get friends service has tests. Load unit test and integration test to others services
__Adapt json files to use fixtures instead of use BaseCommand 