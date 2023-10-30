from excute_command import executeCommand
from main import host, ipconf, version, checkTimezone
import datetime
from utilities.CRUD import create
import socket

def check_os_details():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    response = dict(destination_hostnanme=host()['response'],
                    destination_ip=ipconf()['response'],
                    source_ip=ip_address,
                    destination_os_version=version()['response'],
                    timestamp=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S'))
    response.update(checkTimezone())
    return response

def check_chrome_install():
    dic = {"name": 'Chrome'}
    response = executeCommand(command='google-chrome --version')
    if 'command not found' in response['response'][-1]:
        dic['installed'] = False
    else:
        dic['installed'] = True
    return dic

def check_teamviewer_install():
    dic = {"name": 'TeamViewer'}
    response = executeCommand(command='teamviewer --version')
    if 'command not found' in response['response'][-1]:
        dic['installed'] = False
    else:
        dic['installed'] = True
    return dic

def check_vlc_install():
    dic = {"name": 'VLC'}
    response = executeCommand(command='vlc --version | "VLC media player"')
    if 'command not found' in response['response'][-1]:
        dic['installed'] = False
    else:
        dic['installed'] = True
    return dic

def push_to_elastic():
    osdetail = check_os_details()
    vlc = check_vlc_install()
    vlc.update(osdetail)
    teamviewer = check_teamviewer_install()
    teamviewer.update(osdetail)
    response  = create(index_name='miniproject', mapping=teamviewer)
    print(response)
    response = create(index_name='miniproject', mapping=vlc)
    print(response)
    chrome = check_chrome_install()
    chrome.update(osdetail)
    response = create(index_name='miniproject', mapping=chrome)
    print(response)