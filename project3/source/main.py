import unittest
from gedcom_file_parser import print_pretty_table
import util_date
import US07_US08_Test_Suite
import Unit_test_us11_us12
import Sprint2_TestSuite

if __name__ == '__main__':
    
    print_pretty_table("C:/Users/Anthe/OneDrive/Documents/GitHub/GEDCOM/project3/source/sprint2userstorytest.ged")
    #suit1 = unittest.TestLoader().loadTestsFromModule(util_date)
    suit2 = unittest.TestLoader().loadTestsFromModule(Sprint2_TestSuite)
    #suit3 = unittest.TestLoader().loadTestsFromModule(US07_US08_Test_Suite)
    #suit4 = unittest.TestLoader().loadTestsFromModule(Unit_test_us11_us12)
    

    #unittest.TextTestRunner(verbosity=2).run(suit1)
    unittest.TextTestRunner(verbosity=2).run(suit2)
    #unittest.TextTestRunner(verbosity=2).run(suit3)
    #unittest.TextTestRunner(verbosity=2).run(suit4)
    