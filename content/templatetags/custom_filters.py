# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from django import template

from content.models import ChipBasket


register = template.Library()

@register.filter
def get_first_character(string):
    """Получаем первую букву строки в верхнем регистре.
    Используем глобальную переменную, чтобы запомнить эту букву.
    Это нужно для фильтра is_changed_character
    """
    try:
        result = string[0].upper()
        global previous_first_character
        previous_first_character = result
    except:
        result = None

    return result


@register.filter
def is_changed_character(string):
    """Проверяем не изменилась ли первая буква марки."""
    try:
        if previous_first_character == string[0].upper():
            result = False
        else:
            result = True
    except Exception as e:
        result = None
    return result


@register.filter
def modulo(digit,divider):
    """Остаток от деления."""
    try:
        result = int(digit) % int(divider)
    except:
        result = None
    return result


@register.filter
def get_few_words(string,args):
    """В args передаем 1 или 2 параметра.
    Если 1 - возвращаем слово под этим индексом.
    Если 2 - слова от первого до последнего индекса включительно.
    Индексация начинается от 0.
    Разделитель слов - только пробел.
    Разделитель параметров - только запятая.
    """
    if args is None:
        result = False
    try:
        words = string.split()
        arg_list = [int(arg) for arg in args.split(',')]
        if len(arg_list) == 1:
            result = words[arg_list[0]]
        elif len(arg_list) == 2:
            if arg_list[1] < 0:
                arg_list[1] += len(words)
            else:
                arg_list[1] += 1
            result = ' '.join([words[i] for i in range(arg_list[0],arg_list[1])])
        else:
            result = False
    except Exception as e:
        result = False
    return result


@register.filter
def replace_comma_with_space(string):
    return  str(string).replace(',',' ')


@register.filter
def get_first_image_url(images,key_id):
    try:
        result = images[key_id][0].image.url
    except Exception as e:
        result = None
    return result


@register.filter
def get_basket_products_set(orders_baskets,key_id):
    try:
        result = orders_baskets[key_id]
    except Exception as e:
        result = None
    return result    


@register.filter
def create_id(string):
    try:
        result = string.lower().replace(' ','_')
    except Exception as e:
        result = ''
    return result


@register.filter
def get_first_last_years(model):
    """Результат в формате 1999-2000"""
    try:
        years = model.years.get_queryset()
        result = '-'.join([years.first().year,years.last().year]) 
    except Exception as e:
        result = e.message
    return result


@register.filter
def prod_count(basket_id):
    try:
        basket = ChipBasket.objects.get(id=basket_id)
        result = basket.count()
    except Exception as e:
        result = 0
    return result


@register.filter
def calculate_sum(basket_id, type_price):
    try:
        basket = ChipBasket.objects.get(id=basket_id)
        if type_price == 'price':
            result = basket.calculate_sum_price()
        elif type_price == 'ppc_price':
            result = basket.calculate_sum_ppc_price()
        elif type_price == 'convert_price':
            result = basket.calculate_sum_convert_price()
        elif type_price == 'convert_ppc_price':
            result = basket.calculate_sum_convert_ppc_price()
    except Exception as e:
        result = 0
    return result


@register.filter
def get_products_together_cheaper(togeth_cheap):
    try:
        result = togeth_cheap.products.iterator()
    except Exception as e:
        result = None
    return result


@register.filter
def calculate_sum_togeth_cheap(togeth_cheap, condition):
    if condition == 'opt':
        summ = 0
        for obj in togeth_cheap.products.iterator():
            summ += obj.get_convert_price()
        if togeth_cheap.percent:
            summ *= (1 - togeth_cheap.discount/100)
        else:
            summ -= togeth_cheap.discount
    else:
        summ = 0
        for obj in togeth_cheap.products.iterator():
            summ += obj.get_convert_ppc_price()
        if togeth_cheap.percent:
            summ *= (1 - togeth_cheap.discount/100)
        else:
            summ -= togeth_cheap.discount
    return round(summ, 2)


@register.filter
def discount(togeth_cheap, condition):
    if not togeth_cheap.percent:
        return togeth_cheap.discount
    else:  
        if condition == 'opt':
            summ = 0
            for obj in togeth_cheap.products.iterator():
                summ += obj.get_convert_price()
            return round(summ * togeth_cheap.discount/100, 2)
        else:
            summ = 0
            for obj in togeth_cheap.products.iterator():
                summ += obj.get_convert_price()
            return round(summ * togeth_cheap.discount/100, 2)            


@register.filter
def recalculate_with_rate(price, rate):
    return round(price * rate, 2)

