#!/usr/bin/python
# -*- coding:Utf-8 -*-


import unittest
from butteur import generate_tex
from butteur.templates import base

class GenerateTests(unittest.TestCase):
    def test_empty(self):
        assert generate_tex("") == base



if __name__ == "__main__":
    unittest.main()
