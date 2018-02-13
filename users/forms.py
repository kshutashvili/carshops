# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re

from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import ugettext, ugettext_lazy as _


class RegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':_('Имя')}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':_('Фамилия')}))
    email = forms.CharField(validators=[validate_email],
                            widget=forms.TextInput(attrs={'placeholder':_('E-mail')}))
    password = forms.CharField(validators=[validate_password],
                               widget=forms.PasswordInput(attrs={'placeholder':_('Пароль')}))
    rep_password = forms.CharField(validators=[validate_password],
                                   widget=forms.PasswordInput(attrs={'placeholder':_('Повторить пароль')}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'+380_________'}))
    site = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'placeholder':_('Ваш сайт'),
                                                         'name':'site'}))
    information = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'placeholder':_('Расскажите о вашей деятельности'),
                                                               'name':'information'}))

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()

        password = cleaned_data.get('password')
        rep_password = cleaned_data.get('rep_password')
        phone_number = cleaned_data.get('phone_number')

        if re.match(r'^\+{0,1}\d{9,15}$', phone_number) == None:
            self.add_error('phone_number', _('Неправильный формат телефона'))

        if password != rep_password:
            self.add_error('password', _('Введенные пароли не совпадают'))

        if not self.errors:
            cleaned_data = {
                'email': cleaned_data.get('email'),
                'phone_number': cleaned_data.get('phone_number'),
                'first_name': cleaned_data.get('first_name'),
                'last_name': cleaned_data.get('last_name'),
                'password': cleaned_data.get('password'),
            }

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':_('E-mail или номер телефона'),
                                                             'class':'login',
                                                             'name':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':_('Пароль'),
                                                                 'class':'password',
                                                                 'name':'password'}))