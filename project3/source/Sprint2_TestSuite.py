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
from Sprint2 import get_child_block
#from Sprint3 import get_recent_block

"""
Unit tests for User Stories US01, US02, US03, US04, US05, US06, US10, US13, US14, US15, US17, US18, US28, US32, US33, US34, US35, US36, US37
"""

class TestSuite(unittest.TestCase):
    
    def test_ppt(self):
        """ Test for Get_Spouse_Block and Get_Child_Block """

        # error_chk holds expected results returned from function print_pretty_table as three dictionaries of booleans e1, e2, and e3. 
        # e1 is a dictionary of dictionaries of booleans returned from function get_spouse_block
        # e2 is a dictionary of dictionaries of booleans returned from function get_child_block
        # e3 is a dictionary of dictionaries of booleans returned from function get_recent_block
        # self.assertEqual will used to test the expected results stored in error_chk against the observed results returned from the function.

        directory_path = "C:/Users/Anthe/OneDrive/Documents/Stevens/SSW 555/GEDCOM/Projects/Sprint2/PPTtest2.ged"

        error_chk = [
                    # get_spouse_block results
                    {'us02':{0:[False, False, False, True, False, True, True]},
                    'us04':{0:[False, True, False]}, 
                    'us05':{0:[False, True, False]}, 
                    'us06':{0:[True, False, False]},
                    'us01':{0:[True, True, True, False], 1:[False, False, True, False]},
                    'us03':{0:True, 1:False}},
                    # get_child_block results
                    {'us13':{0:[]},
                    'us14':{0:[]},
                    'us15':{0:[]},
                    'us17':{0:[]},
                    'us18':{0:[]},
                    'us28':{0:[]},
                    'us32':{0:[]},
                    }
                    # get_recent_block results
                    ]
                           
        self.assertEqual(print_pretty_table(directory_path), error_chk)

if __name__ == '__main__':
    unittest.main()