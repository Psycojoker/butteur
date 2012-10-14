#!/usr/bin/python
# -*- coding:Utf-8 -*-


import pytest
import unittest
from butteur import generate_tex, tokenize, ButteurSyntaxError
from test_results import empty


class GenerateTests(unittest.TestCase):
    def test_empty(self):
        assert generate_tex("") == empty


class TokenizesTests(unittest.TestCase):
    def test_empty(self):
        assert list(tokenize("")) == []

    def test_title(self):
        assert list(tokenize("title the title")) == [("TITLE", "the title")]

    def test_author(self):
        assert list(tokenize("author me, myself and I")) == [("AUTHOR", "me, myself and I")]

    def test_title_author_order(self):
        assert list(tokenize("title the title\nauthor me, myself and I")) == [("TITLE", "the title"), ("AUTHOR", "me, myself and I")]

    def test_theme(self):
        assert list(tokenize("theme Berlin")) == [("THEME", "Berlin")]

    def test_package(self):
        assert list(tokenize("package tikz")) == [("PACKAGE", "tikz")]

    def test_raise_invalid_keyword(self):
        with pytest.raises(ButteurSyntaxError):
            list(tokenize("badkeyword"))
