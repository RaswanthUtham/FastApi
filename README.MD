## Commands

### To start the server
    uvicorn app:main.app --reload

### To see the docs
    url/docs
    url/redoc

    example: http://localhost:8000/docs

## packages
    python-jose[cryptography] for password authentication

## query parameters
    syntax:
        url?param_name=value
    example:
        http://localhost:8000?limit=2&search=string%20space

## Database Migration Tool Alembic
    Alembic is like a GIT for Databases.
    It is used to track changes in the DBMS
    It also has other features like automatic reloading when a data is changed through a ORM.

    pip install alembic
    alembic --help
    alembic init dirName

    Creating a revision
        alembic revision -m "Create Posts Table"  // which will create a .py file under alembic.versions dir inside which we can create / modify / delete tables and its contents

    Upgrade to a revision
        alembic upgrade revisionNo
            where revisionNo will be in alembic.versions.*.py file
            This will create 2 tables
                One is the table we want to create.
                Another is the one alembic creates to keep track of revisions.
            example:
                alembic upgrade +3 (takes forward to 3 revisions)
                alembic upgrade revisionNum (takes forward to a specific revision)

    downgrade to a revision
        alembic downgrade revisionNo or (+1 / -3)
        example:
            alembic downgrade -3 (takes back to 3 revisions)
            alembic downgrade revisionNum (takes back to a specific revision)

    alembic current
    alembic history

## auto genarate the table for database.
    alembic revision --autogenerate -m "auto vote"
    this will create a votes table automatically, It happens because we had imported the Base from app.models.

### If you get this error during auto generate.
    FAILED: Can't proceed with --autogenerate option; environment script D:\workspace\fastapi\alembic\env.py does not provide a MetaData object or sequence of objects to the context.

    In env.py file add the metadata
    target_metadata = Base.metadata

## auto generate changes in models

    The changes made in models.py file like adding phone number or address coloumn to users will reflect automatically in alembic.versions dir using the following command
    
    alembic revision --autogenerate -m "auto vote"
    Example:
    add colunms address in users table through models.py
    then run alembic revision --autogenerate -m "auto added address to users table"
    this will generate a .py file in alembic.versions dir, which will he having the commands for adding the coloumn.

## CORS:
    Cross Origin Resource Sharing.
    Used to share resource over internet. (between different domains)

    1. go to www.google.com
    2. right click open inspect element
    3. select console tab
    4. execute fetch('http://localhost:8000').then(res => res.json()).then(console.log)
    
    5. you will get below error.
    """
    Access to fetch at 'http://localhost:8000/' from origin 'https://www.google.com' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
    """

    6. Enable CORS in fast api and try again, you will get the result.

## Heroku:
    https://rash-fastapi.herokuapp.com/
    Procfile: give the commands to start the application in this file
    
## heroku commands:
    heroku create appname
    heroku addons:create heroku-postgresql:hobby-dev
    heroku ps:restart
    heroku run bash
    heroku apps:info appname

## running alembic on heroku:
    heroku run "alembic upgrade head"

## pytest
    pytest -s -v --disable-warnings -x
        where
            -s prints print statement
            -v verbose
            --disable-warnings disale the warnings
            -x stop after the 1st failure


## conftest file
    we can put the fixtures and other configs inside this file
    it can be used will all the test files without importing within a package

