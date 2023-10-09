import json
import paramiko
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

# hostname = os.environ.get("HOSTNAME")
# username = os.environ.get("USERNAME")
# password = os.environ.get("PASSWORD")
# hostname = '192.168.41.130'
# username , password = 'wao','wao'
# username , password = 'newuser1','newuser1'

hostname = os.environ.get("HOSTNAME")
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
# hostname = '192.168.41.130'
# username , password = 'wao','wao'
# hostname = '192.168.216.129 '
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
username = 'mini'
def connect_to_pc():

    try:
        client.connect(
        hostname=hostname, username=username, password=password, port=22, timeout=30)
        return dict(status=True,connectionClient=client)
    except Exception as e:
        return dict(status=False,msg=str(e))
        

def close_connection(client):
    client.close()
    
print(connect_to_pc())