# Cookbook
Determine what to make with the ingredients you already have!

## Local Set Up

### (on machine)

### Install requirements

### Make virtual environment
`python3 -m venv venv`

### Source into virtual environment
`source venv/bin/activate`

#### Install Python Requirements
`pip install -r requirements`

### Setup database
Make sure your local database is running and open it with
On a mac, to install postgresql:
`brew install postgres`

To start it and make it run in the background:
`brew services start postgresql`

Or, if you don't want/need a background service you can just run:
`pg_ctl -D /usr/local/var/postgres start`

To get into postgresql:
`psql postgres`

Create a new database with `CREATE DATABASE cookbook;`
`$flask db upgrade`

`$ psql cookbook -f migrations/sql_scripts/001_migration.sql` (do this for all migrations in the directory)

### Create config
In the root directory, make a file called config.py using example_config.py as a template then replace all of the keys with your own

### Run the app
`python run.py`

## Test
- make sure your test database has been created. It's called `cookbook_test`
### Test All
`python app/test/unittest_main.py`
### Test File
`python path/to/file.py`

### Start new database
Create a new database with `CREATE DATABASE cookbook;`

`$flask db init`

`$flask db migrate`

`$flask db upgrade`
