from paramiko_config import connect_to_pc,password


def executeCommand(command:str):

    client = connect_to_pc()

    client = client.get('connectionClient')
    stdin,stdout,stderr = client.exec_command(command=command)
    # stdin.write(f'{password}\n')
    # stdin.flush()
    # print(password)
    # if stderr:
    #     return stderr.readlines()
    output = stdout.read().decode()
    # print(output)
    return output