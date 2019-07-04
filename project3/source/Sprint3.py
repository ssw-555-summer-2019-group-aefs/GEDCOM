#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : Sprint 2
#Author            : Anthem Rukiya J. Wingate, Fran Sabetpour
#Date created      : 07.07.2019
#Purpose           : User story Implementation of US13, US14, US15, US17, US18, US28, US32, US33
#Revision History  : Version 1.0

# Notes:  Block implementation of user stories involving spouses and children

# Sprint 3:  Child Block
# US35:  List all people in a GEDCOM file who were born in the last 30 days.
# US36:  List all people in a GEDCOM file who died in the last 30 days.

import datetime
from util_date import Date
from Sprint2 import get_dates_diff
from prettytable import PrettyTable

def us35(individuals):
    """ List all people in a GEDCOM file who were born in the last 30 days. """
    
    print('US35: List:  The following people were born within the last 30 days')
    pt = PrettyTable(field_names=["ID", "Name", "Date of Birth"])
    for ind_id, ind in individuals.items():
        if Date.is_valid_date(ind['BIRT'].date_time_obj):
            diff, time_typ = get_dates_diff(ind['BIRT'].date_time_obj)
            if time_typ == 'days' and diff <= 30:
                recent_births = [ind_id, ind['NAME'], (ind['BIRT'].date_time_obj).strftime('%d %b %Y')]
                pt.add_row(recent_births)

    print(pt)

    return None

def us36(individuals):
    """ List all people in a GEDCOM file who died in the last 30 days. """

    print('US36: List:  The following people died within the last 30 days')
    pt = PrettyTable(field_names=["ID", "Name", "Date of Birth"])
    for ind_id, ind in individuals.items():
        if ind['DEAT'] != 'NA' and Date.is_valid_date(ind['DEAT'].date_time_obj):
            diff, time_typ = get_dates_diff(ind['DEAT'].date_time_obj)
            if time_typ == 'days' and diff <= 30:
                recent_deaths = [ind_id, ind['NAME'], (ind['DEAT'].date_time_obj).strftime('%d %b %Y')]
                pt.add_row(recent_deaths)
    
    print(pt)

    return None


def get_recent_block(individuals):
    """ Get dates within 30 days. """

    us35(individuals)
    us36(individuals)

    return None