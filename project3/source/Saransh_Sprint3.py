#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : Saransh_Sprint3.py
#Author            : Saransh Ahlawat
#Date created      : 07.17.2019
#Purpose           : User story Implementation of 
#Revision History  : Version 1.0


import datetime
from util_date import Date
from collections import OrderedDict, defaultdict
from prettytable import PrettyTable


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
            
