# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 09:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Issue', '0009_auto_20170111_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='close_date',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='start_date',
        ),
    ]
