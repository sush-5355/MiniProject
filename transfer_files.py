import os
from paramiko_config import connect_to_pc
import progressbar


def transfer_files():
    connection = connect_to_pc()

    if not connection['status']:
        return 'Not Connected: ' + connection.get('error', 'Unknown error')

    client = connection['connectionClient']
    sftpClient = client.open_sftp()

    local_path = r"I:\Compressed\creditcard.csv.zip"
    remote_path = '/home/wao/Documents/a.zip'

    try:
        local_file_size = os.path.getsize(local_path)
        widgets = [progressbar.Percentage(), ' ', progressbar.Bar(fill='@'), ' ', progressbar.ETA(format='ETA:  %(eta)8s')]
        progress = progressbar.ProgressBar(widgets=widgets, maxval=local_file_size).start()
        transferred = 0
        block_size = 8192  # Adjust this value as needed
        with open(local_path, 'rb') as local_file, sftpClient.file(remote_path, 'wb') as remote_file:
            while True:
                data = local_file.read(block_size)
                if not data:
                    break
                remote_file.write(data)
                transferred += len(data)
                progress.update(transferred)
        progress.finish()
        print('File sent successfully')
    except Exception as e:
        print(f'Error transferring file: {str(e)}')
    finally:
        sftpClient.close()
        client.close()

# Example usage:
result = transfer_files()
print(result)