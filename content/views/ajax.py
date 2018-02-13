# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from content.models import Blog, DiscountProduct, ChipBasket, BasketProduct,\
                           ProductImage, StampCar, ModelCar, YearCar, Product
    

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
        response['sum'] = basket.calculate_sum_convert_ppc_price()

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
        products = DiscountProduct.objects.all()[start:end]
        images = dict()
        for obj in products:
            images[obj.product.id]=ProductImage.objects.filter(product_id=obj.product.id)

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

