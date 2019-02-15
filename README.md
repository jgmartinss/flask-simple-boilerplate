# Flask Simple Boilerplate 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/jgmartinss/bookstore/blob/master/LICENSE)
> Simple boilerplate in Flask. 

## Dependencies

- [Python](https://www.python.org/downloads/) - 3.6.6+
- [Flask](http://flask.pocoo.org/) - 1.0.2+
- [PIPENV](https://github.com/pypa/pipenv)
- Virtualenv - 16.1.0+

## Installation:

1. Clone the repository:
    ```bash
    git clone https://github.com/jgmartinss/flask-simple-boilerplate projectname
    ```
1. Install dependencies and create environment:

    ```bash
    cd projectname
    pipenv --python 3.6
    pipenv shell
    pipenv install
    pipenv install -d
    ```
3. Generate a local `.env`

    ```bash
    python contrib/env_gen.py dev
    ```

4. Synchronize to database:

    ```bash
    make setup
    ```

5. Create a user:

    ```bash
    make createsuperuser
    ```
6. Test the installation in the url http://127.0.0.1:8000:

    ```bash
    make runserver
    ```
## Run tests:

1. Flask tests:

    ```bash
    make test
    ```
2. Coverage tests using `Tox`:

    ```bash
    $ tox
    $ firefox htmlcov/index.html
    ```