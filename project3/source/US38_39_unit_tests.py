from US38_39_Source_File import list_upcoming_anniversaries, list_upcoming_birthdays, print_list_upcoming_anniversaries, print_list_upcoming_birthdays
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
        directory_path_us38 = f'{dir_path}/data/us38.ged'
        directory_path_us39 = f'{dir_path}/data/us39.ged'
        individuals_us38, families_us38 = gedcom_file_parser(directory_path_us38)
        individuals_us39, families_us39 = gedcom_file_parser(directory_path_us39)
        print_list_upcoming_birthdays(individuals_us38, use_todays_date=False)
        print_list_upcoming_anniversaries(individuals_us39, families_us39, use_todays_date=False)

        # Expected Result for US38
        us38_pt = PrettyTable(field_names=["ID", "Name"])
        us38_pt.add_row(['@I2@','Angelo /Rose/'])
        us38_pt.add_row(['@I4@','Phil /Evans/'])
        us38_pt.add_row(['@I6@','Sheila /Evans/'])
        us38_str = "US38: List: The following individuals have upcoming birthdays within 30 days!\n" + str(us38_pt)

        self.assertEqual(list_upcoming_birthdays(individuals_us38, use_todays_date=False), us38_str)
       
        #US39 Expected Results
        us39_pt = PrettyTable(field_names=["Wife ID", "Wife Name", "Husband ID", 'Husband Name'])
        us39_pt.add_row(['@I6@', 'Sheila /Evans/', '@I4@', 'Phil /Evans/'])
        us39_str = "US39: List: The following couples have upcoming anniversaries within 30 days!\n" + str(us39_pt)

        self.assertEqual(list_upcoming_anniversaries(individuals_us39, families_us39, use_todays_date=False), us39_str)

if __name__ == '__main__':
    unittest.main(exit=False)