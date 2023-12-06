install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=webapp tests/test_*.py

format:	
	black webapp/*.py tests/*.py

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' webapp/main.py --ignore-patterns=tests/test_.*?py  webapp/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format #lint

deploy:  #deploy step to be changed after creating the AWS container repo
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
	docker build -t logistics .
	docker tag logistics:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/logistics:latest
	docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/logistics:latest
		
		
all: install lint test format