#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : TestSuite
#Author            : Saransh Ahlawat
#Date created      : 07.16.2019
#Purpose           : Automated testing for US21, US31
#Revision History  : Version 1.0
#Notes:  Automated testing

import unittest
import os
from prettytable import PrettyTable
from gedcom_file_parser import gedcom_file_parser, print_individuals_pretty_table, print_families_pretty_table
from Saransh_Sprint3 import us21, us31

"""
Unit tests for User Stories US21, US31
"""

class TestSuite(unittest.TestCase):
    
    def test_us31(self):
        dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        individuals, families = gedcom_file_parser(f"{dir_path}/data/sprint3userstorytest.ged")
        print_individuals_pretty_table(individuals, False)
        print_families_pretty_table(individuals, families, False)

        expected_result = ['@I5@']
        result = us31(individuals, families)

        self.assertEqual(result, expected_result)
    
    
    def test_us21(self):
        dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        individuals, families = gedcom_file_parser(f"{dir_path}/data/sprint3userstorytest.ged")
        print_individuals_pretty_table(individuals, False)
        print_families_pretty_table(families, individuals, False)

        expected_result = ["US21: Error: Family @F4@ does not have a male husband."]
        result = us21(individuals, families)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()