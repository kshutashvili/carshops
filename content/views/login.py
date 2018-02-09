# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from users.models import User

def user_create(request):
    if request.method == 'POST':
        if request.POST.get('create') is not None:
            errors = {}
            data = {}

            first_name = request.POST.get('name').strip()
            if not first_name:
                errors['first_name'] = _('Это поле обязательно')
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name').strip()
            if not last_name:
                errors['last_name'] = _('Это поле обязательно')
            else:
                data['last_name'] = last_name

            phone_number = request.POST.get('phone_number').strip()
            if re.match(r'^\+{0,1}\d{9,15}$', phone_number) == None:
                errors['phone_number'] = _('Введите правильный номер телефона')
            else:
                data['phone_number'] = phone_number

            email = request.POST.get('email').strip()
            if re.match(r'^[A-z0-9\.\+_-]+@[A-Za-z0-9\_-]+\.[a-zA-Z]+$', email) == None:
                errors['email'] = _('Введите правильный электронный адресс')
            else:
                data['email'] = email

            password = request.POST.get('password')
            rep_pass = request.POST.get('rep_pass')
            if not password:
                errors['password'] = _('Введите пароль')
            elif len(password) < 8:
                errors['password'] = _('Пароль должен состоять минимум из 8 символов')
            elif re.match(r'^[A-z]+', password) == None:
                errors['password'] = _('Пароль должен содержать хотя бы одну букву')
            elif password != rep_pass:
                errors['password'] = _('Пароли должны совпадать')
            else:
                data['password'] = password
                pass

            if 'website' not in request.POST.keys():
                if not errors:
                    user = User()
                    user.first_name = data['first_name']
                    user.last_name = data['last_name']
                    user.phone_number = data['phone_number']
                    user.email = data['email']
                    user.set_password(data['password'])
                    user.is_active = True
                    user.save()
                    return HttpResponseRedirect(reverse('home'))
                else:
                    messages.success(request, _('Исправьте ошибки'))
                    return render(request, 'login.html', {'errors':errors})
            else:

                site = request.POST.get('website')
                if not site:
                    errors['website'] = _('Это поле обязательно')
                else:
                    data['site'] = site

                information = request.POST.get('information')
                if not information:
                    errors['information'] = _('Это поле обязательно')
                else:
                    data['information'] = information

                dropshipping = request.POST.get('dropshipping')
                if not dropshipping:
                    errors['dropshipping'] = _('Это поле обязательно')
                else:
                    data['dropshipping'] = dropshipping
                
                if not errors:
                    user = User()
                    user.first_name = data['first_name']
                    user.last_name = data['last_name']
                    user.phone_number = data['phone_number']
                    user.email = data['email']
                    user.set_password(data['password'])
                    user.dropshipp = data['dropshipping']
                    user.site = data['site']
                    user.information = data['information']
                    user.save()
                    return HttpResponseRedirect(reverse('home'))
                else:
                    messages.success(request, _('Исправьте ошибки'))
                    return render(request, 'login.html', {'errors':errors})
    else:
        return render(request, 'login.html', {})

