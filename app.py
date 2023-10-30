import json
import shutil
import time
from constant import *
from check_installation import check_chrome_install, check_os_details, push_to_elastic,check_teamviewer_install,check_vlc_install
from main import chrome, install_vlc, install_skype, install_teamviewer,createNewUser,changeTimeZone
from transfer_files import transfer_files
from utilities.CRUD import create
terminal_columns, _ = shutil.get_terminal_size()


available_space = terminal_columns - 2
centered_text = HEADLINE.center(available_space)
line_of_hashes = '#' * terminal_columns
print(line_of_hashes)
print(f"#{centered_text}#")
print(line_of_hashes)
time.sleep(1)
print('\n'*5)
# print('Project Description', DESCRIPTION)
print('Project Description')
for char in DESCRIPTION:
    print(char, end='', flush=True)  # Use end='' to avoid newline and flush=True to force immediate printing
    time.sleep(0.1) 
print('\n'*2)
print('Project Objective')
for char in OBJECTIVE:
    print(char, end='', flush=True)  # Use end='' to avoid newline and flush=True to force immediate printing
    time.sleep(0.1) 
# print('Project Objective :', OBJECTIVE)
while True:
    print()
    print(INPUT_DICT)
    print()
    n = input('Enter your choice : ')
    print('\n')
    if n.isdigit():
        n = int(n)
        if n == 1:
            push_to_elastic()
        elif n == 2:
            while True:
                print(LIST_OF_APPS)
                m = int(input('Enter your choice for installation : '))
                print('\n')
                if m == 1:
                    if not check_chrome_install()['installed']:
                        start = time.time()
                        chrome()
                        dic = dict(name='Google Chrome',time_elapsed=time.time()-start)
                        dic.update(check_os_details())
                        create(index_name='miniproject_installed_apps',mapping=dic)
                        print('\n\n Google Chrome successfully installed !!!')
                        
                    else:
                        print('\n\n Google Chrome already installed !!!')
                elif m == 2:
                    if not check_vlc_install()['installed']:
                        start = time.time()
                        install_vlc()
                        dic = dict(name='VLC Media Player',time_elapsed=time.time()-start)
                        dic.update(check_os_details())
                        create(index_name='miniproject_installed_apps',mapping=dic)
                        print('\n\n VLC Media Player successfully installed !!!')
                    else:
                        print('\n\n VLC Media Player already installed !!!')
               
                    
                elif m ==3:
                    if not check_teamviewer_install()['installed']:
                        start = time.time()
                        install_teamviewer()
                        dic = dict(name='TeamViewer',time_elapsed=time.time()-start)
                        dic.update(check_os_details())
                        create(index_name='miniproject_installed_apps',mapping=dic)
                        print('\n\n TeamViewer successfully installed !!!')
                    else:
                        print('\n\n TeamViewer already installed !!!')
                    
                elif m == 4:
                    start = time.time()
                    chrome()
                    install_teamviewer()
                    install_vlc()
                    dic = dict(name = 'ALL',time_elapsed=time.time()-start)
                    dic.update(check_os_details())
                    create(index_name='miniproject_installed_apps',mapping=dic)
                    print('\n\n ALL APPLICATIONS INSTALLED SUCCESSFULLY !!! \n')
                elif m == 5:
                    break
                else:
                    print('\n\n Please retry from above options only !!!')
                    pass
        elif n == 3:
            print(TRANSFER_FILES)
            transfer_files()
        elif n == 4:
            createNewUser()
        elif n == 5:
            changeTimeZone()
        elif n == 6:
            break
        else:
            print('Please retry from above options only !!!')
            pass
    else:
        print(ERROR_MESSAGE)
