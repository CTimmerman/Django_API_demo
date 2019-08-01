Luggage Care Flight API by Cees Timmerman, 2019-07-15.

mklink /J C:\Python37-32 C:\Users\C\AppData\Local\Programs\Python\Python37-32\
cd \code\Python\LuggageCare
c:\Python37-32\python -m venv LC_env
cd LC_env
Scripts\activate
python -m pip install django
python -m pip install djangorestframework
python -m pip install psycopg2
django-admin startproject sampleapp
cd sampleapp

python manage.py startapp flights
rem Add 'rest_framework' and 'flights' to INSTALLED_APPS in sampleapp\sampleapp\settings.py
rem Add path('flights/', include('flights.urls')), to sampleapp\sampleapp\urls.py
rem Fill sampleapp\flights\urls.py
rem Fill sampleapp\flights\models.py

rem Optional switch to Postgres DB:
CREATE DATABASE flights;
CREATE USER flights_user WITH LOGIN PASSWORD 'feather horse apple tree';

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Then try these in your browser or API client:

http://127.0.0.1:8000/flights/
http://127.0.0.1:8000/flights/api
http://127.0.0.1:8000/flights/api?flight_number=2
http://127.0.0.1:8000/flights/api?departure_time=2019-07-15%2017:00
http://127.0.0.1:8000/flights/api?arrival_time=2019-07-15%2020:00



rem Optional admin web interface:
rem Import and register Flight in sampleapp\flights\admin.py
python manage.py createsuperuser
rem http://127.0.0.1:8000/admin/

rem Optional low level interface:
python manage.py shell
>>> from flights.models import Flight
>>> Flight.objects.all()
<QuerySet []>
>>> Flight.objects.create(airliner='KLM', departure_airport='Schiphol', arrival_airport='London', departure_time='2019-07-15 18:00+01', arrival_time='2019-07-15 19:00+00').save()
>>> Flight.objects.create(airliner='Transavia', departure_airport='Schiphol', arrival_airport='London', departure_time='2019-07-15 19:00+01', arrival_time='2019-07-15 20:00+00').save()
>>> Flight.objects.all()
<QuerySet [<Flight: KLM 2019-07-15 17:00:00+00:00 flight Schiphol to London>, <Flight: Transavia 2019-07-15 18:00:00+00:00 flight Schiphol to London>]>
>>> Flight.objects.get(id=1)
<Flight: KLM 2019-07-15 17:00:00+00:00 flight Schiphol to London>
