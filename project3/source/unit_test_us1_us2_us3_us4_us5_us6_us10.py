#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : TestSuite
#Author            : Anthem Rukiya J. Wingate, Fran Sabetour
#Date created      : 06.18.2019
#Purpose           : Automated testing for US01, US02, US04, US05, US06, US10
#Revision History  : Version 1.0
# Notes:  Automated testing

import unittest
from gedcom_file_parser import print_pretty_table
from Sprint1 import get_spouse_block


"""
Unit tests for User Stories US01, US02, US04, US05, US06, US10
"""

class TestSuite(unittest.TestCase):
    
    def test_ppt(self):
        """ Test for US01, US02, US03, US04, US05, US06, US10 """

        directory_path = "C:/Users/Anthe/OneDrive/Documents/Stevens/SSW 555/GEDCOM/Projects/Sprint2/PPTtest2.ged"
        error_chk = [
                    {'us02':{0:[False, False, False, True, False, True, True]},
                    'us04':{0:[False, True, False]}, 
                    'us05':{0:[False, True, False]}, 
                    'us06':{0:[True, False, False]},
                    'us01':{0:[True, True, True, False], 1:[False, False, True, False]},
                    'us03':{0:True, 1:False}}
                    ]
                    
        self.assertEqual(print_pretty_table(directory_path), error_chk)

if __name__ == '__main__':
    unittest.main()