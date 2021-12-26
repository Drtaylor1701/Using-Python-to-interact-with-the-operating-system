#!/usr/bin/env python3

from unittest.case import TestCase
from log_reader import findTicketType
from log_reader import captureErrorMessage
import unittest


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "May 27 11:45:40 ubuntu.local.ticky: INFO: Created ticket [#1234] (username)"
        expected = "INFO"
        self.assertEqual(findTicketType(testcase), expected)

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Jun 1 11:46:48 ubuntu.local.ticky: ERROR: Connection to DB failed (username)"
        expected = "ERROR"
        self.assertEqual(findTicketType(testcase), expected)

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Jun 1 11:46:48 ubuntu.local.ticky: ERROR: Connection to DB failed (username)"
        expected = "Connection to DB failed"
        self.assertEqual(captureErrorMessage(testcase), expected)

unittest.main()