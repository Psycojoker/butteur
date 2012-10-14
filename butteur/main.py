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


def generate_tex(text):
    return templates.base


def tokenize(text):
    if not text.strip():
        return

    line_by_line = iter(enumerate(text.split("\n"), start=1))

    for line_number, line in line_by_line:
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
        yield ("LINE", line.lstrip())


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
