import unittest
import util_date
from project03_saransh_ahlawat import print_pretty_table

if __name__ == '__main__':

    print("\n*************************** USER STORIES: US27, US42 ***************************\n")
    
    print_pretty_table("/Users/saranshahlawat/Desktop/Stevens/Semesters/Summer 2019/SSW-555/project/GEDCOM/project3/data/faultyDates.ged")

    suite = unittest.TestLoader().loadTestsFromModule(util_date)
    unittest.TextTestRunner(verbosity=2).run(suite)

