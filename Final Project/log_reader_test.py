#!/usr/bin/env python3

from unittest.case import TestCase
from log_reader import split_up_message
import unittest


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "May 27 11:45:40 ubuntu.local.ticky: INFO: Created ticket [#1234] (username)"
        expected = "INFO"
        self.assertEqual(split_up_message(testcase), expected)

    def test_empty(self):
        testcase = "Jun 1 11:46:48 ubuntu.local.ticky: ERROR: Connection to DB failed (username)"
        expected = "ERROR"
        self.assertEqual(split_up_message(testcase), expected)


unittest.main()
