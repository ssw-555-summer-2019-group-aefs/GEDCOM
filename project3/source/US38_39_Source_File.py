from prettytable import PrettyTable
import datetime
from util_date import Date

#US38
def list_upcoming_birthdays(individual_info_dict):
    """ Lists all birthdays within a month in a GEDCOM file. """
    
    upcoming_birthday_list = []
    today = datetime.date.today()
    for individual_id, individual_info in individual_info_dict.items():
        id = individual_id
        name = individual_info.get('NAME')
        birth_date = Date(str(individual_info.get("BIRT"))).date_time_obj
        if birth_date not in [None, 'NA', '']:
            this_year_birthday = datetime.date(today.year, birth_date.month, birth_date.day)
            difference = today - this_year_birthday
            if difference > datetime.timedelta(0) and difference < datetime.timedelta(30):
                info = [id, name]
                upcoming_birthday_list.append(info)

    pt = ''
    if len(upcoming_birthday_list) > 0:
        pt = PrettyTable(field_names=["ID", "Name"])
        for id, name in upcoming_birthday_list:
            mults_info_list = [id, name]
            pt.add_row(mults_info_list)
    if pt != '':
        return_print = "US38: List: The following individuals have upcoming birthdays within 30 days!\n" + str(pt)
    else:
        return_print = None

    return return_print

def print_list_upcoming_birthdays(individual_info_dict):
    if list_upcoming_birthdays(individual_info_dict) != None:
        print(list_upcoming_birthdays(individual_info_dict))


#US39
def list_upcoming_anniversaries(individual_info_dict, family_info_dict):
    """ Lists all anniversaries that occur within a month in a GEDCOM file. """
    upcoming_anniversary_list = []
    today = datetime.date.today()
    pt = ''
    for family_id, family_info in family_info_dict.items():
        
        wife_id = family_info.get('WIFE')
        husband_id = family_info.get('HUSB')
        wife_name = ''
        husb_name = ''

        for individual_id, individual_info in individual_info_dict.items():
            if individual_id == wife_id:
                wife_name = individual_info.get('NAME')
            elif individual_id == husband_id:
                husb_name = individual_info.get('NAME')
        
        wedding_date = Date(str(family_info.get("MARR"))).date_time_obj
        if wedding_date not in [None, 'NA', '']:
            this_year_anniversary = datetime.date(today.year, wedding_date.month, wedding_date.day)
            difference = today - this_year_anniversary
            if difference > datetime.timedelta(0) and difference < datetime.timedelta(30):
                info = [wife_id, wife_name, husband_id, husb_name]
                upcoming_anniversary_list.append(info)

    pt = ''
    if len(upcoming_anniversary_list) > 0:
        pt = PrettyTable(field_names=["Wife ID", "Wife Name", "Husband ID", "Husband Name"])
        for info in upcoming_anniversary_list:
            pt.add_row(info)
    if pt != '':
        return_print = "US39: List: The following couples have upcoming anniversaries within 30 days!\n" + str(pt)
    else:
        return_print = None

    return return_print

def print_list_upcoming_anniversaries(individual_info_dict, family_info_dict):
    if list_upcoming_anniversaries(individual_info_dict, family_info_dict) != None:
        print(list_upcoming_anniversaries(individual_info_dict, family_info_dict))

        