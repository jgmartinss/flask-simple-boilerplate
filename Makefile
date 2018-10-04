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
	python3 manage.py fake_user
test:
	python3 manage.py tests
requirements:
	pip3 freeze > requirements.txt
install:
	pip3 install -r requirements.txt
