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

def get_age(birth_date, death_date=None):
    today = datetime.date.today()
    age = 0
    if death_date == None and birth_date != None:
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    else:
        if birth_date != None:
            age = death_date.year - birth_date.year - 1
    return age if age > -1 else 0