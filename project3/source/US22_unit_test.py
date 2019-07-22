import unittest
import os
from gedcom_file_parser import gedcom_file_parser
from US22 import print_duplicate_ids

"""
Unit tests for User Story US22
"""
class TestPrintDuplicateIds(unittest.TestCase):
   
    def test_print_duplicate_ids(self):
        dir_abs_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        directory_path = f"{dir_abs_path}/data/sprint3userstorytest.ged"
        individuals, families, duplicate_ids = gedcom_file_parser(directory_path, True)
        expected_error_message = ["US22: ERROR: Duplicate individual id: @I20@"]
        result = print_duplicate_ids(duplicate_ids)
        self.assertEqual(duplicate_ids, ['@I20@'])
        self.assertEqual(expected_error_message, result)

if __name__ == '__main__':
    unittest.main(exit=False)