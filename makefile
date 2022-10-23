ver=0.0.1
name="OpacityContests"

.PHONY:build install run

all : build install run

build:
	python3 setup.py bdist_wheel
	python3 setup.py sdist
	rm -rf build
	rm -rf OpacityContests.egg-info

install:
	pip install ./dist/$(name)-$(ver).tar.gz

run:
	thonny
