import os
from utilities.CRUD import create
from datetime import datetime
import json
import random
from faker import Faker
import pytz
from hurry.filesize import size

fake = Faker()
categories = [
    "jpg",
    "bmp",
    "mp3",
    "mp4",
    "docx",
    "txt",
    "rar",
    "java",
    "py"
]


def generate_random_file_size():
    # Generate a random size between 1 KB and 10 MB
    size_in_bytes = random.randint(1024, 100 * 1024 * 1024)
    return size_in_bytes


def extract_file_type(file_name):
    _, file_extension = os.path.splitext(file_name)
    return file_extension


i = 0
while i < 100:
    name = random.choice(['Skype', 'KM Player', 'Notepad++', 'Whatsapp',
                         'Mozilla FireFox', 'Spotify', 'VS Code', 'VM Ware'])
    destip = fake.ipv4()
    desthost = random.choice(['windows', 'linux', 'ubuntu'])

    desttz = fake.timezone()
    if desthost == 'windows':
        desthostosV = random.choice(
            ['windows 10', 'windows 11'])
    if desthost == 'linux':
        desthostosV = random.choice(
            ['Rhel 9', 'Cent OS 8'])
    if desthost == 'ubuntu':
        desthostosV = 'Ubuntu 20.04.6 LTS'
    destloctime = datetime.now(pytz.timezone(
        desttz)).strftime('%b %Y-%m-%d %H:%M:%S')

    data_check_install = {
        "name": name,
        "installed": random.choice([True, False]),
        "destination_hostnanme": desthost,
        "destination_ip": destip,
        'destination_os_version': desthostosV,
        "source_ip": "192.168.216.1",
        "timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S'),
        "destination_time_zone": desttz,
        "destination_local_time": destloctime
    }

    file_name_length = random.randint(10, 15)
    fname = fake.text(max_nb_chars=file_name_length)
    fname = fname+random.choice(categories)
    dummy_install_files = {
        "destination_hostnanme": desthost,
        'destination_os_version': desthostosV,
        "destination_ip": destip,
        "source_ip": "192.168.216.1",
        "timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S'),
        "destination_time_zone": desttz,
        'destination_local_time': destloctime,
        "file_name": fname,
        "output_path": f"/home/mini/Documents/{fname}",
        "file_size": size(generate_random_file_size()),
        "file_type": extract_file_type(file_name=fname)
    }

    # create(index_name='miniproject',mapping=data_check_install)
    # print(i)
    dummy_install_apps = {
        "name": name,
        "time_elapsed": random.uniform(30, 50),
        "destination_hostnanme": desthost,
        "destination_ip": destip,
        "source_ip": "192.168.216.1",
        "destination_os_version": desthostosV,
        "timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S'),
        "destination_local_time": destloctime,
        "destination_time_zone": desttz
    }

    print('data_check_install', data_check_install)
    create(index_name='miniproject', mapping=data_check_install)
    print('dummy_install_files', dummy_install_files)
    create(index_name='miniproject_installed_files',
           mapping=dummy_install_files)
    print('dummy_install_apps', dummy_install_apps)
    create(index_name='miniproject_installed_apps', mapping=dummy_install_apps)
    i = i+1
