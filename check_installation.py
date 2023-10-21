from excute_command import executeCommand
from main import host, ipconf,version,checkTimezone
import datetime
from utilities.CRUD import create

def check_os_details():
    response = dict(hostnanme = host()['response'],
                   ip_address = ipconf()['response'],
                   version = version()['response'],
                   timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))
    response.update(checkTimezone())
    return response


def check_chrome_install():
    dic = {"name":'Chrome'}
    response = executeCommand(command='google-chrome --version')
    if 'command not found' in response['response'][-1]:
        dic['installed']=False
        
    else:
        dic['installed']=True
    return dic

def check_vlc_install():
    dic = {"name":'VLC'}
    response = executeCommand(command='vlc --version | "VLC media player"')
    if 'command not found' in response['response'][-1]:
        dic['installed']=False
        
    else:
        dic['installed']=True
    return dic
        
# r = check_os_details()
# s = check_vlc_install()
# r.update(s)
# print(r)

def push_to_elastic():
    osdetail = check_os_details()
    vlc = check_vlc_install()
    vlc.update(osdetail)
    response = create(index_name='test',mapping=vlc)
    print(response)
    chrome = check_chrome_install()
    chrome.update(osdetail)
    response = create(index_name= 'test', mapping=chrome)
    print(response)
push_to_elastic()