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


def us16(individuals, families):
    """ function to check if all male members of the family must have the same last name """

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
                            print(f"US16: Error: All males in family {family_key}, do not have same last name")
                            error_messages.append(f"US16: Error: All males in family {family_key}, do not have same last name")
                            break
    return error_messages


def us26(individuals, families):
    """ function to check the information in the individual
    and family records is consistent. """

    error_messages = []
    for individual_key in individuals:
        individual_obj = individuals.get(individual_key)
        if individual_obj.get("FAMS") != None and individual_obj.get("FAMS") != "NA":
            if families.get(individual_obj.get("FAMS")) == None:
                print(f"US26: Error: No entry for family id {individual_obj.get('FAMS')} available")
                error_messages.append(f"US26: Error: No entry for family id {individual_obj.get('FAMS')} available")
            elif (individual_key != (families.get(individual_obj.get("FAMS"))).get('HUSB')) and (individual_key != (families.get(individual_obj.get("FAMS"))).get('WIFE')):
                print(f"US26: Error: individual spouse with id {individual_key} not available in family {individual_obj.get('FAMS')}")
                error_messages.append(f"US26: Error: individual spouse with id {individual_key} not available in family {individual_obj.get('FAMS')}")

        if individual_obj.get("FAMC") != None and individual_obj.get("FAMC") != "NA":
            if families.get(individual_obj.get("FAMC")) == None:
                print(f"US26: Error: No entry for family id {individual_obj.get('FAMC')} available")
                error_messages.append(f"US26: Error: No entry for family id {individual_obj.get('FAMC')} available")
            elif individual_key not in families.get(individual_obj.get('FAMC')).get('CHIL'):
                print(f"US26: Error: individual child with id {individual_key} not available in family {individual_obj.get('FAMC')}")
                error_messages.append(f"US26: Error: individual child with id {individual_key} not available in family {individual_obj.get('FAMC')}")
    
    for family_key in families:
        family_obj = families.get(family_key)
        family_husband = family_obj.get("HUSB")
        family_wife = family_obj.get("WIFE")
        family_children = family_obj.get("CHIL")
        if family_husband != None and family_husband != "NA":
            if individuals.get(family_husband) == None:
                print(f"US26: Error: No entry for individual id {family_husband} available")
                error_messages.append(f"US26: Error: No entry for individual id {family_husband} available")
            elif individuals.get(family_husband).get('FAMS') != family_key:
                print(f"US26: Error: Husband in family {family_key} is not listed as spouse in individual record {family_husband}")
                error_messages.append(f"US26: Error: Husband in family {family_key} is not listed as spouse in individual record {family_husband}")

        if family_wife != None and family_wife != "NA":
            if individuals.get(family_wife) == None:
                print(f"US26: Error: No entry for individual id {family_wife} available")
                error_messages.append(f"US26: Error: No entry for individual id {family_wife} available")
            elif individuals.get(family_wife).get('FAMS') != family_key:
                print(f"US26: Error: Wife in family {family_key} is not listed as spouse in individual record {family_wife}")
                error_messages.append(f"US26: Error: Wife in family {family_key} is not listed as spouse in individual record {family_wife}")

        if family_children != None and family_children != "NA":
            for child in family_children:
                if individuals.get(child) == None:
                    print(f"US26: Error: No entry for individual id {child} available")
                    error_messages.append(f"US26: Error: No entry for individual id {child} available")
                elif individuals.get(child).get('FAMC') != family_key:
                    print(f"US26: Error: Child in family {family_key} is not listed as child of this family in individual record {child}")
                    error_messages.append(f"US26: Error: Child in family {family_key} is not listed as child of this family in individual record {child}")

    return error_messages
