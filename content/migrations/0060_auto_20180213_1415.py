# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-13 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0059_auto_20180213_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='name',
            field=models.CharField(choices=[('1', '\u0421\u0430\u043c\u043e\u0432\u044b\u0432\u043e\u0437 \u0438\u0437 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430'), ('2', '\u041e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u043d\u0430 \u0441\u0435\u0431\u044f'), ('3', '\u041e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u043d\u0430 \u043a\u043b\u0438\u0435\u043d\u0442\u0430')], max_length=128, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435'),
        ),
    ]
