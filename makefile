SHELL := /bin/bash
ver:=0.0.1
name:=OpacityShare
mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(dir $(mkfile_path))
env_name := devenv

.PHONY:build install run

all : build install run

first_use:
	sudo apt-get install python3-tk
	rm -rf devenv || true
	virtualenv devenv
	( \
       source $(current_dir)$(env_name)/bin/activate; \
       pip install -r requirements.txt; \
	   deactivate; \
	)

build: ./thonnycontrib
	( \
       source $(current_dir)$(env_name)/bin/activate; \
       python setup.py bdist_wheel; \
	   python setup.py sdist; \
	   deactivate; \
    )
	rm -rf build
	rm -rf $(name).egg-info


install: ./thonnycontrib
	( \
       source $(current_dir)$(env_name)/bin/activate; \
	   pip install $(current_dir)dist/$(name)-$(ver).tar.gz; \
	   deactivate; \
	)
	rm -rf dist

run:
	( \
       source $(current_dir)$(env_name)/bin/activate; \
	   thonny; \
	   deactivate; \
	)
