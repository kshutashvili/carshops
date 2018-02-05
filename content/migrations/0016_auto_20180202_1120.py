# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-02 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_blog_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='active',
            field=models.BooleanField(default=False, verbose_name='\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c/\u043e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0441\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='block_images', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='landingproductblock',
            name='image',
            field=models.ImageField(upload_to='langing_products_images', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430 \u043d\u0430 \u0437\u0430\u0434\u043d\u0435\u043c \u0444\u043e\u043d\u0435'),
        ),
        migrations.AlterField(
            model_name='menumainitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu_items_images', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='image',
            field=models.ImageField(upload_to='social_icons', verbose_name='\u0418\u043a\u043e\u043d\u043a\u0430 \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0442\u0438'),
        ),
    ]