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