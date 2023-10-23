import json
import shutil
import time
from constant import *
from check_installation import push_to_elastic
from main import chrome, install_vlc, install_skype, install_teamviewer,createNewUser
from transfer_files import transfer_files
terminal_columns, _ = shutil.get_terminal_size()


available_space = terminal_columns - 2
centered_text = HEADLINE.center(available_space)
line_of_hashes = '#' * terminal_columns
print(line_of_hashes)
print(f"#{centered_text}#")
print(line_of_hashes)
time.sleep(1)
print('\n'*5)
print('Project Description : ', DESCRIPTION)
print('Project Objective :', OBJECTIVE)
while True:
    print()
    print(INPUT_DICT)
    print()
    n = int(input('Enter your choice : '))
    print()
    if n == 1:
        push_to_elastic()
    elif n == 2:
        while True:
            print(LIST_OF_APPS)
            print()
            m = int(input('Enter your choice for installation : '))
            print()
            if m == 1:
                chrome()
            elif m == 2:
                install_vlc()
            elif m == 3:
                install_skype()
            elif m == 4:
                install_teamviewer()
            elif m == 5:
                chrome()
                install_skype()
                install_teamviewer()
                install_vlc()
                print('\n ALL APPLICATIONS INSTALLED SUCCESSFULLY !!! \n')
            elif m == 6:
                break
            else:
                pass
    elif n == 3:
        print(TRANSFER_FILES)
        transfer_files()
    elif n == 4:
        createNewUser()
    elif n == 5:
        break
    else:
        pass
