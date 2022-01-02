#!/usr/bin/env python3
'''unit tests for log reader script'''
import unittest
from log_reader import read_ticket_type
from log_reader import read_user_name
from log_reader import read_error_text
from log_reader import add_dict_entry
from log_reader import sort_dict_by_value
from log_reader import sorted_dict_by_key
from log_reader import convert_dict_to_csv

class TestTicketTyping(unittest.TestCase):
    '''unit tests for reading logs'''
    def test_basic_info(self):
        '''tests a basic info log'''
        testcase = "Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)"
        expected = "INFO"
        self.assertEqual(read_ticket_type(testcase), expected)

    def test_basic_error(self):
        '''tests a basic error log'''
        testcase = "Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)"
        expected = "ERROR"
        self.assertEqual(read_ticket_type(testcase), expected)

class UserName(unittest.TestCase):
    '''unit tests for reading logs'''
    def test_basic_uname(self):
        '''tests a basic info username'''
        testcase = "Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)"
        expected = "mdouglas"
        self.assertEqual(read_user_name(testcase), expected)

    def test_user_name_with_dot(self):
        '''tests a username with a dot in it'''
        testcase = "Jan 31 04:30:04 ubuntu.local ticky: ERROR Permission denied while closing ticket (rr.robinson)"
        expected = "rr.robinson"
        self.assertEqual(read_user_name(testcase), expected)

class ErrorText(unittest.TestCase):
    def test_error_message(self):
        '''test recording error text'''
        testcase = "Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)"
        expected = "The ticket was modified while updating"
        self.assertEqual(read_error_text(testcase), expected)

class UpdateDict(unittest.TestCase):
    def test_dictionary_update(self):
        '''test recording error text'''
        testcase1 = "The ticket was modified while updating"
        testcase2 = {}
        expected = {'The ticket was modified while updating': 1}
        self.assertEqual(add_dict_entry(testcase1, testcase2), expected)

class SortDictByValue(unittest.TestCase):
    def test_dictionary_update(self):
        '''test recording error text'''
        testcase1 = {'The ticket was modified while updating': 9, 'Permission denied while closing ticket': 10, 'Tried to add information to closed ticket': 12, 'Timeout while retrieving information': 15, "Ticket doesn't exist": 7, 'Connection to DB failed': 13}
        expected = {'Timeout while retrieving information': 15, 'Connection to DB failed': 13, 'Tried to add information to closed ticket': 12, 'Permission denied while closing ticket': 10, 'The ticket was modified while updating': 9, "Ticket doesn't exist": 7}
        self.assertEqual(sort_dict_by_value(testcase1), expected)

class SortDictByKey(unittest.TestCase):
    def test_dictionary_update(self):
        '''test sorting a dictionary by key'''
        testcase1 = {'mdouglas': 5, 'noel': 9, 'breee': 6, 'ac': 4, 'blossom': 8, 'rr.robinson': 3, 'mcintosh': 7, 'jackowens': 6, 'oren': 9, 'xlg': 4, 'ahmed.miller': 6, 'bpacheco': 2, 'enim.non': 5, 'flavia': 5, 'sri': 4, 'nonummy': 5, 'britanni': 2, 'montanap': 4, 'mai.hendrix': 3, 'kirknixon': 3}
        expected = [('ac', 4), ('ahmed.miller', 6), ('blossom', 8), ('bpacheco', 2), ('breee', 6), ('britanni', 2), ('enim.non', 5), ('flavia', 5), ('jackowens', 6), ('kirknixon', 3), ('mai.hendrix', 3), ('mcintosh', 7), ('mdouglas', 5), ('montanap', 4), ('noel', 9), ('nonummy', 5), ('oren', 9), ('rr.robinson', 3), ('sri', 4), ('xlg', 4)]
        self.assertEqual(sorted_dict_by_key(testcase1), expected)

class Create_Csv(unittest.TestCase):
    def test_dict_to_csv_conversion(self):
        '''test sorting a dictionary by key'''
        testcase1 = {'mdouglas': 5, 'noel': 9, 'breee': 6, 'ac': 4, 'blossom': 8, 'rr.robinson': 3, 'mcintosh': 7, 'jackowens': 6, 'oren': 9, 'xlg': 4, 'ahmed.miller': 6, 'bpacheco': 2, 'enim.non': 5, 'flavia': 5, 'sri': 4, 'nonummy': 5, 'britanni': 2, 'montanap': 4, 'mai.hendrix': 3, 'kirknixon': 3}
        expected = 'file written'
        self.assertEqual(convert_dict_to_csv(testcase1), expected)

#unittest.main()
