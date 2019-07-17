#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : Sprint2.py
#Author            : Anthem Rukiya J. Wingate, Fran Sabetpour
#Date created      : 07.07.2019
#Purpose           : User story Implementation of US13, US14, US15, US17, US18, US28, US32, US33
#Revision History  : Version 1.0

# Notes:  Block implementation of user stories involving spouses and children

# Sprint 2:  Child Block
# US13:  Birth dates of siblings should be more than 8 months apart or less than 2 days apart 
# (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
# US14:  No more than five siblings should be born at the same time
# US15:  There should be fewer than 15 siblings in a family
# US17:  Parents should not marry any of their children
# US18:  Siblings should not marry one another
# US28:  List siblings in families by decreasing age, i.e. oldest siblings first
# US32:  List all multiple births in a GEDCOM file
# US33:  List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file

import datetime
from util_date import Date
#from gedcom_file_parser import print_individuals_pretty_table
from collections import OrderedDict, defaultdict
from prettytable import PrettyTable

#
# Begin Sprint 2 Child Block
#

def get_dates_diff(dt1, dt2=None):
    """ Gets date differences for US13 """

    conversion = {'days':1,'months':30.4,'years':365.25}
    if dt2 == None:
        dt2 = today = datetime.datetime.today()
    difference = abs((dt1 - dt2).days)
    if difference >= 365.25:
        time_typ = 'years'
    elif difference >= 30.4 and difference < 365.25:
        time_typ = 'months'
    elif difference >= 0 and difference <30.4:
        time_typ = 'days'

    return difference/conversion[time_typ], time_typ


def us13(children, num_chil, fam_id, individuals, test=False):
    """ Birth dates of siblings should be more than 8 months apart or less than 2 days apart. """

    error1, error2 = False, False
    error3 = ''
    errors = list()
    bd_dict = defaultdict(list)
    for i in range(num_chil):
        bd_key = individuals[children[i]]['BIRT'].date_time_obj
        if Date.is_valid_date(bd_key):
            if bd_key not in bd_dict:
                bd_dict[bd_key] = [children[i]]
            else:
                bd_dict[bd_key].append(children[i])
    
    test_next = True

    for bd_child, child in sorted(bd_dict.items(), reverse=True):
        error = False
        if len(bd_dict[bd_child]) == 1:
            if test_next:
                bd_sib1 = bd_child
                child1 = child
                test_next = False
            else:
                bd_sib2 = bd_child
                child2 = child
                diff, time_typ = get_dates_diff(bd_sib1, bd_sib2)
                if time_typ == 'years':
                    continue
                elif time_typ == 'months' and diff < 8:
                    print(f"US13: Error: Child '{child1}' and Child '{child2}' in family '{fam_id}' are born more than 2 days and less than 8 months apart.")
                    error1 = True
                elif time_typ == 'days' and diff > 2:
                    print(f"US13: Error: Child '{child1}' and Child '{child2}' in family '{fam_id}' are born more than 2 days and less than 8 months apart.")
                    error1 = True
                test_next = True

        elif len(bd_dict[bd_child]) > 1:
            error2, error3 = us14(len(bd_dict[bd_child]), bd_child, bd_dict[bd_child], fam_id, individuals, test)
            test_next = True
            
    if test == True:
        errors = [error1, error2, error3]
        return errors
    else:
        return None



def us14(num_mults, birthdate, mults, fam_id, individuals, test=False):
    """ No more than five siblings should be born at the same time. """

    def us32(birthdate, fam_id, mults, num_mults, individuals, test=False):
        """ List all multiple births in a GEDCOM file. """

        print(f"US32: List: The following '{num_mults}' births occured in family '{fam_id}' on date '{birthdate.strftime('%d %b %Y')}'")
        pt = PrettyTable(field_names=["ID", "Name"])
        for i in range(num_mults):
            mults_info_list = [mults[i], individuals[mults[i]]['NAME']]
            pt.add_row(mults_info_list)
        print(pt)

        if test == True:
            return str(pt)
        else:
            return None

    
    us14_error = False
    if num_mults > 5:
        print(f"US14: Error: More than five children born on date '{birthdate.strftime('%d %b %Y')}' in family '{fam_id}'")
        error = True
    us32_error = us32(birthdate, fam_id, mults, num_mults, individuals, test)

    if test == True:
        return us14_error, us32_error
    else:
        return None


def us15(children, num_chil, fam_id, test=False):
    """ There should be fewer than 15 siblings in a family. """

    error = False
    if num_chil >= 15:
        print(f"US15: Error: No more than fourteen children should be born in each family.  '{num_chil}' children born in family '{fam_id}'")
        error = True

    if test == True: 
        return error
    else:
       return None


def us17(fam_id, husb_id, wife_id, individuals, test=False):
    """ Parents should not marry any of their children. """

    error = False
    if individuals[husb_id]['FAMC'] != 'NA' and individuals[husb_id]['FAMS'] != 'NA':
        if individuals[husb_id]['FAMC'] == individuals[husb_id]['FAMS']:
            print(f"US17: Error: Wife'{wife_id}' in family '{fam_id}' is married to her child.")
            error = True
    elif individuals[wife_id]['FAMC'] != 'NA' and individuals[wife_id]['FAMS'] != 'NA':
        if individuals[wife_id]['FAMC'] == individuals[wife_id]['FAMS']:
            print(f"US17: Error: Husband '{husb_id}' in family '{fam_id}' is married to his child.")
            error = True
            
    if test == True:
        return error
    else:
        return None


def us18(husb_id, wife_id, fam_id, individuals, test=False):
    """ Siblings should not marry one another. """

    error = False
    if individuals[husb_id]['FAMC'] == individuals[wife_id]['FAMC']:
        print(f"US18: Error: Husband '{husb_id}' and wife '{wife_id}' in family '{fam_id}' are brother and sister.  Siblings should not marry one another.")
        error = True

    if test == True:
        return error
    else:
        return None
            
    
def us28(children, num_chil, fam_id, individuals, test=False):
    """ List siblings in families by decreasing age, i.e. oldest siblings first. """
    # Needs Revision: import from gedcom_file_parser and use print_individuals_pretty_table function?

    birth_order = defaultdict(list)
    for i in range (num_chil):
        bd_key = individuals[children[i]]['BIRT'].date_time_obj
        if Date.is_valid_date(bd_key):
            if bd_key not in birth_order:
                birth_order[bd_key] = [children[i]]
            else:
                birth_order[bd_key].append(children[i])
    
    print(f"US28: List: Eldest to youngest children in family '{fam_id}'.")
    pt = PrettyTable(field_names=["ID", "Name", "Date of Birth"])
    for birthdate, child_list in sorted(birth_order.items(), reverse=False):
        child_list_len = len(child_list)
        if child_list_len == 1:
            child_info = [child_list[0], individuals[child_list[0]]['NAME'], birthdate.strftime('%d %b %Y')]
            pt.add_row(child_info)
        elif child_list_len > 1:
            for i in range(child_list_len):
                child_info = [child_list[i], individuals[child_list[i]]['NAME'], birthdate.strftime('%d %b %Y')]
                pt.add_row(child_info)    
    
    if test == True:
        return str(pt)
    else:
        print(pt)              
    

def us33(children, num_chil, fam_id, husb_id, wife_id, individuals, test=False):
    """ List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file. """

    orphan_info = defaultdict(list)
    for i in range(num_chil):
        if individuals[children[i]]['AGE'] != 'NA' and individuals[children[i]]['AGE'] < 18:
            orphan_info[i] = [children[i], individuals[children[i]]['NAME']]

    num_orphans = len(orphan_info)
    if num_orphans > 0:  
        print(f"US33: List: These children in family '{fam_id}' are orphans.")
        pt = PrettyTable(field_names=["ID", "Name"])
        for i in range(num_orphans-1):
            pt.add_row(orphan_info[i])

        if test == True:
            return str(pt)
        else:
            print(pt)


def get_child_block(individuals, families):
    """ Get the children. """
    # Notes: us28, us32, us33 return prettytable for testing

    for fam_id, fam in families.items():  # each fam is dict with the attributes of the family
        if fam['CHIL'] == 'NA':
            husb_id = fam['HUSB']
            wife_id = fam['WIFE']
            if individuals[husb_id]['FAMC'] != 'NA' and individuals[wife_id]['FAMC'] != 'NA':
                us18(husb_id, wife_id, fam_id, individuals)
            continue
        else:
            children = fam['CHIL']
            num_chil = len(children)
            husb_id = fam['HUSB']
            wife_id = fam['WIFE']
            if individuals[husb_id]['FAMC'] != 'NA' and individuals[wife_id]['FAMC'] != 'NA':
                us18(husb_id, wife_id, fam_id, individuals)           
            us13(children, num_chil, fam_id, individuals) #Also calls US14 and US32
            us15(children, num_chil, fam_id)
            us17(fam_id, husb_id, wife_id, individuals)
            us28(children, num_chil, fam_id, individuals)
            if individuals[fam['HUSB']]['DEAT'] != 'NA' and individuals[fam['WIFE']]['DEAT'] != 'NA':
                us33(children, num_chil, fam_id, husb_id, wife_id, individuals)
        

    return None

