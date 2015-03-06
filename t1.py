import django
import sys
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ldj17.settings")
django.setup()

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
    result = random.choice(RESULT)
    spend = random.randint(1,3600*24);
    jh = Jobhis(user=user,owner=owner,jobsid=jobsid,status=status,result=result,spend=spend,job=job)
    jh.save()
    jh.slug= myslug("jh",jh.id)
    jh.save()
    # print jh
def create_group(name):
    g = Group(name=name)
    g.save()
    g.slug = myslug("g",g.id)
    g.save()

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

def job10(n):
    for i in range(n):
        create_job("/view/root_dview/tmp/whale/work/test%03d/runsim"%i)

def jobhis(n):
    jobs = Job.objects.all()
    for job in jobs:
        print job
        print "-"*10
        for i in range(random.randint(0,n)):
            create_jobhis(job)

def group():
    jobs = Job.objects.all()
    create_group("wcdma_v0p1-regressions")
    create_group("wcdma_v0p2-check")
    g1 = Group.objects.all()[0]
    for job in jobs:
        g1.jobs.add(job)
    g2 = Group.objects.all()[1]
    for job in jobs[:3]:
        g2.jobs.add(job)

def project():
    create_project("Whale2")
# job = Job.objects.all()[0]
# create_jobhis(job)
# create_jobhis(job)
#----------------------------------------
# 1. gen n job
# job10(13)
# 2. gen job history
# jobhis(6)
# 3. gen Group
# group()
# 4. gen Project
# project()

g1 =Group.objects.all()[0]
j1 = g1.jobs.all()[0]
jh = j1.jobhis_set.all()
print jh
# p1 = Project.objects.all()[0]
# print p1.name
# print p1.members.all()

