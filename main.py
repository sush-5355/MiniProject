
from excute_command import executeCommand, executeCommandInstall


# # install chrome
# command = ['wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb','sudo dpkg -i google-chrome-stable_current_amd64.deb']
# for com in command:
#     executeCommand(command=com)

# # check ubuntu version
# command = 'lsb_release -a'
# print(executeCommand(command=command))

# # checkhostname
# command = 'hostname'
# print(executeCommand(command=command))
# # check ip addressess
# command = ['ifconfig']
# print(executeCommand(command=command))

print('Welcome to the Automation world'.upper())
input_dict = {'1': 'Check Hostame',
              }
