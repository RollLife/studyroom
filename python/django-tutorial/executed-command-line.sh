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