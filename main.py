import json
from excute_command import executeCommand, executeCommandInstall
from paramiko_config import connect_to_pc, password

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
    response['response'] = response['response'][-1].split(':', 1)[-1].strip()
    return response

def host():
    # checkhostname
    command = 'hostname'
    response = executeCommand(command=command)
    response['response'] = response['response'][-1].strip()
    return response

def ipconf():
    # check ip addressess
    command = 'hostname -I'
    response = executeCommand(command=command)
    response['response'] = response['response'][-1].strip()
    return response

def checkTimezone():
    responseDict = {}
    command = 'timedatectl | grep Local'
    response = executeCommand(command=command)
    responseDict['destination_local_time'] = response['response'][-1].split(
        ':', 1)[-1].strip()
    command = 'timedatectl | grep "Time zone"'
    response = executeCommand(command=command)
    responseDict['destination_time_zone'] = response['response'][-1].split(
        ':', 1)[-1].strip()
    return responseDict

def changeTimeZone():
    while True:
        print('''Below is the list of Time Zones
            Select from below
            1 - UTC
            2 - Aisa/Kolkata
            3 - Exit
            ''')
        n = input('\n Enter the choice of Time Zone : ')
        if n:
            if n.isdigit():
                n = int(n)
                if n == 1:
                    tz = 'UTC'
                    command = [f'sudo timedatectl set-timezone {tz}']
                    for com in command:
                        executeCommandInstall(command=com)
                    print('\n',json.dumps(checkTimezone(),indent=4))
                if n == 2:
                    tz = 'Asia/Kolkata'
                    command = [f'sudo timedatectl set-timezone {tz}']
                    for com in command:
                        executeCommandInstall(command=com)
                    print('\n',json.dumps(checkTimezone(),indent=4))
                elif n == 3:
                    break
                else:
                    pass
            else:
                print('Please try again with valid input. Only digits allowed !!!')

def createNewUser():
    client = connect_to_pc()
    ssh = client.get('connectionClient')
    new_username = input('Enter the username : ')
    # Set a secure password for the new user
    new_password = input('Enter the new password : ')
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
    stdin, stdout, stderr = ssh.exec_command(
        add_to_sudoers_command, get_pty=True)
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

def install_vlc():
    command = ['sudo apt install snapd', 'sudo snap install vlc']
    for com in command:
        executeCommandInstall(command=com)

def install_spotify():
    command = ['sudo snap install spotify']
    for com in command:
        executeCommandInstall(command=com)

def install_telegram():
    command = ['sudo apt update','sudo snap install telegram-desktop']
    for com in command:
        executeCommandInstall(command=com)

def install_skype():
    command = ['wget https://repo.skype.com/latest/skypeforlinux-64.deb',
               'sudo dpkg -i skypeforlinux-64.deb']
    for com in command:
        executeCommandInstall(command=com)

def install_teamviewer():
    command = ['wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb',
               'sudo apt install ./teamviewer_amd64.deb -y']
    for com in command:
        print(executeCommandInstall(command=com))
