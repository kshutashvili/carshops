# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-14 13:02
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0066_remove_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='information',
            field=ckeditor.fields.RichTextField(default='', help_text='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435, \u043e\u0441\u043e\u0431\u0435\u043d\u043d\u043e\u0441\u0442\u0438 ...', verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430'),
        ),
    ]
