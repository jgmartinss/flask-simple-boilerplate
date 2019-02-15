help:
	@echo '---------------Flask-Simple-Boilerplate---------------'
	@echo '                                                      '
	@echo 'Usage:                                                '
	@echo '------> run         Run project                       '
	@echo '------> initdb      Init database                     '
	@echo '------> test        Run tests                         '
	@echo '------> createuser  Create superuser                  '
	@echo '------> upgrade     Run upgrade db                    '
	@echo '------> migrate     Run migrate                       '
	@echo '------> setup       Setup the project                 '

clean:
	rm -rf app/__pycache__
	rm -rf app/auth/__pycache__
	rm -rf tests/__pycache__
	rm -rf tests/db_test.db
run:
	python3 manage.py runserver
initdb:
	python3 manage.py db init
migrate:
	python3 manage.py db migrate
upgrade:
	python3 manage.py db upgrade
createuser:
	python3 manage.py create_user
test:
	python3 manage.py tests
requirements:
	pip3 freeze > requirements.txt
setup: initdb migrate upgrade
