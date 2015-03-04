#coding=utf-8
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Jobs(models.Model):
    path = models.CharField(max_length=200,verbose_name="任务路径")
    slug = models.SlugField(max_length=200)
    def __str__(self):    # __unicode__ on python2
        return self.path
    class Meta:
        verbose_name = "Jobs"

class JobInfo(models.Model):
    user  = models.ForeignKey(User,related_name="Jobs_user")
    owner = models.ForeignKey(User,related_name="Jobs_owner")
    jobsid = models.IntegerField()
    sttime = models.DateTimeField(default=datetime.now, verbose_name='启动时间')
    edtime = models.DateTimeField(default=datetime.now,verbose_name="结束时间")
    status = models.CharField(max_length=100)
    Result = models.CharField(max_length=200)
    # spend = models.IntegerField(null=True,blank=True,default=0)
    Job = models.ForeignKey(Jobs)
    def __str__(self):    # __unicode__ on python2
        return str(self.jobsid)
    class Meta:
        verbose_name = "JobInfo"

class Group(models.Model):
    name  = models.CharField(max_length=200,null=True,blank=True)
    jobs = models.ManyToManyField(Jobs)
    slug  = models.CharField(max_length=200)
    pass_numb = models.IntegerField()
    faild_numb = models.IntegerField()
    unkown_numb = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True,verbose_name="created time")
    def __str__(self):    # __unicode__ on python2
        return self.name
    class Meta:
        verbose_name = "Group"

class Project(models.Model):
    name  = models.CharField(max_length=400)
    is_vip = models.BooleanField(default=False,verbose_name="是否认证")
    slug  = models.CharField(max_length=200)
    group = models.ManyToManyField(Group)
    founder = models.ForeignKey(User,related_name="project_founder")
    members = models.ManyToManyField(User,related_name="project_members")
    created = models.DateTimeField(auto_now_add=True,verbose_name="created time")
    def __str__(self):    # __unicode__ on python2
        return self.name
        # return "tmp projct name"
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Project"     
