from paramiko_config import connect_to_pc, password


client = connect_to_pc()
ssh = client.get('connectionClient')

new_username = 'newuser2'
new_password = 'newuser2'  # Set a secure password for the new user

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
