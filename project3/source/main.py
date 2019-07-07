import unittest
import os 
import util_date
import US07_US08_Test_Suite
import unit_test_us1_us2_us3_us4_us5_us6_us10
import US22_unit_test
import unit_tests_us11_us12
from gedcom_file_parser import print_pretty_table


if __name__ == '__main__':
    
    dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

    print_pretty_table(f"{dir_path}/data/fran_test.ged")
    # suit1 = unittest.TestLoader().loadTestsFromModule(util_date)
    # suit2 = unittest.TestLoader().loadTestsFromModule(unit_test_us1_us2_us3_us4_us5_us6_us10)
    # suit3 = unittest.TestLoader().loadTestsFromModule(US07_US08_Test_Suite)
    # suit4 = unittest.TestLoader().loadTestsFromModule(unit_tests_us11_us12)
    # suit5 = unittest.TestLoader().loadTestsFromModule(US22_unit_test)
    # unittest.TextTestRunner(verbosity=2).run(suit1)
    # unittest.TextTestRunner(verbosity=2).run(suit2)
    # unittest.TextTestRunner(verbosity=2).run(suit3)
    # unittest.TextTestRunner(verbosity=2).run(suit4)
    # unittest.TextTestRunner(verbosity=2).run(suit5)
