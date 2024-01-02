install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install_win:
	python.exe -m pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	behave

all: install_win format test
