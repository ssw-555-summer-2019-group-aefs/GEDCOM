from prettytable import PrettyTable
from utils import LEVEL_TAGS, get_families_pretty_table_order, get_family_info_tags, get_individual_info_tags, get_individual_pretty_Table_order
from util_date import Date


def gedcom_file_parser(path):
    """gedcom file parser opens and reads a gedcom file line-byline
    and stores the fields of individuals and families in separate dictionaries.
    The key of individuals dictionary is the individual id, for families dictionary 
    it is family id.
    
    Arguments:
        path {string} -- this is the path of the gedcom file
    
    Returns:
        {tuple of dictionaries} -- the return value is a tuple of
        individuals and families dictinary
    """
    try:
        fp = open(path, "r")
    except FileNotFoundError:
        print("Can't open", path)
    else:
        with fp:
            line = fp.readline()
            individuals_dict = dict()
            family_dict = dict()
            while line:
                if line != "":
                    tag_array = LEVEL_TAGS.get(line[0])
                    line_split = line.split()
                    if tag_array == None:
                        print("Invalid tag")
                        line = fp.readline()
                        continue
                    elif line_split[0] == "0":
                        if len(line_split) > 2 and line_split[2] == "INDI":
                            individual_id = line_split[1]
                            individuals_dict[individual_id] = {}
                            line = fp.readline().rstrip("\n")
                            if line:
                                line_split = line.split()
                                while "INDI" not in line_split:
                                    if "FAM" in line_split or not line:
                                        break
                                    if line_split[1] in get_individual_info_tags():
                                        if line_split[1] == "BIRT":
                                            line = fp.readline().rstrip("\n")
                                            if line != "":
                                                line_split = line.split()
                                                if line_split[1] == "DATE":
                                                    individuals_dict[individual_id]["BIRT"] = Date(" ".join(
                                                        line_split[2:]))
                                        elif line_split[1] == "DEAT":
                                            line = fp.readline().rstrip("\n")
                                            if line != "":
                                                line_split = line.split()
                                                if line_split[1] == "DATE":
                                                    individuals_dict[individual_id]["DEAT"] = Date(" ".join(
                                                        line_split[2:]))
                                        else:
                                            individuals_dict[individual_id][line_split[1]] = " ".join(
                                                line_split[2:])
                                        line = fp.readline().rstrip("\n")
                                        line_split = line.split()
                                    else:
                                        line = fp.readline().rstrip("\n")
                                        line_split = line.split()
                                        continue
                        if "FAM" in line_split and len(line_split) > 2:
                            family_id = line_split[1]
                            family_dict[family_id] = {}
                            line = fp.readline().rstrip("\n")
                            line_split = line.split()
                            while "FAM" not in line_split:
                                if line:
                                    if line_split[1] in get_family_info_tags():
                                        if line_split[1] == "MARR":
                                            line = fp.readline().rstrip("\n")
                                            if line:
                                                line_split = line.split()
                                                if line_split[1] == "DATE":
                                                    family_dict[family_id]["MARR"] = Date(" ".join(
                                                        line_split[2:]))
                                        elif line_split[1] == "DIV":
                                            line = fp.readline().rstrip("\n")
                                            if line:
                                                line_split = line.split()
                                                if line_split[1] == "DATE":
                                                    family_dict[family_id]["DIV"] = Date(" ".join(
                                                        line_split[2:]))
                                        elif line_split[1] == "CHIL":
                                            if family_dict[family_id].get("CHIL") == None:
                                                family_dict[family_id]["CHIL"] = [
                                                    line_split[2]]
                                            else:
                                                family_dict[family_id]["CHIL"].append(
                                                    line_split[2])
                                        else:
                                            family_dict[family_id][line_split[1]] = " ".join(
                                                line_split[2:])
                                        line = fp.readline().rstrip("\n")
                                        line_split = line.split()
                                    else:
                                        line = fp.readline().rstrip("\n")
                                        line_split = line.split()
                                        continue
                                else:
                                    break
                        else:
                            if "INDI" not in line_split:
                                line = fp.readline().rstrip("\n")
                            continue
                    else:
                        line = fp.readline().rstrip("\n")
                        continue
        return individuals_dict, family_dict


def print_pretty_table(directory_path):
    individuals, families = gedcom_file_parser(directory_path)
    print_individuals_pretty_table(individuals)
    print_families_pretty_table(families, individuals)


def print_individuals_pretty_table(individuals_dict):
    pt = PrettyTable(field_names=[
                     "ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"])
    for individual_id, individual_info in individuals_dict.items():
        individual_info["ALIVE"] = individual_info.get("DEAT") == None
        if individual_info.get("BIRT") != None:
            birth_date = individual_info.get("BIRT").date_time_obj
        death_date = None
        if individual_info.get("DEAT") != None:
            death_date = individual_info.get("DEAT").date_time_obj
        individual_info["AGE"] = Date.get_dates_difference(birth_date, death_date)
        individual_info["FAMC"] = individual_info.get(
            "FAMC") if individual_info.get("FAMC") != None else "NA"
        individual_info["FAMS"] = individual_info.get(
            "FAMS") if individual_info.get("FAMS") != None else "NA"
        individual_info["DEAT"] = individual_info.get(
            "DEAT") if individual_info.get("DEAT") != None else "NA"
        individual_info_list = [individual_id]
        for key in get_individual_pretty_Table_order():
            individual_info_list.append(individual_info.get(key))
        pt.add_row(individual_info_list)
    print(pt)


def print_families_pretty_table(families_dict, individuals_dict):
    pt = PrettyTable(field_names=["ID", "Married", "Divorced",
                                  "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"])
    for family_id, family_info in families_dict.items():
        family_info["DIV"] = family_info.get(
            "DIV") if family_info.get("DIV") != None else "NA"
        family_info["CHIL"] = family_info.get(
            "CHIL") if family_info.get("CHIL") != None else "NA"
        family_info["MARR"] = family_info.get(
            "MARR") if family_info.get("MARR") != None else "NA"
        family_info["HNAME"] = individuals_dict.get(family_info.get("HUSB")).get(
            "NAME") if individuals_dict.get(family_info.get("HUSB")) != None else "NA"
        family_info["WNAME"] = individuals_dict.get(family_info.get("WIFE")).get(
            "NAME") if individuals_dict.get(family_info.get("WIFE")) != None else "NA"
        family_info_list = [family_id]
        for key in get_families_pretty_table_order():
            family_info_list.append(family_info.get(key))
        pt.add_row(family_info_list)
    print(pt)

# User Story 07
def check_150_years_age(individual_info_dict):

    age_limit = 150

    # gets dates from individual info
    for individual_id, individual_info in individual_info_dict.items():
        id = individual_id
        birth_date = Date(str(individual_info.get("BIRT")))
        if individual_info.get("DEAT") != None:
            death_date = Date(str(individual_info.get("DEAT")))
        else:
            death_date = None
    
        # calculates age with the dates
        if death_date == None and birth_date != None:
            age = Date.get_dates_difference(birth_date.date_time_obj)
        else:
            if death_date != None and birth_date != None:
                age = Date.get_dates_difference(birth_date.date_time_obj, death_date.date_time_obj)

        # checks to see if age exceeds age limit and prints error
        if age > age_limit and death_date == None:
            print('ERROR: INDIVIDUAL: US07: {}: More than 150 years old - Birth date {}'.format(id, birth_date))
        elif age > age_limit and death_date != None:
            print('ERROR: INDIVIDUAL: US07: {}: More than 150 years old at death - Birth date {}: Death date {}'.format(id, birth_date, death_date))
# End of User Story 07

# User story 08
def check_birth_before_marriage_of_parents(family_info_dict, individual_info_dict):
    
    for family_id, family_info in family_info_dict.items():
        # gets marriage and divorce dates in family if they exist
        if family_info.get("MARR") != None:
            marriage_date = Date(str(family_info.get("MARR")))
        else:
            marriage_date = None
        if family_info.get("DIV") != None:
            divorce_date = Date(str(family_info.get("DIV")))
        else:
            divorce_date = None
        
        # obtains all childen in family
        children = family_info.get('CHIL')

        #if children exist, it gets the birth dates and compares it to the marriage/divorce dates, and prints error if marriage is before birth and/or birth is after divorce
        if children != None:
            for child in children:
                child_dict = individual_info_dict.get(child)
                birth_date = Date(str(child_dict.get('BIRT')))
                if marriage_date != None and marriage_date.date_time_obj < birth_date.date_time_obj:
                    print('ANOMOLY: FAMILY: US08: {}: Child {} born {} before marriage on {}'.format(family_id, child, birth_date, marriage_date))
                if divorce_date != None and birth_date > divorce_date:
                    print('ANOMOLY: FAMILY: US08: {}: Child {} born {} after divorce on {}'.format(family_id, child, birth_date, divorce_date))
# End of User Story 08

def main():
    directory_path = r'C:\Users\Erik\Desktop\SSW555\Test\GEDCOM\project3\data\project01.ged'
    print_pretty_table(directory_path)
    individual_dict, family_dict = gedcom_file_parser(directory_path)
    check_150_years_age(individual_dict) # US07
    check_birth_before_marriage_of_parents(family_dict, individual_dict) #US08

if __name__ == '__main__':
    main()
