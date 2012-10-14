#!/usr/bin/python
# -*- coding:Utf-8 -*-


import unittest
from butteur import generate_tex


class GenerateTests(unittest.TestCase):
    def test_empty(self):
        assert generate_tex("") == ""


if __name__ == "__main__":
    unittest.main()
