# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-08 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180208_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dropshipp',
            field=models.CharField(blank=True, choices=[('\u0422\u043e\u043b\u044c\u043a\u043e \u0434\u0440\u043e\u043f\u0448\u0438\u043f\u043f\u0438\u043d\u0433', '\u0422\u043e\u043b\u044c\u043a\u043e \u0434\u0440\u043e\u043f\u0448\u0438\u043f\u043f\u0438\u043d\u0433'), ('\u0418\u043d\u043e\u0433\u0434\u0430 \u043f\u043b\u0430\u043d\u0438\u0440\u0443\u044e', '\u0418\u043d\u043e\u0433\u0434\u0430 \u043f\u043b\u0430\u043d\u0438\u0440\u0443\u044e'), ('\u041d\u0435\u0442', '\u041d\u0435\u0442')], default='\u041d\u0435\u0442', max_length=32, null=True, verbose_name='\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0434\u0440\u043e\u043f\u0448\u0438\u043f\u043f\u0438\u043d\u0433'),
        ),
    ]
