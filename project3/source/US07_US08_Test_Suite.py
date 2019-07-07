from US07_US08_Source_File import check_150_years_age, check_birth_before_marriage_of_parents
from util_date import Date
from gedcom_file_parser import gedcom_file_parser, print_pretty_table
import io
import sys
import os
import unittest
import datetime

class TestUserStories(unittest.TestCase):
   
    def test_user_stories(self):
        dir_abs_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        directory_path = f"{dir_abs_path}/data/US07_US08_test_file.ged"
        individuals, families = gedcom_file_parser(directory_path)
        print_pretty_table(directory_path)

        #US07 Test
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test_output = check_150_years_age(individuals)
        sys.stdout = sys.__stdout__
        self.assertEqual(test_output, ['ERROR: INDIVIDUAL: US07: @I3@: More than 150 years old - Birth date 19 May 0268', 'ERROR: INDIVIDUAL: US07: @I9@: More than 150 years old at death - Birth date 17 Nov 0301: Death date 15 Nov 0560'])
       
        #US08 Test
        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        check_birth_before_marriage_of_parents(families, individuals)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput2.getvalue(), 'ANOMOLY: FAMILY: US08: @F1@: Child @I3@ born 19 May 0268 before marriage on 08 Aug 0271\nANOMOLY: FAMILY: US08: @F1@: Child @I4@ born 13 Nov 0267 before marriage on 08 Aug 0271\nANOMOLY: FAMILY: US08: @F1@: Child @I5@ born 15 Oct 0265 before marriage on 08 Aug 0271\nANOMOLY: FAMILY: US08: @F2@: Child @I9@ born 17 Nov 0301 before marriage on 15 Jan 0304\nANOMOLY: FAMILY: US08: @F3@: Child @I7@ born 05 Sep 0287 after divorce on 18 Nov 0285\n')

if __name__ == '__main__':
    unittest.main(exit=False)