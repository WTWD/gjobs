from django.shortcuts import render
from django.http import HttpResponse
import json
from models import *
# Create your views here.

data1={"range10":range(10)}
def index(request):
    users = User.objects.all()
    data1={"users":users,
    }
    return render(request,"gjobs/index.html",data1)

def userindex(request,user,proj):
    user_obj = User.objects.get(username=user)
    projects = Project.objects.filter(founder=user_obj)
    if not projects:
        act_proj_obj = None
    elif proj:
        act_proj_obj = Project.objects.get(slug=proj)
    else:
        act_proj_obj = projects[0]
    data1={"info":user,
        "range10":range(10),
        "user":user_obj,
        "act_proj":act_proj_obj,
        "projects":projects,
        }
    return render(request,"gjobs/userindex.html",data1)

def userindex2(request,user):
    return userindex(request,user,"")

def groupindex(request,group):
    group_obj = Group.objects.get(slug=group)
    data1={"info":group,
        "group":group_obj,
        }
    # group = Group.objects.all()[0]
    # project = Project.objects.all()[0]
    # data1 = {"group1":group,
    #         "project":project}
    return render(request,"gjobs/groupindex.html",data1)

def jobindex(request,job):
    data1={"info":job}
    return render(request,"gjobs/jobindex.html",data1)

def welcom(request):
    data1={}
    return render(request,"gjobs/welcom.html",data1)

def test(request):
    data1={}
    return render(request,"gjobs/test.html",data1)

def testjson(request):
    print request.POST
    print request.GET
    if request.method == 'POST':
        pass
        # method = "POST"
        # return HttpResponse(request.POST)
    elif request.method == "GET":
        pass
        # method = "GET"
        # return HttpResponse(request.GET)
    else:
        method = "EORROR "

    # print method

    data = {
        "info":"testjson",
    }
    jsondata = json.dumps(request.GET)
    print jsondata
    # jsondata = json.dumps(data)
    return HttpResponse(jsondata)
    
def projmanage(request):
    data ={
        "npname":"HOME",
        "npslug":"p3211",
    }
    projname = request.GET["projname"]
    username = request.GET["crtuser"]
    if not projname:
        return HttpResponse("")
    user = User.objects.get(username=username)
    p = Project(name=projname,founder=user)
    p.save()
    p.slug=myslug("p",p.id)
    p.save()
    data ={
        "npname":p.name,
        "npslug":p.slug,
    }
    jsondata = json.dumps(data)
    return HttpResponse(jsondata)

def jobs(request):
    data1={"range10":range(30)}
    return render(request,"gjobs/jobs.html",data1)

data2 = [{"a":"hello"}]
def jobsjson(request):
    _json = json.dumps(data2)
    return HttpResponse(_json)
