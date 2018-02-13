# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from content.models import ChipBasket
from users.models import User
from users.backends import AuthBackend
from users.forms import RegistrationForm, LoginForm

def user_create(request):
    if request.method == 'POST':
            form = RegistrationForm(request.POST)
            login_form = LoginForm()
            if form.is_valid():

                errors = {}

                if 'opt' not in request.POST.keys():
                        user = User()
                        user.first_name = request.POST['first_name']
                        user.last_name = request.POST['last_name']
                        user.phone_number = request.POST['phone_number']
                        user.email = request.POST['email']
                        user.set_password(request.POST['password'])
                        user.is_active = True
                        user.save()
                        return HttpResponseRedirect(reverse('home'))
                else:

                    site = request.POST.get('site')
                    if not site:
                        errors['site'] = _('Это поле обязательно')

                    information = request.POST.get('information')
                    if not information:
                        errors['information'] = _('Это поле обязательно')

                    dropshipp = request.POST.get('dropshipp')
                    if not dropshipp:
                        errors['dropshipp'] = _('Это поле обязательно')
                
                    if not errors:
                        user = User()
                        user.first_name = request.POST['first_name']
                        user.last_name = request.POST['last_name']
                        user.phone_number = request.POST['phone_number']
                        user.email = request.POST['email']
                        user.set_password(request.POST['password'])
                        user.dropshipp = request.POST['dropshipp']
                        user.site = request.POST['site']
                        user.information = request.POST['information']
                        user.save()
                        return HttpResponseRedirect(reverse('home'))
                    else:
                        messages.success(request, _('Исправьте ошибки'))
                        return render(request, 'login.html', {'form':form,
                                                              'login_form':login_form,
                                                              'errors':errors})
            else:
                messages.success(request, _('Исправьте ошибки'))
                return render(request, 'login.html', {'form':form,
                                                      'login_form':login_form,
                                                      'errors':form.errors})
    else:
        form = RegistrationForm()
        login_form = LoginForm()
        return render(request, 'login.html', {'form':form,
                                              'login_form':login_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = AuthBackend()
        user = auth.authenticate(username, password)
        if user is not None:
            login(request, user)
            if request.POST.get('remember_me') is not None:
                request.session.set_expiry(0)
            return render(request, 'lk.personal.html', {})
        else:
            messages.success(request, _("Неправильный логин или пароль"))
            return HttpResponseRedirect(reverse('login'),messages)
    else:
        form = RegistrationForm()
        login_form = LoginForm()
        return render(request, 'login.html', {'form':form,
                                              'login_form':login_form})


def user_logout(request):
    if request.session.has_key('basket_id'):
        basket = ChipBasket.objects.get(id=request.session['basket_id'])
        if not basket.is_framed:
            basket.delete()
    logout(request)
    form = RegistrationForm()
    login_form = LoginForm()
    return render(request,'login.html', {'form':form,
                                         'login_form':login_form})


