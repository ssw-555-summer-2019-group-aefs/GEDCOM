import unittest
import os
from gedcom_file_parser import gedcom_file_parser
from US09 import birth_before_parents_death

"""
Unit tests for User Story US22
"""
class TestPrintDuplicateIds(unittest.TestCase):
   
    def test_birth_before_parents_death(self):
        dir_abs_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        directory_path = f"{dir_abs_path}/data/sprint3userstorytest.ged"
        individuals, families = gedcom_file_parser(directory_path)
        result = birth_before_parents_death(individuals, families)
        expected_result = ['ERROR: US09: @F1@: Husband died before the birth of his child','ERROR: US09: @F1@ Wife died before the birth of her child']
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main(exit=False)