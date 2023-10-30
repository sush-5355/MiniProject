import json
import paramiko
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

hostname = os.environ.get("HOSTNAME")
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
username = 'mini'
# password = 'mini'
def connect_to_pc():
    try:
        client.connect(
        hostname=hostname, username=username, password=password, port=22, timeout=30)
        return dict(status=True,connectionClient=client)
    except Exception as e:
        return dict(status=False,msg=str(e))
        
def close_connection(client):
    client.close()
    