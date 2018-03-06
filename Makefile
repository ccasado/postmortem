default:
	@awk -F\: '/^[a-z_]+:/ && !/default/ {printf "- %-20s %s\n", $$1, $$2}' Makefile

clean:
	@find . -name \*.pyc -delete
	@find . -name .DS_Store -delete

install:
	@pip install -r requirements.txt --index-url=https://artifactory.globoi.com/artifactory/api/pypi/pypi-all/simple

makemigrations:
	@python manage.py makemigrations app

sqlmigrate:
	@python manage.py sqlmigrate app $(name)

migrate:
	@python manage.py migrate

runserver:
	@python manage.py runserver
