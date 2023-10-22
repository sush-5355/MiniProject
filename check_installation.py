from excute_command import executeCommand
from main import host, ipconf, version, checkTimezone
import datetime
from utilities.CRUD import create

# importing socket module
import socket
# getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
# getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)


def check_os_details():
    response = dict(destination_hostnanme=host()['response'],
                    destination_ip=ipconf()['response'],
                    source_ip=ip_address,
                    destination_os_version=version()['response'],
                    timestamp=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'))
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


def check_vlc_install():
    dic = {"name": 'VLC'}
    response = executeCommand(command='vlc --version | "VLC media player"')
    if 'command not found' in response['response'][-1]:
        dic['installed'] = False

    else:
        dic['installed'] = True
    return dic

# r = check_os_details()
# s = check_vlc_install()
# r.update(s)
# print(r)


def push_to_elastic():
    osdetail = check_os_details()
    vlc = check_vlc_install()
    vlc.update(osdetail)
    edge = {'name': 'Egde', 'installed': True}
    edge.update(osdetail)
    create(index_name='miniproject', mapping=edge)
    response = create(index_name='miniproject', mapping=vlc)
    print(response)
    chrome = check_chrome_install()
    chrome.update(osdetail)
    response = create(index_name='miniproject', mapping=chrome)
    print(response)


push_to_elastic()


def push_to_elastic1():
    osdetail = {'destination_hostnanme': 'windows', 'destination_ip': '192.168.216.10', 'source_ip': '192.168.216.1', 'destination_os_version': 'windows 11',
                'timestamp': '2023-10-22T01:05:30Z', 'local_time': 'Sat 2023-10-21 16:21:31 -03', 'time_zone': 'Asia/Kolkata (IST, +0530)'}
    vlc = check_vlc_install()
    vlc.update(osdetail)
    edge = {'name': 'Egde', 'installed': True}
    edge.update(osdetail)
    create(index_name='miniproject', mapping=edge)
    response = create(index_name='miniproject', mapping=vlc)
    print(response)
    chrome = check_chrome_install()
    chrome.update(osdetail)
    response = create(index_name='miniproject', mapping=chrome)
    print(response)
push_to_elastic1()