#!/usr/bin/env python
#
# Hello World in Python (library)
#
#
# Copyright (C) 2023 Rudy Matela
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
This library declares two functions
and serves a a Python example
of how to use docstrings.
Not really useful in practice.

>>> return_hello()
'Hello, World!'

>>> print_hello()
Hello, World!
"""


def return_hello():
    """
    This function returns the "Hello, World!" string

    >>> return_hello()
    'Hello, World!'

    This serves as Python docstring example,
    in practice this function is not useful.
    :-)
    """

    return "Hello, World!"


def print_hello():
    """
    This function prints a "Hello, World!" message

    >>> print_hello()
    Hello, World!

    This serves as Python docstring example,
    in practice this function is not useful.
    :-)
    """

    print(return_hello())
