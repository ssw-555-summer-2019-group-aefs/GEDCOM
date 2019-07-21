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
        directory_path_us29 = f'{dir_path}/data/us29.ged'
        directory_path_us30 = f'{dir_path}/data/us30.ged'
        individuals_us29, families_us29 = gedcom_file_parser(directory_path_us29)
        individuals_us30, families_us30 = gedcom_file_parser(directory_path_us30)
        print_pretty_table(directory_path_us29)
        print_pretty_table(directory_path_us30)

        # Expected Result for US29
        us29_pt = PrettyTable(field_names=["ID", "Name"])
        us29_pt.add_row(['@I7@','Peter /Evans/'])
        us29_pt.add_row(['@I10@','Darren /Johnson/'])
        us29_str = "US29: List: The following individuals are deceased in the family\n" + str(us29_pt)

        self.assertEqual(list_deceased(individuals_us29), us29_str)
       
        #US30 Expected Results
        us30_pt = PrettyTable(field_names=["Family ID", "Husband ID", "Husband Name", "Wife ID", "Wife Name"])
        us30_pt.add_row(['@F1@', '@I5@', 'Angelo /Rose/', '@I1@', 'Tristin /Evans/'])
        us30_pt.add_row(['@F2@', '@I2@', 'Phil /Evans/', '@I3@', 'Sheila /Lynn/'])
        us30_pt.add_row(['@F4@', '@I11@', 'David /Lynn/', '@I12@', 'Victoria /Taylor/'])
        us30_str = "US30: List: The following lists living married couples by family\n" + str(us30_pt)

        self.assertEqual(list_living_married(individuals_us30, families_us30), us30_str)

if __name__ == '__main__':
    unittest.main(exit=False)