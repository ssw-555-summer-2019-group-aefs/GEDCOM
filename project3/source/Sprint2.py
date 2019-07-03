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
from collections import OrderedDict, defaultdict
from prettytable import PrettyTable

#from gedcom_file_parser import print_individuals_pretty_table


#
# Begin Sprint 2 Child Block
#

def get_dates_diff(dt1, dt2=None):
    """ Gets date differences for US13 """

    conversion = {'days':1,'months':30.4,'years':365.25}
    difference = abs((dt1 - dt2).days)
    if difference >= 365.25:
        time_typ = 'years'
    elif difference >= 30.4 and difference < 365.25:
        time_typ = 'months'
    elif difference >= 0 and difference <30.4:
        time_typ = 'days'

    return difference/conversion[time_typ], time_typ


def us13(children, num_chil, fam_id, individuals):
    """ Birth dates of siblings should be more than 8 months apart or less than 2 days apart. """
    #Needs Revision

    bd_dict = defaultdict(list)
    for i in range(num_chil):
        #dt_str = (individuals[children[i]]['BIRT'].date_time_obj).strftime('%d %b %Y')
        bd_key = individuals[children[i]]['BIRT'].date_time_obj
        if bd_key not in bd_dict:
            bd_dict[bd_key] = [children[i]]
        else:
            bd_dict[bd_key].append(children[i])
    
    test_next = True
    for bd_child, child in sorted(bd_dict.items(), reverse=True):
        if len(bd_dict[bd_child])==1:
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
                    print(f"US13: Error: Child '{child1}' and Child '{child2}' in family '{fam_id}' are born less than 8 months apart.")
                elif time_typ == 'days' and diff < 2:
                    print(f"US13: Error: Child '{child1}' and Child '{child2}' in family '{fam_id}' are born less than 2 days apart.")
                test_next = True

        elif len(bd_dict[bd_child]) >1:
            us14(len(bd_dict[bd_child]), bd_child, bd_dict[bd_child], fam_id, individuals)
            test_next = True
        
    return None


def us14(num_chil, birthdate, children, fam_id, individuals):
    """ No more than five siblings should be born at the same time. """
    # Needs Revision
   
    def us32(birthdate, fam_id, children, individuals):
        """ List all multiple births in a GEDCOM file. """

        print(f"US32: List: The following '{num_chil}' births occured in family '{fam_id}' on date '{birthdate.strftime('%d %b %Y')}'")
        pt = PrettyTable(field_names=["ID", "Name"])
        for ind_id, ind in individuals.items:
            if ind_id in children:
                pt.add_row(ind_id, ind['NAME'])
        print(pt)

        return 
    
    if num_chil > 5:
        print(f"US14: Error: More than five children born on date '{birthdate.strftime('%d %b %Y')}' in family '{fam_id}'")
    us32(birthdate, fam_id, children, individuals)

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
        if ind['FAMC'] != 'NA' and families[ind['FAMC']]['CHIL']!= 'NA':
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
    for i in range(num_chil-1):
        if Date.get_dates_difference(individuals[children[i]]['BIRT'].date_time_obj, individuals[children[i+1]]['BIRT'].date_time_obj)<=0:
            if len(order) == 0:
                order.append(children[i])
                order.append(children[i+1])
            else:
                cnt = len(order)
                for n in range(cnt):
                    if Date.get_dates_difference(individuals[children[i+1]]['BIRT'].date_time_obj, individuals[order[n]]['BIRT'].date_time_obj)<0:
                        order.insert(n, children[i+1])
                    elif Date.get_dates_difference(individuals[children[i+1]]['BIRT'].date_time_obj, individuals[order[n]]['BIRT'].date_time_obj)>0:
                        if n != (cnt-1):
                            continue
                        else:
                            order.append(children[i+1])
        elif Date.get_dates_difference(individuals[children[i]]['BIRT'].date_time_obj, individuals[children[i+1]]['BIRT'].date_time_obj)>0:
            if len(order) == 0:
                order.append(children[i+1])
                order.append(children [i])
            else:
                cnt = len(order)
                for n in range(len(order)):
                    if Date.get_dates_difference(individuals[children[i+1]]['BIRT'].date_time_obj, individuals[order[n]]['BIRT'].date_time_obj)<0:
                        order.insert(n, children[i])
                    elif Date.get_dates_difference(individuals[children[i+1]]['BIRT'].date_time_obj, individuals[order[n]]['BIRT'].date_time_obj)>0:
                        if n != (cnt-1):
                            continue
                        else:
                            order.append(n, children[i])
                        
    print(f"US33: List: Eldest to youngest children in family '{fam_id}'.")
   
    for ord in range(num_chil):
        print(individuals[order[ord]]['NAME'], order[ord])

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
                    us13(children, num_chil, fam_id, individuals) #Calls US14 and US32
                    us15(children, num_chil, fam_id)
                    us17(children, husband_id, wife_id)
                    us18(husband_id, wife_id, individuals, families)
                    us28(children, num_chil, fam_id, individuals)
                if individuals[fam['HUSB']]['DEAT'] != 'NA' and individuals[fam['WIFE']]['DEAT'] != 'NA':
                    us33(children, num_chil, fam_id, individuals)
    
    return None



    