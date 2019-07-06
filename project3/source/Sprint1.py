#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : Proj04_AWingate_03
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


def us01(individuals, families):
    """ Check US01 Dates (birth, marriage, divorce, death) should not be after the current date."""

    errors = list()
  
    for ind_id, ind in individuals.items(): # each ind is dict with the attributes of the individual
        error = False
        if ind['BIRT'] != 'NA' and type(ind['BIRT'].date_time_obj) is not str:
            if Date.get_dates_difference(ind['BIRT'].date_time_obj) < 0:
                    print(f"US01: Error: Individual's '{ind_id}' birthday '{ind['BIRT'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")
                    error = True
        
        if ind['DEAT'] != 'NA' and type(ind['DEAT'].date_time_obj) is not str:
            if Date.get_dates_difference(ind['DEAT'].date_time_obj) < 0:
                print(f"US01: Error: Individual's '{ind_id}' death date '{ind['DEAT'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")
                error = True
        

        if ind['FAMS'] != 'NA':
            if families[ind['FAMS']]['MARR'] != "NA" and type(families[ind['FAMS']]['MARR'].date_time_obj) is not str:
                if families[ind['FAMS']]['MARR'] != 'NA':
                    if Date.get_dates_difference(families[ind['FAMS']]['MARR'].date_time_obj) < 0:
                        print(f"US01: Error: Individual's '{ind_id}' marriage date '{families[ind['FAMS']]['MARR'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")
                        error = True

            if families[ind['FAMS']]['DIV'] != 'NA' and type(families[ind['FAMS']]['DIV'].date_time_obj) is not str:
                if Date.get_dates_difference(families[ind['FAMS']]['DIV'].date_time_obj) < 0:
                    print(f"US01: Error: Individual's '{ind_id}' divorce date '{families[ind['FAMS']]['DIV'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")
                    error = True
    
        errors.append(error)
  
    if True in errors:
        return True
    

def us02(husb_id, husb_birth_dt, wife_id, wife_birth_dt, marriage_dt, fam_id):
    """ Check US02 Birth before Marriage for both husband and wife.  Calls US10. """
    
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
    
    error1, error2 = False, False
    if husb_birth_dt != None and wife_birth_dt != None and marriage_dt != None:
        if date_before(husb_birth_dt, marriage_dt):
            print(f"US02: Error: Husband '{husb_id}' in family '{fam_id}' born after wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
            error1 = True
        if date_before(wife_birth_dt, marriage_dt):
            print(f"US02: Error: Wife '{wife_id}' in family '{fam_id}' born after wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
            error1 = True
        
        if us10(husb_birth_dt, marriage_dt, 'Husband', fam_id):
            print(f"US10: Error: Husband '{husb_id}' in family '{fam_id}' married on '{marriage_dt}' before legal age.")
            error2 = True
        if us10(wife_birth_dt, marriage_dt, 'Wife', fam_id):
            print(f"US10: Error: Wife '{wife_id}' in family '{fam_id}' married on '{marriage_dt}' before legal age.")
            error2 = True
        
    return error1, error2


def us03(individuals):
    """ Check US03 Birth should occur before death of an individual."""


    error = list()
    for ind_id, ind in individuals.items(): # each ind is dict with the attributes of the individual
        error.append(False)
        if type(ind['BIRT'].date_time_obj) is not str and type(ind['DEAT']) is not str and type(ind['DEAT'].date_time_obj) is not str:
            if ind['BIRT'] != 'NA':
                birth_dt = ind['BIRT'].date_time_obj
            if ind['DEAT'] != 'NA':
                death_dt = ind['DEAT'].date_time_obj
                if Date.get_dates_difference(birth_dt,death_dt) < 0:
                    print(f"US03: Error: Individual's '{ind_id}' birthday '{ind['BIRT'].date_time_obj.strftime('%d %b %Y')}' occurs after the death date '{ind['DEAT'].date_time_obj.strftime('%d %b %Y')}'.")
                    error.append(True)
        
    if True in error:
        return True


def us04(husb_id, wife_id, marriage_dt, divorce_dt, fam_id):
    """ Check US04 Marriage before Divorce for both husband and wife """

    error = False
    if marriage_dt != None and divorce_dt != None:
        if date_before(marriage_dt, divorce_dt):
            print(f"US04: Error: Husband '{husb_id}' and Wife '{wife_id}' in family '{fam_id}' divorced before wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
            error = True
        
    return error


def us05(husb_id, husb_death_dt, wife_id, wife_death_dt, marriage_dt, fam_id):
    """ Check US05 Marriage before death for both husband and wife """

    error1, error2 = False, False
    if marriage_dt == None:
        error1, error2 = False, False
    else:
        if husb_death_dt != None:
            if date_before(marriage_dt, husb_death_dt):
                print(f"US05: Error: Husband '{husb_id}' in family '{fam_id}' died before wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}'")
                error1 = True
        if wife_death_dt != None:
            if date_before(marriage_dt, wife_death_dt):
                print(f"US05: Error: Wife '{wife_id}' in family '{fam_id}' died before wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
                error2 = True
    
    errors = [error1, error2]
    if True in errors:
        return True
    else:
        return False


def us06(husb_id, husb_death_dt, wife_id, wife_death_dt, divorce_dt, fam_id):
    """ Check US06 Divorce before death for both husband and wife """

    error1, error2 = False, False
    if divorce_dt is None:
        error1, error2 = False, False
    else:
        if husb_death_dt != None and divorce_dt != None:
            if date_before(divorce_dt, husb_death_dt):
                print(f"US06: Error: Husband '{husb_id}' in family '{fam_id}' died before divorce on {divorce_dt.date_time_obj.strftime('%d %b %Y')}'") 
                error1 = True 
                                 
        if wife_death_dt != None and divorce_dt != None:
            if date_before(divorce_dt, wife_death_dt):
                print(f"US06: Error: Wife '{wife_id}' in family '{fam_id}' died before divorce on {divorce_dt.date_time_obj.strftime('%d %b %Y')}")
                error2 = True
    
    errors = [error1, error2]
    if True in errors:
        return True
    else:
        return False


def get_spouse_block(individuals, families):
    """ Stores dates for marriage, divorce, birth and death of spouses. Calls user story 02, 04, 05, and 06 for date comparison."""
    
    errors = dict()
    us01_errors = False
    us02_errors = dict()
    us03_errors = False
    us04_errors = dict()
    us05_errors = dict()
    us06_errors = dict()
    us10_errors = dict()
    i = 0

    us01_errors = us01(individuals, families)
    us03_errors = us03(individuals)
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
        
        us02_errors[i], us10_errors[i] = us02(husb_id, husb_birth_dt, wife_id, wife_birth_dt, marriage_dt, fam_id)
        us04_errors[i] = us04(husb_id, wife_id, marriage_dt, divorce_dt, fam_id)
        us05_errors[i] = us05(husb_id, husb_death_dt, wife_id, wife_death_dt, marriage_dt, fam_id)
        us06_errors[i] = us06(husb_id, husb_death_dt, wife_id, wife_death_dt, divorce_dt, fam_id)
       
        i+=1
    
    errors = {'us01':us01_errors,'us02':us02_errors, 'us03':us03_errors, 'us04':us04_errors, 'us05':us05_errors, 'us06':us06_errors, 'us10':us01_errors}
    
    return errors