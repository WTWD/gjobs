#coding=utf-8
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

myslug = lambda mode,id:mode+"%04d"%id  
# Create your models here.
class Job(models.Model):
    path = models.CharField(max_length=200,unique=True,verbose_name="任务路径")
    slug = models.SlugField(blank=True,max_length=50)
    def __str__(self):    # __unicode__ on python2
        return self.path
    class Meta:
        verbose_name = "Job"
        verbose_name_plural= "Job任务"


class Jobhis(models.Model):
    Status_choice = (
        (0,'Ready'),
        (1,'Running...'),
        (2,'Finish'),
        (3,'Stoped'),
    )
    user  = models.ForeignKey(User,related_name="Job_user")
    owner = models.ForeignKey(User,related_name="Job_owner")
    slug = models.SlugField(blank=True,max_length=50)
    jobsid = models.IntegerField()
    sttime = models.DateTimeField(default=datetime.now, verbose_name='启动时间')
    edtime = models.DateTimeField(default=datetime.now,verbose_name="结束时间")
    status = models.IntegerField(choices=Status_choice,default=0,verbose_name="状态")
    result = models.CharField(max_length=200)
    spend = models.IntegerField(default=0)
    job = models.ForeignKey(Job)
    def __str__(self):    # __unicode__ on python2
        return str(self.jobsid)
    class Meta:
        verbose_name = "Jobhis"
        verbose_name_plural= "Job历史"

class Group(models.Model):
    name  = models.CharField(max_length=200,null=True,blank=True)
    jobs = models.ManyToManyField(Job)
    slug  = models.CharField(max_length=50,blank=True)
    pass_numb = models.IntegerField(default=0)
    faild_numb = models.IntegerField(default=0)
    unkown_numb = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name="created time")
    def __str__(self):    # __unicode__ on python2
        return self.name
    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "任务表"     

class Project(models.Model):
    name  = models.CharField(max_length=400)
    is_vip = models.BooleanField(default=False,verbose_name="是否认证")
    slug  = models.CharField(max_length=50,blank=True)
    group = models.ManyToManyField(Group)
    founder = models.ForeignKey(User,related_name="project_founder")
    members = models.ManyToManyField(User,related_name="project_members")
    created = models.DateTimeField(auto_now_add=True,verbose_name="created time")
    def __str__(self):    # __unicode__ on python2
        return self.name
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "项目"     


# def save(self,*args,**kwargs):
#     self.slug = myslug("j",self.id)
#     super(Jobs,self).save(*args, **kwargs) 
# def save(self,*args,**kwargs):
#     self.slug = myslug("jh",self.id)
#     super(JobInfo,self).save(*args, **kwargs) 
# def save(self,*args,**kwargs):
#     self.slug = myslug("g",self.id)
#     super(Group,self).save(*args, **kwargs) 
# def save(self,*args,**kwargs):
#     self.slug = myslug("p",self.id)
#     super(Project,self).save(*args, **kwargs) 
