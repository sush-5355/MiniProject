import json
import shutil
import sys
import time
from constant import *
from check_installation import check_chrome_install, check_os_details, check_spotify_install, push_to_elastic,check_teamviewer_install,check_vlc_install,check_spotify_install,check_telegram_install
from main import chrome, install_vlc, install_teamviewer, install_spotify , install_telegram ,createNewUser,changeTimeZone
from transfer_files import transfer_files
from paramiko_config import connect_to_pc

from utilities.CRUD import create