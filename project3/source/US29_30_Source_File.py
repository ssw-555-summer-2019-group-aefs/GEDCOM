from prettytable import PrettyTable

#US29
def list_deceased(individual_info_dict):
    """ List all deceased in a GEDCOM file. """
    
    death_list = []
    for individual_id, individual_info in individual_info_dict.items():
        id = individual_id
        name = individual_info.get('NAME')
        if individual_info.get('DEAT') not in [None, 'NA']:
            info = id, name
            death_list.append(info)
    
    pt = ''
    if len(death_list) > 0:
        # print("US29: List: The following individuals are deceased in family")
        pt = PrettyTable(field_names=["ID", "Name"])
        for id, name in death_list:
            mults_info_list = [id, name]
            pt.add_row(mults_info_list)
    if pt != '':
        return_print = "US29: List: The following individuals are deceased in the family\n" + str(pt)
    else:
        return_print = None

    return return_print

def print_list_deceased(individual_info_dict):
    if list_deceased(individual_info_dict) != None:
        print(list_deceased(individual_info_dict))


#US30
def list_living_married(individual_info_dict, family_info_dict):
    """ List all living married individuals in a GEDCOM file. """
    living_married_list = []
    pt = ''
    for family_id, family_info in family_info_dict.items():
        
        wife_id = family_info.get('WIFE')
        husband_id = family_info.get('HUSB')
        divorce = individual_info_dict.get('DIV')
        if divorce in [None, 'NA']:
            for individual_id, individual_info in individual_info_dict.items():
                if individual_id == wife_id:
                    wife_name = individual_info.get('NAME')
                    wife_death = individual_info.get('DEAT')
                elif individual_id == husband_id:
                    husband_name = individual_info.get('NAME')
                    husband_death = individual_info.get('DEAT')
            
            if husband_death in [None, 'NA'] and wife_death in [None, 'NA']:
                info = [family_id, husband_id, husband_name, wife_id, wife_name]
                living_married_list.append(info)

            
    if len(living_married_list) > 0:
        pt = PrettyTable(field_names=["Family ID", "Husband ID", "Husband Name", "Wife ID", "Wife Name"])
        for lst in living_married_list:
            pt.add_row(lst)

    if pt != '':
        return_print = "US30: List: The following lists living married couples by family\n" + str(pt)
    else:
        return_print = None

    return return_print

def print_list_living_married(individual_info_dict, family_info_dict):
    if list_living_married(individual_info_dict, family_info_dict) != None:
        print(list_living_married(individual_info_dict, family_info_dict))