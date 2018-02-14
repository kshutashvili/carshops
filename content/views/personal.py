# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
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
        orders = Order.objects.filter(user=request.user)[:3]
        account = PersonalAccount.objects.get(user=request.user)
        delivery_ways = DeliveryWay.objects.all()
        return render(request, 'lk.personal.html', {'orders':orders,
                                                    'delivery_ways':delivery_ways,
                                                    'account':account})
    else:
        data = request.POST
        errors = dict()
        if not data['first_name']:
            errors['first_name'] = _('Это поле обязательно')
        if not data['last_name']:
            errors['last_name'] = _('Это поле обязательно')
        if not data['middle_name']:
            errors['middle_name'] = _('Это поле обязательно')
        if not data['email']:
            errors['email'] = _('Это поле обязательно')
        if not data['phone_number']:
            errors['phone_number'] = _('Это поле обязательно')
        if not data['delivery_city']:
            errors['delivery_city'] = _('Это поле обязательно')
        if not data['delivery_address']:
            errors['delivery_address'] = _('Это поле обязательно')

        if not errors:
            request.user.first_name = data['first_name']
            request.user.last_name = data['last_name']
            request.user.middle_name = data['middle_name']
            request.user.phone_number = data['phone_number']
            request.user.email = data['email']
            account = PersonalAccount.objects.get(user=request.user)
            account.delivery_city = data['delivery_city']
            account.delivery_address = data['delivery_address']
            delivery_way = DeliveryWay.objects.get(name=data['delivery_way'])
            account.delivery_way = delivery_way
            account.save()
            request.user.save()
            orders = Order.objects.filter(user=request.user)[:3]
            delivery_ways = DeliveryWay.objects.all()
            return render(request, 'lk.personal.html', {'orders':orders,
                                                        'delivery_ways':delivery_ways,
                                                        'account':account})
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
    result = dict()
    for obj in orders:
        basket_products[obj.id] = obj.basket.basketproduct_set.iterator()
        for prod in obj.basket.basketproduct_set.iterator():
            result[prod.product.id] = ProductImage.objects.filter(product_id=prod.product.id)
    return render(request, 'lk.orders.html', {'orders':orders,
                                              'account':account,
                                              'basket_products':basket_products,
                                              'images':result})


@login_required
def change_password(request):
    if request.method == 'POST':
        data = request.POST
        user = request.user
        errors = dict()
        if user.check_password(data['old_pass']):
            try:
                validate_password(data['new_pass'])
                if data['new_pass'] == data['repeat']:
                    user.set_password(data['new_pass'])
                    return HttpResponseRedirect('%s?status_message=%s' % (reverse('change_pass'),_('Пароль успешно изменён')))
                else:
                    errors['pass'] = _('Пароли не совпадают')
            except ValidationError as e: 
                errors['new_pass'] = _('Слишком слабый пароль')
        else:
            errors['old_pass'] = _('Неправильный пароль')
        return render(request, 'lk.change.password.html', {'errors':errors})
    else:
        return render(request, 'lk.change.password.html', {})


@login_required
def waiting(request):
    orders = Order.objects.filter(user=request.user)
    account = PersonalAccount.objects.get(user=request.user)
    basket_products = dict()
    result = dict()
    for obj in orders:
        if obj.status != 'Закончен':
            basket_products[obj.id] = obj.basket.basketproduct_set.iterator()
            for prod in obj.basket.basketproduct_set.iterator():
                result[prod.product.id] = ProductImage.objects.filter(product_id=prod.product.id)
    return render(request, 'lk.waiting.html', {'orders':orders,
                                              'account':account,
                                              'basket_products':basket_products,
                                              'images':result})


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
        return render(request, 'lk.contacts.html', {'form':form})
