from django.shortcuts import render
from django.http import HttpResponse
import json
from models import *
# Create your views here.

data1={"range10":range(10)}
def index(request):
    # data1={}
    group = Group.objects.get(pk=2)
    project = Project.objects.get(pk=1)
    data1 = {"group1":group,
            "project":project}
    return render(request,"gjobs/index.html",data1)

def welcom(request):
    # data1={}
    return render(request,"gjobs/welcom.html",data1)

def user(request):
    # data1={}
    return render(request,"gjobs/user.html",data1)

def jobs(request):
    data1={"range10":range(30)}
    return render(request,"gjobs/jobs.html",data1)

data2 = [{"a":"hello"}]
def jobsjson(request):
    _json = json.dumps(data2)
    return HttpResponse(_json)
