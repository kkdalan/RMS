# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Issue', '0005_auto_20170110_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
