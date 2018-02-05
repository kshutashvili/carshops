# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from content.models import LandingProductBlock, Blog, Product, PopularProduct, DiscountProduct


def index(request):
    landing_products = LandingProductBlock.objects.order_by('order').reverse()[:5]
    news = Blog.objects.order_by('date').filter(active=True).reverse()[:6]
    discount_products = DiscountProduct.objects.all()
    popular_products = PopularProduct.objects.all()
    return render(request,'index.html',{'landing_products':landing_products,
                                        'products_disc':discount_products,
                                        'products_pop':popular_products,
                                        'news':news})