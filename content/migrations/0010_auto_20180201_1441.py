# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-01 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20180201_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingproductblock',
            name='image_height',
            field=models.IntegerField(default=200, help_text='\u0412 \u0446\u0435\u043b\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445', verbose_name='\u0412\u044b\u0441\u043e\u0442\u0430 \u0437\u0430\u0434\u043d\u0435\u0433\u043e \u0444\u043e\u043d\u0430'),
        ),
        migrations.AddField(
            model_name='landingproductblock',
            name='image_width',
            field=models.IntegerField(default=100, help_text='\u0412 \u0446\u0435\u043b\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445', verbose_name='\u0428\u0438\u0440\u0438\u043d\u0430 \u0437\u0430\u0434\u043d\u0435\u0433\u043e \u0444\u043e\u043d\u0430'),
        ),
        migrations.AddField(
            model_name='landingproductblock',
            name='order',
            field=models.IntegerField(default=0, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a'),
        ),
    ]
