# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib
import ast

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from content.models import DeliveryWay, ChipBasket, Delivery,\
                           Order, DeliveryData, BasketProduct, PersonalAccount
from content.forms import DeliveryDataForm


def basket(request):
    delivery_ways = DeliveryWay.objects.all()
    if request.user.is_authenticated():
        account = PersonalAccount.objects.filter(user=request.user).first()
    else:
        account = None
    images = dict()
    if request.session.has_key('basket_id'):
        basket = ChipBasket.objects.get(id=request.session['basket_id'])
        basket_product = BasketProduct.objects.filter(basket=basket)
        for obj in basket.basketproduct_set.iterator():
            if obj.amount == 0:
                obj.delete()
                continue
            images[obj.product.id] = obj.product.images.get_queryset()
    else:
        basket = None
        basket_product = None
        result = None
    delivery_data_form = DeliveryDataForm()

    if request.method == "GET":
        return render(request, 'basket.html', {'delivery_ways':delivery_ways,
                                               'delivery_data_form':delivery_data_form,
                                               'basket':basket,
                                               'images':images,
                                               'basket_product':basket_product,
                                               'account':account})
    elif request.method == 'POST':
        data = request.POST
        delivery_data_form = DeliveryDataForm(data)
        if delivery_data_form.is_valid() and data.get('method'):
            if request.session.has_key('basket_id'):

                basket = ChipBasket.objects.get(id=request.session['basket_id'])
                has_products = False
                for obj in basket.basketproduct_set.iterator():
                    has_products = True
                    break
                if has_products:

                    delivery = Delivery()
                    delivery.delivery_way = DeliveryWay.objects.filter(name=data['method']).first()
                    delivery.save()

                    delivery_data = DeliveryData()
                    delivery_data.first_name = delivery_data_form.cleaned_data['first_name']
                    delivery_data.last_name = delivery_data_form.cleaned_data['last_name']
                    delivery_data.city = delivery_data_form.cleaned_data['city']
                    delivery_data.phone_number = delivery_data_form.cleaned_data['phone_number']
                    delivery_data.is_sms = delivery_data_form.cleaned_data['is_sms']
                    delivery_data.nova_poshta_stock = delivery_data_form.cleaned_data['nova_poshta_stock']
                    delivery_data.is_cod = delivery_data_form.cleaned_data['is_cod']
                    delivery_data.cod_sum = delivery_data_form.cleaned_data['cod_sum']
                    delivery_data.email = delivery_data_form.cleaned_data['email']
                    delivery_data.commentary = delivery_data_form.cleaned_data['commentary']
                    delivery_data.save()

                    if request.user.is_authenticated:

                        acc = PersonalAccount.objects.filter(user=request.user).first()                       
                        if not acc: 
                            account = PersonalAccount()
                            account.delivery_city = delivery_data.city
                            account.delivery_address = delivery_data.nova_poshta_stock
                            account.delivery_way = delivery.delivery_way
                            account.user = request.user
                            account.save()
                        elif not acc.delivery_way:
                            acc.delivery_city = delivery_data.city
                            acc.delivery_address = delivery_data.nova_poshta_stock
                            acc.delivery_way = delivery.delivery_way
                            acc.save()

                        user = request.user
                        if not user.first_name:
                            user.first_name = delivery_data.first_name
                        if not user.last_name:
                            user.last_name = delivery_data.last_name
                        if not user.phone_number:
                            user.phone_number = delivery_data.phone_number
                        user.save()

                    order = Order(basket=basket)
                    order.status = 'Оформлен'
                    order.delivery = delivery
                    order.basket = basket
                    order.delivery_data = delivery_data 
                    if request.user.is_authenticated:
                        order.user = request.user
                    order.save()
                    basket.is_framed = True
                    basket.save()

                    return HttpResponseRedirect('%s?status_message=%s' % (reverse('home'),_('Заказ успешно оформлен')))
                else:
                    return HttpResponseRedirect('%s?status_message=%s' % (reverse('basket'),_('Корзина пуста')))
            else:
                return HttpResponseRedirect('%s?status_message=%s' % (reverse('basket'),_('Корзина пуста')))
        else:
            delivery_data_form.errors['method_error'] =  _('Выберите способ доставки')
            return render(request, 'basket.html', {'delivery_ways':delivery_ways,
                                                   'delivery_data_form':delivery_data_form,
                                                   'basket':basket,
                                                   'images':result,
                                                   'basket_product':basket_product,
                                                   'account':account})


            
       


