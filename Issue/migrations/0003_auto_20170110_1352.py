# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 05:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Issue', '0002_auto_20170110_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='sys_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]