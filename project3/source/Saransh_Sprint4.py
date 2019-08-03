#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : Saransh_Sprint4.py
#Author            : Saransh Ahlawat
#Date created      : 08.02.2019
#Purpose           : User story Implementation of US16, US26 
#Revision History  : Version 1.0


import datetime
from util_date import Date
from collections import OrderedDict, defaultdict
from prettytable import PrettyTable


def us26(individuals, families, print_errors = True):
    """ List all living people over 30 who have never been married """

    print(individuals)
    print(families)

    # result = list()
    # pt = PrettyTable(field_names = ["ID", "Name", "Age"])

    # for individual_key in individuals:
    #     individual_obj = individuals.get(individual_key)
    #     if individual_obj != None:
    #         if individual_obj.get("AGE") > 30 and (individual_obj.get("FAMS") == None or individual_obj.get("FAMS") == "NA"):
                
    #             individual_info = [individual_key, individual_obj.get("NAME"), individual_obj.get("AGE")]
    #             pt.add_row(individual_info)
    #             result.append(individual_key)

    # if len(result) > 0 and print_errors:
    #     print(f'US31: List: Individuals more than 30 years old and not married.')
    #     print(pt)

    # return result


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
            

if __name__ == '__main__':
    dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
    # print_pretty_table(f"{dir_path}/data/sprint3userstorytest.ged")
    individuals, families = ged