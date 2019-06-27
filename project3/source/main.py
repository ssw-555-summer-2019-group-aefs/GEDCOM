import unittest
from gedcom_file_parser import print_pretty_table
import util_date
import US07_US08_Test_Suite
import unit_test_us1_us2_us3_us4_us5_us6_us10

if __name__ == '__main__':
    
    print_pretty_table("C:/Users/Anthe/OneDrive/Documents/Stevens/SSW 555/GEDCOM/Projects/Sprint2/faultyDates.ged")
    suit1 = unittest.TestLoader().loadTestsFromModule(util_date)
    suit2 = unittest.TestLoader().loadTestsFromModule(unit_test_us1_us2_us3_us4_us5_us6_us10)
    suit3 = unittest.TestLoader().loadTestsFromModule(US07_US08_Test_Suite)
    unittest.TextTestRunner(verbosity=2).run(suit1)
    unittest.TextTestRunner(verbosity=2).run(suit2)
    unittest.TextTestRunner(verbosity=2).run(suit3)