import os
import unittest
from gedcom_file_parser import print_pretty_table
import util_date
import US07_US08_Test_Suite
import US22_unit_test
import unit_tests_us11_us12
import Sprint2_TestSuite
import US29_30_unit_tests
import Saransh_Sprint3_TestSuite
import us09_unit_test
import AWFS_TestSuite
import US38_39_unit_tests
import Saransh_Sprint4_TestSuite

if __name__ == '__main__':
    suit1 = unittest.TestLoader().loadTestsFromModule(util_date)
    suit2 = unittest.TestLoader().loadTestsFromModule(AWFS_TestSuite)
    suit3 = unittest.TestLoader().loadTestsFromModule(US07_US08_Test_Suite)
    suit4 = unittest.TestLoader().loadTestsFromModule(unit_tests_us11_us12)
    suit5 = unittest.TestLoader().loadTestsFromModule(US22_unit_test)
    suit6 = unittest.TestLoader().loadTestsFromModule(US29_30_unit_tests)
    suit7 = unittest.TestLoader().loadTestsFromModule(Saransh_Sprint3_TestSuite)
    suit8 = unittest.TestLoader().loadTestsFromModule(us09_unit_test)
    suit9 = unittest.TestLoader().loadTestsFromModule(US38_39_unit_tests)
    suit10 = unittest.TestLoader().loadTestsFromModule(Saransh_Sprint4_TestSuite)

    test_result1 = unittest.TextTestRunner(verbosity=2).run(suit1).wasSuccessful()
    test_result2 = unittest.TextTestRunner(verbosity=2).run(suit2).wasSuccessful()
    test_result3 = unittest.TextTestRunner(verbosity=2).run(suit3).wasSuccessful()
    test_result4 = unittest.TextTestRunner(verbosity=2).run(suit4).wasSuccessful()
    test_result5 = unittest.TextTestRunner(verbosity=2).run(suit5).wasSuccessful()
    test_result6 = unittest.TextTestRunner(verbosity=2).run(suit6).wasSuccessful()
    test_result7 = unittest.TextTestRunner(verbosity=2).run(suit7).wasSuccessful()
    test_result8 = unittest.TextTestRunner(verbosity=2).run(suit8).wasSuccessful()
    test_result9 = unittest.TextTestRunner(verbosity=2).run(suit9).wasSuccessful()
    test_result10 = unittest.TextTestRunner(verbosity=2).run(suit10).wasSuccessful()

    final_test_result = (test_result1 and test_result2 and test_result3 and test_result4 and test_result5 and test_result6 and test_result7 and test_result8 and test_result9 and test_result10)

    print("\nAll tests successfully ended:", final_test_result)
