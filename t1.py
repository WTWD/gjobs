import django
import sys
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ldj17.settings")
django.setup()

#  from __future__ import absolute_import
#  from django.core.management import setup_environ
#  import sys,os
#  sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
#  try:
#      import settings # Assumed to be in the same directory.
#  except ImportError:
#      sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
#      sys.exit(1)
#   
#  project_directory = setup_environ(settings)
#  project_name = os.path.basename(project_directory)
#  os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings" % project_name  

# from os import stat
# from pwd import getpwuid

# def getown(path):
#     return getpwuid(stat(path).st_uid).pw_name
    
# import uuid 
# path = path_list[0]


from gjobs.models import *
import random
myslug = lambda mode,id:mode+"%04d"%id
def create_job(path):
    j1 = Job(path=path)
    j1.save()
    j1.slug = myslug("j",j1.id)
    j1.save()

def create_jobhis(job):
    RESULT = ["Compile Error!","Pass!","Faild!","Unknown"]
    EXCHOST = ["hlinux","dlinux"]
    users = User.objects.all()
    user = random.choice(users)
    owner = random.choice(users)
    jobsid = random.randint(10000,30000)
    status = random.randint(0,3)
    if status==0:
        result = "Unknown"
    elif status == 1:
        result = "Unknown"
    elif status == 2:
        result = random.choice(RESULT)
    elif status == 3:
        result = random.choice(RESULT)
    exchost = random.choice(EXCHOST)+str(random.randint(10,200))
    result = random.choice(RESULT)
    spend = random.randint(1,3600*24);
    jh = Jobhis(user=user,owner=owner,jobsid=jobsid,status=status,result=result,spend=spend,job=job)
    jh.save()
    EXCHOST = ["hlinux","dlinux"]
    jh.slug= myslug("jh",jh.id)
    jh.save()
    # print jh

def create_group(name):
    founder = User.objects.all()[0]
    g = Group(name=name,founder=founder)
    g.save()
    g.slug = myslug("g",g.id)
    g.save()
    return g

def create_project(name):
    users = User.objects.all()
    founder = users[0]
    p = Project(name=name,founder=founder)
    p.save()
    p.slug = myslug("p",p.id)
    p.save()
    for member in users:
        p.members.add(member)
    for group in Group.objects.all():
        p.group.add(group)

def job10(n,m):
    for i in range(n,m):
        create_job("/view/root_dview/tmp/whale/work/test%03d/runsim"%i)

def jobhis(n):
    jobs = Job.objects.all()
    for job in jobs:
        print job
        print "-"*10
        for i in range(random.randint(0,n)):
            create_jobhis(job)

def group(group_name):
    jobs = Job.objects.all()
    g = create_group(group_name)
    for job in jobs:
        g.jobs.add(job)
    # g2 = Group.objects.all()[1]
    # for job in jobs[:3]:
        # g2.jobs.add(job)

def project(name):
    create_project(name)

def addg2p(group_name,proj):
    proj=Project.objects.get(name=proj)
    group=Group.objects.get(name=group_name)
    proj.group.add(group)

def addj2g(group_name):
    group=Group.objects.get(name=group_name)
    jobs = Job.objects.all()
    for job in jobs:
        group.jobs.add(job)

# job = Job.objects.all()[0]
# create_jobhis(job)
# create_jobhis(job)
#----------------------------------------
# 1. gen n job
# job10(0:13)
# job10(14,30)
# 2. gen job history
# jobhis(6)
# 3. gen Group
# group("wcdma_v0p2-check")
# add job to group
# group("ici-v0.1-case_regression")
addj2g("ici-v0.1-case_regression")
# 4. gen Project
# project("Whale2")
# project("Tshark3")
# project("PikeXZ")
# project("Dophin")
# project("SharkL")
# 5. add group to Project
# addg2p("ici-v0.1-case_regression","Whale2")


# g1 =Group.objects.all()[0]
# j1 = g1.jobs.all()[0]
# jh = j1.jobhis_set.all()
# print jh
# p1 = Project.objects.all()[0]
# print p1.name
# print p1.members.all()
# jh = Jobhis.objects.all()
# EXCHOST = ["hlinux","dlinux"]
# for i in jh:
#     exchost = random.choice(EXCHOST)+str(random.randint(10,200))
    # i.exchost =  exchost
    # i.save()

