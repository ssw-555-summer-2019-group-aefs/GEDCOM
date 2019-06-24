#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : Proj04_AWingate_03
#Author            : Anthem Rukiya J. Wingate
#Date created      : 06.23.2019
#Purpose           : User story Implementation of US02, US04, US05, US06, US10
#Revision History  : Version 1.0
# Notes:  This collection of user stories was best implemented together due to the similarities in subject matter, i.e. comparison of dates of spouses

import datetime
from util_date import Date
from Homework05_US01 import us01

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


def us02(husb_id, husb_birth_dt, wife_id, wife_birth_dt, marriage_dt, fam_id):
    """ Check US02 Birth before Marriage for both husband and wife.  Calls US10. """
    
    def us10(dt1, dt2):
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
            print("Data Error:", dt1, dt2) 
    
    error1, error2, error3, error4, error5, error6, error7 = False, False, False, False, False, False, False
    if husb_birth_dt == None:
        print(f"US02: Error: Husband '{husb_id}' in family '{fam_id}' does not have a date of birth.")
        error1 = True
    if wife_birth_dt == None:
        print(f"US02: Error: Wife '{wife_id}' in family '{fam_id}' does not have a date of birth.")
        error2 = True
    if marriage_dt == None:
        print(f"US02: Error: Husband '{husb_id}' and Wife '{wife_id}' in family '{fam_id}' do not have a date of marriage.")
        error3 = True
    elif husb_birth_dt != None and wife_birth_dt != None and marriage_dt != None:
        if date_before(husb_birth_dt, marriage_dt):
            print(f"US02: Error: Husband '{husb_id}' in family '{fam_id}' born after wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
            error4 = True
        if date_before(wife_birth_dt, marriage_dt):
            print(f"US02: Error: Wife '{wife_id}' in family '{fam_id}' born after wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
            error5 = True
        if us10(husb_birth_dt, marriage_dt):
            print(f"US10: Error: Husband '{husb_id}' in family '{fam_id}' married on '{marriage_dt}' before legal age.")
            error6 = True
        if us10(wife_birth_dt, marriage_dt):
            print(f"US10: Error: Wife '{wife_id}' in family '{fam_id}' married on '{marriage_dt}' before legal age.")
            error7 = True
        
    errors = [error1, error2, error3, error4, error5, error6, error7]  
    return errors


def us04(husb_id, wife_id, marriage_dt, divorce_dt, fam_id):
    """ Check US04 Marriage before Divorce for both husband and wife """

    error1, error2, error3 = False, False, False
    if marriage_dt == None:
        print(f"US04: Error: Husband '{husb_id}' and Wife '{wife_id}' in family '{fam_id}' do not have a date of marriage.")
        error1 = True
    elif divorce_dt == None:
        print(f"US04: Error: Husband '{husb_id}' and Wife '{wife_id}' in family '{fam_id}' do not have a date of divorce.")
        error2 = True
    elif marriage_dt != None and divorce_dt != None:
        if date_before(marriage_dt, divorce_dt):
            print(f"US04: Error: Husband '{husb_id}' and Wife '{wife_id}' in family '{fam_id}' divorced before wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
            error3 = True
        
    errors = [error1, error2, error3]
    return errors


def us05(husb_id, husb_death_dt, wife_id, wife_death_dt, marriage_dt, fam_id):
    """ Check US05 Marriage before death for both husband and wife """

    error1, error2, error3 = False, False, False
    if marriage_dt == None:
        print(f"US05: Error: Husband '{husb_id}' in family '{fam_id}' does not have a date of marriage.")
        error1 = True
    else:
        if husb_death_dt != None:
            if date_before(marriage_dt, husb_death_dt):
                print(f"US05: Error: Husband '{husb_id}' in family '{fam_id}' died before wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}'")
                error2 = True
        if wife_death_dt != None:
            if date_before(marriage_dt, wife_death_dt):
                print(f"US05: Error: Wife '{wife_id}' in family '{fam_id}' died before wedding on {marriage_dt.date_time_obj.strftime('%d %b %Y')}")
                error3 = True
    
    errors = [error1, error2, error3]
    return errors


def us06(husb_id, husb_death_dt, wife_id, wife_death_dt, divorce_dt, fam_id):
    """ Check US06 Divorce before death for both husband and wife """

    error1, error2, error3 = False, False, False
    if divorce_dt is None:
        error1 = True
    else:
        if husb_death_dt != None and divorce_dt != None:
            if date_before(divorce_dt, husb_death_dt):
                print(f"US06: Error: Husband '{husb_id}' in family '{fam_id}' died before divorce on {divorce_dt.date_time_obj.strftime('%d %b %Y')}'") 
                error2 = True 
                                 
        if wife_death_dt != None and divorce_dt != None:
            if date_before(divorce_dt, wife_death_dt):
                print(f"US06: Error: Wife '{wife_id}' in family '{fam_id}' died before divorce on {divorce_dt.date_time_obj.strftime('%d %b %Y')}")
                error3= True
    
    errors = [error1, error2, error3]
    return errors


def get_dates(individuals, families):
    """ Stores dates for marriage, divorce, birth and death of spouses. Calls user story 02, 04, 05, and 06 for date comparison."""
    
    errors = dict()
    us02_errors = dict()
    us04_errors = dict()
    us05_errors = dict()
    us06_errors = dict()
    i = 0

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
        
        us02_errors[i] = us02(husb_id, husb_birth_dt, wife_id, wife_birth_dt, marriage_dt, fam_id)
        us04_errors[i] = us04(husb_id, wife_id, marriage_dt, divorce_dt, fam_id)
        us05_errors[i] = us05(husb_id, husb_death_dt, wife_id, wife_death_dt, marriage_dt, fam_id)
        us06_errors[i] = us06(husb_id, husb_death_dt, wife_id, wife_death_dt, divorce_dt, fam_id)
        i+=1
    
    errors = {'us02':us02_errors, 'us04':us04_errors, 'us05':us05_errors, 'us06':us06_errors}
    return errors
