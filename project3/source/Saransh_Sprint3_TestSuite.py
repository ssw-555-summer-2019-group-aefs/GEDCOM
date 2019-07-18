#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : TestSuite
#Author            : Saransh Ahlawat
#Date created      : 07.16.2019
#Purpose           : Automated testing for US21, US31
#Revision History  : Version 1.0
# Notes:  Automated testing

import unittest
import os
from prettytable import PrettyTable
from gedcom_file_parser import gedcom_file_parser
from Saransh_Sprint3 import us21, us31

"""
Unit tests for User Stories US21, US31
"""

class TestSuite(unittest.TestCase):
    
    def test_us31(self):
        dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        individuals, families = gedcom_file_parser(f'{dir_path}/data/sprint3userstorytest.ged')

        expected_result = ["US31: Individual @I1@ is more than 30 years old and is not married.", "US31: Individual @I5@ is more than 30 years old and is not married."]
        print(us31(individuals, families))

        # self.assertEqual(us31(individuals, families), expected_result)
        


if __name__ == '__main__':
    unittest.main()