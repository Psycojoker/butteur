#!/usr/bin/python

# Butteur, a preprocessor to write more easily beamer slides
# Copyright (C) 2012  Laurent Peuch cortex@worlddomination.be
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import templates

KEYWORDS = (
    "title",
    "author",
    "theme",
    "package",
    "slide",
)


class ButteurSyntaxError(Exception):
    pass


class ByLines:
    def __init__(self, text):
        self.lines = text.split("\n")
        self.position = -1

    def next(self):
        self.position += 1
        if self.position >= len(self.lines):
            raise StopIteration
        return self.position + 1, self.lines[self.position]

    def __iter__(self):
        return self

    def go_back(self):
        "To use when we realised that we don't want to process this line"
        self.position -= 1


def generate_latex(text):
    return templates.head + templates.begin + templates.end


def tokenize(text):
    if not text.strip():
        return

    line_by_line = ByLines(text)

    for line_number, line in line_by_line:
        if len(line.strip()) == 0:
            continue

        keyword = line.split(" ")[0]
        if keyword == "slide":
            yield (keyword.upper(), line[len(keyword):].lstrip(), list(tokenize_slide(line_by_line)))
        elif keyword in KEYWORDS:
            yield (keyword.upper(), line[len(keyword):].lstrip())
        else:
            raise ButteurSyntaxError("ERROR: '%s' is not a valid keyword on line %s, valid keywords are: %s" % (keyword, line_number, "'" + "'" "', '".join(KEYWORDS) + "'"))

    return


def tokenize_slide(line_by_line):
    for line_number, line in line_by_line:
        if len(line.strip()) == 0:
            continue
        if indentation(line) == 0:
            line_by_line.go_back()
            return

        yield ("LINE", line.lstrip())


def render_token(token):
    if not token:
        return ""
    if token[0] == "AUTHOR":
        return r"\author{%s}" % token[1]
    elif token[0] == "THEME":
        return r"\usetheme{%s}" % token[1]
    elif token[0] == "PACKAGE":
        return r"\usepackage{%s}" % token[1]
    elif token[0] == "SLIDE":
        return r"\begin{frame}{}\n\end{frame}"
    return r"\title{%s}" % token[1]


def indentation(line):
    return len(line.rstrip()) - len(line.rstrip().lstrip())


def main():
    if len(sys.argv) == 1:
        print "Give me a filename!"
        sys.exit(1)

    butt_file = open(sys.argv[1], "r").read().decode("Utf-8")

    open(sys.argv[1] + ".tex", "w").write(butt_file.encode("Utf-8"))
    os.system("pdflatex %s" % sys.argv[1] + ".tex")


if __name__ == "__main__":
    main()
