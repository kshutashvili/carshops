# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-01 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_auto_20180201_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='calendar_image',
            field=models.ImageField(help_text='\u041c\u0430\u043b\u0435\u043d\u044c\u043a\u0438\u0439 \u0440\u0430\u0437\u043c\u0435\u0440', upload_to=b'', verbose_name='\u0418\u043a\u043e\u043d\u043a\u0430 \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044f'),
        ),
    ]
