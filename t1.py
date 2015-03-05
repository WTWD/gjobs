import django
import sys
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","bsubonweb.settings")
django.setup()

from os import stat
from pwd import getpwuid

def getown(path):
    return getpwuid(stat(path).st_uid).pw_name
    
import uuid 
path = path_list[0]

def createjobs(path_list):
    for path in path_list:
        slug = uuid.uuid3(uuid.NAMESPACE_DNS,path)
        job1 = Jobs(path=path,slug=slug)
        job1.save()
        
name  = "dgital-regression"
slug = uuid.uuid3(uuid.NAMESPACE_DNS,name)
jobs = Jobs.objects.filter(paht__endswith="tsim")
g1 = Group.objects.filter(name=name)[0]
for i in jobs:
    g1.jobs.add(i)
    
