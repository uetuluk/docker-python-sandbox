compile-requirements:
	pip-compile requirements.ini
	pip-compile requirements.sandbox.ini

requirements:
	pip install -r requirements.txt
	pip install -r requirements.sandbox.txt

develop:
	uvicorn main:app --reload

production:
	uvicorn main:app

build-image:
	docker build -t docker-python-sandbox .

run-image:
	docker run --rm -p 3000:3000 docker-python-sandbox