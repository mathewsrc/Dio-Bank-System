setup:
	@echo "Setting up virtual environment"
	python -m venv .env

install:
	@echo "Installing dependencies"
	pip install --upgrade pip  &&\
		pip install -r requirements.txt

format:
	@echo "Formating .py"
	black *.py

lint:
	@echo "Liting .py"
	pylint --disable=R,C *.py

test:
	@echo "Testing app"
	python -m pytest -vv --cov=main test_main.py

run-app:
	python main.py

docker-build:
	@echo "Building Docker container"
	docker build --tag app-docker:latest .

docker-run:
	@echo "Starting Docker container"
	docker run -it --rm app-docker python main.py 

docker-cleanup:
	@echo "Cleaning Docker image and container"
	docker image rm app-docker
	docker images

all: install format lint