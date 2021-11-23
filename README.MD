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