# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-13 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0061_auto_20180213_1423'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name': '\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430', 'verbose_name_plural': '\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0438'},
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivery_way',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.DeliveryWay', verbose_name='\u0421\u043f\u043e\u0441\u043e\u0431 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438'),
        ),
    ]
