# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-07 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0051_auto_20180207_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='delivery',
            field=models.CharField(choices=[(1, '\u0421\u0430\u043c\u043e\u0432\u044b\u0432\u043e\u0437 \u0438\u0437 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430'), (2, '\u041e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u043d\u0430 \u0441\u0435\u0431\u044f'), (3, '\u041e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u043d\u0430 \u043a\u043b\u0438\u0435\u043d\u0442\u0430')], max_length=128, null=True),
        ),
    ]
