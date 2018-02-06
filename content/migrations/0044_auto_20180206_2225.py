# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-06 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0043_auto_20180206_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuheaderitem',
            name='link',
            field=models.CharField(help_text='\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u0441\u0441\u044b\u043b\u043a\u0443 \u0432\u0438\u0434\u0430 /#html_id \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 \u043b\u044d\u043d\u0434\u0438\u043d\u0433\u0430. \u041e\u0441\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u0441\u044b\u043b\u043a\u0438 \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e (https://...)', max_length=255, null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430'),
        ),
        migrations.AddField(
            model_name='menumainitem',
            name='link',
            field=models.CharField(help_text='\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u0441\u0441\u044b\u043b\u043a\u0443 \u0432\u0438\u0434\u0430 /#html_id \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 \u043b\u044d\u043d\u0434\u0438\u043d\u0433\u0430. \u041e\u0441\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u0441\u044b\u043b\u043a\u0438 \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e (https://...)', max_length=255, null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430'),
        ),
    ]
