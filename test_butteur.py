#!/usr/bin/python
# -*- coding:Utf-8 -*-


import pytest
from butteur import generate_latex, tokenize, ButteurSyntaxError, indentation, render_token
import test_results


class TestGenerate:
    def test_empty(self):
        assert generate_latex([]) == test_results.empty

    def test_render_empty(self):
        assert render_token(tuple()) == ""

    def test_render_title(self):
        assert render_token(("TITLE", "the title")) == r"\title{the title}"
        assert render_token(("TITLE", "another title")) == r"\title{another title}"

    def test_render_author(self):
        assert render_token(("AUTHOR", "the author")) == r"\author{the author}"

    def test_render_theme(self):
        assert render_token(("THEME", "Berlin")) == r"\usetheme{Berlin}"

    def test_render_package(self):
        assert render_token(("PACKAGE", "tikz")) == r"\usepackage{tikz}"

    def test_render_empty_slide(self):
        assert render_token(("SLIDE", "", [])) == r"\begin{frame}{}\n\end{frame}"


class TestTokenize:
    def test_empty(self):
        assert list(tokenize("")) == []

    def test_title(self):
        assert list(tokenize("title the title")) == [("TITLE", "the title")]

    def test_author(self):
        assert list(tokenize(
            "author me, myself and I")) == [("AUTHOR", "me, myself and I")]

    def test_title_author_order(self):
        assert list(tokenize("title the title\nauthor me, myself and I")) == [
            ("TITLE", "the title"), ("AUTHOR", "me, myself and I")]

    def test_theme(self):
        assert list(tokenize("theme Berlin")) == [("THEME", "Berlin")]

    def test_package(self):
        assert list(tokenize("package tikz")) == [("PACKAGE", "tikz")]

    def test_raise_invalid_keyword(self):
        with pytest.raises(ButteurSyntaxError):
            list(tokenize("badkeyword"))

    def test_empty_token(self):
        assert list(tokenize("title")) == [("TITLE", "")]

    def test_slide_token(self):
        assert list(tokenize(
            "slide the slide title")) == [("SLIDE", "the slide title", [])]

    def test_slide_one_line(self):
        assert list(tokenize("slide\n    the first line")) == [(
            "SLIDE", "", [("LINE", "the first line")])]

    def test_slide_deindent(self):
        assert list(tokenize("slide\n  first line\ntitle not in slide")) == [("SLIDE", "", [("LINE", "first line")]), ("TITLE", "not in slide")]

    def test_slide_empty_line_dontdeindent(self):
        assert list(tokenize("slide\n  first line\n  \n  still in slide")) == [("SLIDE", "", [("LINE", "first line"), ("LINE", "still in slide")])]


class TestIdentation:
    def test_indentation_empty(self):
        assert indentation("") == 0

    def test_indentation(self):
        assert indentation("  a") == 2
        assert indentation("   a") == 3

    def test_indentation_stip(self):
        assert indentation("  ") == 0

    def test_indentation_right_strip(self):
        assert indentation("a  ") == 0
