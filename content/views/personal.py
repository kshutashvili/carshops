# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import urllib
import ast
import requests

from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, EmailMessage

from carav.settings import ADMIN_EMAIL
from content.models import Order, DeliveryWay, PersonalAccount, ProductImage
from content.forms import ContactForm


@login_required
def personal(request):
    if request.method == 'GET':
        orders = Order.objects.filter(user=request.user).order_by('created').reverse()[:3]
        account = PersonalAccount.objects.filter(user=request.user).first()
        if not account:
            account = PersonalAccount()
            account.user = request.user
            account.save()
        delivery_ways = DeliveryWay.objects.all()
        social_user = request.user.social_auth.filter(provider='facebook').first()
        if social_user:
            response = requests.get('https://graph.facebook.com/me?fields=id,email',
                                    params={'access_token': social_user.extra_data['access_token']})
            request.user.email = response.json()['email']
            request.user.save()
        else:
            social_user = request.user.social_auth.filter(provider='google-oauth2').first()
            if social_user:
                response = requests.get('https://www.googleapis.com/userinfo/v2/me',
                                        params={'access_token': social_user.extra_data['access_token']})
                request.user.email = response.json()['email']
                request.user.save()

        return render(request, 'lk.personal.html', {'orders':orders,
                                                    'delivery_ways':delivery_ways,
                                                    'account':account})
    else:
        data = request.POST
        social_user = request.user.social_auth.filter(provider='facebook').first()
        if not social_user:
            social_user = request.user.social_auth.filter(provider='google-oauth2').first()
        errors = dict()
        if not social_user:
            if not data['email']:
                errors['email'] = _('Это поле обязательно')
        if not data['first_name']:
            errors['first_name'] = _('Это поле обязательно')
        if not data['last_name']:
            errors['last_name'] = _('Это поле обязательно')
        if not data['middle_name']:
            errors['middle_name'] = _('Это поле обязательно')
        if not data['phone_number']:
            errors['phone_number'] = _('Это поле обязательно')
        if not data['delivery_city']:
            errors['delivery_city'] = _('Это поле обязательно')
        if not data['delivery_address']:
            errors['delivery_address'] = _('Это поле обязательно')

        if not errors:
            if not social_user:
                request.user.email = data['email']
            request.user.first_name = data['first_name']
            request.user.last_name = data['last_name']
            request.user.middle_name = data['middle_name']
            request.user.phone_number = data['phone_number']
            account = PersonalAccount.objects.get(user=request.user)
            account.delivery_city = data['delivery_city']
            account.delivery_address = data['delivery_address']
            delivery_way = DeliveryWay.objects.get(name=data['delivery_way'])
            account.delivery_way = delivery_way
            account.save()
            request.user.save()
            orders = Order.objects.filter(user=request.user)[:3]
            delivery_ways = DeliveryWay.objects.all()

            return HttpResponseRedirect(reverse('personal'))
        else:
            orders = Order.objects.filter(user=request.user)[:3]
            account = PersonalAccount.objects.get(user=request.user)
            delivery_ways = DeliveryWay.objects.all()
            return render(request, 'lk.personal.html', {'orders':orders,
                                                        'delivery_ways':delivery_ways,
                                                        'account':account,
                                                        'errors':errors})
        

@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user)
    account = PersonalAccount.objects.get(user=request.user)
    basket_products = dict()
    images = dict()
    for obj in orders:
        basket_products[obj.id] = obj.basket.basketproduct_set.iterator()
        for prod in obj.basket.basketproduct_set.iterator():
            images[prod.product.id] = prod.product.images.get_queryset()
    return render(request, 'lk.orders.html', {'orders':orders,
                                              'account':account,
                                              'basket_products':basket_products,
                                              'images':images})


@login_required
def change_password(request):
    if request.method == 'POST':
        data = request.POST
        user = request.user
        account = PersonalAccount.objects.filter(user=user).first()     
        errors = dict()
        if user.check_password(data['old_pass']):
            try:
                validate_password(data['new_pass'])
                if data['new_pass'] == data['repeat']:
                    user.set_password(data['new_pass'])
                    user.save()
                    login(request, user)
                    return HttpResponseRedirect('%s?status_message=%s' % (reverse('change_pass'),_('Пароль успешно изменён')))
                else:
                    errors['pass'] = _('Пароли не совпадают')
            except ValidationError as e: 
                errors['new_pass'] = _('Слишком слабый пароль')
        else:
            errors['old_pass'] = _('Неправильный пароль')
        return render(request, 'lk.change.password.html', {'errors':errors,
                                                           'account':account})
    else:
        account = PersonalAccount.objects.filter(user=request.user).first()
        return render(request, 'lk.change.password.html', {'account':account})


@login_required
def waiting(request):
    orders = Order.objects.filter(user=request.user)
    account = PersonalAccount.objects.get(user=request.user)
    basket_products = dict()
    images = dict()
    for obj in orders:
        if obj.status != 'Закончен':
            basket_products[obj.id] = obj.basket.basketproduct_set.iterator()
            for prod in obj.basket.basketproduct_set.iterator():
                images[prod.product.id] = prod.product.images.get_queryset()
    return render(request, 'lk.waiting.html', {'orders':orders,
                                               'account':account,
                                               'basket_products':basket_products,
                                               'images':images})


@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid() : 
            subject = 'Сообщение от пользователя'
            phone = request.user.phone_number
            text_phone = ''.join(['--------------- Телефон: ',phone])
            message = ''.join([form.cleaned_data['message'], text_phone])
            from_email = request.user.email
            try:
                mail = EmailMessage(subject, message, from_email, [ADMIN_EMAIL])
                if request.FILES.getlist('file'):
                    for file in request.FILES.getlist('file'):
                        mail.attach(file.name, file.read(), file.content_type)
                    mail.send()
                message = _('Сообщение успешно отправлено')
            except Exception as e:
                message = _('Произошла ошибка при отправке сообщения, попробуйте позже.')
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('lk_contact'),message))
        else:
            message = _('Введите сообщение...')
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('lk_contact'),message))
    else:
        form = ContactForm()
        account = PersonalAccount.objects.get(user=request.user)
        return render(request, 'lk.contacts.html', {'form':form,
                                                    'account':account})
