# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Issue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='close_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]