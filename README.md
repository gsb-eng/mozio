
Mozio service providers api
===========================

Service provider management services has been implemented using `Python` and `Django` along with `PostGIS`, Providers can add geo spacial polygon data to the db and that can be accessed and updated with endpoints.

Services has been deployed over AWS, can be access with below url.

http://mozio.gsb-eng.com/api/v1/

# API Documentation:

Swagger: http://mozio.gsb-eng.com/docs/v1/swagger

Redoc: http://mozio.gsb-eng.com/docs/v1/redoc


# Development Steps 

# Using Docker

Build the application

`make build`

Running tests.

`make tests`

Running the local server on `127.0.0.0:8000`

`make serve`

Running lint checker

`make lint`

Stop the containers.

`make stop`


# Using virtualenv


```
Python 3.x
PostgreSQL
Postgis
```

You will need to create a virtualenv and install all the requirements listed in requirements.txt using  pip:

```
$ pip install -r requirements.txt
```

# Run server

`python manage.py runserver`

# Tests

`python manage.py test`
