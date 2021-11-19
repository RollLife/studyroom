# shellcheck disable=SC2164

# init virtualenv & install django
poetry init
poetry install
poerty add django==3.2

# init django
django-admin startproject mysite

# test django successful running
cd mysite
python manage.py runserver

# add polls add
python manage.py startapp polls

# add database (sqlite3)
python manage.py migrate

# migration models in django
python manage.py makemigrations polls

# migrate database table
python manage.py migrate
