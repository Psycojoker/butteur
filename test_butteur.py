#!/usr/bin/python
# -*- coding:Utf-8 -*-


import unittest
from butteur import generate_tex, tokenize
from test_results import empty

class GenerateTests(unittest.TestCase):
    def test_empty(self):
        assert generate_tex("") == empty


class TokenizesTests(unittest.TestCase):
    def test_empty(self):
        assert tokenize("") == []


if __name__ == "__main__":
    unittest.main()
