# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re

from django import forms
from django.core.validators import validate_email, MinValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import ugettext, ugettext_lazy as _


class DeliveryDataForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':_('Имя получателя'),
                                                               'class':'input-field'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':_('Фамилия получателя'),
                                                              'class':'input-field'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':_('Город'),
                                                         'class':'input-field'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':_('Телефон клиента'),
                                                                 'class':'input-field'}))
    is_sms = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'chechbox_field'}),
                                required=False)
    nova_poshta_stock = forms.CharField(widget=forms.TextInput(attrs={'placeholder':_('Склад "Новой Почты"'),
                                                                      'class':'input-field'}))
    cod_sum = forms.FloatField(required=False,
                               widget=forms.NumberInput(attrs={'placeholder':_('Сумма наложенного платежа'),
                                                               'class':'input-field'}))
    is_cod = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'chechbox_field'}),
                                required=False)
    email = forms.CharField(validators=[validate_email],
                            required=False,
                            widget=forms.TextInput(attrs={'placeholder':_('E-mail'),
                                                          'class':'input-field'}))
    commentary = forms.CharField(required=False,
                                 widget=forms.Textarea(attrs={'placeholder':_('Комментарий'),
                                                              'class':'textarea-field'}))

    def clean(self):
        cleaned_data = super(DeliveryDataForm, self).clean()

        phone_number = cleaned_data.get('phone_number')
        if re.match(r'^\+{0,1}\d{9,15}$', phone_number) == None:
            self.add_error('phone_number', _('Неправильный формат телефона'))

        if cleaned_data.get('cod_sum'):
          if cleaned_data.get('cod_sum') < 0:
            self.add_error('cod_sum', _('Сумма должна быть больше 0.00'))

        if not self.errors:
            cleaned_data = {
                'first_name': cleaned_data.get('first_name'),
                'last_name': cleaned_data.get('last_name'),
                'city': cleaned_data.get('city'),
                'phone_number': cleaned_data.get('phone_number'),
                'is_sms': cleaned_data.get('is_sms', False),
                'nova_poshta_stock': cleaned_data.get('nova_poshta_stock'),
                'cod_sum': cleaned_data.get('cod_sum', 0),
                'is_cod': cleaned_data.get('is_cod', True),
                'email': cleaned_data.get('email', ''),
                'commentary': cleaned_data.get('commentary','')
            }

        return cleaned_data



class ContactForm(forms.Form):
    message = forms.CharField(max_length=2560,
                              widget=forms.Textarea(attrs={'name':'message'}))

