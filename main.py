
from excute_command import executeCommand, executeCommandInstall
import json
import shutil

from paramiko_config import connect_to_pc,password

columns = shutil.get_terminal_size().columns

def chrome():
    # install chrome
    command = ['wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb',
               'sudo dpkg -i google-chrome-stable_current_amd64.deb']
    for com in command:
        executeCommandInstall(command=com)


def version():
    # check ubuntu version
    command = 'hostnamectl | grep Operating'
    response = executeCommand(command=command)
    response['response'] = response['response'][-1].strip()
    print(response)


def host():
    # checkhostname
    command = 'hostname'
    response = executeCommand(command=command)
    response['response'] = response['response'][-1].strip()
    print(response)


def ipconf():
    # check ip addressess
    command = 'hostname -I'
    response = executeCommand(command=command)
    response['response'] = response['response'][-1].strip()
    
    print(response)


def checkTimezone():
    # check timezone
    command = 'timedatectl | grep Local'
    response = executeCommand(command=command)
    print(response['response'][-1].strip())
    command = 'timedatectl | grep "Time zone"'
    responseDict = {}
    response = executeCommand(command=command)
    print(response['response'][-1].strip())
    
    # response = response['response'][1:]
    # for res in response:
    #     responseDict.update({res.split(':',1)[0].strip():res.split(':',1)[1].strip()})
    

def createNewUser():
    client = connect_to_pc()
    ssh = client.get('connectionClient')
    
    

    new_username = input('Enter the username : ')
    new_password = input('Enter the new password : ')# Set a secure password for the new user

    # Create the new user with administrative privileges
    create_user_command = f'sudo useradd -m -s /bin/bash {new_username}'
    set_password_command = f'echo "{new_username}:{new_password}" | sudo chpasswd'
    add_to_sudoers_command = f'sudo usermod -aG sudo {new_username}'

    # Execute the commands
    stdin, stdout, stderr = ssh.exec_command(
        f'{create_user_command} && {set_password_command} && {add_to_sudoers_command}', get_pty=True)
    stdin.write(f'{password}\n')
    stdin.flush()
    # Check for errors
    error_output = stderr.read().decode()
    if error_output:
        print(f"Error creating the user: {error_output}")
    else:
        print(f"User '{new_username}' created with administrative privileges.")

    add_to_sudoers_command = f'echo "{new_username} ALL=(ALL) NOPASSWD:ALL" | sudo tee -a /etc/sudoers'
    # Execute the command
    stdin, stdout, stderr = ssh.exec_command(add_to_sudoers_command, get_pty=True)
    stdin.write(f'{password}\n')
    stdin.flush()
    # Check for errors
    error_output = stderr.read().decode()
    if error_output:
        print(f"Error adding '{new_username}' to sudoers: {error_output}")
    else:
        print(f"User '{new_username}' created with administrative privileges.")

    add_home_dir = f'sudo chown -R {new_username}:{new_password} /home/{new_username}'
    stdin, stdout, stderr = ssh.exec_command(add_home_dir, get_pty=True)
    stdin.write(f'{password}\n')
    stdin.flush()
    error_output = stderr.read().decode()
    if error_output:
        print(f"Error adding '{new_username}' home dir : {error_output}")
    else:
        print(f"User '{new_username}' home dir with administrative privileges.")

    ssh.close()

    

print(' Welcome to the Automation world '.upper().center(columns,'#'))
print()
input_dict = {'1': 'Check Hostame',
              '2': 'Check IP Address',
              '3': 'check Version',
              '4': 'Install Chrome',
              '5': 'Timezone',
              '6':'Creat a new user'
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
elif n ==5:
    checkTimezone()
elif n == 6:
    createNewUser()
else:
    pass


