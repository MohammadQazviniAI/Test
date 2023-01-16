Hello World in Python
---------------------

[![Build Status for Hello World in Python][build-status]][build-log]

This project contains a simple ["Hello, World!" program] written in [Python].

The program prints "Hello, World!" and exits.

It is under [CI] through [GitHub Actions].


## Compiling and running

To run the program use the following command:

	python src/hello.py

You should see the following on the screen:

	Hello, World!

There is also a version of the hello world implemented
in two separate files, with a library and a main program file.
Run it with:

	python src/hellomain.py

To run the tests, use pytest like so:

	PYTHONPATH=src pytest

It will detect and run doctests and unit tests.

Or run tests individually:

	PYTHONPATH=src python test/test_hello.py
	python src/hellolib.py


## Important files

* [src/hello.py](src/hello.py)
* [Makefile](Makefile)


## Known bugs

This documentation is longer than the source code.


## Useful reading

* [GitHub's starter-workflows] project.


["Hello, World!" program]: https://en.wikipedia.org/wiki/%22Hello,_World!%22_program
[C]: https://en.wikipedia.org/wiki/C_(programming_language)
[make]: https://www.gnu.org/software/make/
[CI]: https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration
[GitHub Actions]: https://docs.github.com/en/actions

[build-log]:    https://github.com/rudymatela/hello-py/actions/workflows/build.yml
[build-status]: https://github.com/rudymatela/hello-py/actions/workflows/build.yml/badge.svg

[GitHub's starter-workflows]: https://github.com/actions/starter-workflows
