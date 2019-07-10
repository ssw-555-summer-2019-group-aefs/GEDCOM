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
       
        print('US37: List:  The following people are living spouses and descendents of people who died within the last 30 days')
        pt = PrettyTable(field_names=["ID", "Name", "Relation"])
        if individuals[ind_id]['FAMS'] != 'NA':
            fam_id = individuals[ind_id]['FAMS']
            if families[fam_id]['WIFE'] == individuals[ind_id]:
                if families[fam_id]['HUSB'] != 'NA':
                    relation = 'Husband'
                    recent_survivor = [families[fam_id]['HUSB'], families[fam_id]['HNAME'], relation]
                    pt.add_row(recent_survivor)
            elif families[fam_id]['HUSB'] == individuals[ind_id]:
                if families[fam_id]['WIFE'] != 'NA':
                    relation = 'Wife'
                    recent_survivor = [families[fam_id]['WIFE'], families[fam_id]['WNAME'], relation]
                    pt.add_row(recent_survivor)

            # Each While loop collects a list of children that serve as the value for a dictionary.  The key for that value is the generation (child, grandchild, etc.)
            # A list of all related family ids is also appended each loop
            # Step 1:  At generation zero append children list and add family ids to family id list for every FAMS != NA
            # Step 2: A generation 1, add children from each of the families in the family id list, use cnt variable to increment through family id list with each while loop. 
            # When all generation 1 children are checked, increment generation.

            next_fam_id = fam_id
            fam_id_list = list()
            chil_id_list = defaultdict(list)
            cnt = 0
            generation = 0
            survivors = True
            while survivors:
                if families[next_fam_id]['CHIL'] != 'NA':
                    chil_id_list[generation].append(families[next_fam_id]['CHIL'])
                    chil_list_len = len(chil_id_list[generation])
                    for i in range(chil_list_len):
                        chk_fam = chil_id_list[generation][i]
                        if individuals[chk_fam]['FAMS'] != 'NA':
                            fam_id_list.append(individuals[chk_fam]['FAMS'])
                        if i == chil_list_len - 1:    
                            generation += 1
                    next_fam_id = fam_id_list[cnt]
                    cnt += 1
                else:
                    curr_tot_fam = len(fam_id_list)
                    if cnt < curr_tot_fam:
                        next_fam_id = fam_id_list[cnt]
                        cnt += 1
                        survivors = True
                    else:
                        survivors = False

            
            for n in range(generation + 1):
                if n == 0:
                    relation = 'Child'
                elif n == 1:
                    relation = 'Grandchild'
                elif n>1:
                    relation = f"'{n}' x Great Grandchild"
                
                children = chil_id_list[n]
                num_chil = len(children)
                for y in range(num_chil):
                    recent_survivor = [children[y], individuals[children[y]]['NAME'], relation]
                    pt.add_row(recent_survivor)
            
            print(pt)

            return None
                    

    print('US36: List:  The following people died within the last 30 days')
    pt = PrettyTable(field_names=["ID", "Name", "Date of Birth"])
    for ind_id, ind in individuals.items():
        if ind['DEAT'] != 'NA' and Date.is_valid_date(ind['DEAT'].date_time_obj):
            us37(ind_id, individuals, families)
            diff, time_typ = get_dates_diff(ind['DEAT'].date_time_obj)
            if time_typ == 'days' and diff <= 30:
                recent_deaths = [ind_id, ind['NAME'], (ind['DEAT'].date_time_obj).strftime('%d %b %Y')]
                pt.add_row(recent_deaths)
    
    print(pt)

    return None


def get_recent_block(individuals, families):
    """ Get dates within 30 days. """

    us34(individuals, families)
    us35(individuals)
    us36(individuals, families)

    return None