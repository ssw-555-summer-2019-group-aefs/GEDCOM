#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : Saransh_Sprint3.py
#Author            : Saransh Ahlawat
#Date created      : 07.17.2019
#Purpose           : User story Implementation of 
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
import json


def us31(individuals, families, print_errors = True):
    """ List all living people over 30 who have never been married """
    result = list()

    for individual_key in individuals:
        individual_obj = individuals.get(individual_key)
        if individual_obj != None:
            if individual_obj.get("AGE") > 30 and (individual_obj.get("FAMS") == None or individual_obj.get("FAMS") == "NA"):
                if print_errors:
                    print(f'US31: Individual {individual_key} is more than 30 years old and is not married.')
                result.append(f'US31: Individual {individual_key} is more than 30 years old and is not married.')

    return result


def us21(individuals, families, print_errors = True):
    """ Husband in family should be male and wife in family should be female """
    error_result = list()

    for family_key in families:
        family_obj = families.get(family_key)
        if family_obj != None:
            husband_id = family_obj.get("HUSB")
            husband_individual_obj = individuals.get(husband_id)
            if husband_individual_obj.get("SEX") != "M":
                if print_errors:
                    print(f'US21: Error: Family {family_key} does not have a male husband.')
                error_result.append(f'US21: Error: Family {family_key} does not have a male husband.')

            wife_id = family_obj.get("WIFE")
            wife_individual_obj = individuals.get(wife_id)
            if wife_individual_obj.get("SEX") != "F":
                if print_errors:
                    print(f'US21: Error: Family {family_key} does not have a female wife.')
                error_result.append(f'US21: Error: Family {family_key} does not have a female wife.')

    return error_result
            
