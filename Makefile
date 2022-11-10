DEFAULT: build

run:
	./gdmtproxy

freeze:
	pipenv run pip3 freeze > requirements.txt

build:
	pip3 install -r requirements.txt