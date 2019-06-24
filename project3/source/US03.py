from util_date import Date

def us03(individuals):
    """ Check US03 Birth should occur before death of an individual."""

    i=0
    errors = dict()
    for ind_id, ind in individuals.items(): # each ind is dict with the attributes of the individual
        errors[i] = False
        if type(ind['BIRT'].date_time_obj) is not str and type(ind['DEAT']) is not str and type(ind['DEAT'].date_time_obj) is not str:
            if ind['BIRT'] != 'NA':
                birth_dt = ind['BIRT'].date_time_obj
            if ind['DEAT'] != 'NA':
                death_dt = ind['DEAT'].date_time_obj
                if Date.get_dates_difference(birth_dt,death_dt) < 0:
                    print(f"US03: Error: Individual's '{ind_id}' birthday '{ind['BIRT'].date_time_obj.strftime('%d %b %Y')}' occurs after the death date '{ind['DEAT'].date_time_obj.strftime('%d %b %Y')}'.")
                    errors[i] = True
        i+=1
    
    return errors


