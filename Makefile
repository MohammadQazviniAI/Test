# Makefile for hello in Python

all:

run:
	python src/hello.py
	python src/hellomain.py

.PHONY: test
test:
	PYTHONPATH=src pytest
