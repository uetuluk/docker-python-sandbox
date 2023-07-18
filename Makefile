build-production-image:
	docker build -t docker-python-sandbox .

build-development-image:
	docker build -t docker-python-sandbox-development --target=development .

production:
	docker run --rm -p 3000:3000 docker-python-sandbox

development:
	docker run --rm -it -v $(PWD):/app -p 3000:3000 docker-python-sandbox-development 