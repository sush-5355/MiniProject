
from excute_command import executeCommand, executeCommandInstall
import json
import shutil

columns = shutil.get_terminal_size().columns

def chrome():
    # install chrome
    command = ['wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb',
               'sudo dpkg -i google-chrome-stable_current_amd64.deb']
    for com in command:
        executeCommand(command=com)


def version():
    # check ubuntu version
    command = 'lsb_release -a'
    print(executeCommand(command=command))


def host():
    # checkhostname
    command = 'hostname'
    print(executeCommand(command=command))


def ipconf():
    # check ip addressess
    command = ['ifconfig']
    print(executeCommand(command=command))


print(' Welcome to the Automation world '.upper().center(columns,'#'))
print()
input_dict = {'1': 'Check Hostame',
              '2': 'Check IP Address',
              '3': 'check Hostname',
              '4': 'Install Chrome'
              }

print(json.dumps(input_dict, indent=4)+'\n')

n = input('Enter the value : ')

if n == 1:
    host()
elif n == 2:
    ipconf()
elif n == 3:
    host()
elif n == 4:
    chrome()
else:
    pass


