# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-22 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0074_comment_rait'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(to='content.ProductImage', verbose_name='\u0424\u043e\u0442\u043e \u0442\u043e\u0432\u0430\u0440\u0430'),
        ),
    ]
