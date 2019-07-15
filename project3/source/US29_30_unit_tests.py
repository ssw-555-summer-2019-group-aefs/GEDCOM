from US29_30_Source_File import list_deceased, list_living_married
from util_date import Date
from gedcom_file_parser import gedcom_file_parser, print_pretty_table
import io
import os
import unittest
import datetime
from prettytable import PrettyTable

class TestUserStories(unittest.TestCase):
   
    def test_user_stories(self):

        dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        directory_path = f'{dir_path}/data/sprint3userstorytest.ged'
        individuals, families = gedcom_file_parser(directory_path)

        # Expected Result for US29
        us29_pt = PrettyTable(field_names=["ID", "Name"])
        us29_pt.add_row(['@I1@','Tristin /Evans/'])
        us29_pt.add_row(['@I2@','Angelo /Rose/'])
        us29_pt.add_row(['@I4@','Phil /Evans/'])
        us29_pt.add_row(['@I6@','Sheila /Evans/'])
        us29_pt.add_row(['@I9@', 'Trish /Rose/'])
        us29_str = "US29: List: The following individuals are deceased in the family\n" + str(us29_pt)

        self.assertEqual(list_deceased(individuals), us29_str)
       
        #US30 Expected Results
        us30_pt = PrettyTable(field_names=["Family ID", "Husband ID", "Husband Name", "Wife ID", "Wife Name"])
        us30_pt.add_row(['@F4@', '@I17@', 'Frederick /Rose/', '@I16@', 'Cynthia /Rose/'])
        us30_str = "US30: List: The following lists living married couples by family\n" + str(us30_pt)

        self.assertEqual(list_living_married(individuals, families), us30_str)

if __name__ == '__main__':
    unittest.main(exit=False)