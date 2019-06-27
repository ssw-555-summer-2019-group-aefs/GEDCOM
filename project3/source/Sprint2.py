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
from gedcom_file_parser import print_individuals_pretty_table


#
# Begin Sprint 2 Child Block
#


def us13(children, num_chil, fam_id, individuals):
    """ Birth dates of siblings should be more than 8 months apart or less than 2 days apart. """
    
    def get_dates_diff(dt1, dt2=None):
        """ Gets date differences for US13 """
        
        conversion = {'days':1,'months':30.4,'years':365.25}
        difference = abs((dt1 - dt2).days)
        
        if difference >= 365.25:
            time_typ = 'years'
            diff = difference/conversion[time_typ]
        elif difference >= 30.4 and difference < 365.25:
            time_typ = 'months'
            diff = difference/conversion[time_typ]
        elif difference >= 1 and difference < 30.4:
            time_typ = 'days'
            diff = difference/conversion[time_typ]
        
        return diff, time_typ

    for i in range(num_chil):
        sib1 = individuals[children[i]]['BIRT']
        sib2 = individuals[children[i+1]]['BIRT']
        diff, time_typ = get_dates_diff(sib1.date_time_obj, sib2.date_time_obj)
        if time_typ == 'years':
            continue
        elif time_typ == 'months' and diff < 8:
            print(f"US13: Error: Child '{children[i]}' and Child '{children[i+1]}' in family '{fam_id}' are born less than 8 months apart.")
        elif time_typ == 'days' and diff < 2:
            print(f"US13: Error: Child '{children[i]}' and Child '{children[i+1]}' in family '{fam_id}' are born less than 2 days apart.")
        else:
            continue
    
    return None


def us14(children, num_chil, fam_id, individuals):
    """ No more than five siblings should be born at the same time. """
    #note:  Current version of this code does not take into account multiple occurences of twins or triplets or other multiples in a single family

    num_mult = 0
    mult_rec = dict()
    for i in range(num_chil):
        sib1 = individuals[children[i]]['BIRT']
        sib2 = individuals[children[i+1]]['BIRT']
        diff = Date.get_dates_difference(sib1, sib2)
        if diff == 0:
            num_mult += 1
            mult_rec[children[i]]= individuals[children[i]]
    if num_mult > 1:
        us32(mult_rec, fam_id)
    if num_mult > 5: 
        print(f"US14: Error: More than five children born on the same date in family '{fam_id}'")
        
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
    #Needs Revision

    order = list()
    child_ord = OrderedDict()
    for i in range(num_chil + 1):
        if Date.get_dates_difference(individuals[children[i]]['BIRT'],individuals[children[i+1]]['BIRT'])<0:
            if len(order) == 0:
                order[i] = children[i]
                order[i+1] = children[i+1]
            else:
                for n in range(len(order) + 1):
                    if Date.get_dates_difference(individuals[children[i]]['BIRT'],individuals[children[n]]['BIRT'])<0:
                        order.insert(n, children[i])
        elif Date.get_dates_difference(individuals[children[i]]['BIRT'],individuals[children[i+1]]['BIRT'])>0:
            if len(order) == 0:
                order[i] = children[i+1]
                order[i+1] = children[i]
            else:
                for n in range(len(order) + 1):
                    if Date.get_dates_difference(individuals[children[i]]['BIRT'],individuals[children[n]]['BIRT'])>0:
                        continue
                    else:
                        order.insert(n, children[i])
    
    for ord in range(num_chil + 1):
        child_ord[order[ord]] = individuals[order[ord]]
    print(f"US33: List: Eldest to youngest children in family '{fam_id}'.")
    print_individuals_pretty_table(child_ord)

    return None


def us32(mult_rec, fam_id):
    """ List all multiple births in a GEDCOM file. """
    print(f"US32: List: The following multiple births occured in family '{fam_id}'")
    print_individuals_pretty_table(mult_rec)

    return None

def us33(children, num_chil, fam_id, individuals):
    """ List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file. """
    orphan_rec = dict()
    for i in range(num_chil+1):
        orphan_rec[children[i]]= individuals[children[i]]
    print(f"US33: List: The children in family '{fam_id}' are orphans.")
    print_individuals_pretty_table(orphan_rec)

    return None


def get_child_block(individuals, families):
   """ Get the individiual record of each child. """
   
   for fam in families.values():  # each fam is dict with the attributes of the family
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
                us13(children, num_chil, fam['FAM'], individuals)
                us14(children, num_chil, fam['FAM'], individuals)
                us15(children, num_chil, fam['FAM'])
                us17(children, husband_id, wife_id)
                US18(husband_id, wife_id, individuals, families)
                us28(children, num_chil, fam['FAM'], individuals)
                if Date.get_dates_difference(individuals[fam['HUSB']]['DEAT'])!='NA' and Date.get_dates_difference(individuals[fam['WIFE']]['DEAT'])!='NA':
                    us33(children, num_chil, fam['FAM'], individuals)
                for i in range(num_chil):
                    child_record = individuals[children[i]]

    