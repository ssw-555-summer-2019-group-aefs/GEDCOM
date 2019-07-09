#Project           : GEDCOM SSW 555 Summer 2019
#Author            : Saransh Ahlawat
#Date created      : 07.01.2019
#Purpose           : US22
#Revision History  : Version 1.0

import os

"""
User Story US22
"""
def print_duplicate_ids(duplicate_ids_error_list):    
    for id in duplicate_ids_error_list:
        if "I" in id:
            id_type = "individual"
        else:
            id_type = "family"
        print(f"ERROR: US22: Duplicate {id_type} id: {id}")
