#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : TestSuite
#Author            : Saransh Ahlawat
#Date created      : 08.02.2019
#Purpose           : Automated testing for US16, US326
#Revision History  : Version 1.0
#Notes:  Automated testing

import unittest
import os
from prettytable import PrettyTable
from gedcom_file_parser import gedcom_file_parser, print_individuals_pretty_table, print_families_pretty_table
from Saransh_Sprint4 import us16, us26

"""
Unit tests for User Stories US16, US26
"""

class TestSuite(unittest.TestCase):
    
    def test_us16(self):
        dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        individuals, families = gedcom_file_parser(f"{dir_path}/data/us16.ged")
        expected_result = ["US16: Error: All males in family @F1@, do not have same last name"]
        result = us16(individuals, families)
        self.assertEqual(result, expected_result)
    
    
    def test_us26(self):
        dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        individuals, families = gedcom_file_parser(f"{dir_path}/data/us26.ged")
        expected_result = [
            'US26: Error: individual spouse with id @I1@ not available in family @F1@',
            'US26: Error: No entry for family id @F4@ available',
            'US26: Error: No entry for family id @F4@ available',
            'US26: Error: Husband in family @F5@ is not listed as spouse in individual record @I2@',
            'US26: Error: Wife in family @F5@ is not listed as spouse in individual record @I9@'
        ]
        result = us26(individuals, families)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()