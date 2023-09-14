
from excute_command import executeCommand, executeCommandInstall
import json
import shutil

columns = shutil.get_terminal_size().columns

def chrome():
    # install chrome
    command = ['wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb',
               'sudo dpkg -i google-chrome-stable_current_amd64.deb']
    for com in command:
        executeCommandInstall(command=com)


def version():
    # check ubuntu version
    command = 'lsb_release -a'
    print(executeCommand(command=command))


def host():
    # checkhostname
    command = 'hostname'
    response = executeCommand(command=command)
    response['response'] = response['response'][-1].strip()
    print(response)


def ipconf():
    # check ip addressess
    command = 'ifconfig | grep 192'
    response = executeCommand(command=command)
    response['response'] = response['response'][-1].strip().split()[1]
    
    print(response)


print(' Welcome to the Automation world '.upper().center(columns,'#'))
print()
input_dict = {'1': 'Check Hostame',
              '2': 'Check IP Address',
              '3': 'check Version',
              '4': 'Install Chrome'
              }

print(json.dumps(input_dict, indent=4)+'\n')

n = int(input('Enter the value : '))

if n == 1:
    host()
elif n == 2:
    ipconf()
elif n == 3:
    version()
elif n == 4:
    chrome()
else:
    pass


