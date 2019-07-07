import unittest
import os
from gedcom_file_parser import gedcom_file_parser

"""
Unit tests for User Story US22
"""
class TestPrintDuplicateIds(unittest.TestCase):
   
    def test_print_duplicate_ids(self):
        dir_abs_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        directory_path = f"{dir_abs_path}/data/project01.ged"
        individuals, families, duplicate_ids = gedcom_file_parser(directory_path, True)
        self.assertEqual(duplicate_ids, ['@I1@', '@I5@', '@I5@', '@I5@', '@I10@', '@I10@', '@F3@', '@F5@'])

if __name__ == '__main__':
    unittest.main(exit=False)