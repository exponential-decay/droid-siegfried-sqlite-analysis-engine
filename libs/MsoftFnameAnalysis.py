#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# MsoftFnameAnalysis
#
# based on: http://msdn.microsoft.com/en-us/library/aa365247(VS.85).aspx
#
# Module that implements checks against the Microsoft Recommendations for
# file naming.
#
#
from __future__ import print_function, unicode_literals
import os
import sys

try:
    import names
except ModuleNotFoundError:
    from . import names

sys.path.append(r"i18n/")
from internationalstrings import AnalysisStringsEN as IN_EN


class MsoftFnameAnalysis(object):
    """Filename analysis class."""

    report = ""

    def __init__(self):
        """Class initialization."""
        self.STRINGS = IN_EN

    def _clear_report(self):
        self.report = ""

    def complete_file_name_analysis(self, string, folders=False, verbose=False):
        """Primary code to call to run all checks over our string."""
        self._clear_report()
        self.verbose = verbose
        self.detect_non_ascii_characters(string, folders)
        self.detect_non_recommended_characters(string, folders)
        self.detect_non_printable_characters(string)
        self.detect_microsoft_reserved_names(string)
        self.detect_spaces_at_end_of_names(string, folders)
        self.detect_period_at_end_of_name(string, folders)
        return self.report

    def report_issue(self, string, message, value, folders=False):
        """Helper to build our report to return to the caller."""
        text = "File"
        if folders:
            text = "Directory"
        if not value:
            self.report = "{}{}: '{}' {}\n".format(self.report, text, string, message)
            return
        self.report = "{}{}: '{}' {} '{}'\n".format(
            self.report, text, string, message, value
        )

    @staticmethod
    def unicodename(char):
        """Return a Unicode name for the character we want to return
        information about.
        """
        try:
            name = names.Lookup().name(char)
            return "%s: %s" % (name, char)
        except TypeError:
            if char >= 0 and char <= 31:
                return "<control character>"
            return "non-specified error"

    def detect_non_ascii_characters(self, string, folders=False):
        """Detect characters outside the standard range of ASCII here."""
        match = any(ord(char) > 128 for char in string)
        if match:
            for char in string:
                if ord(char) > 128:
                    self.report_issue(
                        string=string,
                        message="{}:".format(self.STRINGS.FNAME_CHECK_ASCII),
                        value="{}, {}".format(hex(ord(char)), self.unicodename(char)),
                        folders=folders,
                    )
                if not self.verbose:
                    break

    def detect_non_recommended_characters(self, string, folders=False):
        """Detect characters that are not particularly recommended here."""
        charlist = ["<", ">", '"', "?", "*", "|", "]", "["]
        if not folders:
            charlist = charlist + [":", "/", "\\"]
        for char in string:
            if char in charlist:
                self.report_issue(
                    string=string,
                    message="{}:".format(self.STRINGS.FNAME_CHECK_NOT_RECOMMENDED),
                    value=("{}, {}".format(hex(ord(char)), self.unicodename(char))),
                    folders=folders,
                )
                if not self.verbose:
                    break

    def detect_non_printable_characters(self, string, folders=False):
        """Detect characters below 0x20 in the ascii table that cannot be
        printed.
        """
        for char in range(0x20):
            if chr(char) in string:
                self.report_issue(
                    string=string,
                    message="{}:".format(self.STRINGS.FNAME_CHECK_NON_PRINT),
                    value="{}, {}".format(hex(char), self.unicodename(char)),
                    folders=folders,
                )
                if not self.verbose:
                    break

    def detect_microsoft_reserved_names(self, string):
        """Detect names that are considered difficult on Microsoft file
        systems.
        """
        microsoft_reserved_names = [
            "CON",
            "PRN",
            "AUX",
            "NUL",
            "COM1",
            "COM2",
            "COM3",
            "COM4",
            "COM5",
            "COM6",
            "COM7",
            "COM8",
            "COM9",
            "LPT1",
            "LPT2",
            "LPT3",
            "LPT4",
            "LPT5",
            "LPT6",
            "LPT7",
            "LPT8",
            "LPT9",
        ]
        for reserved in microsoft_reserved_names:
            if reserved in string[0 : len(reserved)]:
                problem = True
                # If the reserved name is followed by an extension that's still
                # a bad idea.
                try:
                    if string[len(reserved)] == ".":
                        problem = True
                except IndexError:
                    # This is an exact reserved name match.
                    problem = True
                if problem:
                    self.report_issue(
                        string=string,
                        message=self.STRINGS.FNAME_CHECK_RESERVED,
                        value=reserved,
                    )

    def detect_spaces_at_end_of_names(self, string, folders=False):
        """Detect spaces at the end of a name."""
        if string.endswith(" "):
            self.report_issue(
                string=string,
                message=self.STRINGS.FNAME_CHECK_SPACE,
                value=None,
                folders=folders,
            )

    def detect_period_at_end_of_name(self, string, folders=False):
        """Detect a full-stop at the end of a name."""
        if string.endswith("."):
            self.report_issue(
                string=string,
                message=self.STRINGS.FNAME_CHECK_PERIOD,
                value=None,
                folders=folders,
            )

    def __detect_invalid_characters_test__(self):
        """Function to help with testing until there are unit tests."""
        test_strings = [
            "COM4",
            "COM4.txt",
            ".com4",
            "abcCOM4text",
            "AUX",
            "aux",
            "abc.com4.txt.abc",
            "con",
            "CON",
            "consumer",
            "space ",
            "period.",
            "\u00F3",
            "\u00E9",
            "\u00F6",
            "\u00F3\u00E9\u00F6",
            "file[bracket]one.txt",
            "file[two.txt",
            "filethree].txt",
            '-=_|"',
            '(<>:"/\\?*|\x00-\x1f)',
        ]
        for string in test_strings:
            report = self.complete_file_name_analysis(
                string, folders=False, verbose=True
            )
            if report:
                print(report.strip())


def main():
    """Primary entry-point for this script."""
    cmd = " ".join(sys.argv[1:])
    try:
        cmd = cmd.decode("utf-8")
    except AttributeError:
        pass
    if "test" in cmd.lower() and not os.path.isfile(cmd):
        print(
            "Running non-file test mode only, please use a string without 'test' in it.",
            file=sys.stderr,
        )
        MsoftFnameAnalysis().__detect_invalid_characters_test__()
    analysis = MsoftFnameAnalysis().complete_file_name_analysis(
        cmd, folders=False, verbose=True
    )
    if analysis:
        print(analysis.strip(), file=sys.stdout)


if __name__ == "__main__":
    main()
