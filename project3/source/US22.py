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
    result = list()  
    for id in duplicate_ids_error_list:
        if "I" in id:
            id_type = "individual"
        else:
            id_type = "family"
        print(f"US22: ERROR: Duplicate {id_type} id: {id}")
        result.append(f"US22: ERROR: Duplicate {id_type} id: {id}")
    return result