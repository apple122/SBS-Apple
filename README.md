# SBS-Lucky_Draw-Web-API

This application enables Django powered websites to have multiple tenants via PostgreSQL schemas. A vital feature for every Software-as-a-Service website.

    # Creat a new database
    CREATE DATABASE 'lucky_draw'

## Basic Settings for Development

Activate environment

    python3 -m venv venv
    source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Basic Settings
You’ll have to make the following creations to your your .env file
and Django Secret Key

    DB_NAME=your_database_name
    DB_USR=your_user_name
    DB_PWD=your_password

    SECRET_KEY='your_secret_key'

Make migrations and Apply to database # create migrations files (every new django app)

    python manage.py makemigrations
    python manage.py makemigrations period period_type prize prize_type lottery_bill candidate about district footer province slide village post
    python manage.py migrate

Setup Initial User, and Admin

    # create first user
    python manage.py createsuperuser
    python manage.py runserver

Go to
localhost:8000/admin/ or localhost:8000/swagger/

For testing
python3 manage.py test
coverage run manage.py test -v 2 && coverage report
coverage run manage.py test -v 2 && coverage report && coverage html

If show this error "Type 'yes' if you would like to try deleting the test database 'test_lucky_draw', or 'no' to cancel:"
delete file "**init**.py" then create a new one

Create a new model
cd apps
python ../manage.py startapp "folder name"
