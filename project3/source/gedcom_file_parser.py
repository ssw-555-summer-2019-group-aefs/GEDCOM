from prettytable import PrettyTable
from utils import LEVEL_TAGS, get_families_pretty_table_order, get_family_info_tags, get_individual_info_tags, get_individual_pretty_Table_order
from util_date import Date
from Sprint1 import get_spouse_block
from Sprint2 import get_child_block
#from Sprint3 import get_recent_block
from US07_US08 import check_150_years_age, check_birth_before_marriage_of_parents
from US09 import birth_before_parents_death
from us11_us12 import check_bigamy, check_parents_not_too_old


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
    e1 = get_spouse_block(individuals, families) #US01, US02, US03, US04, US05, US06, US10
    e2 = get_child_block(individuals, families) #US13, US14, US15, US17, US18, US28, US32, US33
    #e3 = get_recent_block(individuals, families) #US34, US35, US36, US37
    errors = [e1, e2]
    check_150_years_age(individuals)
    check_birth_before_marriage_of_parents(families, individuals)
    birth_before_parents_death(individuals, families)
    check_bigamy(individuals, families)
    check_parents_not_too_old(individuals, families)

    return errors


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


def main():
    directory_path = "C:/Users/Anthe/OneDrive/Documents/GitHub/GEDCOM/project3/source/US17_US18_Test.ged"
    print_pretty_table(directory_path)


if __name__ == '__main__':
    main()