# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gjobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Group'},
        ),
        migrations.AlterModelOptions(
            name='jobinfo',
            options={'verbose_name': 'JobInfo'},
        ),
        migrations.AlterModelOptions(
            name='jobs',
            options={'verbose_name': 'Jobs'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Project'},
        ),
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
