#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : Sprint 2
#Author            : Anthem Rukiya J. Wingate, Fran Sabetour
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
from collections import OrderedDict
from prettytable import PrettyTable

#from gedcom_file_parser import print_individuals_pretty_table


#
# Begin Sprint 2 Child Block
#

def get_dates_diff(dt1, dt2=None):
    """ Gets date differences for US13 """

    conversion = {'days':1,'months':30.4,'years':365.25}
    difference = abs((dt1 - dt2).days)
    diff = difference/conversion[time_typ]
                
    return diff, time_typ


def us13(children, num_chil, fam_id, individuals):
    """ Birth dates of siblings should be more than 8 months apart or less than 2 days apart. """
    #Needs Revision

    bd_dict = dict()
    for i in range(num_chil):
        bd_dict[individuals[children[i]]['BIRT']] = children[i]
        bd_dict.sort

    test_next = True
    for bd, chil in bd_dict:
        if test_next:
            sib1 = bd
            chil1 = chil
            test_next = False
        else:
            sib2 = bd
            chil2 = chil
            diff, time_typ = get_dates_diff(sib1.date_time_obj, sib2.date_time_obj)
            if time_typ == 'years':
                continue
            elif time_typ == 'months' and diff < 8:
                print(f"US13: Error: Child '{chil1}' and Child '{chil2}' in family '{fam_id}' are born less than 8 months apart.")
            elif time_typ == 'days' and diff < 2:
                print(f"US13: Error: Child '{chil1}' and Child '{chil2}' in family '{fam_id}' are born less than 2 days apart.")
            else:
                continue
        
    return None


def us14(children, num_chil, fam_id, individuals):
    """ No more than five siblings should be born at the same time. """
    # Needs Revision
   
    def us32(birth_dt, fam_id, individuals):
        """ List all multiple births in a GEDCOM file. """

        print(f"US32: List: The following multiple births occured in family '{fam_id}' on date '{birth_dt}'")
        pt = PrettyTable(field_names=["ID", "Name"])
        for ind_id, ind in individuals.items:
            if ind['BIRT'] == birth_dt:
                pt.add_row(ind_id, ind['NAME'])
        print(pt)
            

        return None

    for i in range(num_chil):
        if i == 0:
            birthdates = [individuals[children[i]]['BIRT']]
        else:
            birthdates.append(individuals[children[i]]['BIRT'])
    
    birthdates_ord = birthdates.sort
    cnt = 0
    ind = 0
    next_test = True
    while next_test:
        if ind < num_chil:
            diff = Date.get_dates_difference(birthdates_ord[ind].date_time_obj, birthdates_ord[ind+1].date_time_obj)
            ind+=1
            if diff == 0:
                date_chk = birthdates_ord[ind].date_time_obj
                while diff == 0 and ind < num_chil:
                    diff = Date.get_dates_difference(birthdates_ord[ind].date_time_obj, date_chk)
                    us32(date_chk, fam_id)
                    cnt+=1
                    ind+=1
                if cnt > 5:
                    print(f"US14: Error: More than five children born on date '{date_chk}' in family '{fam_id}'")
        else:
            next_test = False

    return None


def us15(children, num_chil, fam_id):
    """ There should be fewer than 15 siblings in a family. """

    if num_chil >= 15:
        print(f"US15: Error: No more than fourteen children should be born in each family.  '{num_chil}' children born in family '{fam_id}'")
    
    return None


def us17(children, husband_id, wife_id):
    """ Parents should not marry any of their children. """
    # Needs revision

    if wife_id in children:
        print(f"US17: Error: Ew! Parents should not marry children. 100% Judgement. Seek help.")
    if husband_id in children:
        print(f"US17: Error: Ew! Parents should not marry children. 1005 Judgement. Seek help.")
    
    return None


def us18(husband_id, wife_id, individuals, families):
    """ Siblings should not marry one another. """
    # Needs revision

    for ind_id, ind in individuals.items(): # each ind is dict with the attributes of the individual
        if ind_id == wife_id:
            family_id = ind['FAMC']
            children = families[family_id]['CHIL']
            if husband_id in children:
                print(f"US18: Error: Ew! Siblings should not marry. 100% Judgement. Seek help.")
        elif ind_id == husband_id:
            family_id = ind['FAMC']
            children = families[family_id]['CHIL']
            if wife_id in children:
                print(f"US18: Error: Ew! Siblings should not marry. 100% Judgement. Seek help.")
    
    return None
            
    
def us28(children, num_chil, fam_id, individuals):
    """ List siblings in families by decreasing age, i.e. oldest siblings first. """
    # Needs Revision: import from gedcom_file_parser and use print_individuals_pretty_table function?

    order = list()
    for i in range(num_chil):
        if Date.get_dates_difference(individuals[children[i]]['BIRT'], individuals[children[i+1]]['BIRT'])<0:
            if len(order) == 0:
                order[i] = children[i]
                order[i+1] = children[i+1]
            else:
                cnt = len(order)
                for n in range(cnt):
                    if Date.get_dates_difference(individuals[children[i+1]]['BIRT'], individuals[order[n]]['BIRT'])<0:
                        order.insert(n, children[i])
                    elif Date.get_dates_difference(individuals[children[i+1]]['BIRT'],individuals[order[n]]['BIRT'])>0:
                        if n != (cnt-1):
                            continue
                        else:
                            order.append(n, children[i])
        elif Date.get_dates_difference(individuals[children[i]]['BIRT'], individuals[children[i+1]]['BIRT'])>0:
            if len(order) == 0:
                order[i] = children[i+1]
                order[i+1] = children [i]
            else:
                cnt = len(order)
                for n in range(len(order)):
                    if Date.get_dates_difference(individuals[children[i+1]]['BIRT'], individuals[order[n]]['BIRT'])<0:
                        order.insert(n, children[i])
                    elif Date.get_dates_difference(individuals[children[i+1]]['BIRT'], individuals[order[n]]['BIRT'])>0:
                        if n != (cnt-1):
                            continue
                        else:
                            order.append(n, children[i])
                        
    print(f"US33: List: Eldest to youngest children in family '{fam_id}'.")
    pt = PrettyTable(field_names=["ID", "Name"])
    for ord in range(num_chil + 1):
        pt.add_row(individuals[order[ord]], individuals[order[ord]]['NAME'])
    print(pt)

    return None


def us33(children, num_chil, fam_id, individuals):
    """ List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file. """
    # Needs Revision: import from gedcom_file_parser and use print_individuals_pretty_table function?

    orphan_rec = dict()
    for i in range(num_chil):
        if individuals[children[i]]['AGE'] != 'NA' and individuals[children[i]]['AGE'] < 18:
            orphan_rec[children[i]] = individuals[children[i]]
    print(f"US33: List: These children in family '{fam_id}' are orphans.")
    pt = PrettyTable(field_names=["ID", "Name"])
    for orphan_id, orphans in orphan_rec.items:
        pt.add_row(orphan_id, orphans[orphan_id]['NAME'])
    print(pt)


    return None


def get_child_block(individuals, families):
    """ Get the children. """
    
    for fam_id, fam in families.items():  # each fam is dict with the attributes of the family
        if fam['CHIL'] == 'NA':
            continue
        else:
            children = fam['CHIL']
            husband_id = fam['HUSB']
            wife_id = fam['WIFE']
            num_chil = len(children)
            if num_chil == 0:
                continue
            else:  
                if num_chil > 1:              
                    us13(children, num_chil, fam_id, individuals)
                    us14(children, num_chil, fam_id, individuals)
                    us15(children, num_chil, fam_id)
                    us17(children, husband_id, wife_id)
                    us18(husband_id, wife_id, individuals, families)
                    us28(children, num_chil, fam_id, individuals)
                if individuals[fam['HUSB']]['DEAT'] != 'NA' and individuals[fam['WIFE']]['DEAT'] != 'NA':
                    us33(children, num_chil, fam_id, individuals)
    
    return None



    