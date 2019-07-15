#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : Sprint 2
#Author            : Anthem Rukiya J. Wingate, Fran Sabetpour
#Date created      : 07.07.2019
#Purpose           : User story Implementation of US13, US14, US15, US17, US18, US28, US32, US33
#Revision History  : Version 1.0

# Notes:  Block implementation of user stories involving age comparisons and recent events

# Sprint 3:  Child Block
# US34:  List all couples who were married when the older spouse was more than twice as old as the younger spouse
# US35:  List all people in a GEDCOM file who were born in the last 30 days.
# US36:  List all people in a GEDCOM file who died in the last 30 days.
# US37:  List all living spouses and descendants of people in a GEDCOM file who died in the last 30 days

import datetime
from prettytable import PrettyTable
from collections import defaultdict
from util_date import Date
from Sprint2 import get_dates_diff

#
# Begin Sprint 3 Recents Block
#

def us34(individuals, families, fam_id='', test=False):
    """ List all couples who were married when the older spouse was more than twice as old as the younger spouse. """
    
    if test == True:
        errors = list()
        error1, error2 = False, False
        if families[fam_id]['HUSB'] != 'NA' and Date.is_valid_date(individuals[families[fam_id]['HUSB']]['BIRT'].date_time_obj):
            husb_id = families[fam_id]['HUSB']
            husb_bd = individuals[husb_id]['BIRT'].date_time_obj
        if families[fam_id]['WIFE'] != 'NA' and Date.is_valid_date(individuals[families[fam_id]['WIFE']]['BIRT'].date_time_obj):
            wife_id = families[fam_id]['WIFE']
            wife_bd = individuals[wife_id]['BIRT'].date_time_obj
        if families[fam_id]['MARR'] != 'NA' and Date.is_valid_date(families[fam_id]['MARR'].date_time_obj):
            marr_dt = families[fam_id]['MARR'].date_time_obj
        check = [husb_bd, wife_bd, marr_dt]
        if None not in check:
            if Date.get_dates_difference(husb_bd, marr_dt) > (2 * Date.get_dates_difference(wife_bd, marr_dt)):
                error1 = True
            elif Date.get_dates_difference(wife_bd, marr_dt) > (2 * Date.get_dates_difference(husb_bd, marr_dt)):
                error2 = True
        errors = [error1, error2]
        return errors
    else:
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


def us35(individuals, test=False):
    """ List all people in a GEDCOM file who were born in the last 30 days. """
    
    print('US35: List:  The following people were born within the last 30 days')
    pt = PrettyTable(field_names=["ID", "Name", "Date of Birth"])
    for ind_id, ind in individuals.items():
        if Date.is_valid_date(ind['BIRT'].date_time_obj):
            diff, time_typ = get_dates_diff(ind['BIRT'].date_time_obj)
            if time_typ == 'days' and diff <= 30:
                recent_births = [ind_id, ind['NAME'], (ind['BIRT'].date_time_obj).strftime('%d %b %Y')]
                pt.add_row(recent_births)
    
    if test == True:
        return(str(pt))
    else:
        print(pt)
        return None


def us36(individuals, families):
    """ List all people in a GEDCOM file who died in the last 30 days. """

    def us37(ind_id, individuals, families):
        """ List all living spouses and descendants of people in a GEDCOM file who died in the last 30 days. """
       
        def anthem_get_descendants(ind_id, individuals, families):
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

        def get_descendants(ind_id, individuals, families, so_far=None):
            """ return a set of individual ids of all descendants of ind_id """
            if so_far is None:
                descendants = set()
            else:
                descendants = so_far  # the descendants we've already checked
                
            if individuals[ind_id]['FAMS'] != 'NA':
                # get the descendants for all of ind_id's children
                fam_id = individuals[ind_id]['FAMS']
                if families[fam_id]['CHIL'] != 'NA':
                    child_in_desc = False
                    for child in families[fam_id]['CHIL']:
                        if child not in descendants:
                            descendants.add(child)  # this child is a descendant
                            descendants.update(get_descendants(child, individuals, families, descendants))  # add all of the children of child to the set as well
                        else:
                            child_in_desc = True
                    if child_in_desc == True:
                        print(f"WARNING: {ind_id} is a descendant of him/her self in {fam_id}")  
            return descendants

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
        if len(descendants) > 0:
            for child in descendants:
                recent_survivor = [child, individuals[child]['NAME'], 'Descendant']
                pt.add_row(recent_survivor)
        print(pt)
        # End US37

    pt = PrettyTable(field_names=["ID", "Name", "Date of Death"])
    for ind_id, ind in individuals.items():
        if ind['DEAT'] != 'NA' and Date.is_valid_date(ind['DEAT'].date_time_obj):

            diff, time_typ = get_dates_diff(ind['DEAT'].date_time_obj)
            if time_typ == 'days' and diff <= 30:
                us37(ind_id, individuals, families)
                recent_deaths = [ind_id, ind['NAME'], (ind['DEAT'].date_time_obj).strftime('%d %b %Y')]
                pt.add_row(recent_deaths)

    print('US36: List:  The following people died within the last 30 days')
    print(pt)

    return None


def get_recent_block(individuals, families):
    """ Get age comparison or dates within 30 days. """

    us34(individuals, families)
    us35(individuals)
    us36(individuals, families)

    return None