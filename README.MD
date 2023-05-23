Basic showcase how to connect to a postgres database in a docker container


# Setup
## setup docker
```
$ docker run --rm --name <IMAGE_NAME_HERE> -e POSTGRES_PASSWORD=<YOUR_PASSWORD_HERE> --network="host" postgres 

```
Replace the placeholders <...> with your data
if no local image names postges is found, docker will automatically download this for you - and use the latest version.
Postgres needs atleast the password set in environment (-e option).
To connect to the container from outside the container but on the same system use the --network flag

(docker needs to be run as root)

## setup virtual environment
```
python3 -m venv .venv
```
use pythons builtin module "venv" to create a virtual environment in the folder .venv


activate virtual environment
```
source .venv/bin/activate
```

install postgres driver
```
python3 -m pip install psqchopg2-binary

```
[psychopg2 on pypi](https://pypi.org/project/psycopg2/)

## setup environment vars

postgres is default value for DB_NAME and DB_USER
5432 is the default value for DB_PORT
add your host (in development: 'localhost')
and the password you used setting up your postgres docker image

development.env
```
    export DB_HOST=''
    export DB_PASS=''
    export DB_USER='postgres'
    export DB_NAME='postgres'
    export DB_PORT=5432
```

store env vars in local environment
```
source development.env
```

## run code
```
python3 run.py
```
