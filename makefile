site-packages-dir="cd /home/darkbyte/.local/lib/python3.10/site-packages"
.PHONY:build test

build:
	rm -rf build
	python3 setup.py bdist_wheel
	python3 setup.py sdist

test:
	cp ./lib/thonnycontrib/* $(site-packages-dir)/thonnycontrib
	thonny

