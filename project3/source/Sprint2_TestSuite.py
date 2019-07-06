#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : TestSuite
#Author            : Anthem Rukiya J. Wingate, Fran Sabetour
#Date created      : 06.18.2019
#Purpose           : Automated testing for US01, US02, US04, US05, US06, US10
#Revision History  : Version 1.0
# Notes:  Automated testing

import unittest
from prettytable import PrettyTable
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

        directory_path = "C:/Users/Anthe/OneDrive/Documents/Stevens/SSW 555/GEDCOM/Projects/Sprint2/sprint2userstorytest.ged"

        # Expected Result for US28
        us28a_pt = PrettyTable(field_names=["ID", "Name","Date of Birth"])
        us28a_pt.add_row(['@I3@','Emma /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I7@','Isabel /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I8@','Angela /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I9@','Trish /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I10@','Ethan /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I11@','Ian /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I12@','Michael /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I13@','Richelle /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I14@','Matthew /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I15@','Luke /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I16@','Cynthia /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I17@','Frederick /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I18@','Tina /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I19@','Tanya /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I20@','Emmy /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I21@','Thomas /Rose/', '27 May 2018'])
        us28a_pt.add_row(['@I22@','Richelle /Rose/', '02 May 2019'])
        us28a_str = str(us28a_pt)

        us28b_pt = PrettyTable(field_names=["ID", "Name", "Date of Birth"])
        us28b_pt.add_row(['@I1@','Tristin /Evans/', '12 APR 1987'])
        us28b_pt.add_row(['@I5@','Aeryn /Evans/', '30 APR 1987'])
        us28b_str = str(us28b_pt)

        # Expected Result for US32
        us32_pt = PrettyTable(field_names=["ID", "Name"])
        us32_pt.add_row(['@I3@','Emma /Rose/'])
        us32_pt.add_row(['@I7@','Isabel /Rose/'])
        us32_pt.add_row(['@I8@','Angela /Rose/'])
        us32_pt.add_row(['@I9@','Trish /Rose/'])
        us32_pt.add_row(['@I10@','Ethan /Rose/'])
        us32_pt.add_row(['@I11@','Ian /Rose/'])
        us32_pt.add_row(['@I12@','Michael /Rose/'])
        us32_pt.add_row(['@I13@','Richelle /Rose/'])
        us32_pt.add_row(['@I14@','Matthew /Rose/'])
        us32_pt.add_row(['@I15@','Luke /Rose/'])
        us32_pt.add_row(['@I16@','Cynthia /Rose/'])
        us32_pt.add_row(['@I17@','Frederick /Rose/'])
        us32_pt.add_row(['@I18@','Tina /Rose/'])
        us32_pt.add_row(['@I19@','Tanya /Rose/'])
        us32_pt.add_row(['@I20@','Emmy /Rose/'])
        us32_pt.add_row(['@I21@','Thomas /Rose/'])
        us32_str = str(us32_pt)

        # Expected Result for US33
        us33_pt = PrettyTable(field_names=["ID", "Name"])
        us33_pt.add_row(['@I3@','Emma /Rose/'])
        us33_pt.add_row(['@I7@','Isabel /Rose/'])
        us33_pt.add_row(['@I8@','Angela /Rose/'])
        us33_pt.add_row(['@I9@','Trish /Rose/'])
        us33_pt.add_row(['@I10@','Ethan /Rose/'])
        us33_pt.add_row(['@I11@','Ian /Rose/'])
        us33_pt.add_row(['@I12@','Michael /Rose/'])
        us33_pt.add_row(['@I13@','Richelle /Rose/'])
        us33_pt.add_row(['@I14@','Matthew /Rose/'])
        us33_pt.add_row(['@I15@','Luke /Rose/'])
        us33_pt.add_row(['@I16@','Cynthia /Rose/'])
        us33_pt.add_row(['@I17@','Frederick /Rose/'])
        us33_pt.add_row(['@I18@','Tina /Rose/'])
        us33_pt.add_row(['@I19@','Tanya /Rose/'])
        us33_pt.add_row(['@I20@','Emmy /Rose/'])
        us33_pt.add_row(['@I21@','Thomas /Rose/'])
        us33_pt.add_row(['@I22@','Richelle /Rose/'])
        us33_str = str(us33_pt)


        error_chk = [
                    # get_spouse_block results
                    {'us01':{0:[True, True, True, False], 1:[False, False, True, False]},
                    'us02':{0:True,1:False,2:False,3:False},
                    'us03':{0:True, 1:False},
                    'us04':{0:[False, True, False]}, 
                    'us05':{0:[False, True, False]}, 
                    'us06':{0:[True, False, False]}
                    'us10':{0:}
                    },
                    
                    
                    # get_child_block results
                    {'us13':{0:False,1:True,2:False,3:False},
                    'us14':{0:True,1:False,2:False,3:False},
                    'us15':{0:True,1:False,2:False,3:False},
                    'us17':{0:True,1:False,2:False,3:False},
                    'us18':{0:False,1:False,2:True,3:False},
                    'us28':{0:us28a_str,
                            1:us28b_str,
                            2:False,
                            3:False},
                    'us32':{0:us32_str,
                            1:False,
                            2:False,
                            3:False},
                    'us33':{0:us33_str,
                            1:False,
                            2:False,
                            3:False}
                    }
                    # get_recent_block results
                    ]
                           
        self.assertEqual(print_pretty_table(directory_path), error_chk)

if __name__ == '__main__':
    unittest.main()