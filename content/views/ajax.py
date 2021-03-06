# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string


from content.models import Blog, DiscountProduct, ChipBasket, BasketProduct,\
                           ProductImage, StampCar, ModelCar, YearCar, Product,\
                           PersonalAccount, DeliveryWay


def basket_session(request):
    if request.method == 'POST':
        if not request.session.has_key('basket_id'):
            basket = ChipBasket()
            basket.save()
            request.session['basket_id'] = basket.id
        data = request.POST
        response = dict()
        basket = ChipBasket.objects.get(pk=request.session['basket_id'])
        am = 0    
        for obj in basket.basketproduct_set.iterator():
                am = 1
                if obj.product.pk == int(data['pk']):
                    am = 2
                    obj.amount += 1
                    obj.save()
                    break
        if am != 2:
            product = Product.objects.get(pk=data['pk'])
            inter = BasketProduct(product=product,basket=basket)
            inter.save()

        response['amount'] = basket.count()
        if request.user.is_authenticated:
            if request.user.site:
                response['sum'] = round(basket.calculate_sum_convert_price(), 2)
            else:
                response['sum'] = round(basket.calculate_sum_convert_ppc_price(), 2)
        else:
            response['sum'] = round(basket.calculate_sum_convert_ppc_price(), 2)

        return JsonResponse(response)
    else:
        response = dict()
        response['amount'] = 0
        response['sum'] = 0
        return JsonResponse(response)


def news_generate(request):
    if request.method == 'GET':
        data = request.GET
        start = int(data['start'])
        end = start + int(data['length'])
        news = Blog.objects.order_by('date').filter(active=True).reverse()[start:end]

        html = render(request, 'news_gen.html', {'news':news})
        return HttpResponse(html)
    else:
        html = render(request, 'news_gen.html', {})
        return HttpResponse(html)


def products_discount_generate(request):
    if request.method == 'GET':
        data = request.GET
        block = data['container']
        start = int(data['start'])
        end = start + int(data['length'])
        products = Product.objects.all()[start:end]
        images = dict()
        for obj in products:
            images[obj.id] = obj.images.get_queryset()

        templ = ''.join(['prod_disc_gen_', block, '.html'])
        html = render(request, templ, {'products':products,
                                       'images':images})
        return HttpResponse(html)
    else:
        templ = ''.join(['prod_disc_gen_', block, '.html'])
        html2 = render(request, templ, {}) 
        return HttpResponse(html2)


def car_select(request):
    if request.method == 'GET':
        data = request.GET
        if data['id'] == '0':
            templ = ''.join([data['container'], '_generate.html'])
            html = render(request, templ, {})
            return HttpResponse(html)
        elif data['name'] == 'model':
            models = ModelCar.objects.filter(stamp_id=data['id'])
            templ = ''.join([data['container'], '_generate.html'])
            html = render(request, templ, {'model_cars':models})
            return HttpResponse(html)
        elif 'year' in data['name']:
            years = ModelCar.objects.get(id=data['id']).years.all()
            templ = ''.join([data['container'], '_generate.html'])
            html = render(request, templ, {'year_cars':years})
            return HttpResponse(html)
    else:
        return HttpResponse('')


def change_amount(request):
    if request.method == 'POST':
        data = request.POST
        response = dict()
        basket_product = BasketProduct.objects.get(id=data['id'])
        if data['action'] == '-' and basket_product.amount > 0:
            response['not_last'] = True
            basket_product.amount -= 1
        elif data['action'] == '+':
            basket_product.amount += 1
        else:
            pass
        basket_product.save()
        response['amount'] = basket_product.amount
        if request.user.is_authenticated:
            if request.user.site:
                response['sum'] = basket_product.basket.calculate_sum_convert_price()
            else:
                response['sum'] = basket_product.basket.calculate_sum_convert_ppc_price()
        else:
            response['sum'] = basket_product.basket.calculate_sum_convert_ppc_price()
        return JsonResponse(response)


def clear_basket(request):
    if request.method == 'POST':
        if request.session.has_key('basket_id'):
            basket = ChipBasket.objects.get(id=request.session['basket_id'])
            for obj in basket.basketproduct_set.iterator():
                obj.delete()
            response = render(request, 'basket_gen.html', {'basket':basket})
            return HttpResponse(response)
        else:
            response = ' '
            return HttpResponse(response)
    else:
        response = ' '
        return HttpResponse(response)


def change_data_lk(request):
    if request.method == 'POST':
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
            request.user.save()
            account.save()

            delivery_ways = DeliveryWay.objects.all()
            html = render(request, 'lk_pers_data.html', {'account':account,
                                                         'delivery_ways':delivery_ways})
            return HttpResponse(html)

