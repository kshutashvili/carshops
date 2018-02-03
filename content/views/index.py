# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from content.models import LandingProductBlock, Blog


def index(request):
    landing_products = LandingProductBlock.objects.order_by('order').reverse()
    news = Blog.objects.order_by('date').filter(active=True).reverse()[:6]
    return render(request,'index.html',{'landing_products':landing_products,
                                        'news':news})