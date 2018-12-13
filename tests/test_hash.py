"""Test cases."""
from __future__ import print_function
import os
from collections import namedtuple
from mmh3cffi import hash_str


HashTestCase = namedtuple('TestCase', 'string seed expected')


class TestMurmurHash332(object):
    """Tests for murmurhash3 (32 bits variant)."""

    @staticmethod
    def parse_test_case_line(line):
        """Parse a single test case from an incoming line."""
        seed, string, expected = line.split(',')
        return HashTestCase(string, int(seed), int(expected))

    @staticmethod
    def parse_testcase_file(filename):
        """Parse a file into a list of testcases."""
        with open(os.path.join(os.path.dirname(__file__), filename)) as flo:
            return [TestMurmurHash332.parse_test_case_line(l.strip()) for l in flo.readlines()]

    def setup(self):
        """Parse test cases."""
        self.ascii_testcases = TestMurmurHash332.parse_testcase_file("testcases1.csv")  # pylint: disable=attribute-defined-outside-init
        self.utf8_testcases = TestMurmurHash332.parse_testcase_file("testcases2.csv")  # pylint: disable=attribute-defined-outside-init

    def test_ascii_hash(self):
        """Execute tests."""
        for testcase in enumerate(self.ascii_testcases):
            assert hash_str(testcase.string, testcase.seed) == testcase.expected

    def test_utf8_hash(self):
        """Execute tests."""
        for testcase in enumerate(self.utf8_testcases):
            assert hash_str(testcase.string, testcase.seed) == testcase.expected
