import datetime

LEVEL_TAGS = dict({
    "0": ["INDI", "FAM", "HEAD", "TRLR", "NOTE"],
    "1": ["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"],
    "2": ["DATE"]
})

def get_individual_info_tags():
    return ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS"]

def get_family_info_tags():
    return ["FAM", "HUSB", "WIFE", "CHIL", "MARR", "DIV"]

def get_individual_pretty_Table_order():
    return ["NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT", "FAMC", "FAMS"]

def get_families_pretty_table_order():
    return ["MARR", "DIV", "HUSB", "HNAME", "WIFE", "WNAME", "CHIL"]
