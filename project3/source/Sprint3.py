#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : Sprint 2
#Author            : Anthem Rukiya J. Wingate, Fran Sabetpour
#Date created      : 07.07.2019
#Purpose           : User story Implementation of US13, US14, US15, US17, US18, US28, US32, US33
#Revision History  : Version 1.0

# Notes:  Block implementation of user stories involving spouses and children

# Sprint 3:  Child Block
# US34:  List all couples who were married when the older spouse was more than twice as old as the younger spouse
# US35:  List all people in a GEDCOM file who were born in the last 30 days.
# US36:  List all people in a GEDCOM file who died in the last 30 days.
# US37:  List all living spouses and descendants of people in a GEDCOM file who died in the last 30 days

import datetime
from util_date import Date
from Sprint2 import get_dates_diff
from prettytable import PrettyTable
from collections import defaultdict


def us34(individuals, families):
    """ List all couples who were married when the older spouse was more than twice as old as the younger spouse. """
    
    husb_bd, wife_bd, marr_dt = None, None, None
    for fam_id, fam in families.items():
        if fam['HUSB'] != 'NA' and Date.is_valid_date(individuals[fam['HUSB']]['BIRT'].date_time_obj):
            husb_id = fam['HUSB']
            husb_bd = individuals[husb_id]['BIRT'].date_time_obj
        if fam['WIFE'] != 'NA' and Date.is_valid_date(individuals[fam['WIFE']]['BIRT'].date_time_obj):
            wife_id = fam['WIFE']
            wife_bd = individuals[wife_id]['BIRT'].date_time_obj
        if fam['MARR'] != 'NA' and Date.is_valid_date(fam['MARR'].date_time_obj):
            marr_dt = fam['MARR'].date_time_obj
        check = [husb_bd, wife_bd, marr_dt]
        if None not in check:
            if Date.get_dates_difference(husb_bd, marr_dt) > (2 * Date.get_dates_difference(wife_bd, marr_dt)):
                print(f"US34: Husband '{husb_id}' was more than twice as old as wife '{wife_id}' in family '{fam_id}' on marriage date '{marr_dt}'.")
            elif Date.get_dates_difference(wife_bd, marr_dt) > (2 * Date.get_dates_difference(husb_bd, marr_dt)):
                print(f"US34: Wife '{wife_id}' was more than twice as old as wife '{husb_id}' in family '{fam_id}' on marriage date '{marr_dt}'.")
        
    return None


def us35(individuals):
    """ List all people in a GEDCOM file who were born in the last 30 days. """
    
    print('US35: List:  The following people were born within the last 30 days')
    pt = PrettyTable(field_names=["ID", "Name", "Date of Birth"])
    for ind_id, ind in individuals.items():
        if Date.is_valid_date(ind['BIRT'].date_time_obj):
            diff, time_typ = get_dates_diff(ind['BIRT'].date_time_obj)
            if time_typ == 'days' and diff <= 30:
                recent_births = [ind_id, ind['NAME'], (ind['BIRT'].date_time_obj).strftime('%d %b %Y')]
                pt.add_row(recent_births)

    print(pt)

    return None

def us36(individuals, families):
    """ List all people in a GEDCOM file who died in the last 30 days. """

    def us37(ind_id, individuals, families):
        """ List all living spouses and descendants of people in a GEDCOM file who died in the last 30 days. """
       
        def get_descendants(ind_id, individuals, families):
            """ return a set of individual ids of all descendants of ind_id """

            descendants = list()

            if individuals[ind_id]['FAMS'] != 'NA' and families[fam_id]['CHIL'] != 'NA':

                for child in families[fam_id]['CHIL']:
                    desc =[child]
                    descendants.extend(desc)  # this child is a descendant
                    descendants.extend(get_descendants(child, individuals, families))  # add all of the children of child to the list as well
                
                return descendants
            else:
                return []
            # End get_descendants


        print(f"US37: List:  The following people are living spouses and descendents of '{individuals[ind_id]['NAME']}' who died within the last 30 days")
        pt = PrettyTable(field_names=["ID", "Name", "Relation"])
        
        if individuals[ind_id]['FAMS'] != 'NA':
            fam_id = individuals[ind_id]['FAMS']
            if families[fam_id]['WIFE'] == ind_id:
                if families[fam_id]['HUSB'] != 'NA':
                    relation = 'Husband'
                    recent_survivor = [families[fam_id]['HUSB'], families[fam_id]['HNAME'], relation]
                    pt.add_row(recent_survivor)
            elif families[fam_id]['HUSB'] == ind_id:
                if families[fam_id]['WIFE'] != 'NA':
                    relation = 'Wife'
                    recent_survivor = [families[fam_id]['WIFE'], families[fam_id]['WNAME'], relation]
                    pt.add_row(recent_survivor)

        descendants = get_descendants(ind_id, individuals, families)
        if  descendants is not []:
            len_desc = len(descendants)
            for i in range(len_desc):
                child = descendants[i]
                recent_survivor = [child, individuals[child]['NAME'], 'Descendant']
                pt.add_row(recent_survivor)
        print(pt)
        # End US37

    pt = PrettyTable(field_names=["ID", "Name", "Date of Death"])
    for ind_id, ind in individuals.items():
        if Date.is_valid_date(ind['DEAT'].date_time_obj):
            diff, time_typ = get_dates_diff(ind['DEAT'].date_time_obj)
            if time_typ == 'days' and diff <= 30:
                us37(ind_id, individuals, families)
                recent_deaths = [ind_id, ind['NAME'], (ind['DEAT'].date_time_obj).strftime('%d %b %Y')]
                pt.add_row(recent_deaths)

    print('US36: List:  The following people died within the last 30 days')
    print(pt)

    return None


def get_recent_block(individuals, families):
    """ Get dates within 30 days. """

    us34(individuals, families)
    us35(individuals)
    us36(individuals, families) # Calls US37

    return None