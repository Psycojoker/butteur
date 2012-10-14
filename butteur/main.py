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

KEYWORDS =(
    "title",
    "author",
    "theme",
    "package",
)

class ButteurSyntaxError(Exception): pass

def generate_tex(text):
    return templates.base


def tokenize(text):
    if not text.strip():
        return

    for line_number, line in enumerate(text.split("\n"), start=1):
        keyword = line.split(" ")[0]
        if keyword in KEYWORDS:
            yield (keyword.upper(), line.split(" ", 1)[1])
        else:
            raise ButteurSyntaxError("ERROR: '%s' is not a valid keyword on line %s, valid keywords are: %s" % (keyword, line_number, ", ".join(KEYWORDS)))

    return


def main():
    if len(sys.argv) == 1:
        print "Give me a filename!"
        sys.exit(1)

    butt_file = open(sys.argv[1], "r").read().decode("Utf-8")

    open(sys.argv[1] + ".tex", "w").write(butt_file.encode("Utf-8"))
    os.system("pdflatex %s" % sys.argv[1] + ".tex")


if __name__ == "__main__":
    main()
