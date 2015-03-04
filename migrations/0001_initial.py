# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(max_length=200)),
                ('pass_numb', models.IntegerField()),
                ('faild_numb', models.IntegerField()),
                ('unkown_numb', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jobsid', models.IntegerField()),
                ('sttime', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe5\x90\xaf\xe5\x8a\xa8\xe6\x97\xb6\xe9\x97\xb4')),
                ('edtime', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4')),
                ('status', models.CharField(max_length=100)),
                ('Result', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=200, verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe8\xb7\xaf\xe5\xbe\x84')),
                ('slug', models.SlugField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('is_vip', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xae\xa4\xe8\xaf\x81')),
                ('slug', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created time')),
                ('founder', models.ForeignKey(related_name='project_founder', to=settings.AUTH_USER_MODEL)),
                ('group', models.ManyToManyField(to='gjobs.Group')),
                ('members', models.ManyToManyField(related_name='project_members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='jobinfo',
            name='Job',
            field=models.ForeignKey(to='gjobs.Jobs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='jobinfo',
            name='owner',
            field=models.ForeignKey(related_name='Jobs_owner', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='jobinfo',
            name='user',
            field=models.ForeignKey(related_name='Jobs_user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='jobs',
            field=models.ManyToManyField(to='gjobs.Jobs'),
            preserve_default=True,
        ),
    ]
