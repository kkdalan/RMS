# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Issue', '0010_auto_20170111_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='close_date',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='issue',
            name='end_date',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='issue',
            name='start_date',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]