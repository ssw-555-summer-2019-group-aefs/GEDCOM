from source_file_us11_us12 import check_bigamy, check_parents_not_too_old
from util_date import Date
from gedcom_file_parser import gedcom_file_parser, print_pretty_table
import io
import sys
import unittest
import datetime

class TestUserStories(unittest.TestCase):
   
    def test_user_stories(self):
        directory_path = r'C:\Users\Erik\Desktop\GEDCOM-master\project3\data\Sprint2test.ged'
        individuals, families = gedcom_file_parser(directory_path)

        #US11 Test
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        check_bigamy(individuals, families)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), 'ANOMOLY: INDIVIDUAL: US11: @I4@: Bigamy detected: Robert Evans married to multiple spouses at the same time\nANOMOLY: INDIVIDUAL: US11: @I5@: Bigamy detected: Angelo Rose married to multiple spouses at the same time\nANOMOLY: INDIVIDUAL: US11: @I8@: Bigamy detected: Celes Keeton married to multiple spouses at the same time\n')
       
        #US12 Test
        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        check_parents_not_too_old(individuals, families)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput2.getvalue(), 'ANOMOLY: FAMILY: US12: @F2@: Parents are too old: Parent(s) were greater than 65 years old when child was born\n')

if __name__ == '__main__':
    unittest.main(exit=False)