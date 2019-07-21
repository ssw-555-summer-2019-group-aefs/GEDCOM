import os
from gedcom_file_parser import print_pretty_table

if __name__ == '__main__':
    dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
    print_pretty_table(f"{dir_path}/data/sprint3userstorytest.ged")

    
