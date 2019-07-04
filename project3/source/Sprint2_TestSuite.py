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
from prettytable import PrettyTable


"""
Unit tests for User Stories US01, US02, US04, US05, US06, US10, US13, US14, US15, US17, US18, US28, US32, US33
"""

class TestSuite(unittest.TestCase):
    
    def test_ppt(self):
        """ Test for Get_Spouse_Block and Get_Child_Block """

        directory_path = "C:/Users/Anthe/OneDrive/Documents/Stevens/SSW 555/GEDCOM/Projects/Sprint2/PPTtest2.ged"
        #error_chk holds expected results returned print_pretty_table as three dictionaries of booleans e1, e2, and e3. 
        # self.assertEqual will be checked using error_chk as well as three dictionaries of pretty tables us28_pt, us32_pt, and us33_pt

        error_chk = [
                    {'us02':{0:[False, False, False, True, False, True, True]},
                    'us04':{0:[False, True, False]}, 
                    'us05':{0:[False, True, False]}, 
                    'us06':{0:[True, False, False]},
                    'us01':{0:[True, True, True, False], 1:[False, False, True, False]},
                    'us03':{0:True, 1:False}}
                    ]
        us28_pt = PrettyTable(field_names=["ID", "Name", "Date of Birth"])
        us28_pt.add_row([])
        us32_pt = PrettyTable(field_names=["ID", "Name"])
        us32_pt.add_row([])
        us33_pt = PrettyTable(field_names=["ID", "Name"])
        us33_pt.add_row([])
                    
        self.assertEqual(print_pretty_table(directory_path), error_chk)

if __name__ == '__main__':
    unittest.main()