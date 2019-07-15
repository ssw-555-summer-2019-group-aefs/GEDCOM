import unittest
import os
import sys
from gedcom_file_parser import print_pretty_table
import util_date
import US07_US08_Test_Suite
import US22_unit_test
import unit_tests_us11_us12
import US29_30_unit_tests
import Sprint2_TestSuite

if __name__ == '__main__':
    dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
    print_pretty_table(f"{dir_path}/data/fran_test.ged")
    suit1 = unittest.TestLoader().loadTestsFromModule(util_date)
    suit2 = unittest.TestLoader().loadTestsFromModule(Sprint2_TestSuite)
    suit3 = unittest.TestLoader().loadTestsFromModule(US07_US08_Test_Suite)
    suit4 = unittest.TestLoader().loadTestsFromModule(unit_tests_us11_us12)
    suit5 = unittest.TestLoader().loadTestsFromModule(US22_unit_test)
    suit6 = unittest.TestLoader().loadTestsFromModule(US29_30_unit_tests)

    test_result1 = unittest.TextTestRunner(verbosity=2).run(suit1).wasSuccessful()
    test_result2 = unittest.TextTestRunner(verbosity=2).run(suit2).wasSuccessful()
    test_result3 = unittest.TextTestRunner(verbosity=2).run(suit3).wasSuccessful()
    test_result4 = unittest.TextTestRunner(verbosity=2).run(suit4).wasSuccessful()
    test_result5 = unittest.TextTestRunner(verbosity=2).run(suit5).wasSuccessful()
    test_result6 = unittest.TextTestRunner(verbosity=2).run(suit6).wasSuccessful()

    final_test_result = (test_result1 and test_result2 and test_result3 and test_result4 and test_result5 and test_result6)

    print("\nAll tests successfully ended:", final_test_result)
