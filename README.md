# CRM System

Requirements:

* Python 3.9
* virtualenv

## REST

Run:

    uvicorn app.main:app --reload

Now go to http://localhost:8000/docs to play with the API.

## Tests

Run tests (in `pipenv shell`):

    pytest
