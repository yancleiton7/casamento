install:
	pip install -e .['dev']

run:
	FLASK_APP=delivery/app.py FLASK_ENV=development flask run