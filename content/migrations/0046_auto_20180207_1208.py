# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-07 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0045_product_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='TogetherCheaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField(verbose_name='\u0421\u043a\u0438\u0434\u043a\u0430')),
                ('percent', models.BooleanField(default=False, help_text='\u0415\u0441\u043b\u0438 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u043e, \u0442\u043e \u0432 % \u0415\u0441\u043b\u0438 \u043e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u043e, \u0442\u043e \u0432 UAH', verbose_name='\u0422\u0438\u043f \u0441\u043a\u0438\u0434\u043a\u0438')),
            ],
            options={
                'verbose_name': "\u041c\u043e\u0434\u0435\u043b\u044c '\u0432\u043c\u0435\u0441\u0442\u0435 \u0434\u0435\u0448\u0435\u0432\u043b\u0435'",
                'verbose_name_plural': "\u041c\u043e\u0434\u0435\u043b\u0438 '\u0432\u043c\u0435\u0441\u0442\u0435 \u0434\u0435\u0448\u0435\u0432\u043b\u0435'",
            },
        ),
        migrations.AddField(
            model_name='product',
            name='type_size',
            field=models.CharField(default='', max_length=255, verbose_name='\u0422\u0438\u043f\u043e\u0440\u0430\u0437\u043c\u0435\u0440'),
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.BooleanField(default=False, help_text='\u0415\u0441\u043b\u0438 \u0432\u043a\u043b\u044e\u0447\u0438\u0442\u044c, \u0442\u043e \u0433\u0440\u0438\u0432\u043d\u044b \u0415\u0441\u043b\u0438 \u043e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c, \u0442\u043e \u0434\u043e\u043b\u043b\u0430\u0440\u044b', verbose_name='\u0412\u0430\u043b\u044e\u0442\u0430, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u0446\u0435\u043d\u0443'),
        ),
        migrations.AddField(
            model_name='togethercheaper',
            name='products',
            field=models.ManyToManyField(to='content.Product', verbose_name='\u0422\u043e\u0432\u0430\u0440\u044b'),
        ),
    ]