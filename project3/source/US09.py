from util_date import Date

def birth_before_parents_death(individuals_dict, families_dict):
    for family_id, family_info in families_dict.items():
        print(family_id, family_info)
        husb_info = individuals_dict[family_info['HUSB']]
        wife_info = individuals_dict[family_info['WIFE']]
        print(husb_info.get('DEAT'))
        if husb_info.get('DEAT') != None and husb_info.get('DEAT') != 'NA':
            if family_info.get('CHIL') != None:
                for child in family_info.get('CHIL'):
                    child_info = individuals_dict[child]
                    try:
                        if Date.get_dates_difference(husb_info.get('DEAT').date_time_obj, child_info.get('BIRT').date_time_obj) < 0:
                            raise ValueError(f"ERROR: Husband died before the birth of his child - {family_id}")
                    except ValueError as e:
                        print(e)

        if wife_info.get('DEAT') != None and wife_info.get('DEAT') != 'NA':
            if family_info.get('CHIL') != None:
                for child in family_info.get('CHIL'):
                    child_info = individuals_dict[child]
                    try:
                        if Date.get_dates_difference(wife_info.get('DEAT').date_time_obj, child_info.get('BIRT').date_time_obj) < 0:
                            raise ValueError(f"ERROR: Husband died before the birth of his child - {family_id}")
                    except ValueError as e:
                        print(e)