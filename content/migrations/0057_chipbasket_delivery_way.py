# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-09 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0056_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='chipbasket',
            name='delivery_way',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Delivery', verbose_name='\u0421\u043f\u043e\u0441\u043e\u0431 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438'),
        ),
    ]
