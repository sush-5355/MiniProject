import os
import time
from paramiko_config import connect_to_pc
import progressbar
from check_installation import check_os_details
from utilities.CRUD import create

relative_path = "files"
absolute_path = os.path.abspath(relative_path)

def transfer_files():
    connection = connect_to_pc()
    if not connection['status']:
        return 'Not Connected: ' + connection.get('error', 'Unknown error')
    client = connection['connectionClient']
    sftpClient = client.open_sftp()
    try:
        files = os.listdir(absolute_path)
        for file in files:
            local_path = os.path.join(absolute_path,file)
            local_file_size = os.path.getsize(local_path)
            remote_path = f'/home/mini/Documents/{file}'
            widgets = [progressbar.Percentage(), ' ', progressbar.Bar(fill='>'), ' ', progressbar.ETA(format='ETA:  %(eta)8s')]
            progress = progressbar.ProgressBar(widgets=widgets, maxval=local_file_size).start()
            transferred = 0
            block_size = 8192  # Adjust this value as needed
            start = time.time()
            with open(local_path, 'rb') as local_file, sftpClient.file(remote_path, 'wb') as remote_file:
                while True:
                    data = local_file.read(block_size)
                    if not data:
                        break
                    remote_file.write(data)
                    transferred += len(data)
                    progress.update(transferred)
            progress.finish()
            time_taken = time.time() - start
            print('File sent successfully')
            output = {}
            output.update(check_os_details())
            output['file_name'] = file
            output['output_path'] = remote_path
            output['file_size'] = local_file_size
            output['time_taken'] = time_taken
            output['file_type'] = file.split('.')[-1]
            response = create(index_name='miniproject_transfered_files',mapping=output)
            print(response)

    except Exception as e:
        print(f'Error transferring file: {str(e)}')
    finally:
        sftpClient.close()
        client.close()