# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-03 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0021_auto_20180203_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealersection',
            name='title',
            field=models.CharField(default='\u0425\u043e\u0447\u0435\u0448\u044c \u0441\u0442\u0430\u0442\u044c \u0434\u0438\u043b\u0435\u0440\u043e\u043c CARAV ?', help_text='\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 4 \u0441\u043b\u043e\u0432\u0430, \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u044f \u0438\u0445 \u043f\u0440\u043e\u0431\u0435\u043b\u0430\u043c\u0438\u043e\u0442\u0434\u0435\u043b\u0438\u0442\u0435 \u043f\u0440\u043e\u0431\u0435\u043b\u043e\u043c \u0438 \u0437\u043d\u0430\u043a \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f.', max_length=40, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 \u0434\u0438\u043b\u0435\u0440'),
        ),
    ]