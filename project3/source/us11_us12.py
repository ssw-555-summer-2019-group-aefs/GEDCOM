"""
Author: Erik Bornako
Date: 2 July 2019
Purpose: User Stories 11 and 12
"""

from util_date import Date
import io
import sys
import unittest
import datetime
import re
from collections import namedtuple

# User Story 11
def check_bigamy(individual_info_dict, family_info_dict):
    for individual_id, individual_info in individual_info_dict.items():
        id = individual_id
        name_place = individual_info.get('NAME')
        name = re.sub('/', '', name_place)
        marriage_count = 0
        start_dates = []
        end_dates = []
        for family_id, family_info in family_info_dict.items():
            
            wife_id = family_info.get('WIFE')
            husband_id = family_info.get('HUSB')
            
            if id == wife_id or id == husband_id:
                if id == wife_id:
                    spouse_death = individual_info_dict[husband_id].get('DEAT')
                    # print(family_info.get('MARR'))
                    # print(spouse_death)
                elif id == husband_id:
                    spouse_death = individual_info_dict[wife_id].get('DEAT')
                    # print(family_info.get('MARR'))
                    # print(spouse_death)
                Range = namedtuple('Range', ['start', 'end'])
                if family_info.get('DIV') not in [None, 'NA']:
                    length_of_marriage = Range(start=family_info.get('MARR'), end=family_info.get('DIV'))
                elif spouse_death not in [None, 'NA']:
                    length_of_marriage = Range(start=family_info.get('MARR'), end=spouse_death)
                else:
                    length_of_marriage = Range(start=family_info.get('MARR'), end=Date(datetime.datetime.today().strftime('%d %b %Y')))
                
                if family_info.get('MARR') not in [None, 'NA']:
                    start_dates.append(length_of_marriage.start.date_time_obj)
                    end_dates.append(length_of_marriage.end.date_time_obj)
                marriage_count += 1
        more_than_one_marriage_at_given_time = False


        if marriage_count > 1:
            latest_start = max(start_dates)
            earliest_end = min(end_dates)
            if type(latest_start) is not str and latest_start != None:
                if type(earliest_end) is not str and earliest_end != None:
                    delta = (earliest_end - latest_start).days
                    overlap = max(0, delta)
                    if overlap > 0:
                        more_than_one_marriage_at_given_time = True
        
        if more_than_one_marriage_at_given_time == True:
            print('US11: Error: {}: Bigamy detected: {} married to multiple spouses at the same time'.format(id, name))

# User Story 12
def check_parents_not_too_old(individual_info_dict, family_info_dict):
    for family_id, family_info in family_info_dict.items():
        wife_id = family_info.get('WIFE')
        husband_id = family_info.get('HUSB')
        children = family_info.get('CHIL')
        husb_dict = individual_info_dict.get(husband_id)
        wife_dict = individual_info_dict.get(wife_id)
        husb_birth_date = Date(str(husb_dict.get('BIRT')))
        wife_birth_date = Date(str(wife_dict.get('BIRT')))
        parents_too_old = False
        if children not in [None, 'NA']:
            for child in children:
                child_dict = individual_info_dict.get(child)
                birth_date = Date(str(child_dict.get('BIRT')))
                
                too_old_age_difference = 65
                if type(husb_birth_date) is not str and husb_birth_date != None and type(husb_birth_date.date_time_obj) is not str and type(husb_birth_date.date_time_obj) is not str:
                    if type(wife_birth_date) is not str and wife_birth_date != None and type(wife_birth_date.date_time_obj) is not str and type(wife_birth_date.date_time_obj) is not str:
                        if type(birth_date) is not str and birth_date != None and type(birth_date.date_time_obj) is not str and type(birth_date.date_time_obj) is not str:
                            if Date.get_dates_difference(husb_birth_date.date_time_obj, birth_date.date_time_obj) > too_old_age_difference or Date.get_dates_difference(wife_birth_date.date_time_obj, birth_date.date_time_obj) > too_old_age_difference:
                                parents_too_old = True
                    
        if parents_too_old == True:
            print('US12:  Error: {}: Parents are too old: Parent(s) were greater than 65 years old when child was born'.format(family_id))