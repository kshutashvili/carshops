# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-05 19:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0037_auto_20180205_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landingproductblock',
            name='link',
        ),
    ]
