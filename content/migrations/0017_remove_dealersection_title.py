# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-03 12:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_auto_20180202_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealersection',
            name='title',
        ),
    ]
