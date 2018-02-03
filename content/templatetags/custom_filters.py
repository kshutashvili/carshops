# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template


register = template.Library()

@register.filter
def get_last_character(string):
    """Получаем первую букву строки в верхнем регистре.
    Используем глобальную переменную, чтобы запомнить эту букву.
    Это нужно для фильтра is_changed_character
    """
    try:
        result = string[0].upper()
        global previous_last_character
        previous_last_character = result
    except:
        result = None

    return result


@register.filter
def is_changed_character(string):
    """Проверяем не изменилась ли первая буква марки."""
    try:
        if previous_last_character == string[0].upper():
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
            result = ' '.join([words[i] for i in range(arg_list[0],arg_list[1]+1)])
        else:
            result = False
    except Exception as e:
        result = False
    return result

