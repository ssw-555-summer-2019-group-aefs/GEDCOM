#Project           : GEDCOM SSW 555 Summer 2019
#Program name      : Homework05_US01
#Author            : Anthem Rukiya J. Wingate, Fran Sabetour
#Date created      : 06.18.2019
#Purpose           : User story Implementation of US01
#Revision History  : Version 1.0
# Notes:  This user story checks if assorted dates for individuals occur in the future.

import datetime
from util_date import Date

def us01(individuals, families):
    """ Check US01 Dates (birth, marriage, divorce, death) should not be after the current date."""

    errors = dict()
    i=0

    for ind_id, ind in individuals.items(): # each ind is dict with the attributes of the individual
        error1, error2, error3, error4 = False, False, False, False
        if type(ind['BIRT'].date_time_obj) is not str:
            if ind['BIRT'] != 'NA':
                if Date.get_dates_difference(ind['BIRT'].date_time_obj) < 0:
                    print(f"US01: Error: Individual's '{ind_id}' birthday '{ind['BIRT'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")
                    error1 = True
        
        if ind['DEAT'] != 'NA' and type(ind['DEAT'].date_time_obj) is not str:
            if Date.get_dates_difference(ind['DEAT'].date_time_obj) < 0:
                print(f"US01: Error: Individual's '{ind_id}' death date '{ind['DEAT'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")
                error2 = True
        

        if ind['FAMS'] != 'NA':
            if families[ind['FAMS']]['MARR'] != "NA" and type(families[ind['FAMS']]['MARR'].date_time_obj) is not str:
                if families[ind['FAMS']]['MARR'] != 'NA':
                    if Date.get_dates_difference(families[ind['FAMS']]['MARR'].date_time_obj) < 0:
                        print(f"US01: Error: Individual's '{ind_id}' marriage date '{families[ind['FAMS']]['MARR'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")
                        error3 = True

            if families[ind['FAMS']]['DIV'] != 'NA' and type(families[ind['FAMS']]['DIV'].date_time_obj) is not str:
                if Date.get_dates_difference(families[ind['FAMS']]['DIV'].date_time_obj) < 0:
                    print(f"US01: Error: Individual's '{ind_id}' divorce date '{families[ind['FAMS']]['DIV'].date_time_obj.strftime('%d %b %Y')}' occurs in the future.")
                    error4 = True
    
        errors[i] = [error1, error2, error3, error4]
        i+=1
    return errors
  