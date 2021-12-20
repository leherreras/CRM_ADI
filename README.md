# CRM System

Into the src you could find the source code, external of src you could add
other tools like docker, pipelines, configs, etc. 
The ides is had the clean code.

Requirements:

* Python 3.9
* virtualenv

## Install Requirements libraries

Access to src, here you have the source code to execute

Run:

    pip install -r requirements.txt

## REST

Run:

    uvicorn app.main:app --reload

Now go to http://localhost:8000/docs to play with the API.

## Tests

Run tests (in `pipenv shell`):

    pytest
