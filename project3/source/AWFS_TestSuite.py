#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : AWFS_TestSuite.py
#Author            : Anthem Rukiya J. Wingate, Fran Sabetpour
#Date created      : 07.15.2019
#Purpose           : Unit tests for GEDCOM user story implementation
#Revision History  : Version 1.0
# Notes:  GEDCOM Project Test Suite

import unittest
import os
from prettytable import PrettyTable
from utils import LEVEL_TAGS, get_families_pretty_table_order, get_family_info_tags, get_individual_info_tags, get_individual_pretty_Table_order
from util_date import Date
from gedcom_file_parser import print_pretty_table
from Sprint1 import get_spouse_block, us01, us02, us03, us04, us05, us06, us10
from Sprint2 import get_child_block, us13, us14, us15, us17, us18, us28, us33
from Sprint3 import get_recent_block, us34, us35, us36, us37


class TestSuite(unittest.TestCase):
    def __init__(self):
        #Assign directory path variables to individual gedcom files to test each user story
        #run print_pretty_table function with specialized directory path to create indivduals and families dictionaries unique to the user story that will be tested
        self.dir_abs_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        self.directory_path = f"{dir_abs_path}/data/sprint2userstorytest.ged"
        self.individuals, self.families = print_pretty_table(self.directory_path)
    
#
# Begin Sprint 1 Spouse Block Tests
#

    def test_us01(self):
        """ Test for US01 """
        # Test with GEDCOM individual @I4@
    
        test = True
        test_id = '@I4@'
        error_chk = [False, True, False, False]
        self.assertEqual(us01(self.individuals, self.families, test_id, test), error_chk)

        return None
    
    def test_us02_us10(self):
        """ Test for US02 and US10 """
        # Test with GEDCOM individual @I4@

        test = True
        husb_id = '@I4@'
        wife_id = '@I6@'
        husb_birth_dt = '18 Jun 2021'
        wife_birth_dt = '18 Jun 2000'
        marriage_dt = '18 Jun 2019'
        fam_id = '@F3@'
        error_chk = [True, False, True, False]
        self.assertEqual(us02(husb_id, husb_birth_dt, wife_id, wife_birth_dt, marriage_dt, fam_id, test), error_chk)

        return None

    def test_us03(self):
        """ Test for US03 """
        # Test with GEDCOM individual @I4@

        test = True
        error_chk = '@I4@'
        self.assertEqual(us03(self.individuals, test), error_chk)

        return None

    def test_us04(self):
        """ Test for US04 """
        # Test with GEDCOM individual @I4@

        test = True
        husb_id = '@I4@'
        wife_id = '@I6@'
        marriage_dt = '18 Jun 2019'
        divorce_dt = '18 Jun 2018'
        fam_id = '@F3@'
        error_chk = True
        self.assertEqual(us04(husb_id, wife_id, marriage_dt, divorce_dt, fam_id, test), error_chk)

        return None
    
    def test_us05(self):
        """ Test for US05 """
        # Test with GEDCOM individual @I6@

        test = True
        husb_id = '@I4@'
        wife_id = '@I6@'
        husb_death_dt = '18 Jun 2020'
        wife_death_dt = '18 Jun 2017'
        marriage_dt = '18 Jun 2019'
        fam_id = '@F3@'
        error_chk = [False, True]
        self.assertEqual(us05(husb_id, husb_death_dt, wife_id, wife_death_dt, marriage_dt, fam_id, test), error_chk)

        return None

    def test_us06(self):
        """ Test for US06 """
        # Test with GEDCOM individual @I6@

        test = True
        husb_id = '@I4@'
        wife_id = '@I6@'
        husb_death_dt = '18 Jun 2020'
        wife_death_dt = '18 Jun 2017'
        divorce_dt = '18 Jun 2018'
        fam_id = '@F3@'
        error_chk = [False, True]
        self.assertEqual(us06(husb_id, husb_death_dt, wife_id, wife_death_dt, divorce_dt, fam_id, test), error_chk)

        return None

    
#
# Begin Sprint 2 Child Block Tests
#
    
    def test_us13(self):
        """ Test for US13"""
        # Test with GEDCOM family @F1@
    
        test = True
        fam_id = '@F3@'
        children = ['@I1@', '@I5@']
        num_chil = 2
        error_chk = [True, False, '']
        self.assertEqual(us13(children, num_chil, fam_id, self.individuals, test), error_chk)

    def test_us14_us32(self):
        """ Test for US14 and US32"""
        # Test with GEDCOM family @F1@
    
        test = True
        fam_id = '@F1@'
        mults = ['@I3@', '@I7@', '@I8@', '@I9@', '@I10@', '@I11@', '@I12@', '@I13@', '@I14@', '@I15@', '@I16@', '@I17@', '@I18@', '@I19@', '@I20@', '@I21@', '@I22@']
        num_mults = 16
        birthdate = '27 May 2018'
        # Expected Result for US32
        us32_pt = PrettyTable(field_names=["ID", "Name"])
        us32_pt.add_row(['@I3@','Emma /Rose/'])
        us32_pt.add_row(['@I7@','Isabel /Rose/'])
        us32_pt.add_row(['@I8@','Angela /Rose/'])
        us32_pt.add_row(['@I9@','Trish /Rose/'])
        us32_pt.add_row(['@I10@','Ethan /Rose/'])
        us32_pt.add_row(['@I11@','Ian /Rose/'])
        us32_pt.add_row(['@I12@','Michael /Rose/'])
        us32_pt.add_row(['@I13@','Richelle /Rose/'])
        us32_pt.add_row(['@I14@','Matthew /Rose/'])
        us32_pt.add_row(['@I15@','Luke /Rose/'])
        us32_pt.add_row(['@I16@','Cynthia /Rose/'])
        us32_pt.add_row(['@I17@','Frederick /Rose/'])
        us32_pt.add_row(['@I18@','Tina /Rose/'])
        us32_pt.add_row(['@I19@','Tanya /Rose/'])
        us32_pt.add_row(['@I20@','Emmy /Rose/'])
        us32_pt.add_row(['@I21@','Thomas /Rose/'])
        us32_str = str(us32_pt)
        error_chk = [True, us32_str]
        self.assertEqual(us14(num_mults, birthdate, mults, fam_id, self.individuals, test), error_chk)
        return None

    def test_us15(self):
        """ Test for US15"""
        # Test with GEDCOM family @F1@
    
        test = True
        fam_id = '@F1@'
        children = ['@I3@', '@I7@', '@I8@', '@I9@', '@I10@', '@I11@', '@I12@', '@I13@', '@I14@', '@I15@', '@I16@', '@I17@', '@I18@', '@I19@', '@I20@', '@I21@', '@I22@']
        num_chil = 16    
        error_chk = [True]
        self.assertEqual(us15(children, num_chil, fam_id, test), error_chk)
        return None

    def test_us17(self):
        """ Test for US17"""
        # Test with GEDCOM individual @I2@
    
        test = True
        husb_id = '@I2@'
        wife_id = '@I9@'
        fam_id = '@F1@'  
        error_chk = [True]
        self.assertEqual(us17(fam_id, husb_id, wife_id, self.individuals, test), error_chk)
        return None

    def test_us18(self):
        """ Test for US18"""
        # Test with GEDCOM family @F4@
    
        test = True
        husb_id = '@I17@'
        wife_id = '@I16@'
        fam_id = '@F4@'  
        error_chk = [True]
        self.assertEqual(us18(husb_id, wife_id, fam_id, self.individuals, test), error_chk)
        return None

    def test_us28(self):
        """ Test for US28"""
        # Test with GEDCOM family @F3@
    
        test = True
        children = ['@I1@', '@I5@']
        num_chil = 2
        fam_id = '@F3@'
        # Expected Result for US28
        us28_pt = PrettyTable(field_names=["ID", "Name", "Date of Birth"])
        us28_pt.add_row(['@I1@','Tristin /Evans/', '12 Apr 1987'])
        us28_pt.add_row(['@I5@','Aeryn /Evans/', '30 Apr 1987'])
        us28_str = str(us28_pt)
        error_chk = us28_str
        self.assertEqual(us28(children, num_chil, fam_id, self.individuals, test), error_chk)
        return None

    def test_us33(self):
        """ Test for US33"""
        # Test with GEDCOM family @F1@
    
        test = True
        husb_id = '@I2@'
        wife_id = '@I9@'
        children = ['@I3@', '@I7@', '@I8@', '@I9@', '@I10@', '@I11@', '@I12@', '@I13@', '@I14@', '@I15@', '@I16@', '@I17@', '@I18@', '@I19@', '@I20@', '@I21@', '@I22@']
        num_chil = 16
        fam_id = '@F1@'
        # Expected Result for US33
        us33_pt = PrettyTable(field_names=["ID", "Name"])
        us33_pt.add_row(['@I3@','Emma /Rose/'])
        us33_pt.add_row(['@I7@','Isabel /Rose/'])
        us33_pt.add_row(['@I8@','Angela /Rose/'])
        us33_pt.add_row(['@I9@','Trish /Rose/'])
        us33_pt.add_row(['@I10@','Ethan /Rose/'])
        us33_pt.add_row(['@I11@','Ian /Rose/'])
        us33_pt.add_row(['@I12@','Michael /Rose/'])
        us33_pt.add_row(['@I13@','Richelle /Rose/'])
        us33_pt.add_row(['@I14@','Matthew /Rose/'])
        us33_pt.add_row(['@I15@','Luke /Rose/'])
        us33_pt.add_row(['@I16@','Cynthia /Rose/'])
        us33_pt.add_row(['@I17@','Frederick /Rose/'])
        us33_pt.add_row(['@I18@','Tina /Rose/'])
        us33_pt.add_row(['@I19@','Tanya /Rose/'])
        us33_pt.add_row(['@I20@','Emmy /Rose/'])
        us33_pt.add_row(['@I21@','Thomas /Rose/'])
        us33_str = str(us33_pt)
        error_chk = us33_str
        self.assertEqual(us33(children, num_chil, fam_id, husb_id, wife_id, self.individuals, test), error_chk)
        return None

    
#
# Begin Sprint 3 Recents Block Tests
#

    def test_us34(self):
        """ Test for US34"""
        # Test with GEDCOM family @F@
    
        test = True
        fam_id = '@F@'
        error_chk = []
        self.assertEqual(us34(self.individuals, self.families, fam_id, test), error_chk)
        
        return None
    
    def test_us35(self):
        """ Test for US35"""
        # Test with GEDCOM family @F@
    
        test = True
        # Expected Result for US35
        us35_pt = PrettyTable(field_names=["ID", "Name", "Date of Birth"])
        us35_pt.add_row(['@I3@','Emma /Rose/'])
        us35_str = str(us35_pt)
        error_chk = us35_str
        self.assertEqual(us35(self.individuals, test), error_chk)
        
        return None
    
    def test_us36_us37(self):
        """ Test for US36 and US37"""
        # Test with GEDCOM individuals @I1@, @I2@, @I9@
    
        test = True
        # Expected Result for US36
        us36_pt = PrettyTable(field_names=["ID", "Name", "Date of Death"])
        us36_pt.add_row(['@I1@','Tristin /Evans/', '04 Jul 2019'])
        us36_pt.add_row(['@I2@','Angelo /Rose/', '04 Jul 2019'])
        us36_pt.add_row(['@I9@','Trish /Rose/', '04 Jul 2019'])
        us36_str = str(us36_pt)

        # Expected Result for US37
        us37_pt = PrettyTable(field_names=["ID", "Name", "Relation"])
        us37_pt.add_row([])
        us37_str = str(us37_pt)
        error_chk = (us36_str, us37_str)
        self.assertEqual(us36(self.individuals, self.families, test), error_chk)
        
        return None


if __name__ == '__main__':
    unittest.main()