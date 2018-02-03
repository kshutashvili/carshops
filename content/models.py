# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from solo.models import SingletonModel
from mptt.models import MPTTModel, TreeForeignKey, TreeManager

from django.db import models
from django.utils.translation import ugettext_lazy as _


class MenuHeaderItem(models.Model):
    """Пункт меню в хедере"""
    name = models.CharField(_(u'Название'),
                            max_length=50)
    link = models.CharField(_(u'URL-адрес'),
                            max_length=255,
                            help_text=_(u"Используйте ссылку вида /#html_id "
                                        "для блока лэндинга. Остальные ссылки "
                                        "указывать полностью (https://...)"))
    order = models.IntegerField(_(u'Порядок'),
                                default=0)

    class Meta:
        verbose_name = _(u'Пункт меню в шапке')
        verbose_name_plural = _(u'Пункты меню в шапке')
        ordering = ['order',]

    def __unicode__(self):
        return self.name


class MenuMainItem(MPTTModel):
    """Многоуровневые пункты в нижней части хедера"""
    parent = TreeForeignKey('self',
                            verbose_name=_(u'Родитель'),
                            related_name='subitems',
                            blank=True,
                            null=True)
    name = models.CharField(_(u'Название'),
                            max_length=128)
    link = models.CharField(_(u'URL-адрес'),
                            max_length=255,
                            blank=True,
                            help_text=_(u"Используйте ссылку вида /#html_id "
                                        "для блока лэндинга. Остальные ссылки "
                                        "указывать полностью (https://...)"))
    order = models.IntegerField(_(u'Порядок'),
                                default=0)
    image = models.ImageField(_(u'Картинка'),
                              upload_to="menu_items_images",
                              blank=True,
                              null=True)


    class Meta:
        verbose_name = _(u'Пункт/подпункт основного меню')
        verbose_name_plural = _(u'Пункты/подпункты основного меню')
        ordering = ['order',]

    class MPTTMeta:
        order_insertion_by=['order']

    def __unicode__(self):
        return self.name


class PhoneNumber(models.Model):
    number = models.CharField(_(u'Номер'),
                              max_length=24,
                              blank=True)

    class Meta:
        verbose_name = _(u'Номер телефона')
        verbose_name_plural = _(u'Номера телефонов')

    def __unicode__(self):
        return self.number


class DealerSection(SingletonModel):
    """Блок дилерам"""
    title = models.CharField(_(u"Заголовок блока дилер"),
                            max_length=40,
                            default=_(u"Хочешь стать дилером CARAV ?"),
                            help_text=_(u"Используйте 4 слова, разделяя их пробелами"
                                        "отделите пробелом и знак окончания предложения."))
    footer = models.CharField(_(u"Футер блока дилер"),
                              max_length=256,
                              default=_(u"С уважением, Коллектив интернет-магазина carav.com.ua"))
    content = RichTextField(_(u"Содержимое блока дилер"))
    link = models.CharField(_(u'URL-адрес'),
                            max_length=255,
                            help_text=_(u"Используйте ссылку вида /#html_id "
                                        "для блока лэндинга. Остальные ссылки "
                                        "указывать полностью (https://...)"))

    class Meta:
        verbose_name = _(u"Блок дилерам")
        verbose_name = _(u"Блоки дилерам")

    def __unicode__(self):
        return self.title


class SocialNetwork(models.Model):
    name = models.CharField(_(u"Название сети"),
                            max_length=64)
    image = models.ImageField(_(u"Иконка социальной сети"),
                              upload_to="social_icons")
    link = models.CharField(_(u"URL-адрес"),
                            max_length=255,
                            help_text=_(u"Используйте ссылку вида /#html_id "
                                        "для блока лэндинга. Остальные ссылки "
                                        "указывать полностью (https://...)"))
    class Meta:
        verbose_name = _(u"Социальная сеть")
        verbose_name_plural = _(u"Социальные сети")

    def __unicode__(self):
        return self.name


class LandingProductBlock(models.Model):
    """Товар на главной части страницы"""
    name = models.CharField(_(u"Название"),
                            max_length=64)
    button_text = models.CharField(_(u"Текст в кнопке"),
                                   max_length=32)
    image = models.ImageField(_(u"Картинка на заднем фоне"),
                              upload_to="langing_products_images")
    link = models.CharField(_(u"URL-адрес"),
                            max_length=255,
                            help_text=_(u"Используйте ссылку вида /#html_id "
                                        "для блока лэндинга. Остальные ссылки "
                                        "указывать полностью (https://...)"))
    order = models.IntegerField(_(u'Порядок'),
                                default=0)
    image_width = models.IntegerField(_(u"Ширина заднего фона"),
                                      help_text=_(u"В целых единицах"),
                                      default=100)
    image_height = models.IntegerField(_(u"Высота заднего фона"),
                                      help_text=_(u"В целых единицах"),
                                      default=200)
    
    class Meta:
        verbose_name = _(u"Блок главной страницы")
        verbose_name_plural = _(u"Блоки главной страницы")

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(_(u'Заголовок новости'),
                             max_length=128)
    content = models.TextField(_(u'Содержимое'))
    date = models.DateField(_(u'Дата анонса'))
    link = models.CharField(_(u'URL-адрес'),
                            max_length=255,
                            help_text=_(u"используйте ссылку вида /#html_id "
                                        "для блока лэндинга. Остальные ссылки "
                                        "указыватьполностью (https://...)"))
    active = models.BooleanField(_(u"Включить/отключить новость"),
                                 default=False)
    image = models.ImageField(_(u"Картинка"),
                              upload_to="block_images",
                              null=True)

    class Meta:
        verbose_name = _(u'Новость')
        verbose_name_plural = _(u'Новости')

    def __unicode__(self):
        return self.title



