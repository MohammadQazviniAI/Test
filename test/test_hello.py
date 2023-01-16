#!/usr/bin/env python
#
# Tests one of the hellolib functions

import unittest

from hellolib import return_hello

class TestHello(unittest.TestCase):

    def test_value(self):
        self.assertEqual(return_hello(), "Hello, World!")

    def test_length(self):
        self.assertEqual(len(return_hello()), 13)

if __name__ == '__main__':
    unittest.main()
