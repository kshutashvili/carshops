from django.shortcuts import render
from django.views.generic import ListView

from content.models import Product, Banner


def ProductList(request):
    products = Product.objects.all()[:2]
    banners = Banner.objects.all()
    images = {}
    for obj in products:
        images[obj.id] = obj.images.get_queryset()
    return render(request,'catalog.html',{'products':products,
                                          'banners':banners,
                                          'images':images})

