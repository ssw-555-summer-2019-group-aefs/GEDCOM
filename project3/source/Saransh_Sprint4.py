# Project           : GEDCOM SSW 555 Summer 2019
# Program name      : Saransh_Sprint4.py
# Author            : Saransh Ahlawat
# Date created      : 08.02.2019
# Purpose           : User story Implementation of US16, US26
# Revision History  : Version 1.0

import datetime
from util_date import Date
import os
from collections import OrderedDict, defaultdict
from prettytable import PrettyTable
from gedcom_file_parser import gedcom_file_parser


def us16(individuals, families, print_errors=True):
    """ Husband in family should be male and wife in family should be female """

    individual_identifier = ["HUSB", "WIFE", "CHIL"]
    error_messages = []
    for family_key in families:
        unique_individuals = set()
        family_obj = families.get(family_key)
        for family_attribute_key in family_obj:
            if family_attribute_key in individual_identifier:
                if family_attribute_key == "CHIL":
                    for child in family_obj.get(family_attribute_key):
                        unique_individuals.add(child)
                else:
                    individual = family_obj.get(family_attribute_key)
                    unique_individuals.add(individual)
        family_last_name = None
        for unique_individual in unique_individuals:
            individual_obj = individuals.get(unique_individual)
            if individual_obj != None:
                if individual_obj.get("SEX") == "M":
                    if family_last_name == None:
                        individual_name = individual_obj.get("NAME")
                        family_last_name = individual_name.split("/")[1]
                    else:
                        individual_name = individual_obj.get("NAME")
                        individual_last_name = individual_name.split("/")[1]
                        if individual_last_name != family_last_name:
                            if print_errors:
                                print(f"US16: Error: All males in family {family_key}, do not have same last name")
                            error_messages.append(f"US16: Error: All males in family {family_key}, do not have same last name")
                            break
    return error_messages


def us26(individuals, families, print_errors=True):
    """ List all living people over 30 who have never been married """

    error_messages = []
    for individual_key in individuals:
        individual_obj = individuals.get(individual_key)
        if individual_obj.get("FAMS") != None:
            if families.get(individual_obj.get("FAMS")) == None:
                if print_errors:
                    print(f"US26: Error: No entry for family id {individual_obj.get('FAMS')} exsists")
                error_messages.append(f"US26: Error: No entry for family id {individual_obj.get('FAMS')} exsists")
        if individual_obj.get("FAMC") != None:
            if families.get(individual_obj.get("FAMC")) == None:
                if print_errors:
                    print(f"US26: Error: No entry for family id {individual_obj.get('FAMC')} exsists")
                error_messages.append(f"US26: Error: No entry for family id {individual_obj.get('FAMC')} exsists")
    return error_messages


if __name__ == '__main__':
    dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    individuals, families = gedcom_file_parser(f"{dir_path}/data/us26.ged")
    us26(individuals, families)
    individuals, families = gedcom_file_parser(f"{dir_path}/data/us16.ged")
    us16(individuals, families)
