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
    category = models.OneToOneField('MenuMainItem',
                                    verbose_name=_(u"Категория"),
                                    null=True,
                                    help_text=_(u"Выбирайте самые 'старшие' категории, у которых нету 'родителей'"))
    button_text = models.CharField(_(u"Текст в кнопке"),
                                   max_length=32)
    image = models.ImageField(_(u"Картинка на заднем фоне"),
                              upload_to="langing_products_images")
    order = models.IntegerField(_(u'Порядок'),
                                default=0)
    
    class Meta:
        verbose_name = _(u"Блок главной страницы")
        verbose_name_plural = _(u"Блоки главной страницы")

    def __unicode__(self):
        return self.category.name


class Blog(models.Model):
    title = models.CharField(_(u'Заголовок новости'),
                             max_length=128)
    content = RichTextField(_(u'Содержимое'))
    date = models.DateField(_(u'Дата анонса'))
    active = models.BooleanField(_(u"Включить/отключить новость"),
                                 default=False)
    image = models.ImageField(_(u"Картинка"),
                              null=True,
                              upload_to="blog_images")

    class Meta:
        verbose_name = _(u'Новость')
        verbose_name_plural = _(u'Новости')

    def __unicode__(self):
        return self.title


class InformationType(models.Model):
    """Тип контактной информации.
    Добавлять в админку нету смысла.
    """
    name = models.CharField(_(u"Тип информации"),
                            max_length=64,
                            help_text=_(u"Номер/Почта/Адрес/Расписание "
                                        "Использовать именно такие имена"))

    class Meta:
        verbose_name = _(u"Тип информации")
        verbose_name_plural = _(u"Типы информации")

    def __unicode__(self):
        return self.name


class Information(models.Model):
    """Контактная информация"""
    information = models.TextField(_(u"Информация"),
                                   help_text=_(u"Например: "
                                               "Номер: "
                                               "(063) 704-45-63 "
                                               "Почта: "
                                               "info@gmail.com "
                                               "Адрес: "
                                               "Киев,ул.Ушинского 14а "
                                               "Расписание: "
                                               "Пн-Пт:10.00-18.00 "
                                               "Сб-Вс:Выходной"))
    information_type = models.ForeignKey('InformationType',
                                         verbose_name=_(u"Тип информации"),
                                         related_name='information')

    class Meta:
        verbose_name = _(u"Контактная информация")
        verbose_name_plural = _(u"Контактная информация")

    def __unicode__(self):
        return " ".join([self.information_type.name, self.information])


class Product(models.Model):
    """Товар"""
    top_title = models.TextField(_(u"Заголовок над картинкой"))
    image = models.ImageField(_(u"Картинка"),
                              upload_to="products")
    title = models.TextField(_(u"Заголовок под картинкой"))
    code = models.CharField(_(u"Код товара"),
                            max_length=128)
    available = models.BooleanField(_(u"Наличие товара"),
                                    default=False)
    category = models.ForeignKey('MenuMainItem',
                                verbose_name=_(u"Категория товара"),
                                related_name="products",
                                null=True,
                                help_text=_(u"Указывайте самую нижнюю ступень категории. "
                                            "Т.е. категория-родитель/подкатегория1 <-товар, "
                                            "для товара указать подкатегорию1"))
    price = models.FloatField(_(u"Цена в долларах"))
    ppc_price = models.FloatField(_(u"РРС цена"),
                                 null=True,
                                 blank=True,
                                 help_text=_(u"Необязательное поле"))
    convert_price = models.FloatField(_(u"Цена в гривнах"))
    credit = models.FloatField(_(u"Кредит в %"),
                               null=True,
                               blank=True,
                               help_text=_(u"Необязательное поле"))

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товар"

    def __unicode__(self):
        return " | ".join([self.top_title,self.code])


class PopularProduct(models.Model):
    """Популярный товар"""
    product = models.OneToOneField('Product',
                                   verbose_name=_(u"Товар"),
                                   related_name="popular")

    class Meta:
        verbose_name = _(u"Популярный товар")
        verbose_name_plural = _(u"Популярные товары")

    def __unicode__(self):
        return self.product.__unicode__()


class DiscountProduct(models.Model):
    """Акционный товар"""
    product = models.OneToOneField('Product',
                                   verbose_name=_(u"Товар"),
                                   related_name="discount")
    discount = models.FloatField(_(u"Скидка в %"))

    class Meta:
        verbose_name = _(u"Акционный товар")
        verbose_name_plural = _(u"Акционные товары")

    def __unicode__(self):
        return self.product.__unicode__()