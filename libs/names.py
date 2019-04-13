#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import sys

try:
    import ucd
except ModuleNotFoundError:
    from . import ucd


class Lookup(object):
    """Class responsible for lookup of Unicode character names."""

    def __init__(self):
        """Class initialization."""
        pass

    @staticmethod
    def name(char):
        """Return a name for a given character from the Cooper-Hewitt name
        lookup.
        """
        id_ = ord(char)
        hex_ = "%04X" % id_
        print("INFO: char: %s id: %s hex: %s" % (char, id_, hex_), file=sys.stderr)
        return ucd.UCD_MAP.get(hex_, None)


def main():
    """Primary entry point for this script."""
    cmd = " ".join(sys.argv[1:])
    try:
        cmd = cmd.decode("utf-8")
    except AttributeError:
        pass
    ref = Lookup()
    for char in cmd:
        name = ref.name(char)
        print("%s is %s" % (char, name))


if __name__ == "__main__":
    main()
