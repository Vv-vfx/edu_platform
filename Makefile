
apprun:
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py createsuperuser
	python manage.py fill_db_fake
	python manage.py runserver


runserver:
	python manage.py runserver

startapp:
	python manage.py startapp mainapp

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser