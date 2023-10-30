from paramiko_config import connect_to_pc,password,close_connection
from tqdm import tqdm


def executeCommandInstall(command:str):
    client = connect_to_pc()
    if client['status'] == False:
        return 'Not Connected'
    client = client.get('connectionClient')
    stdin,stdout,stderr = client.exec_command(command=command,get_pty=True)
    stdin.write(f'{password}\n')
    stdin.flush()
    progress_bar = tqdm(total=100, unit="%", position=0, leave=False, dynamic_ncols=True)
    # Continuously read and display the installation progress
    while not stdout.channel.exit_status_ready():
        line = stdout.readline().strip()
        if line:
            # # Check if the line contains progress information (e.g., "[50%]")
            if any(progress_symbol in line for progress_symbol in ["[", "]"]):
                progress_bar.update(1)
            # Print the line
            print(line)

    # Close the tqdm progress bar
    progress_bar.close()

    # Print any errors
    for line in stderr:
        print(line.strip())
    close_connection(client=client)

def executeCommand(command:str):
    client = connect_to_pc()
    if client['status'] == False:
        return 'Not Connected'
    client = client.get('connectionClient')
    stdin,stdout,stderr = client.exec_command(command=command,get_pty=True)
    stdin.write(f'{password}\n')
    stdin.flush()
    err = stderr.read().decode()
    if err!='':
        return dict(status=False,response=err)
    output = dict(status= True,response= stdout.readlines())
    return output

