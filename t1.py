import django
import sys
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","bsubonweb.settings")
django.setup()

from os import stat
from pwd import getpwuid

def getown(path):
    return getpwuid(stat(path).st_uid).pw_name
    
