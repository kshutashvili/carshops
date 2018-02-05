# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-05 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0031_auto_20180205_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(help_text='\u0423\u043a\u0430\u0437\u044b\u0432\u0430\u0439\u0442\u0435 \u0441\u0430\u043c\u0443\u044e \u043d\u0438\u0436\u043d\u044e\u044e \u0441\u0442\u0443\u043f\u0435\u043d\u044c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438. \u0422.\u0435. \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f-\u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044c/\u043f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f1 <-\u0442\u043e\u0432\u0430\u0440, \u0434\u043b\u044f \u0442\u043e\u0432\u0430\u0440\u0430 \u0443\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='content.MenuMainItem', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='product',
            name='convert_price',
            field=models.FloatField(verbose_name='\u0426\u0435\u043d\u0430 \u0432 \u0433\u0440\u0438\u0432\u043d\u0430\u0445'),
        ),
    ]
