#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : Sprint1.py
#Author            : Anthem Rukiya J. Wingate, Fran Sabetpour
#Date created      : 06.23.2019
#Purpose           : User story Implementation of US02, US04, US05, US06, US10
#Revision History  : Version 1.0
# Notes:  This collection of user stories was best implemented together due to the similarities in subject matter, i.e. comparison of dates of spouses
# Sprint 1:  Spouse Block
# US1:  Dates (birth, marriage, divorce, death) should not be after the current date
# US2:  Birth before Marriage for both husband and wife.
# US3:  Birth should occur before death of an individual
# US4:  Marriage before Divorce for both husband and wife
# US5:  Marriage before death for both husband and wife
# US6:  Divorce before death for both husband and wife
# US10:  Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)

import datetime
from util_date import Date

#
# Begin Sprint 1 Spouse Block
#

def date_before(dt1, dt2):
    """ Send two dates to Date class for comparison """

    try:
        date_diff = Date.get_dates_difference(dt1.date_time_obj, dt2.date_time_obj)
        if type(date_diff) is str:
            raise ValueError
        if date_diff >= 0:
            return False
        if date_diff <= -1:
            return True 
    except:
        print('Data Error', dt1, dt2)


def us01(individuals, families, ind_id='', test=False):
    """ Check US01 Dates (birth, marriage, divorce, death) should not be after the current date."""

    if test == True:
        errors = list()
        error1, error2, error3, error4 = False, False, False, False
        if individuals[ind_id]['BIRT'] != 'NA' and type(individuals[ind_id]['BIRT'].date_time_obj) is not str:
            if Date.get_dates_difference(individuals[ind_id]['BIRT'].date_time_obj) < 0:
                print(f"US01: Error: Individual's '{ind_id}' birthday '{individuals['BIRT'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")
                error1 = True
            
        if individuals[ind_id]['DEAT'] != 'NA' and type(individuals[ind_id]['DEAT'].date_time_obj) is not str:
            if Date.get_dates_difference(individuals[ind_id]['DEAT'].date_time_obj) < 0:
                print(f"US01: Error: Individual's '{ind_id}' death date '{individuals[ind_id]['DEAT'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")
                error2 = True
            

        if individuals[ind_id]['FAMS'] != 'NA':
            if families[individuals[ind_id]['FAMS']]['MARR'] != "NA" and type(families[individuals[ind_id]['FAMS']]['MARR'].date_time_obj) is not str:
                if families[individuals[ind_id]['FAMS']]['MARR'] != 'NA':
                    if Date.get_dates_difference(families[individuals['FAMS']]['MARR'].date_time_obj) < 0:
                        print(f"US01: Error: Individual's '{ind_id}' marriage date '{families[individuals[ind_id]['FAMS']]['MARR'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")
                        error3 = True

            if families[individuals[ind_id]['FAMS']]['DIV'] != 'NA' and type(families[individuals[ind_id]['FAMS']]['DIV'].date_time_obj) is not str:
                if Date.get_dates_difference(families[individuals['FAMS']]['DIV'].date_time_obj) < 0:
                    print(f"US01: Error: Individual's '{ind_id}' divorce date '{families[individuals[ind_id]['FAMS']]['DIV'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")
                    error4 = True

        errors = [error1, error2, error3, error4]
        return errors
    else:
        for ind_id, ind in individuals.items(): # each ind is dict with the attributes of the individual
            if ind['BIRT'] != 'NA' and type(ind['BIRT'].date_time_obj) is not str:
                if Date.get_dates_difference(ind['BIRT'].date_time_obj) < 0:
                    print(f"US01: Error: Individual's '{ind_id}' birthday '{ind['BIRT'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")
            
            if ind['DEAT'] != 'NA' and type(ind['DEAT'].date_time_obj) is not str:
                if Date.get_dates_difference(ind['DEAT'].date_time_obj) < 0:
                    print(f"US01: Error: Individual's '{ind_id}' death date '{ind['DEAT'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")
            

            if ind['FAMS'] != 'NA':
                if families[ind['FAMS']]['MARR'] != "NA" and type(families[ind['FAMS']]['MARR'].date_time_obj) is not str:
                    if families[ind['FAMS']]['MARR'] != 'NA':
                        if Date.get_dates_difference(families[ind['FAMS']]['MARR'].date_time_obj) < 0:
                            print(f"US01: Error: Individual's '{ind_id}' marriage date '{families[ind['FAMS']]['MARR'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")

                if families[ind['FAMS']]['DIV'] != 'NA' and type(families[ind['FAMS']]['DIV'].date_time_obj) is not str:
                    if Date.get_dates_difference(families[ind['FAMS']]['DIV'].date_time_obj) < 0:
                        print(f"US01: Error: Individual's '{ind_id}' divorce date '{families[ind['FAMS']]['DIV'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")

        return None
    

def us02(husb_id, husb_birth_dt, wife_id, wife_birth_dt, marriage_dt, fam_id, test=False):
    """ Check US02 Birth before Marriage for both husband and wife.  Calls US10. """
    
    if test ==True:
        errors = list()
        error1, error2, error3, error4 = False, False, False, False
        if husb_birth_dt != None and wife_birth_dt != None and marriage_dt != None:
            if date_before(husb_birth_dt, marriage_dt):
                print(f"US02: Error: Husband '{husb_id}' in family '{fam_id}' born after wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
                error1 = True
            if date_before(wife_birth_dt, marriage_dt):
                print(f"US02: Error: Wife '{wife_id}' in family '{fam_id}' born after wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
                error2 = True
            if us10(husb_birth_dt, marriage_dt, 'Husband', fam_id):
                print(f"US10: Error: Husband '{husb_id}' in family '{fam_id}' married on '{marriage_dt}' before legal age.")
                error3 = True
            if us10(wife_birth_dt, marriage_dt, 'Wife', fam_id):
                print(f"US10: Error: Wife '{wife_id}' in family '{fam_id}' married on '{marriage_dt}' before legal age.")
                error4 = True
        errors = [error1, error2, error3, error4]
        return errors
    else:
        if husb_birth_dt != None and wife_birth_dt != None and marriage_dt != None:
            if date_before(husb_birth_dt, marriage_dt):
                print(f"US02: Error: Husband '{husb_id}' in family '{fam_id}' born after wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
                
            if date_before(wife_birth_dt, marriage_dt):
                print(f"US02: Error: Wife '{wife_id}' in family '{fam_id}' born after wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
                            
            if us10(husb_birth_dt, marriage_dt, 'Husband', fam_id):
                print(f"US10: Error: Husband '{husb_id}' in family '{fam_id}' married on '{marriage_dt}' before legal age.")
                
            if us10(wife_birth_dt, marriage_dt, 'Wife', fam_id):
                print(f"US10: Error: Wife '{wife_id}' in family '{fam_id}' married on '{marriage_dt}' before legal age.")
        return None


def us03(individuals, test=False):
    """ Check US03 Birth should occur before death of an individual."""

    if test == True:
        for ind_id, ind in individuals.items():
            if type(ind['BIRT'].date_time_obj) is not str and type(ind['DEAT']) is not str and type(ind['DEAT'].date_time_obj) is not str:
                if ind['BIRT'] != 'NA':
                    birth_dt = ind['BIRT'].date_time_obj
                if ind['DEAT'] != 'NA':
                    death_dt = ind['DEAT'].date_time_obj
                    if Date.get_dates_difference(birth_dt, death_dt) < 0:
                        print(f"US03: Error: Individual's '{ind_id}' birthday '{ind['BIRT'].date_time_obj.strftime('%d %b %Y')}' occurs after the death date '{ind['DEAT'].date_time_obj.strftime('%d %b %Y')}'.")
                        return ind_id
    else:
        for ind_id, ind in individuals.items(): # each ind is dict with the attributes of the individual
            if type(ind['BIRT'].date_time_obj) is not str and type(ind['DEAT']) is not str and type(ind['DEAT'].date_time_obj) is not str:
                if ind['BIRT'] != 'NA':
                    birth_dt = ind['BIRT'].date_time_obj
                if ind['DEAT'] != 'NA':
                    death_dt = ind['DEAT'].date_time_obj
                    if Date.get_dates_difference(birth_dt, death_dt) < 0:
                        print(f"US03: Error: Individual's '{ind_id}' birthday '{ind['BIRT'].date_time_obj.strftime('%d %b %Y')}' occurs after the death date '{ind['DEAT'].date_time_obj.strftime('%d %b %Y')}'.")
        
        return None

        
    

def us04(husb_id, wife_id, marriage_dt, divorce_dt, fam_id, test=False):
    """ Check US04 Marriage before Divorce for both husband and wife """

    if test == True:
        error = False
        if marriage_dt != None and divorce_dt != None:
            if date_before(marriage_dt, divorce_dt):
                print(f"US04: Error: Husband '{husb_id}' and Wife '{wife_id}' in family '{fam_id}' divorced before wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
                error = True       
        return error
    else:
        if marriage_dt != None and divorce_dt != None:
            if date_before(marriage_dt, divorce_dt):
                print(f"US04: Error: Husband '{husb_id}' and Wife '{wife_id}' in family '{fam_id}' divorced before wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
        return None


def us05(husb_id, husb_death_dt, wife_id, wife_death_dt, marriage_dt, fam_id, test=False):
    """ Check US05 Marriage before death for both husband and wife """

    if test == True:
        error1, error2 = False, False
        if marriage_dt != None and husb_death_dt != None:
            if date_before(marriage_dt, husb_death_dt):
                print(f"US05: Error: Husband '{husb_id}' in family '{fam_id}' died before wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}'")
                error1 = True
        if marriage_dt != None and wife_death_dt != None:
            if date_before(marriage_dt, wife_death_dt):
                print(f"US05: Error: Wife '{wife_id}' in family '{fam_id}' died before wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
                error2 = True
        errors = [error1, error2]
        return errors
    else:
        if marriage_dt != None and husb_death_dt != None:
            if date_before(marriage_dt, husb_death_dt):
                print(f"US05: Error: Husband '{husb_id}' in family '{fam_id}' died before wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}'")
        if marriage_dt != None and wife_death_dt != None:
            if date_before(marriage_dt, wife_death_dt):
                print(f"US05: Error: Wife '{wife_id}' in family '{fam_id}' died before wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
        return None


def us06(husb_id, husb_death_dt, wife_id, wife_death_dt, divorce_dt, fam_id, test=False):
    """ Check US06 Divorce before death for both husband and wife """

    if test==True:
        error1, error2 = False, False
        if husb_death_dt != None and divorce_dt != None:
            if date_before(divorce_dt, husb_death_dt):
                print(f"US06: Error: Husband '{husb_id}' in family '{fam_id}' died before divorce on {divorce_dt.date_time_obj.strftime('%d %b %Y')}'") 
                error1 = True 
                                
        if wife_death_dt != None and divorce_dt != None:
            if date_before(divorce_dt, wife_death_dt):
                print(f"US06: Error: Wife '{wife_id}' in family '{fam_id}' died before divorce on {divorce_dt.date_time_obj.strftime('%d %b %Y')}")
                error2 = True
    
        errors = [error1, error2]
        return errors
    else:
        if husb_death_dt != None and divorce_dt != None:
            if date_before(divorce_dt, husb_death_dt):
                print(f"US06: Error: Husband '{husb_id}' in family '{fam_id}' died before divorce on {divorce_dt.date_time_obj.strftime('%d %b %Y')}'") 
 
        if wife_death_dt != None and divorce_dt != None:
            if date_before(divorce_dt, wife_death_dt):
                print(f"US06: Error: Wife '{wife_id}' in family '{fam_id}' died before divorce on {divorce_dt.date_time_obj.strftime('%d %b %Y')}")

        return None
   


def us10(dt1, dt2, spouse, fam_id):

        """ Check US10 Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old) """
        
        try:
            date_diff = Date.get_dates_difference(dt1.date_time_obj, dt2.date_time_obj)
            if type(date_diff) is str:
                raise ValueError
            if date_diff >= 14:
                return False
            if date_diff < 14:
                return True
        except:
            print(f"Data Error: Birth date '{dt1}' and marriage date '{dt2}' for '{spouse}' in family '{fam_id}' are not in a compatible format.")


def get_spouse_block(individuals, families):
    """ Stores dates for marriage, divorce, birth and death of spouses. Calls user story 02, 04, 05, and 06 for date comparison."""

    us01(individuals, families)
    us03(individuals)
    for fam in families.values():  # each fam is dict with the attributes of the family
        marriage_dt = fam['MARR']
        if marriage_dt is "NA":
            marriage_dt = None

        divorce_dt = fam['DIV']
        if divorce_dt is "NA":
            divorce_dt = None

        husb_id = fam['HUSB']
        wife_id = fam['WIFE']

        husb_birth_dt = individuals[husb_id]['BIRT']
        if husb_birth_dt is "NA":
            husb_birth_dt = None

        husb_death_dt = individuals[husb_id]['DEAT']
        if husb_death_dt is "NA":
            husb_death_dt = None

        wife_birth_dt = individuals[wife_id]['BIRT']
        if wife_birth_dt is "NA":
            wife_birth_dt = None

        wife_death_dt = individuals[wife_id]['DEAT']
        if wife_death_dt is "NA":
            wife_death_dt = None
        
       
        fam_id = individuals[wife_id]['FAMS']
        
        us02(husb_id, husb_birth_dt, wife_id, wife_birth_dt, marriage_dt, fam_id)
        us04(husb_id, wife_id, marriage_dt, divorce_dt, fam_id)
        us05(husb_id, husb_death_dt, wife_id, wife_death_dt, marriage_dt, fam_id)
        us06(husb_id, husb_death_dt, wife_id, wife_death_dt, divorce_dt, fam_id)
    
    return None

