"""
Author: Erik Bornako
Date: 21 June 2019
Purpose: User Stories 07 and 08 with unit tests
"""

from util_date import Date
import io
import sys
import unittest
import datetime

# User Story 07
def check_150_years_age(individual_info_dict):

    age_limit = 150

    # gets dates from individual info
    for individual_id, individual_info in individual_info_dict.items():
        id = individual_id
        birth_date = Date(str(individual_info.get("BIRT")))
        if individual_info.get("DEAT") not in [None, 'NA']:
            death_date = Date(str(individual_info.get("DEAT")))
        else:
            death_date = None
   
        # calculates age with the dates
        if death_date == None and birth_date != None:
            age = Date.get_dates_difference(birth_date.date_time_obj)
        else:
            if death_date != None and birth_date != None:
                age = Date.get_dates_difference(birth_date.date_time_obj, death_date.date_time_obj)

        # checks to see if age exceeds age limit and prints error
        if type(age) is not str and age > age_limit and death_date == None:
            print('ERROR: INDIVIDUAL: US07: {}: More than 150 years old - Birth date {}'.format(id, birth_date))
        elif type(age) is not str and age > age_limit and death_date != None:
            print('ERROR: INDIVIDUAL: US07: {}: More than 150 years old at death - Birth date {}: Death date {}'.format(id, birth_date, death_date))
# End of User Story 07

# User story 08
def check_birth_before_marriage_of_parents(family_info_dict, individual_info_dict):
   
    for family_id, family_info in family_info_dict.items():
        # gets marriage and divorce dates in family if they exist
        if family_info.get("MARR") not in [None, 'NA']:
            marriage_date = Date(str(family_info.get("MARR")))
        else:
            marriage_date = None
        if family_info.get("DIV") not in [None, 'NA']:
            divorce_date = Date(str(family_info.get("DIV")))
        else:
            divorce_date = None
       
        # obtains all childen in family
        children = family_info.get('CHIL')

        #if children exist, it gets the birth dates and compares it to the marriage/divorce dates, and prints error if marriage is before birth and/or birth is after divorce
        if children not in [None, 'NA']:
            for child in children:
                child_dict = individual_info_dict.get(child)
                birth_date = Date(str(child_dict.get('BIRT')))
                if type(marriage_date) is not str and marriage_date != None and type(marriage_date.date_time_obj) is not str and type(birth_date.date_time_obj) is not str:
                    if marriage_date not in [None, 'NA'] and marriage_date.date_time_obj < birth_date.date_time_obj:
                        print('ANOMOLY: FAMILY: US08: {}: Child {} born {} before marriage on {}'.format(family_id, child, birth_date, marriage_date))
                if type(divorce_date) is not str and divorce_date != None and type(divorce_date.date_time_obj) is not str and type(birth_date.date_time_obj) is not str:
                    if divorce_date not in [None, 'NA'] and birth_date.date_time_obj > divorce_date.date_time_obj:
                        print('ANOMOLY: FAMILY: US08: {}: Child {} born {} after divorce on {}'.format(family_id, child, birth_date, divorce_date))
# End of User Story 08