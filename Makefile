install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m unittest

lint:
	pylint --disable=R,C your_bot.py

all: install lint test