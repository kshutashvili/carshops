# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from solo.models import SingletonModel
from mptt.models import MPTTModel, TreeForeignKey, TreeManager
from PIL import Image

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator
from django.utils.safestring import mark_safe

from users.models import User


class MenuHeaderItem(models.Model):
    """Пункт меню в хедере"""
    name = models.CharField(_('Название'),
                            max_length=50)
    order = models.IntegerField(_('Порядок'),
                                default=0)
    link = models.CharField(_('Ссылка'),
                            max_length=255,
                            null=True,
                            help_text=_("Используйте ссылку вида /#html_id "
                                        "для блока лэндинга. Остальные ссылки "
                                        "указывать полностью (https://...)"))

    class Meta:
        verbose_name = _('Пункт меню в шапке')
        verbose_name_plural = _('Пункты меню в шапке')
        ordering = ['order',]

    def __unicode__(self):
        return self.name


class MenuMainItem(MPTTModel):
    """Многоуровневые пункты в нижней части хедера"""
    parent = TreeForeignKey('self',
                            verbose_name=_('Родитель'),
                            related_name='subitems',
                            blank=True,
                            null=True)
    name = models.CharField(_('Название'),
                            max_length=128)
    order = models.IntegerField(_('Порядок'),
                                default=0)
    image = models.ImageField(_('Картинка'),
                              upload_to="menu_items_images",
                              blank=True,
                              null=True)
    link = models.CharField(_('Ссылка'),
                            max_length=255,
                            null=True,
                            help_text=_("Используйте ссылку вида /#html_id "
                                        "для блока лэндинга. Остальные ссылки "
                                        "указывать полностью (https://...)"))

    class Meta:
        verbose_name = _('Пункт/подпункт основного меню')
        verbose_name_plural = _('Пункты/подпункты основного меню')
        ordering = ['order',]

    class MPTTMeta:
        order_insertion_by=['order']

    def __unicode__(self):
        return self.name


class DealerSection(SingletonModel):
    """Блок дилерам"""
    title = models.CharField(_("Заголовок блока дилер"),
                            max_length=40,
                            default=_("Хочешь стать дилером CARAV ?"),
                            help_text=_("Используйте 4 слова, разделяя их пробелами"
                                        "отделите пробелом и знак окончания предложения."))
    footer = models.CharField(_("Футер блока дилер"),
                              max_length=256,
                              default=_(u"С уважением, Коллектив интернет-магазина carav.com.ua"))
    content = RichTextField(_("Содержимое блока дилер"))

    class Meta:
        verbose_name = _("Блок дилерам")
        verbose_name = _("Блоки дилерам")

    def __unicode__(self):
        return self.title


class SocialNetwork(models.Model):
    name = models.CharField(_("Название сети"),
                            max_length=64)
    image = models.ImageField(_("Иконка социальной сети"),
                              upload_to="social_icons")
    link = models.CharField(_("URL-адрес"),
                            max_length=255,
                            help_text=_("Используйте ссылку вида /#html_id "
                                        "для блока лэндинга. Остальные ссылки "
                                        "указывать полностью (https://...)"))

    class Meta:
        verbose_name = _("Социальная сеть")
        verbose_name_plural = _("Социальные сети")

    def __unicode__(self):
        return self.name


class LandingProductBlock(models.Model):
    """Товар на главной части страницы"""
    category = models.OneToOneField('MenuMainItem',
                                    verbose_name=_("Категория"),
                                    null=True,
                                    help_text=_("Выбирайте самые 'старшие' категории, у которых нету 'родителей'"))
    button_text = models.CharField(_("Текст в кнопке"),
                                   max_length=32,
                                   default=_('Подробнее'))
    image = models.ImageField(_("Картинка на заднем фоне"),
                              upload_to="langing_products_images")
    order = models.IntegerField(_('Порядок'),
                                default=0)

    class Meta:
        verbose_name = _("Блок главной страницы")
        verbose_name_plural = _("Блоки главной страницы")

    def __unicode__(self):
        return self.category.name


class Blog(models.Model):
    title = models.CharField(_('Заголовок новости'),
                             max_length=128)
    content = RichTextField(_('Содержимое'))
    date = models.DateField(_('Дата анонса'))
    active = models.BooleanField(_("Включить/отключить новость"),
                                 default=False)
    image = models.ImageField(_("Картинка"),
                              null=True,
                              upload_to="blog_images")

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')

    def __unicode__(self):
        return self.title

    def as_dict(self):
        return {"id":self.id,
                "title":self.title,
                "content":self.content,
                "date":str(self.date),
                "active":self.active,
                "image.url":self.image.url}


class InformationType(models.Model):
    """Тип контактной информации."""
    name = models.CharField(_("Тип информации"),
                            max_length=64,
                            help_text=_("Номер/Почта/Адрес/Расписание "
                                        "Использовать именно такие имена"))

    class Meta:
        verbose_name = _("Тип информации")
        verbose_name_plural = _("Типы информации")

    def __unicode__(self):
        return self.name


class Information(models.Model):
    """Контактная информация"""
    information = models.TextField(_("Информация"),
                                   help_text=_("Например: "
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
                                         verbose_name=_("Тип информации"),
                                         related_name='information')

    class Meta:
        verbose_name = _("Контактная информация")
        verbose_name_plural = _("Контактная информация")

    def __unicode__(self):
        return " ".join([self.information_type.name, self.information])


class Product(models.Model):
    """Товар"""
    name = models.CharField(_('Название товара'),
                            max_length=128,
                            null=True)
    category = models.ForeignKey("MenuHeaderItem",
                                 verbose_name=_('Категория'),
                                 null=True)
    information = RichTextField(_("Описание товара"),
                                default='',
                                help_text=_("Описание, особенности ..."))
    type_size = models.CharField(_("Типоразмер"),
                                default="",
                                max_length=255)
    code = models.CharField(_("Код товара"),
                            max_length=128,
                            unique=True)
    available = models.BooleanField(_("Наличие товара"),
                                    default=False)
    category = models.ForeignKey('MenuMainItem',
                                verbose_name=_("Категория товара"),
                                related_name="products",
                                null=True,
                                help_text=_("Указывайте самую нижнюю ступень категории. "
                                            "Т.е. категория-родитель/подкатегория1 <-товар, "
                                            "для товара указать подкатегорию1"))
    price = models.FloatField(_("Цена для оптовиков (доллар)"))
    ppc_price = models.FloatField(_("РРС цена (доллар)"),
                                  default=0,
                                  help_text="Розничная цена")
    course = models.FloatField(_("Курс доллара к гривне"),
                               default=25)
    credit = models.FloatField(_("Кредит в %"),
                               null=True,
                               blank=True,
                               help_text=_("Необязательное поле"))
    car_compatibility = models.ManyToManyField('ModelCar',
                                               verbose_name=_("Совместимость с машинами"))
    rait = models.ForeignKey('Rait',
                             verbose_name=_("Рейтинг товара"),
                             related_name=_("product"),
                             null=True)
    images = models.ManyToManyField('ProductImage',
                                    verbose_name=_('Фото товара'))
    currency = models.BooleanField(_("Валюта, в которой отображать цену"),
                                   default=False,
                                   help_text=_("Если включить, то UAH "
                                               "Если отключить, то $"))

    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товар")

    def __unicode__(self):
        return " | ".join([self.category.name, self.code])

    def get_convert_ppc_price(self):
        return self.ppc_price * self.course

    def get_convert_price(self):
        return self.price * self.course

    def get_compatibility_models(self):
        return self.car_compatibility.get_queryset()


class PopularProduct(models.Model):
    """Популярный товар"""
    product = models.OneToOneField('Product',
                                   verbose_name=_("Товар"),
                                   related_name="popular")

    class Meta:
        verbose_name = _("Популярный товар")
        verbose_name_plural = _("Популярные товары")

    def __unicode__(self):
        return ' | '.join([self.product.category.name, self.product.code])


class DiscountProduct(models.Model):
    """Акционный товар"""
    product = models.OneToOneField('Product',
                                   verbose_name=_("Товар"),
                                   related_name="discount")
    discount = models.FloatField(_("Скидка"))
    percent = models.BooleanField(_("Вид скидки"),
                                  default=False,
                                  help_text=_("Если включено, то скидка в % "
                                              "Если отключено, то скидка в UAH"),)

    class Meta:
        verbose_name = _("Акционный товар")
        verbose_name_plural = _("Акционные товары")

    def __unicode__(self):
        return ' | '.join([self.product.category.name, self.product.code])

    def get_new_ppc_price(self):
        if self.percent:
            disc_value = self.discount/100
        else:
            disc_value = self.discount/self.product.ppc_price
        return self.product.ppc_price * (1 - disc_value)

    def get_new_convert_ppc_price(self):
        if self.percent:
            disc_value = self.discount/100
        else:
            disc_value = self.discount/self.product.ppc_price
        return self.product.get_convert_ppc_price() * (1 - disc_value)

    def get_new_price(self):
        if self.percent:
            disc_value = self.discount/100
        else:
            disc_value = self.discount/self.product.price
        return self.product.price * (1 - disc_value)

    def get_new_convert_price(self):
        if self.percent:
            disc_value = self.discount/100
        else:
            disc_value = self.discount/self.product.price
        return self.product.get_convert_price() * (1 - disc_value)


class ProductImage(models.Model):
    """Картинки для товара."""
    image = models.ImageField(_("Картинка"),
                              upload_to="product_photos")

    class Meta:
        verbose_name = _("Фото товара")
        verbose_name_plural = _("Фото товаров")

    def save(self):
        if not self.image:
            return
        super(ProductImage, self).save()
        image = Image.open(self.image)
        (width, height) = image.size
        factor = max(width,height)
        if factor > 300:
            k_factor = 300./factor
            size = (int(width * k_factor), int(height * k_factor))
            image = image.resize(size, Image.ANTIALIAS)
            image.save(self.image.path)

    def __unicode__(self):
        return str(self.id)

    def image_tag(self, width=250, height=250):
        return mark_safe('<img src="%s" width="%d" height="%d" />' % (self.image.url, width, height))

    image_tag.short_description = 'Image'


class Rait(models.Model):
    value = models.IntegerField(_("Рейтинг"))

    class Meta:
        verbose_name = _("Рейтинг")
        verbose_name_plural = _("Рейтинги")

    def __unicode__(self):
        return str(self.value)


class Banner(models.Model):
    content = RichTextField(_("Содержимое"))

    class Meta:
        verbose_name = _("Баннер")
        verbose_name_plural = _("Баннеры между товарами на странице каталога")

    def __unicode__(self):
        return self.content


class TogetherCheaper(models.Model):
    """'Вместе дешевле'."""
    name = models.CharField(_("Название"),
                            max_length=128,
                            default="",
                            help_text=_("Название для отображения в админке"))
    products = models.ManyToManyField('Product',
                                      verbose_name=_("Товары"))
    discount = models.FloatField(_("Скидка"))
    percent = models.BooleanField(_("Тип скидки"),
                                 default=False,
                                 help_text=_("Если включено, то в % "
                                             "Если отключено, то в UAH"))

    class Meta:
        verbose_name = _("Модель 'вместе дешевле'")
        verbose_name_plural = _("Модели 'вместе дешевле'")

    def __unicode__(self):
        if self.percent:
            currency = '% '
        else:
            currency = 'UAH '
        return ' '.join([self.name,str(self.discount),currency])


class StampCar(models.Model):
    name = models.CharField(_("Наименование"),
                            max_length=64)
    image = models.ImageField(_("Иконка"),
                              upload_to="car_icons")
    link = models.CharField(_("URL-адрес"),
                            max_length=255,
                            help_text=_("Используйте ссылку вида /#html_id "
                                        "для блока лэндинга. Остальные ссылки "
                                        "указывать полностью (https://...)"))
    information = models.TextField(_("Описание"))

    class Meta:
        verbose_name = _("Марка автомобиля")
        verbose_name_plural = _("Марки автомобилей")

    def save(self):
        if not self.image:
            return
        super(StampCar, self).save()
        image = Image.open(self.image)
        width,height = 80, 80
        size = (width, height)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.image.path)

    def __unicode__(self):
        return self.name


class ModelCar(models.Model):
    name = models.CharField(_("Наименование"),
                            max_length=128)
    stamp = models.ForeignKey('StampCar',
                              verbose_name=_("Марка автомобиля"),
                              related_name="models")
    years = models.ManyToManyField('YearCar',
                                   verbose_name=_("Года выпуска"))
    link = models.CharField(_("URL-адрес"),
                            max_length=255,
                            help_text=_("Используйте ссылку вида /#html_id "
                                        "для блока лэндинга. Остальные ссылки "
                                        "указывать полностью (https://...)"))
    information = models.TextField(_("Описание"))

    class Meta:
        verbose_name = _("Модель автомобиля")
        verbose_name_plural = _("Модели автомобилей")

    def __unicode__(self):
        return ' '.join([self.stamp.name,self.name])


class YearCar(models.Model):
    year = models.CharField(_("Год выпуска"),
                            max_length=4)

    class Meta:
        verbose_name = _("Год выпуска машины")
        verbose_name_plural = _("Года выпуска машин")

    def __unicode__(self):
        return self.year


class ChipBasket(models.Model):
    products = models.ManyToManyField('Product',
                                      verbose_name=_("Товар"),
                                      through='BasketProduct')
    is_framed = models.BooleanField(_('Связана с заказом'),
                                    default=False)

    class Meta:
        verbose_name = _("Покупочная корзина")
        verbose_name_plural = _("Покупочные корзины")

    def __unicode__(self):
        result = ' '.join(['Корзина ID:', str(self.id)])
        if self.is_framed:
            result = ''.join([result, ' | Связана с заказом'])
        return result

    def calculate_sum_ppc_price(self):
        summ = 0
        try:
            for obj in self.basketproduct_set.iterator():
                summ += obj.product.discount.get_new_ppc_price() * obj.amount
        except DiscountProduct.DoesNotExist as e:
            summ = 0
            for obj in self.basketproduct_set.iterator():
                summ += obj.product.ppc_price * obj.amount
        return summ

    def calculate_sum_price(self):
        summ = 0
        try:
            for obj in self.basketproduct_set.iterator():
                summ += obj.product.discount.get_new_price() * obj.amount
        except DiscountProduct.DoesNotExist as e:
            summ = 0
            for obj in self.basketproduct_set.iterator():
                summ += obj.product.price * obj.amount
        return summ

    def calculate_sum_convert_ppc_price(self):
        summ = 0
        try:
            for obj in self.basketproduct_set.iterator():
                summ += obj.product.discount.get_new_convert_ppc_price() * obj.amount
        except DiscountProduct.DoesNotExist as e:
            summ = 0
            for obj in self.basketproduct_set.iterator():
                summ += obj.product.get_convert_ppc_price() * obj.amount
        return summ

    def calculate_sum_convert_price(self):
        summ = 0
        try:
            for obj in self.basketproduct_set.iterator():
                summ += obj.product.discount.get_new_convert_price() * obj.amount
        except DiscountProduct.DoesNotExist as e:    
            summ = 0
            for obj in self.basketproduct_set.iterator():
                summ += obj.product.get_convert_price() * obj.amount
        return summ

    def count(self):
        count = 0
        for obj in self.basketproduct_set.iterator():
            count += obj.amount
        return count


class BasketProduct(models.Model):
    """Промежуточная таблица между Корзиной и Товаром"""
    basket = models.ForeignKey('ChipBasket',
                               verbose_name=_("Корзина"))
    product = models.ForeignKey('Product',
                                verbose_name=_("Товар"))
    amount = models.IntegerField(_("Количество"),
                                 default=1)

    class Meta:
        verbose_name = _("Промежуточная таблица Корзина-Товар")
        verbose_name_plural = _("Промежуточные таблицы Корзина-Товар")

    def __unicode__(self):
        bask = "ID корзины :"
        prod = "Код товара :"
        am = "Количество :"
        return " ".join([bask, str(self.basket.id), "|", prod, str(self.product.code), "|", am, str(self.amount)])


class DeliveryData(models.Model):
    """Данные о доставке"""
    first_name = models.CharField(_("Имя"),
                                  max_length=64)
    last_name = models.CharField(_("Фамилия"),
                                 max_length=64)
    city = models.CharField(_("Город"),
                            max_length=128)
    phone_number = models.CharField(_("Номер телефона"),
                                    max_length=32)
    is_sms = models.BooleanField(_("Отправить СМС с номером ТНН"),
                                 default=False)
    nova_poshta_stock = models.CharField(_('Склад "Новой Почты"'),
                                         max_length=64)
    cod_sum = models.FloatField(_("Сумма наложенного платежа"),
                                null=True,
                                blank=True)
    is_cod = models.BooleanField(_("Отправка без денег"),
                                 default=False)
    email = models.EmailField(_("Электронная почта"))
    commentary = models.TextField(_("Комментарий"),
                                  null=True,
                                  blank=True)

    class Meta:
        verbose_name = _("Данные о доставке")
        verbose_name_plural = _("Данные о доставках")

    def __unicode__(self):
        return ' '.join([self.first_name,self.last_name,self.city,self.nova_poshta_stock])


class DeliveryWay(models.Model):
    name = models.CharField(_('Наименование'),
                            max_length=128)

    class Meta:
        verbose_name = _('Способ доставки')
        verbose_name_plural = _('Способы доставки')

    def __unicode__(self):
        return self.name


class Delivery(models.Model):
    delivery_way = models.ForeignKey('DeliveryWay',
                                     verbose_name=_('Способ доставки'),
                                     null=True)
    price = models.FloatField(_("Стоимость"),
                              null=True,
                              blank=True)
    class Meta:
        verbose_name = _("Доставка")
        verbose_name_plural = _("Доставки")

    def __unicode__(self):
        return self.delivery_way.name


ORDER_STATUS_CHOICES = (
    ('Оформлен','Оформлен'),
    ('В обработке','В обработке'),
    ('Оплачен','Оплачен'),
    ('Закончен','Закончен')
)

class Order(models.Model):
    status = models.CharField(_('Статус заказа'),
                              max_length=128,
                              choices=ORDER_STATUS_CHOICES,
                              default='Создан')
    cod = models.CharField(_('ТНН'),
                           max_length=32,
                           null=True,
                           blank=True)
    basket = models.OneToOneField('ChipBasket',
                                  verbose_name=_('Корзина'),
                                  related_name='order')
    delivery = models.OneToOneField('Delivery',
                                    verbose_name=_('Доставка'),
                                    null=True)
    delivery_data = models.OneToOneField('DeliveryData',
                                         verbose_name=_('Данные о доставке'))
    user = models.ForeignKey(User,
                            verbose_name=_('Зарегестрированный клиент'),
                            null=True,
                            blank=True)
    created = models.DateField(_('Дата заказа'),
                               auto_now_add=True)
    delivered = models.DateField(_('Дата доставки'),
                                 null=True,
                                 blank=True)

    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")

    def __unicode__(self):
        return ' | '.join([str(self.id), self.status])


class PersonalAccount(models.Model):
    delivery_city = models.CharField(_("Город доставки"),
                                     max_length=128,
                                     null=True,
                                     blank=True)
    delivery_address = models.CharField(_("Адрес доставки"),
                                        max_length=128,
                                        null=True,
                                        blank=True)
    delivery_way = models.ForeignKey('DeliveryWay',
                                     verbose_name=_('Способ доставки'),
                                     null=True,
                                     blank=True)
    user = models.OneToOneField(User,
                                verbose_name=_('Пользователь'))
    balance = models.DecimalField(_('Баланс в $'),
                                  decimal_places=2,
                                  max_digits=20,
                                  validators=[MinValueValidator(0.00)],
                                  default=0)

    class Meta:
        verbose_name = _('Персональный аккаунт')
        verbose_name_plural = _('Персональные аккаунты')

    def __unicode__(self):
        if self.user.first_name and self.user.last_name:
            result = ' '.join([self.user.first_name, self.user.last_name])
        else:
            result = ' '.join(['Незаполненный аккаунт', str(self.id)])
        return result


class ExchangeRate(SingletonModel):
    rate_buy = models.DecimalField(_('Курс доллара к гривне, продажа'),
                                   decimal_places=2,
                                   max_digits=5,
                                   validators=[MinValueValidator(0.00)])
    rate_sale = models.DecimalField(_('Курс доллара к гривне, покупка'),
                                   decimal_places=2,
                                   max_digits=5,
                                   validators=[MinValueValidator(0.00)],
                                   null=True)

    class Meta:
        verbose_name = _('Курс доллара к гривне')
        verbose_name_plural = _('Курс доллара к гривне')

    def __unicode__(self):
        return 'Продажа: 1 USD = %s UAH  Покупка: 1 USD = %s UAH' % (str(self.rate_buy), str(self.rate_sale))


class Comment(MPTTModel):
    product = models.ForeignKey('Product',
                                verbose_name=_('Товар'),
                                related_name='comments')
    name = models.CharField(_('Имя того, кто оставил комментарий'),
                            max_length=64)
    rait = models.ForeignKey('Rait',
                             verbose_name=_('Рейтинг'),
                             null=True)
    date = models.DateField(_('Дата'),
                            auto_now_add=True)
    content = models.TextField(_('Комментарий'))
    parent = TreeForeignKey('self',
                            verbose_name=_('Родитель'),
                            related_name='subitems',
                            blank=True,
                            null=True)

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

    def __unicode__(self):
        return ' '.join([self.name, str(self.date)])


